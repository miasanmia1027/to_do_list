#내가 지금 하려는 것 좀보이드 프로잭트처럼 어 떤 명령어를 입력하면 어떤것을 띄우는 것
#어떤것== 추가,삭제

#추가적== 중요도 표시

#최종적으로 하고 싶은 것 데이터에 저장 하는것


def add(add_list):
    with open('add.txt', 'a', encoding='utf-8') as text_file:
        text_file.writelines(f"{add_list}\n")

def remove(line_number):
    # 파일의 모든 내용을 읽어서 리스트에 저장합니다.
    with open('add.txt', 'r', encoding='utf-8') as text_file:
        lines = text_file.readlines()

    try:
        line_number = int(line_number)
        if 0 <= line_number - 1 < len(lines):
            del lines[line_number - 1]
    except ValueError:
        print("유효한 숫자를 입력하세요.")

    with open('add.txt', 'w', encoding='utf-8') as text_file:
        text_file.writelines(lines)
    
def finish(finish_list):
    with open('add.txt', 'r', encoding='utf-8') as text_file:
        lines = text_file.readlines()

    try:
        finish_list = int(finish_list)
        if 0 <= finish_list - 1 < len(lines):
            finished_task = lines[finish_list - 1]  # 완료된 항목을 저장
            del lines[finish_list - 1]

            with open('add.txt', 'w', encoding='utf-8') as text_file:
                text_file.writelines(lines)

            with open('finish.txt', 'a', encoding='utf-8') as finish_file:
                finish_file.writelines(finished_task)
        else:
            print("유효한 줄 번호를 입력하세요.")
    except ValueError:
        print("유효한 숫자를 입력하세요.")
    
print("만약 어떤 것을 추가하고 싶으면 '추가'를 입력하세요")
print("어떤 것을 삭제하고 싶으면 '삭제'를 입력하세요")
print("어떤 것을 완료하고 싶으면 '완료'를 입력하세요")

while True:
    user_input = input("명령을 입력하세요 (추가/삭제/완료): ")
    if user_input == "추가":
        plus_list = input("추가할 내용을 입력하세요: ")
        if plus_list == "":
            break
        add(plus_list)
        with open('add.txt', 'r', encoding='utf-8') as text_file:
            line_result_1 = text_file.readlines()
            print("현재 내용:", line_result_1)

    elif user_input == "삭제":
        user_remove_input = input("몇 번째 줄을 삭제하고 싶나요? ")
        if user_remove_input == "":
            break
        remove(user_remove_input)
        with open('add.txt', 'r', encoding='utf-8') as text_file:
            line_result_2 = text_file.readlines()
            print("현재 내용:", line_result_2)

    elif user_input == "완료":
        user_finish_input = input("몇 번째 줄을 완료 하셨나요? ")
        if user_finish_input == "":
            break
        finish(user_finish_input)
        with open('finish.txt', 'r', encoding='utf-8') as text_file:
            line_result_3 = text_file.readlines()
            print("현재 완료 내용:", line_result_3)

    elif user_input == "":
        break
    
    else:
        print("유효한 명령을 입력하세요.")

print("이제 내가 해야 하는 것들:")

with open('add.txt', 'r', encoding='utf-8') as text_file:
    line_result = text_file.readlines()
print(line_result)
