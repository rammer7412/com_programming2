import Beta
import Gamma

data = Beta.get_data()
year = list(data.keys())

print(year,'학년도 과목명>')
for i in range(len(year)):
    print(f'{i + 1}. {year[i]}')
print()

choice = input('원하시는 과목명을 입력해주세요 : ')
Gamma.graph(choice, data[choice])