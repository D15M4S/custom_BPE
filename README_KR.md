[EN](README.md) | [KR](README_KR.md)

# Custom BPE

[Andrej Karpathy의 minbpe](https://github.com/karpathy/minbpe)를 참고하여 Byte Pair Encoding (BPE) 토크나이저를 직접 구현하고 학습하기 위한 개인 프로젝트입니다.

## 개요

이 저장소는 BPE 토크나이제이션을 공부하기 위한 실습 프로젝트입니다. BPE는 GPT와 같은 현대 언어 모델의 핵심 구성 요소입니다. 이 프로젝트의 목표는 BPE 토크나이저를 직접 구현하고, 훈련하며, 실험함으로써 NLP에서 토크나이제이션이 어떻게 작동하는지 깊이 이해하는 것입니다.

## BPE란?

Byte Pair Encoding (BPE)은 원래 데이터 압축 알고리즘이었으나, NLP에서 서브워드 토크나이제이션 방법으로 활용되고 있습니다. 작동 방식은 다음과 같습니다:

1. 개별 바이트/문자로 구성된 어휘로 시작
2. 가장 빈번한 토큰 쌍을 반복적으로 탐색
3. 해당 쌍을 새로운 토큰으로 병합
4. 원하는 어휘 크기에 도달할 때까지 반복

이 접근 방식을 통해 모델은 희귀한 단어를 서브워드로 분할하면서도 일반적인 단어는 단일 토큰으로 유지할 수 있습니다.

## 기능 (구현 예정)

- [ ] 기본 BPE 토크나이저 구현
- [ ] 사용자 정의 텍스트 코퍼스로 훈련
- [ ] 인코딩 및 디코딩 기능
- [ ] 어휘 저장/불러오기 지원
- [ ] RegexBPE (GPT-4 스타일 토크나이저)
- [ ] 성능 벤치마크
- [ ] 시각화 도구

## 프로젝트 구조

```
custom_BPE/
├── README.md
├── README_KR.md
├── LICENSE
├── bpe/
│   ├── __init__.py
│   ├── base.py          # 베이스 토크나이저 클래스
│   ├── basic.py         # 기본 BPE 구현
│   └── regex.py         # 정규식 기반 BPE (GPT-4 스타일)
├── data/                # 훈련 데이터
├── models/              # 저장된 토크나이저 모델
└── tests/               # 유닛 테스트
```

## 설치

```bash
git clone https://github.com/yourusername/custom_BPE.git
cd custom_BPE
pip install -r requirements.txt
```

## 사용법

```python
from bpe import BasicTokenizer

# 토크나이저 초기화
tokenizer = BasicTokenizer()

# 텍스트로 훈련
text = "훈련할 텍스트를 여기에 입력..."
tokenizer.train(text, vocab_size=256)

# 인코딩
tokens = tokenizer.encode("안녕하세요")

# 디코딩
text = tokenizer.decode(tokens)
```

## 학습 자료

- [Andrej Karpathy의 minbpe](https://github.com/karpathy/minbpe) - 참고 구현
- [Neural Machine Translation of Rare Words with Subword Units](https://arxiv.org/abs/1508.07909) - NLP용 BPE 원본 논문
- [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) - GPT-2 논문

## 라이센스

이 프로젝트는 MIT 라이센스에 따라 라이센스가 부여됩니다 - 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 감사의 말

- minbpe 프로젝트와 교육 콘텐츠를 제공해주신 [Andrej Karpathy](https://github.com/karpathy)님께 감사드립니다
