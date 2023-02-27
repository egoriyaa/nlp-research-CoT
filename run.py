from utils import read_jsonl, read_my_jsonl, write_jsonl
from inference import infer
from huggingface_hub import HfFolder
from huggingface_hub import InferenceApi


test_data = read_jsonl('test.jsonl')
prompt = read_my_jsonl('prompt.jsonl')
inference = InferenceApi("bigscience/bloom", token=HfFolder.get_token())
data_CoT = []
for i in range(len(test_data)):
    question = test_data[i]['question']
    model_input = prompt  + 'Q: ' + question + '\n' + 'A:'
    
    output = infer(inference, model_input, max_length=150)
    data_CoT.append({'input': model_input, 'output': output})