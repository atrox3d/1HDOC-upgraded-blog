import requests
import json
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)

URL = "https://api.npoint.io/0067e63917ca7a5034d9"


@dataclass
class BlogPost:
    id: int
    body: str
    date: str
    title: str
    author: str
    subtitle: str


def call_api(url, params=None):
    logger.info(f"GET {url} with params: {params}")
    response = requests.get(url, params)
    response.raise_for_status()
    return response.json()


def gest_posts(url, params=None):
    data = call_api(url, params)
    posts = [BlogPost(**item) for item in data]
    return posts


def get_post(id, url, params=None):
    for post in gest_posts(url, params):
        if post.id == id:
            return post
    return None


if __name__ == '__main__':
    logging.basicConfig(level=logging.NOTSET)
    url = URL
    data = call_api(url)
    print(json.dumps(data, indent=4))
    post = BlogPost(**data[0])
    print(post)

    print(get_post(1, URL))
