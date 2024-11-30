import pandas as pd

data = pd.read_csv('20231231_utf8bom.csv')

data_preprocessing = {}
data_preprocessing['year'] = 2024
check = set()

for subjects in data['유형'] :
    if subjects in check :
        continue
    else :
        data_preprocessing[subjects] = data.loc[data['유형'] == subjects, ["표준점수","남자","여자"]]
        check.add(subjects)
        
def get_data() :
    return data_preprocessing

if __name__ == "__main__":
    print("이 모듈은 직접 실행되었습니다.")
    print(data_preprocessing)