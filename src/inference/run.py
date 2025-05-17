import time 
import pandas as pd
from tqdm import tqdm
import concurrent.futures
from inference.chat import chat
from utils.save import save_csv

def single(
    api_key: str,
    data: pd.DataFrame
) -> pd.DataFrame:
    results = []
    for _, row in tqdm(data.iterrows(), total=len(data)):
        try:
            result = chat(api_key, row['err_sentence'])
        except:
            # 429 에러 대응 로직
            success = False
            time.sleep(5)
            while success == False:
                try:
                    result = chat(api_key, row['err_sentence'])
                    success = True
                except:
                    success = False
                    time.sleep(5)
        results.append({
            'id': row['id'],
            'err_sentence': row['err_sentence'],
            'cor_sentence': result
        })
    return pd.DataFrame(results)


def multiple(
    api_keys: list[str],
    data: pd.DataFrame
) -> pd.DataFrame:
    # 1. API KEY 검사
    assert len(api_keys) >= 2, "api_keys 리스트에 최소 2개 이상의 API 키가 필요합니다."

    # 2. 청크 분할
    chunks = []
    n_workers = len(api_keys)
    chunk_size = len(data) // n_workers
    start_idx = 0
    for _ in range(n_workers):
        # 나머지를 앞쪽 청크에 분배
        end_idx = start_idx + chunk_size
        chunks.append(data.iloc[start_idx:end_idx].reset_index(drop=True))
        start_idx = end_idx

    # 3. 병렬 처리
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=n_workers) as executor:
        future_to_chunk = {
            executor.submit(single, api_keys[i % len(api_keys)], chunk): i
            for i, chunk in enumerate(chunks)
        }
        
        for future in concurrent.futures.as_completed(future_to_chunk):
            chunk_idx = future_to_chunk[future]
            try:
                result = future.result()
                results.append((chunk_idx, result))
            except Exception as e:
                print(f"청크 {chunk_idx} 처리 중 오류 발생: {e}")
                return combined_results
    
    # 4. 결과 정렬 및 결합
    results.sort(key=lambda x: x[0])
    combined_results = pd.concat([r[1] for r in results], ignore_index=True)
    try:
        save_csv(combined_results, 'submission.csv')
    except:
        breakpoint()  # please stop here..
    return combined_results
    
