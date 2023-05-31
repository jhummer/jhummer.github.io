Title: Pyenv
Date: 2023-05-30
Category: Python
Tags: python, pyenv, pip
Summary: Managing Python versions
HEADER_COVER: images/the-snake.jpg

## Managing Python versions

![https://xkcd.com/1987/](/images/python_environment_xkcd.png)

I've found myself surrounded by different python versions in my system a few times. OSX used to ship with python2.7 and I have installed python3 via brew, python.org etc. and manually aliased python in my **.bashrc** or **.zshrc**. Various different approaches which seemed to work for a while. 

But for some reasons I cant find the package I just installed via pip. `＼(〇_ｏ)／`

The last time I had problems the path to python resided in a xcode path on my macOS Ventura. When this has occurred I feel so frustrated for not having a clean system. 

Luckily, there exists a tool for keeping track of installed versions and installing them the right way: [Pyenv](https://github.com/pyenv/pyenv){:target="_blank"}. 

I found it myself via [this](https://opensource.com/article/19/5/python-3-default-mac){:target="_blank"} great article by [Matthew Broberg](https://opensource.com/users/mbbroberg){:target="_blank"} and [Moshe Zadka](https://opensource.com/users/moshez){:target="_blank"} from which this info is all taken from.

## Requirements

Install **pyenv** via brew 

`brew install pyenv`

## Usage

It's simple, install Python version of choice with, ex.

`pyenv install 3.10.11`

To set our newly installed Python version globally run

`pyenv global 3.10.11`

Verify via 

`pyenv version`

`3.10.11 (set by /Users/jocke/.pyenv/version)`

Now we need to add the following to our shell config file, I use `zsh` with the `.zshrc` config file:

`echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.zshrc`

Verify that the `.zshrc` now contains

```bash
if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
fi
```

All is good. 