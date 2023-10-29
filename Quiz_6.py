while True:
    rrn=input('주민번호를 입력해주세요.')
    add=0
    code=[2,3,4,5,6,7,8,9,2,3,4,5]
    if len(rrn)==13:
        for i in range(12):
            add = add+int(rrn[i])*code[i]
        result = 11 - (add % 11)
        if result >= 10:
            result_2=result%10
            if result_2 == int(rrn[-1]):
                print('유효한 주민번호입니다.')
            else:
                print('주민번호가 유효하지 않습니다.')
        else:
            if result == int(rrn[-1]):
                print('알맞은 주민번호입니다.')
            else:
                print('주민번호가 유효하지 않습니다.')
    else:
        print('주민번호를 다시 입력해주세요.')
