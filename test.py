# r==읽기 모드
#w== 쓰기 모드(만약 파일이 없으면 만들어 내는 무시무시 한놈)
#r+==다 한다는 의미

# read() : This function reads the entire file and returns a string
# readline() : This function reads lines from that file and returns as a string. It fetch the line n, if it is been called nth time.
# readlines() : This function returns a list where each element is single line of that file.
# write() : This function writes a fixed sequence of characters to a file.
# writelines() : This function writes a list of string.
# append() : This function append string to the file instead of overwriting the file.



# 파일을 'a' 모드로 열어야 파일 끝에 내용을 추가할 수 있습니다.
text_file = open('to_do_list.txt', 'a')

# writelines 메서드를 사용하여 여러 줄을 추가합니다.
text_file.writelines(           )

# 파일을 닫습니다.
text_file.close()
