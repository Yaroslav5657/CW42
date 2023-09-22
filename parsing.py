from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from typing import Iterable, List, Dict


def parse(
    url: str,
    selectors: Iterable,
    parser: str = "html.parser",
    limit: int = 4,
) -> List[Dict]:
    assert isinstance(selectors, (Iterable,))
    assert len(selectors) == 2
    assert isinstance(limit, int), "Wrong parameter type, use Integer instead"
    assert limit > 0, "Too low limit"
    news_url = f"{url}/news"
    headers_selector, posts_selector = selectors
    with urlopen(news_url) as r:
        soup = bs(r.read(), parser)
    headers = soup.select(headers_selector)
    assert limit < len(headers)
    news = []
    for item in headers[:limit]:
        header = item.text
        link = item.get("href")
        new_link = link if link.startswith("http") else url + link

        with urlopen(new_link) as _:
            soup = bs(_.read(), parser)
            text = soup.select(posts_selector)
            article_body = []
            for i in text:
                p = i.text
                p.replace(":", " -> ")
                p.strip()

                article_body.append(f"{p}\n")
            article_text = "".join(article_body)
            article_text = article_text

            news.append(
                {
                    "header": header.strip(),
                    "link": new_link,
                    "article": article_text,
                }
            )

    return news
