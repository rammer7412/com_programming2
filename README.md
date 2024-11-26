# com_programming2
This is the repository for submitting the assignment of Computer Programming II that is the course of Korea University


11월 22일

각 모듈이 수행하는 내용

Alpha module : Beta module과 Gamma module을 import하여 결과를 출력

Beta module : csv파일을 읽고 필요한 데이터를 추출하여 return

Gamma module : 입력받은 데이터를 기반으로 그래프를 클래스나 그리는 데 필요한 함수 제작

역할 분담

Alpha : 서은찬

Beta : 이종원

Gamma : 배세강

11월 23일
Beta 모듈 초안 작성 완료

import하고 get_data() 함수를 실행하면, data_preprocessing을 반환한다.

data_preprocessing의 자료형은 딕셔너리이며, 데이터의 년도는 key = year를 입력하면 구할 수 있다. 
year를 제외한 모든 key는 시험 과목 유형(물리학 I이면 과학탐구가 아닌 물리학 I이 key값이다)이며 각 key값에 담겨 있는 value는 pandas 데이터 프레임 형태로 0번째 열 : 표본점수 | 1번째 열 : 남자 | 2번째 열 : 여자 이다.