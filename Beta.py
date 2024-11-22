import pandas as pd

data = pd.read_csv('20231231_utf8bom.csv')

data_preprocessing = {}
data_preprocessing['year'] = 2023

 
data_preprocessing['국어'] = data.loc[data['영역'] == "국어", ["표준점수","남자","여자"]]
data_preprocessing['수학'] = data.loc[data['영역'] == "수학", ["표준점수","남자","여자"]]
data_preprocessing['생활과 윤리'] = data.loc[data['유형'] == "생활과 윤리", ["표준점수","남자","여자"]]
data_preprocessing['윤리와 사상'] = data.loc[data['유형'] == "윤리와 사상", ["표준점수","남자","여자"]]
data_preprocessing['한국지리'] = data.loc[data['유형'] == "한국지리", ["표준점수","남자","여자"]]
data_preprocessing['세계지리'] = data.loc[data['유형'] == "세계지리", ["표준점수","남자","여자"]]
data_preprocessing['동아시아사'] = data.loc[data['유형'] == "동아시아사", ["표준점수","남자","여자"]]
data_preprocessing['세계사'] = data.loc[data['유형'] == "세계사", ["표준점수","남자","여자"]]
data_preprocessing['경제'] = data.loc[data['유형'] == "경제", ["표준점수","남자","여자"]]
data_preprocessing['사회·문화'] = data.loc[data['유형'] == "사회·문화", ["표준점수","남자","여자"]]
data_preprocessing['물리학 I'] = data.loc[data['유형'] == "물리학 I", ["표준점수","남자","여자"]]
data_preprocessing['화학 I'] = data.loc[data['유형'] == "화학 I", ["표준점수","남자","여자"]]
data_preprocessing['생명과학 I'] = data.loc[data['유형'] == "생명과학 I", ["표준점수","남자","여자"]]
data_preprocessing['지구과학 I'] = data.loc[data['유형'] == "지구과학 I", ["표준점수","남자","여자"]]
data_preprocessing['물리학 II'] = data.loc[data['유형'] == "물리학 II", ["표준점수","남자","여자"]]
data_preprocessing['화학 II'] = data.loc[data['유형'] == "화학 II", ["표준점수","남자","여자"]]
data_preprocessing['생명과학 II'] = data.loc[data['유형'] == "생명과학 II", ["표준점수","남자","여자"]]
data_preprocessing['지구과학 II'] = data.loc[data['유형'] == "지구과학 II", ["표준점수","남자","여자"]]
data_preprocessing['성공적인 직업생활'] = data.loc[data['유형'] == "성공적인 직업생활", ["표준점수","남자","여자"]]
data_preprocessing['농업 기초 기술'] = data.loc[data['유형'] == "농업 기초 기술", ["표준점수","남자","여자"]]
data_preprocessing['공업 일반'] = data.loc[data['유형'] == "공업 일반", ["표준점수","남자","여자"]]
data_preprocessing['상업 경제'] = data.loc[data['유형'] == "상업 경제", ["표준점수","남자","여자"]]
data_preprocessing['수산·해운 산업 기초'] = data.loc[data['유형'] == "수산·해운 산업 기초", ["표준점수","남자","여자"]]
data_preprocessing['인간 발달'] = data.loc[data['유형'] == "인간 발달", ["표준점수","남자","여자"]]

def get_data() :
    return data_preprocessing

if __name__ == "__main__":
    print("이 모듈은 직접 실행되었습니다.")
    print(data_preprocessing)