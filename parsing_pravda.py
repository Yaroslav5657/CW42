from pprint import pprint
from parsing import parse


base_url = "https://www.pravda.com.ua"
news = parse(
    base_url,
    [
        ".article_header > a",
        ".post__text > p",
    ],
)
pprint(news)
