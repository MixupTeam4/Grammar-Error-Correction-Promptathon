
# 🧪 MixUp_team4 : Grammar Error Correction Promptathon 

본 레포지토리는 Grammar Error Correction Promptathon  실험을 재현하고 확장하기 위한 코드 및 가이드를 제공합니다.


## 📌 프로젝트 개요

* **목표**: Solar Pro API를 활용하여 프롬프트 만으로 한국어 맞춤법 교정 성능을 개선한다. 
* **접근 전략**:
  1. System Prompt에서 role 부여
  2. 반복적인 오류 유형화 & 유형별 대응 전략 수립 -> Few-shot
  3. Few-shot을 system prompt에 포함시키지 않고, user, assistant 멀티턴인 것 처럼 작성해서 간결하고 출력 형식도 지킬 수 있게 함. 
 
 
* **주요 실험 내용**:

  * 실험 진행 방식 작성
---

## ⚙️ 환경 세팅 & 실행 방법

### 1. 사전 준비 

```bash
git clone https://github.com/MixupTeam4/Grammar-Error-Correction-Promptathon.git
```

### 라이브러리 설치

```bash
pip install -r requirements.txt
```

### 데이터 준비 / API KEY 준비

```bash
cd src
mkdir data  # data/test.csv 저장

```
+ API KEY는 src/main.py 내 API_KEYS에 저장
+ 병렬 처리 여부는 src/main.py의 parellel(bool) 값으로 결정

### 실험 실행

```bash
cd src
python main.py
```

---


## 🚧 실험의 한계 및 향후 개선

* **한계**:

  * 과교정 현상 : 동일 의미의 다른 단어로 변경하는 경우를 아예 배제하지 못함
  * 조사 추가 누락 : 말은 되지만 존재하지 않는 조사를 추가하는 것을 놓치는 경우가 존재 
  * 출력 형식 위반 : 존재하지 않았던 명사 간 쉼표를 잘 생성해내지 못함. 
  * 받침형 조사 줄임말 누락 : "이걸"이라는 말 대신 "이거"라고 생성하는 경우가 존재. 

* **향후 개선 방향**  : 2차 교정 도입

    - 1차 교정된 문장에 대한 재교정을 통해 과교정 현상에 대응
    - 1차 교정된 문장에 대한 재교정을 통해 누락하기 쉬운 명사 간 띄어쓰기에 대응

---

## 📂 폴더 구조

```
📁 src/
├── main.py             # 메인 실행 파일
├── requirements.txt    # 필요한 패키지 목록
├── prompt/             # 프롬프트 관련 함수들
│   ├── __init__.py     # prompt 패키지 초기화
│   ├── few_shot.py     # 예시 기반 few_shot 생성
│   └── prompt.py       # 시스템 프롬프트, messages 생성
├── inference/          # 추론/병렬처리 관련 함수들
│   ├── __init__.py     # inference 패키지 초기화
│   ├── chat.py         # 실험 실행 및 API 호출
│   └── run.py          # 평가 지표 계산
├── utils/              # 유틸리티 함수들
│   ├── __init__.py     # utils 패키지 초기화
│   └── save.py         # 파일 저장 함수
└── data/               # 데이터셋 저장
    └── test.csv        # 평가 대상 데이터


