
# user에게 파일 경로와 찾을 단어를 입력받아 offset을 구하는 함수

def find_word_offsets(file_path, keyword):
  offsets = []
  
  try:
    with open(file_path, 'r') as file:
      content = file.read()
      index = content.find(keyword)

      while index != -1:
        offsets.append(index)
        index = content.find(keyword, index+1)
        
      return offsets
    
  except FileNotFoundError:
    return 'File not found'
  except Exception as e:
    print('An error occurred: ', e)
    return []
  
  
def find_offsets(sentence, keyword):
  offsets = []
  index = sentence.find(keyword) # 첫번째 위치 찾기
  print('first index: ', index)
  
  while index != -1: # index가 마지막 위치가 아닐 때 까지
    offsets.append(index)
    index = sentence.find(keyword, index+1)
    
  return offsets

# sentence = 'I like brown and brownie. Brown is my favorite color. Brown is the color of my dog.'
sentence = 'brown Brown Brown brown'
print(find_offsets(sentence, 'Brown'))