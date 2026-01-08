"""
해당 코드는 토크나이저의 기본이 되는 'Tokenizer' 클래스와, 여러 보조(helper) 함수로 구성되어 있습니다.
또한 base class의 경우 토크나이저를 저장하고 불러오는 기능과 같이, 
모든 토크나이저에서 공통으로 사용되는 기능이 포함되어 있습니다.

설계상으로는 인터페이스를 더 엄격하게 분리하는 것도 가능했을 것입니다.
예를 들어, 정규식이나 패턴 처리와 관련된 코드를 'RegexTokenizer'로 완전히 분리할 수도 있었을 것입니다.

다만, 해당 코드에서는 구조를 지나치게 복잡하게 만들기보다는,
전체 흐름을 보다 쉽게 이해할 수 있도록 하기 위해
설계 측면에서 일부 타협을 선택했습니다.
"""


import unicodedata
"""
unicodedata 모듈은 유니코드를 다루기 위한 파이썬 표준 라이브러리입니다.

여기서 유니코드(Unicode)란
전 세계의 모든 문자를 하나의 공통된 표준 체계로 표현하기 위한 문자 인코딩 표준입니다.

유니코드는 모든 문자에 고유한 번호를 부여합니다. 이때 이 번호를 코드 포인트(Code Point)라고 합니다.
예컨대 유니코드는 A는 U+0041, a는 U+0061, 가는 U+AC00라는 코드 포인트로 매핑하여 관리하고 있습니다.

"""

# -----------------------------------------------------------------------------
# BasicTokenizer와 RegexTokenizer에서 공통으로 사용하는 몇 가지 보조(helper) 함수들

def get_stat(ids, counts=None):
    """
    정수로 이루어진 리스트가 주어졌을 때,
    서로 인접한 두 값으로 이루어진 쌍이 각각 몇 번씩 등장하는지를 세어
    그 결과를 딕셔너리 형태로 반환합니다.

    예를 들어, [1, 2, 3, 1, 2]가 주어지면
    {(1, 2): 2, (2, 3): 1, (3, 1): 1} 과 같은 결과로 변환됩니다.

    또한 이미 존재하는 count 딕셔너리에 해당 결과를 누적하여 업데이트하는 것이 가능합니다.
    """
    counts = {} if counts is None else counts
    for pair in zip(ids, ids[1:]):
        counts[pair] = counts.get(pair, 0) + 1
    return counts


def merge(ids, pair, idx):
    """
    정수로 이루어진 리스트, ids에서
    앞뒤로 붙어 있는 값 (pair)을 찾아
    하나의 새 숫자로 (idx)로 바꿉니다.

    예시)
    ids = [1, 2, 3, 1, 2]
    pair = (1, 2)
    idx = 4
    -> 결과 [4, 3, 4]    

    """
    newids = []
    i = 0
    while i < len(ids):
        # 맨 마지막이 아닐 때, 두 값이 pair와 같으면 하나로 바꾼다.
        if ids[i] == pair[0] and i <len(ids) - 1 and ids[i+1] == pair[1]:
            newids.append(idx)
            i += 2
        else:
            newids.append(ids[i])
            i += 1
    return newids

def replace_control_characters(s: str) -> str:
    """
    문자열에 포함된 유니코드 제어 문자(control characters)를
    출력 시 문제가 발생하지 않도록 유니코드 이스케이프 형태 (\\uXXXX)로 치환합니다.

    이는 개행, 탭 등 출력 환경을 왜곡하거나 보이지 않는 문자를
    콘솔에 명시적으로 보여주기 위함입니다.

    예시)
    안녕하세요\n반갑습니다. -> 안녕하세요\u000A반갑습니다.
    """
    chars = []
    for ch in s:
        if unicodedata.category(ch)[0] != "C":
            chars.append(ch)
        else:
            chars.append(f"\\u{ord(ch):04x}")
    return "".join(chars)

def render_token(t: bytes) -> str:
    # 예시) b'\x68\x65\x6c\x6c\x6f\x0a' -> 'hello\u000a'
    s = t.decode('utf-8', errors='replace')
    s = replace_control_characters(s)
    return s

# -----------------------------------------------------------------------------
# the base Tokenizer class