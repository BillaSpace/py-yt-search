# 🎵 py-yt-search 💠

An **unofficial advanced version** of the original [`py_yt_search`](https://pypi.org/project/py-yt-search/) library by **Prakhar Shukla**.  
This version introduces **improved query handling, better URL-based lookups**, and refined search results.

> ⚠️ This repository is an **unofficial GitHub version** of the `py_yt_search` package, which is originally published only as a `.whl` (wheel) or via PyPI (`pip install py-yt-search`).

---

## 🌐 Repository

👉 **GitHub:** [billaspace/py-yt-search](https://github.com/billaspace/py-yt-search)

You Can include this Repository In Your python Project's Requirements.txt simply by:
```git+https://github.com/BillaSpace/py-yt-search.git```
Or
You can directly clone this repo and install locally:
```bash
git clone https://github.com/billaspace/py-yt-search.git
cd py-yt-search
pip install .



---

🚀 Installation

From PyPI

pip install py-yt-search

From GitHub (recommended unofficial version )

pip install git+https://github.com/billaspace/py-yt-search.git


---

🧠 Features

Enhanced YouTube search precision.

Optimized handling for both query-based and URL-based searches.

Minimal dependencies and fast async responses.

Returns structured metadata (title, thumbnails, duration, etc.).

supports channels,artists,playlist search too

---

💻 Example Usage

from py_yt_search import Search

results = Search("Alan Walker Faded").fetch()
for video in results:
    print(video["title"], "-", video["duration"])

Or with URL:

from py_yt_search import Search

video = Search("https://www.youtube.com/watch?v=60ItHLz5WEA").fetch_one()
print(video["title"], video["views"])


---

📦 Project Info

Original Author: Prakhar Shukla

Unofficial Maintainer: billaspace

License: MIT

Python Compatibility: 3.8+



---

❤️ Acknowledgements

Big thanks to the original Devloper of py-yt-search for the original py_yt_search module,
and to the open-source community for continued improvements.


---

🏗️ Note

This project is not affiliated with or endorsed by YouTube or the original author.
It’s a community-maintained enhancement for developers seeking better control and stability
 & does not Infringe/Accociates Any Data of Any individuals.
