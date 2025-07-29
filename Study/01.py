# 인터럽트 예제

import signal
import time


# 핸들러 함수 정의
def handle(signum, frame):
    print("키보드 인터럽트 감지")
    print("신호 번호:", signum)
    print("스택 프레임:", frame)
    exit()


# handle로 등록해야 함
signal.signal(signal.SIGINT, handle)

# 무한 루프
while True:
    print("5초 간격으로 출력 중...")
    time.sleep(5)
