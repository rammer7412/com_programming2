import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import Beta

def graph(data):
    data_pyojum=data['표준점수']
    data_men=data['남자']
    data_women=data['여자']
    plt.plot(x=data_pyojum,y=data_men)
    plt.plot(x=data_pyojum,y=data_women)
    plt.show()




if __name__ == "__main__":
    print("이 모듈은 직접 실행되었습니다.")