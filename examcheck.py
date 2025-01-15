# 1) import examCalculator
# 2) import examCalculator as exC
from examCalculator import *

print('세 과목의 총점,평균,통과여부')

s1=int(input('과목 1의 점수: '))
s2=int(input('과목 2의 점수: '))
s3=int(input('과목 3의 점수: '))

# 1) print(f'세 과목의 총점: {examCalculator.totalscore(s1,s2,s3)}')

# 1) print(f'세 과목의 평균: {examCalculator.averscore(s1,s2,s3):.2f}')

# 1) print(f'세 과목의 통과여부: {examCalculator.passfail(s1,s2,s3)}')

# 2) print(f'세 과목의 총점: {exC.totalscore(s1,s2,s3)}')

# 2) print(f'세 과목의 평균: {exC.averscore(s1,s2,s3):.2f}')

# 2) print(f'세 과목의 통과여부: {exC.passfail(s1,s2,s3)}')

print(f'세 과목의 총점: {totalscore(s1,s2,s3)}')

print(f'세 과목의 평균: {averscore(s1,s2,s3):.2f}')

print(f'세 과목의 통과여부: {passfail(s1,s2,s3)}')
