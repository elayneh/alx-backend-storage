#!/usr/bin/env python3
""" Implementing an expiring web cache and tracker
    obtain the HTML content of a particular URL and returns it """
import redis
import requests
r = redis.Redis()


def get_page(url: str) -> str:
    count = 0
    """ track how many times a
    particular URL was accessed in the key count:{url} """
    r.set(f"cached:{url}", count)
    resp = requests.get(url)
    r.incr(f"count:{url}")
    r.setex(f"cached:{url}", 10, r.get(f"cached:{url}"))
    return resp.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
