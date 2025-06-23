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
    version="2.0.0",
    packages=find_packages(),
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
    ],
    install_requires=[
        "ffmpeg==1.4",
        "pyfiglet==1.0.3",
    ],
    short_description="EToolsByEndie is a Python utility that allows user to download YouTube videos off the web and convert files to other file formats using ffmpeg.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "download_video = ETools:download_video",
            "convert_file = ETools:convert_file",
        ]
    },
)
