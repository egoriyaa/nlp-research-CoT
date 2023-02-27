import json
import re
from typing import List

ANS_RE = re.compile(r"#### (\-?[0-9\.\,]+)")
INVALID_ANS = "[invalid]"

def extract_answer(completion) -> str:
    match = ANS_RE.search(completion)
    if match:
        match_str = match.group(1).strip()
        match_str = match_str.replace(",", "")
        return match_str
    else:
        return INVALID_ANS

def read_my_jsonl(path: str) -> List:
    with open('data_bsearch.jsonl') as f:
        return json.load(f)

def read_jsonl(path: str) -> List:
    with open(path) as fh:
        return [json.loads(line) for line in fh.readlines() if line]
    
def write_jsonl(path: str, data: List):
    with open(path, 'w') as fp:
        json.dump(data, fp, indent=0)

