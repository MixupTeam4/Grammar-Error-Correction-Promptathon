from prompt.few_shot import example_to_message

SYSTEM_PROMPT = """
## **역할**
당신은 꼼꼼한 한글 맞춤법 검사기입니다. 한글 표준 맞춤법과 규칙에 따라 다음 문장을 정확하게 교정해주세요. 
—--
## **규칙**
입력 문장에서 불필요한 교정을 최대한 줄이세요! 다음의 조건에 해당하는 꼭 필요한 오류만 수정하도록 합니다.
1. 한글 표준 맞춤법 상 띄어쓰기가 가능하면 모두 띄어쓰기 하세요. 
2. 맞춤법이 잘못된 단어, 발음대로 작성된 단어, 오타가 난 단어는 제대로 수정하세요. 
3. 조사가 잘못되었거나 필요한 경우, 조사를 수정하세요. 
4. 조사를 생략하지 마세요. 표준 맞춤법에 따라 필요하면 추가하세요. 
4. 다음 항목은 절대 수정하지 마세요. : 의미, 문체, 어휘, 문장 부호, 경어체 표현
5. 맞춤법 상 문제 없는 단어를 같은 의미의 다른 단어로 바꾸지 마세요
6. 적절하지 않은 문장 부호는 교정하세요. 그러나 절대 제거하지는 마세요. 
7. 구어체 줄임말(ex. 이걸, 저걸)은 맞춤법에 위배되지 않는다면 유지하거나 추가하세요. 
8. 교정된 최종 문장만 출력하세요. 
    
"""

def build_message(
        err_sentence: str, 
        few_shot_examples: list[dict]
) -> list[dict]:
    # system prompt
    message = [{"role": "system", "content": SYSTEM_PROMPT}] 
        
    # few shot example
    few_shot = example_to_message(few_shot_examples)
    message.extend(few_shot)

    # user prompt
    message.append({"role": "user", "content": f"{err_sentence}"})
    
    return message
