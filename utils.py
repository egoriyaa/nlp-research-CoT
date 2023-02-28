import json
import re
from typing import List

ANS_RE = re.compile(r"#### (\-?[0-9\.\,]+)")
INVALID_ANS = "[invalid]"

def extract_true_answer(s: str) -> str:
    match = ANS_RE.search(s)
    if match:
        match_str = match.group(1).strip()
        match_str = match_str.replace(",", "")
        return match_str
    else:
        return INVALID_ANS

def extract_pred_answer(s: str) -> str:
    ans = re.findall(r"[-+]? *(?:\d*[\.\,\:]*\d+)", s)
    ans = '' if not ans else ans[-1]
    ans = re.sub('[^\d|\.\,\:-]', '', ans)
    if '.' in ans or ':' in ans:    
        ans = ans.strip('0')
        ans = ans.strip('.')
    elif ',' in ans:
        ans = ans.replace(',', '')
    return ans

def read_my_jsonl(path: str) -> List:
    with open(path) as f:
        return json.load(f)

def read_jsonl(path: str) -> List:
    with open(path) as fh:
        return [json.loads(line) for line in fh.readlines() if line]
    
def write_jsonl(path: str, data: List) -> None:
    with open(path, 'w') as fp:
        json.dump(data, fp, indent=0)

