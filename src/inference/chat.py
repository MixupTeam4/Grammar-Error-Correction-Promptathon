import requests
from prompt.prompt import build_message

url = "https://api.upstage.ai/v1/chat/completions"

def chat(
    api_key: str, 
    err_sentence: str,
    few_shot_examples: list[dict],
    temperature: float = 0.0,
    top_p: float = 1.0,
) -> str:
    # 1. 메시지 생성
    messages = build_message(err_sentence, few_shot_examples)

    # 2. Completion API request
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "solar-pro",
        "messages": messages,
        "temperature": temperature,
        "top_p": top_p
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    results = response.json()

    # 3. 결과 반환
    cor_sentence = results['choices'][0]['message']['content']  
    token_usage = results['usage']['total_tokens']

    # 4. 전체 토큰 수 2000 초과 검사
    if token_usage > 2000:
        raise ValueError(f"전체 토큰 수가 2000 초과입니다. 토큰 수: {token_usage}")

    return cor_sentence