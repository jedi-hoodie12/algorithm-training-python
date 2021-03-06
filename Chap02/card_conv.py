def convert_str(x:int, r:int) -> str:
    """ 10진수인 정수 x를 r진수로 변환한 문자열을 반환 """

    conv_str = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rt_str = ''
    
    while x > 0:
        rt_str += conv_str[x % r]
        x = x // r
    
    return rt_str[::-1]

if __name__ == '__main__':
    """ 10진수를 n진수로 변환 """

    while True:
        x = int(input('음이 아닌 10진수 정수를 입력하시오 : '))
        if x > 0:
            break
    
    while True:
        n = int(input('변환하고싶은 진수로 2와 32사이의 값을 입력하시오 : '))
        if n >=2 and n <=32:
            break
    
    print(f'{x}를 {n}진수로 변환한 값은 {convert_str(x, n)}입니다.')