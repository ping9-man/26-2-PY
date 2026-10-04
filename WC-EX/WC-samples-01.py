# %% [code]
# 셀 1: wordcloud 패키지 설치
# 주피터 노트북의 명령어(pip)는 스크립트 환경에 따라 앞에 느낌표(!)를 붙이거나 터미널에서 실행해야 할 수 있습니다.
!pip install wordcloud

# %% [code]
# 셀 2: 필요한 라이브러리 임포트
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# %% [code]
# 셀 3: 워드클라우드 생성 및 시각화 (노트북 출력 결과에 기반한 예시 코드)
# 텍스트 데이터를 정의한 후 아래와 같이 워드클라우드를 생성하고 시각화할 수 있습니다.
# text = "여기에 분석할 텍스트 데이터를 입력하세요."
# 
# wordcloud = WordCloud(
#     width=1200, 
#     height=1200, 
#     background_color='white'
# ).generate(text)
# 
# plt.figure(figsize=(12, 12))
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis('off')
# plt.show()

from wordcloud import WordCloud, STOPWORDS
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import platform
%matplotlib inline
 
text = open('C:/Users/Lucky/WordCloud/obama-speech-EN.txt', 'r', encoding="utf-8").read()
jesus_mask = np.array(Image.open('C:/Users/Lucky/WordCloud/image_02.png'))

stopwords = set(STOPWORDS)
stopwords.add("unto")
stopwords.add('ye')

path = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=path).get_name()
rc('font', family = font_name)
plt.figure(figsize=(12,12))
plt.imshow(jesus_mask, interpolation='bilinear')
plt.axis('off')
plt.show()
wc = WordCloud(background_color='white', max_words=2000, mask=jesus_mask,
               stopwords=stopwords)
wc = wc.generate(text)
wc.words_

plt.figure(figsize=(12,12))
