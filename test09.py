# 모듈은 파일명 패키지는 폴더명
import glob
import os
import random
import statistics as sts
from urllib.request import urlopen
from datetime import date
from datetime import datetime

print(os.getcwd())  # get current working directory
os.chdir('c:/PythonStudy/')  # change working directory
print(os.getcwd())
print(dir(os))
os.chdir('c:/PythonStudy/Project01')
print(glob.glob('*.py'))

print(random.choice(['John', 'Jane', 'James', 'Johanson', 'Joey']))
print(random.sample(range(1, 45), 6), '+', random.sample(range(1, 9), 1))
print(sts.mean([1, 2, 3, 4, 5]))
f = urlopen('https://www.naver.com')

now = date.today()
now1 = datetime.today()
print(now)
print(now1.strftime('%Y%m%d %H%M%S'))
