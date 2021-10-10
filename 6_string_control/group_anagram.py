#Quiz
#문자열 배열을 받아 애너그램 단위로 그룹핑 하라.



from collections import defaultdict

def groupAnagrams(strs):
    dict = defaultdict(list) #비어있는 값이면 list로 초기화 시키기 위해 선언
    for word in strs :
        print(word, ''.join(sorted(word)))
        
        #dict[''.join(sorted(word))] = word //초기화이기에 덮어 씌우기가 됨
        
        dict[''.join(sorted(word))].append(word) #각 key의 value 값이 []로 초기화되서 추가 가능 
        #dict_items([('aet', ['eat', 'tea', 'ate']), ('ant', ['tan', 'nat']), ('abt', ['bat'])])
    
    return dict.values() 

 #입력
strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
#출력
#[["bat"],["nat","tan"],["ate","eat","tea"]]
