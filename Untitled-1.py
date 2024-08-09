
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
import string

# 下载NLTK数据
nltk.download('stopwords')

# 假设新闻标题存储在一个文本文件news_titles.txt中，每行一个标题
file_path = 'news_titles.txt'

# 读取文件内容
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# 文本预处理
stop_words = set(stopwords.words('english'))
stop_words.update(string.punctuation)
stop_words.update(['“', '”', '’', '...'])  # 添加更多的停用符号

# 生成词云
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='white',
    stopwords=stop_words,
    max_words=100,
    colormap='viridis'
).generate(text)

# 显示词云图
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
