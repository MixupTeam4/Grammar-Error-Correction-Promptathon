import pandas as pd

from inference.run import multiple, single
from utils.save import save_csv

# API KEYS
API_KEYS = [
    "up_00000000000000000000000000000000",
    "up_00000000000000000000000000000000",
    "up_00000000000000000000000000000000",
    "up_00000000000000000000000000000000",
]

# 데이터셋
test = pd.read_csv('./data/test.csv')


# 통합된 실행 함수 
def launch(parallel: bool = True):
    if parallel:
        result = multiple(API_KEYS, test)
    else:
        result = single(API_KEYS[0], test)
        save_csv(result, 'submission.csv')


if __name__ == "__main__":
    launch(parallel=True)  # 병렬 처리 여부
