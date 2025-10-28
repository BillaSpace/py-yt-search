from setuptools import setup, find_packages

setup(
    name="py_yt_search",
    version="0.3",
    author="Prakhar Shukla",
    maintainer="billaspace",
    author_email="",
    description="Unofficial enhanced version of py_yt_search with improved query and URL-based search handling.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/billaspace/py-yt-search",
    project_urls={
        "Source": "https://github.com/billaspace/py-yt-search",
        "Original": "https://pypi.org/project/py-yt-search/",
    },
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Intended Audience :: Developers",
    ],
    keywords=["youtube", "search", "yt", "py_yt_search", "ytsearch"],
    install_requires=[],
)
