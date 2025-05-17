import pandas as pd

from prompt.prompt import build_message
from prompt.few_shot import FEW_SHOT_EXAMPLES, example_to_message
from inference.run import multiple, single
from utils.save import save_csv


API_KEYS = [
    'up_00000000000000000000',
    'up_00000000000000000000',
    'up_00000000000000000000',
    'up_00000000000000000000'
]

test = pd.read_csv('./data/test.csv')


def launch(parallel: bool = True):
    if parallel:
        result = multiple(API_KEYS, test)
    else:
        result = single(API_KEYS[0], test)
        save_csv(result, 'submission.csv')


if __name__ == "__main__":
    launch(parallel=True)
