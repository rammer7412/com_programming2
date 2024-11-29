# com_programming2

This is the repository for submitting the assignment of Computer Programming II that is the course of Korea University


# 각 모듈이 수행하는 내용

Alpha module (main module) : Beta module과 Gamma module을 import하여 결과를 출력

Beta module : csv파일을 읽고 필요한 데이터를 추출하여 return

Gamma module : 입력받은 데이터를 기반으로 그래프를 클래스나 그리는 데 필요한 함수 제작

# 역할 분담

Alpha : 서은찬

Beta : 이종원

Gamma : 배세강

# Alpha 모듈 해결 방안
Alpha module에서는 Beta module에서 데이터를 전달받아 .keys()를 활용하여 준비된 파일 내의 과목명들만을 출력한 후에 Beta module에서 전달받았던 pandas의 데이터 프레임 자료형을 그대로 Gamma module의 graph함수의 입력값으로 넣음으로써 그래프를 출력하였다.

# Beta 모듈 해결 방안
영역과 유형 열에 있는 과목명에 따라 표준점수, 남자, 여자 열의 정보만을 추출한다. 이때 추출한 자료의 자료형은 pandas의 데이터프레임이다. 이후 딕셔너리 자료형인 data_preprocessing에 key 값을 과목명으로 설정하고 value에 앞서 구한 데이터 프레임을 넣어준다. 위 과정을 모든 과목에 대해서 진행한다.

그리고 year를 key 값으로 하고 value에 2024를 넣어준다.

마지막으로 get_data함수를 구현하여 다른 모듈에서 해당 함수를 실행하면 data_preprocessing을 반환한다.


# Gamma 모듈 해결 방안
Alpha에서 데이터를 넘겨주면 그것들을 x와 y에 적절하게 넣어준 후 이를 matplotlib을 이용해 그래프를 그리고자 했다. alpha가 데이터를 넘겨줄 것이기 때문에 함수로 구현하고자 했다.
또한 과목별로 제목이 바뀌어야 하기 때문에 f-string을 이용하였다. 그 외에는 범례, 창 제목, 글꼴 등의 부가적인 요소를 추가하면 될 것이라 생각했다.