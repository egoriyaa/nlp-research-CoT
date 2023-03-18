# NLP-research-CoT

Entry test for Tinkoff NLP research internship.

The task was to make experiments with chain-of-thoughts prompting with [Bloom model](https://huggingface.co/bigscience/bloom) and [GSM8K dataset](https://huggingface.co/datasets/gsm8k)

[Paper 1](https://arxiv.org/pdf/2201.11903.pdf), [Paper 2](https://arxiv.org/pdf/2203.11171.pdf)

Installation:
```
git clone https://github.com/egoriyaa/nlp-research-CoT.git

cd nlp-research-CoT

pip install -r requirements.txt
```

To generate CoT data run:
```python inference.py```

To calculate metrics for CoT and ensemble CoT run:
```python calculator.py```
