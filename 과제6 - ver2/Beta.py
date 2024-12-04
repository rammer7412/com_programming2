import pandas as pd

data_preprocessing = {}
for year in range(2020,2024) :
    loc = str('과제6 - ver2')+'\\'+str(year) +'1231utf8bom.csv'
    data = pd.read_csv(loc)
    temp = {}
    check = set()

    for subjects in data['유형'] :
        if subjects in check :
            continue
        else :
            temp[subjects] = data.loc[data['유형'] == subjects, ["표준점수","남자","여자"]]
            check.add(subjects)
    data_preprocessing[year] = temp
        
def get_data() :
    return data_preprocessing

if __name__ == "__main__":
    print("이 모듈은 직접 실행되었습니다.")
    print(data_preprocessing)