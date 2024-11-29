import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def graph(data):
    data_pyojum = data['표준점수']
    data_men = data['남자']
    data_women = data['여자']

    plt.plot(data_pyojum, data_men, label="남자")
    plt.plot(data_pyojum, data_women, label="여자")

    plt.xlabel("표준점수")
    plt.ylabel("점수")
    plt.title("남자와 여자 점수 비교")
    plt.legend()
    plt.show()



if __name__ == "__main__":
    print("이 모듈은 직접 실행되었습니다.")