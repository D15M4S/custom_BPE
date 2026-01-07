[EN](README.md) | [KR](README_KR.md)

# Custom BPE

A personal project to understand and implement Byte Pair Encoding (BPE) tokenization from scratch, inspired by [Andrej Karpathy's minbpe](https://github.com/karpathy/minbpe).

## Overview

This repository is a hands-on learning project for studying BPE tokenization, which is a fundamental component of modern language models like GPT. The goal is to implement, train, and experiment with BPE tokenizers to gain a deeper understanding of how tokenization works in NLP.

## What is BPE?

Byte Pair Encoding (BPE) is a data compression algorithm that has been adapted for use in NLP as a subword tokenization method. It works by:

1. Starting with a vocabulary of individual bytes/characters
2. Iteratively finding the most frequent pair of tokens
3. Merging that pair into a new token
4. Repeating until reaching the desired vocabulary size

This approach allows models to handle rare words by breaking them into subwords while keeping common words as single tokens.

## Features (Planned)

- [ ] Basic BPE tokenizer implementation
- [ ] Training on custom text corpus
- [ ] Encoding and decoding functionality
- [ ] Vocabulary save/load support
- [ ] RegexBPE (GPT-4 style tokenizer)
- [ ] Performance benchmarks
- [ ] Visualization tools

## Project Structure

```
custom_BPE/
├── README.md
├── README_KR.md
├── LICENSE
├── bpe/
│   ├── __init__.py
│   ├── base.py          # Base tokenizer class
│   ├── basic.py         # Basic BPE implementation
│   └── regex.py         # Regex-based BPE (GPT-4 style)
├── data/                # Training data
├── models/              # Saved tokenizer models
└── tests/               # Unit tests
```

## Installation

```bash
git clone https://github.com/yourusername/custom_BPE.git
cd custom_BPE
pip install -r requirements.txt
```

## Usage

```python
from bpe import BasicTokenizer

# Initialize tokenizer
tokenizer = BasicTokenizer()

# Train on text
text = "your training text here..."
tokenizer.train(text, vocab_size=256)

# Encode
tokens = tokenizer.encode("hello world")

# Decode
text = tokenizer.decode(tokens)
```

## Learning Resources

- [Andrej Karpathy's minbpe](https://github.com/karpathy/minbpe) - Reference implementation
- [Neural Machine Translation of Rare Words with Subword Units](https://arxiv.org/abs/1508.07909) - Original BPE paper for NLP
- [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) - GPT-2 paper

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Andrej Karpathy](https://github.com/karpathy) for the minbpe project and educational content
