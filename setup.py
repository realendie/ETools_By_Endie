from setuptools import setup, find_packages

setup(
    name='ETools Youtube Downloader',
    author='Wyatt Johnson',
    author_email='enderprooffical@gmail.com',
    license='MIT',
    license_files='LICENSE',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'darkdetect==0.8.0',
        'packaging==24.2',
        'yt-dlp',
    ] 
)