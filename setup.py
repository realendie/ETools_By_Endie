from setuptools import setup, find_packages

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name="EToolsbyEndie",
    url="https://github.com/realendie/ETools_By_Endie",
    author="Wyatt Johnson",
    author_email="enderprooffical@gmail.com",
    license="MIT",
    license_files="LICENSE",
    version="1.1.1",
    packages=find_packages(),
    install_requires=[
        "ffmpeg==1.4",
    ],
    keywords=[
        "python",
        "utility",
        "youtube",
        "tools",
        "downloader",
        "video",
        "audio",
        "converter",
        "mp3",
        "mp4",
        "youtube-dl",
        "yt-dlp",
        "ffmpeg",
    ],
    short_description="ETools is an open-source python package that allows you to many things with ease, using command prompt.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "download_video = ETools:download_video",
            "convert_file = ETools:convert_file",
        ]
    },
)
