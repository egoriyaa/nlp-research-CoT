from sklearn.metrics import accuracy_score
from collections import Counter
from utils import read_my_jsonl

def main() -> None:
    data = read_my_jsonl('data.jsonl')

    answers_true = []
    answers_greedy = []
    answers_major = []
    for i in range(len(data)):
        answers_true.append(data[i]['true_ans'])
        answers_greedy.append(data[i]['extracted_ans'][0])
        answers_major.append(Counter(data[i]['extracted_ans']).most_common(1)[0][0])
    print('Accuracy for greedy decoding CoT:', accuracy_score(answers_greedy, answers_true))
    print('Accuracy for self-consistency CoT:', accuracy_score(answers_major, answers_true))  


if __name__ == '__main__':
    main()  