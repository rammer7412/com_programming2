import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def graph(subject,data):
    data_pyojum = data['표준점수']
    data_men = data['남자']
    data_women = data['여자']
    plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.figure(num='컴퓨터프로그래밍II 과제',figsize=(10, 6)) 
    plt.plot(data_pyojum, data_men, label="남자")
    plt.plot(data_pyojum, data_women, label="여자")

    plt.xlabel("표준점수")
    plt.ylabel("학생 수")
    plt.title(f"2024학년도 수능 {subject}과목 분포")
    plt.legend()
    plt.show()



if __name__ == "__main__":
    print("이 모듈은 직접 실행되었습니다.")