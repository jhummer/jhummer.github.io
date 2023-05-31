Title: Pelican deploy to GitHub Pages
Date: 2023-05-30
Category: Python
Tags: python, pelican, github
Summary: Deploy Pelican to GitHub Pages
HEADER_COVER: images/pelican.jpg

## Intro

This is how I push my static content to GitHub Pages. At some time I will add more information here. Feel free to read the Pelican [docs](https://docs.getpelican.com/en/stable/tips.html#user-pages){:target="_blank"}.

## Requirements

A **Pelican** project, ready to deploy and **ghp-import** helper installed. 

## Usage

Generate the Pelican static content in *output* and push it to github

```
$ pelican content -o output -s pelicanconf.py
$ ghp-import output -b gh-pages
$ git push git@github.com:jhummer/jhummer.github.io.git gh-pages:gh-pages
```
