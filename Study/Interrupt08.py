# 내 파이썬 프로그램의 이름을 알아보자.
import os

import psutil

# 현재 프로세스 객체 가져오기
current_process = psutil.Process(os.getpid())

# 전체 경로 출력
full_path = current_process.exe()
print("전체 경로:", full_path)

# 실행 중인 프로세스 이름 출력
print("실행 중인 이름:", current_process.name())

# 현재 실행된 Python 스크립트 파일 이름
print("현재 스크립트 이름:", os.path.basename(__file__))
