# -*- coding: utf-8 -*-
"""
Project Name: zyt_auto_tools
File Created: 2025.01.02
Author: ZhangYuetao
File Name: setup.py
Update: 2025.01.23
"""

from setuptools import setup, find_packages

# 读取 README.md 文件内容作为长描述
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# noinspection PyInterpreter
setup(
    name="zyt_auto_tools",
    version="0.2.3",
    author="ZhangYuetao",
    author_email="zhang894171707@gmail.com",
    description="A collection of automation tools for Python projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VerySeriousMan/zyt_auto_tools",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[],
    entry_points={
        "console_scripts": [
            "auto-generate-init=zyt_auto_tools.auto_generate_init:main",
            "auto-init-python-file=zyt_auto_tools.auto_init_python_file:main",
            "auto-update-ctime=zyt_auto_tools.auto_update_ctime:main",
        ],
    },
)
