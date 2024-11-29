import Beta
import Gamma

data = Beta.get_data()
subject = list(data.keys())[1:]
print('<과목명>')
print(f'{data['year']}학년도 과목명>')
for i in range(len(subject)):
    print(f'{i + 1}. {subject[i]}')
print()

choice = input('원하시는 과목명을 입력해주세요 : ')
print(data[choice])
Gamma.graph(choice, data[choice])