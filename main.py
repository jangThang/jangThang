import feedparser, datetime

tistory_blog_uri="https://star7sss.tistory.com" #Your blog address here
feed = feedparser.parse(tistory_blog_uri+"/rss")

MAX_POST_NUM = 10

markdown_text = """## Hello World! 🖐

[Google](https://google.com" target="_blank) test

📬 Contact Email : star7sss@naver.com

👨‍💻 Tech Blog : https://star7sss.tistory.com

🤪 Daily Blog : https://blog.naver.com/star7sss

[![Portfolio](https://img.shields.io/badge/Portfolio-%23000000.svg?style=for-the-badge&logo=firefox&logoColor=#FF7139)](https://fern-way-13f.notion.site/Jang-Thang-3b7b327981a2456c8ee5952eadb848b9)

[![github stats](https://github-readme-stats.vercel.app/api?username=jangThang&show_icons=true&hide_border=False)](https://star7sss.tistory.com)

[![solved.ac tier](http://mazassumnida.wtf/api/v2/generate_badge?boj=star7sss)](https://solved.ac/star7sss)

## 📋 [Recent blog posts]
""" # list of blog posts will be appended here



for i, feed in enumerate(feed['entries']):
    if i > MAX_POST_NUM:
        break
    dt = datetime.datetime.strptime(feed['published'], "%a, %d %b %Y %H:%M:%S %z").strftime("%b %d, %Y")
    markdown_text += f"[{feed['title']}]({feed['link']}) - {dt}<br>\n"
    print(feed['link'], feed['title'])

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
