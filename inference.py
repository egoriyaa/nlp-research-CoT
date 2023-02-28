from huggingface_hub import HfFolder
from huggingface_hub import InferenceApi
from utils import read_jsonl, read_my_jsonl, write_jsonl, extract_pred_answer, extract_true_answer


def infer(inference, prompt,
          max_length = 32,
          top_k = 0,
          num_beams = 0,
          no_repeat_ngram_size = 2,
          top_p = 0.9,
          seed=42,
          temperature=0.7,
          greedy_decoding = True,
          return_full_text = False
          ) -> str:
    

    top_k = None if top_k == 0 else top_k
    do_sample = False if num_beams > 0 else not greedy_decoding
    num_beams = None if (greedy_decoding or num_beams == 0) else num_beams
    no_repeat_ngram_size = None if num_beams is None else no_repeat_ngram_size
    top_p = None if num_beams else top_p
    early_stopping = None if num_beams is None else num_beams > 0
    params = {
        "max_new_tokens": max_length,
        "top_k": top_k,
        "top_p": top_p,
        "temperature": temperature,
        "do_sample": do_sample,
        "seed": seed,
        "early_stopping":early_stopping,
        "no_repeat_ngram_size":no_repeat_ngram_size,
        "num_beams":num_beams,
        "return_full_text":return_full_text
    }
    
    try:
        return inference(prompt, params=params)[0]['generated_text']
    except NotImplementedError:
        return ''
    

def main() -> None:    
    test_data = read_jsonl('test.jsonl')
    prompt = read_my_jsonl('prompt.json')
    inference = InferenceApi("bigscience/bloom", token=HfFolder.get_token())
    data = []
    for i in range(len(test_data)):
        question = test_data[i]['question']
        model_input = prompt  + 'Q: ' + question + '\n' + 'A:'
        outputs = []
        pred_answers = []
        for j in range(4):
            if j == 0:
                output = infer(inference, model_input, max_length=150, top_k=None, greedy_decoding=True, top_p=None)
            elif j == 1:
                output = infer(inference, model_input, max_length=150, top_k=20, greedy_decoding=False, top_p=None)
            elif j == 2:
                output = infer(inference, model_input, max_length=150, top_k=None, greedy_decoding=False,  top_p=None, num_beams=20)
            else:
                output = infer(inference, model_input, max_length=150, top_k=None, greedy_decoding=False,  top_p=0.9)
            output = output.split('Q:')[0]
            output = output.split('A:')[0].strip()
            pred_ans = extract_pred_answer(output)
            outputs.append(output)
            pred_answers.append(pred_ans)
        true_ans = extract_true_answer(test_data[i]['answer'])
        data.append({'input': model_input, 'output': outputs, 'extracted_ans': pred_answers, 'true_ans:': true_ans})
    write_jsonl('data.jsonl', data)

if __name__ == '__main__':
    main()