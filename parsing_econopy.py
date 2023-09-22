from pprint import pprint
from parsing import parse


news = parse(
    "https://www.epravda.com.ua",
    [
        ".article__title > a",
        ".post_text > p",
    ],
)
pprint(news)
