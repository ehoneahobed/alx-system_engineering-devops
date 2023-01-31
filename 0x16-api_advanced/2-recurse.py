#!/usr/bin/python3

"""
a list containing the titles of all hot articles for a given subreddit
"""

from requests import get


def recurse(subreddit, hot_list=[], after=None):
    """
    function that queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit.
    """

    params = {'show': 'all'}

    if subreddit is None or not isinstance(subreddit, str):
        return None

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}

    url = 'https://www.reddit.com/r/{}/hot/.json?after={}'.format(subreddit,
                                                                  after)

    response = get(url, headers=user_agent, params=params)

    if (response.status_code != 200):
        return None

    results = response.json()

    try:
        c_data = results.get('data').get('children')
        after = results.get('data').get('after')

        if after is None:
            return hot_list

        for i in c_data:
            hot_list.append(i.get('data').get('title'))

        return recurse(subreddit, hot_list, after)
    except Exception:
        print("None")
