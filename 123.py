import requests
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import re

# Step 1: 使用NewsAPI获取最近15天内的全球新闻标题
api_key = '51088ea567704637865bf77ff73ccbd0'
url = 'https://newsapi.org/v2/everything'
params = {
    'q': '',  # 空查询以获取所有新闻
    'from': '2023-07-14',  # 15天前的日期
    'to': '2023-07-29',    # 当前日期
    'language': 'en',
    'sortBy': 'publishedAt',
    'apiKey': api_key
}

response = requests.get(url, params=params)
news_data = response.json()

# Step 2: 处理和清理新闻标题数据
titles = [article['title'] for article in news_data['articles']]
titles_str = ' '.join(titles)

# 去掉非字母字符并转换为小写
cleaned_titles = re.sub(r'[^a-zA-Z\s]', '', titles_str).lower()

# Step 3: 计算词频
words = cleaned_titles.split()
stopwords = set(WordCloud().stopwords)
words = [word for word in words if word not in stopwords]

word_counts = Counter(words)

# Step 4: 绘制词云图
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_counts)

# 显示词云图
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
