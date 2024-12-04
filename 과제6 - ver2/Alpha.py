import Beta
import Gamma

data = Beta.get_data()
year = data.keys()

print(f'연도 선택 ({", ".join(map(str, year))})')
print()
choice_year = int(input('원하시는 연도를 입력해주세요 : '))
print()

subject = list(data[choice_year].keys())

print(f'<{choice_year}학년도 수능 과목>')
for i in range(len(subject)):
    print(f'{i + 1}. {subject[i]}')
print()
choice_subject = subject[int(input('원하시는 과목의 번호를 입력해주세요 : ')) - 1]

Gamma.graph(choice_subject, data[choice_year][choice_subject])