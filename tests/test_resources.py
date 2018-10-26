from freebie import websources, twitter_handles, rss_feeds


def test_resources():
    assert len(websources[0].keys()) == 7
    assert len(twitter_handles[0].keys()) == 8
    assert len(rss_feeds[0].keys()) == 10
    assert 'name' in websources[0].keys()
    assert 'name' in twitter_handles[0].keys()
    assert 'name' in rss_feeds[0].keys()
