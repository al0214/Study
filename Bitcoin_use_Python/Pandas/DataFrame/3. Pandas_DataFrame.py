import pandas as pd
import requests

url = "https://finance.naver.com/item/sise_day.nhn?code=066570" 
df = pd.read_html(requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text)
## 네이버 주식을 가져올때는 requests를 사용하여 헤더에 User-agent': 'Mozilla/5.0을 추가해야 가져올 수 있다.

print(df[0].dropna(axis=0))
# NaN은 네이버 금융 페이지의 HTML Table의 숨겨진 코드 때문에 NaN이 발생 함으로 dropna 함수를 사용하여 행을 삭제합니다.
#  dropna 함수는 NaN 값이 1개라도 포함된 행이나 열을 설정하여 모두 제거한다.


## 추가 설명 ##

# subset 인자 : 특정 열 기준 NaN 값 탐색 제거
# 모든 결측값을 대상으로 행을 제거하는 것이 아닌,

# 특정 열의 위치에서 결측치가 등장할 경우에만 행을 제거하고 싶다면

# subset 인자 내에 결측값 탐색을 원하는 열들의 이름을 리스트로 지정해주시면 됩니다.

 

# 예를 들어, B열에서 NaN 값이 관측되는 행을 제거하고 싶은 경우 예시는 아래와 같습니다.

# df.dropna(subset = ['B'])

# 만일, 결측치 등장 열을 기준으로 제거를 진행하고 있는 경우에는

# subset에 column 이름 대신 index 목록을 적어서 특정 행 위치 결측치 탐색이 가능합니다.

#  how 인자 : 모든 값이 결측치인 경우만 제거 여부 지정
# 기존에는 하나 이상의 값만 결측치여도 해당 행이 제거되었는데,

# 만일 모든 값이 전부 NaN인 행만 제거하고 싶은 경우에는 how 인자를 'all'로 설정하면 됩니다.

# df.dropna(how = 'all')

# 모든 값이 전부 NaN인 첫번째 행만 지워진다

# axis 인자 : 결측치 포함 열 제거 경우 지정
# 결측치를 포함하고 있는 행 대신 열 방향으로 제거하고 싶은 경우

# axis 인자를 1 혹은 'columns'로 지정해주시면 됩니다.

# 이번에는 위에서 사용한 예제와 다른 df2 데이터프레임을 예시로 들어보겠습니다.

# b = {'D' : [1, 2, 3], 'E' : [np.nan, 2, 3], 'F' : [np.nan, np.nan, np.nan]}
# df2 = pd.DataFrame(b)
