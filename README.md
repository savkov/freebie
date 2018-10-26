# Freebie
_A free database of news resources for information extraction_

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


### Resources

- `websources`: a list of news outlet web sites
    - source_id
    - name
    - language
    - cca (country code)
    - coverage (global, national, local)
    - covered_area
    - url
- `twitter_handles`: a list of twitter handles of news outlets
    - handle_id
    - name
    - handle
    - cca (country code)
    - language
    - source_id
    - source_url
    - category    
- `rss_feeds`: a list of RSS feeds of news outlets
    - feed_id
    - source_id
    - name
    - feed_name
    - language
    - cca (country code)
    - coverage (global, national, local)
    - covered_area
    - url
    - rss_url

### Usage

Import each of the three resources as a list of dictionaries.

```python
from freebie import websources

for resource in websources[:1]:
    print(resource)
# {'source_id': '1', 'name': '3BL', 'language': 'en', 'cca': 'US', 'coverage': 'global', 'covered_area': 'world', 'url': 'https://www.3blmedia.com/'}
```


### Contribution

All contributions are wellcome. I'd be happy to review PRs or to receive any data that you would want added via [email](mailto:me@sasho.io).
