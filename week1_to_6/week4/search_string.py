
# sentence = "The quick brown fox jumps over the lazy dog"

# print(sentence.find("fox")) # 16 (16번째 인덱스에 fox가 있음)
# print(sentence.find("wolf")) # -1 (없음)
# print(sentence.find("o")) # 12 (첫번째로 나오는 o의 인덱스)
# print(sentence.rfind("o")) # 41 (마지막으로 나오는 o의 인덱스)
# print(sentence.rfind("jumps")) # 20 (jumps가 시작하는 인덱스)
# print(sentence.startswith("The")) # True (The로 시작)
# print(sentence.startswith("the")) # False (대소문자 구분)
# print(sentence.endswith("dog")) # True (dog로 끝)
# print(sentence.endswith("cat")) # False (없음)
# print(sentence.find("o", 13, 20)) # 16 (13~20 사이에서 o가 처음 나오는 인덱스)


"""
첫번째로 나타나는 문자열 하나만 찾기

input: 파일 이름 filename과 찾을 문자열 key
key가 처음 나타나는 인덱스를 "result.txt"에 저장
key가 없으면 not found을 "result.txt"에 저장하는 "find_first"함수 작성

1. 읽을 파일 쓸 파일 각각 열기
2. 읽을 파일 전체를 문자열로 읽어옴
3. find 메서드 사용해 key가 있는 위치 찾음
4. 쓰는 파일에 인덱스 쓰기
5. 파일들 모두 닫음
"""

def find_first(filename, key):
  infile = open(filename, 'r')
  outfile = open('result.txt', 'w')
  text = infile.read()
  pos = text.find(key)
  if pos == -1:
    outfile.write('is not found. \n')
  else:
    outfile.write(key, "is at", str(pos)+". \n")
  outfile.close()
  infile.close()
  print("DONE")
  
  
"""
두번째로 나타나는 문자열 하나만 찾기

"""

def find_second(filename, key):
  infile = open(filename, 'r')
  outfile = open('result.txt', 'w')
  text = infile.read()
  pos = text.find(key)
  pos = text.find(key, pos+1) # 💡 두번째 위치 찾기
  if pos == -1:
    outfile.write('is not found. \n')
  else:
    outfile.write(key, "is at", str(pos)+". \n")
  outfile.close()
  infile.close()
  print("DONE")