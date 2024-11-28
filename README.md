# com_programming2
This is the repository for submitting the assignment of Computer Programming II that is the course of Korea University


11 / 22
# 본격적인 프로그래밍에 앞서 상의를 통해 모듈을 셋으로 나누어 각자 역할을 분담하기로 결정.

Alpha module(서은찬) : Beta module과 Gamma module을 import하여 데이터를 주고받으며 최종 결과를 출력.

Beta module(이종원) : 준비된 csv파일을 읽고 필요한 데이터들을 추출하여 return.

Gamma module(배세강) : Alpha module로부터 입력받은 데이터를 기반으로 그래프를 그려 return.

11 / 24
Beta module 1차 프로그래밍 완료 : 그래프 작성에 필요한 데이터들을 추출하여 return.

11 / 27
Alpha module 1차 프로그래밍 완료 : Beta module을 import하여 데이터를 전달받아 존재하는 과목을 출력하고
사용자로부터 원하는 과목을 입력받음.

# 아래부터는 계획?
11 / 28
Gamma module 1차 프로그래밍 완료 : Alpha module로부터 입력받을 데이터를 기반으로 그래프를 그려 return.
Alpha module 2차 프로그래밍 완료 : 사용자로부터 입력받은 과목에 대한 그래프를 Gamma module로부터 return받아 출력.

11 / 29
전 모듈 최종 프로그래밍 완료 : 각자 최종적으로 본인 module을 점검하여 코드 간결화 진행.

data_preprocessing의 자료형은 딕셔너리이며, 데이터의 년도는 key = year를 입력하면 구할 수 있다. 
year를 제외한 모든 key는 시험 과목 유형(물리학 I이면 과학탐구가 아닌 물리학 I이 key값이다)이며 각 key값에 담겨 있는 value는 pandas 데이터 프레임 형태로 0번째 열 : 표본점수 | 1번째 열 : 남자 | 2번째 열 : 여자 이다.