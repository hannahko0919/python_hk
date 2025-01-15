#사용자가 3과목의 시험 점수를 입력하면 총점과 평균,통과여부를 출력하는 프로그램 모듈

def totalscore(s1,s2,s3):
    hap=s1+s2+s3
    return hap

if '__name__'=='__main__':
    print(totalscore(100,25,36))

def averscore(s1,s2,s3):
    return (s1+s2+s3)/3

def passfail(s1,s2,s3):
    avg=(s1+s2+s3)/3
    if avg>=60 and s1>=40 and s2>=40 and s3>=40:
        return 'pass'
    else:
        return 'fail'
