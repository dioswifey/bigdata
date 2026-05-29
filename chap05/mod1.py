def sum(a,b):
    return a + b

def safe_sum(a,b):
    if type(a) != type(b):
        print("더할 수 있는 값이 아닙니다.")
        return 
    else:
        return sum(a,b)
    
print(safe_sum('a',1))  #에러발생을 테스트하는거
print(safe_sum(1,4))
print(sum(10,10.4))

#if문을 사용해서 
if __name__ == "main":  # 직접 실행했을때
    print(safe_sum('a',1))  #에러발생을 테스트하는거
    print(safe_sum(1,4))
    print(sum(10,10.4))


