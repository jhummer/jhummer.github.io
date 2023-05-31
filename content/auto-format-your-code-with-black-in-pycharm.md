Title: Auto-format your code with Black in PyCharm
Date: 2023-05-30
Category: Python
Tags: python, black, pycharm
Summary: Let's configure PyCharm to auto-format code with black
HEADER_COVER: images/any-color-as-long-as-its-black.jpg

## Intro

Good formatting keeps your code readable, tidy and uniform. Having a formatting standard doesn't only look good, it helps your teammates avoid confusion and wild discussions about how to format the code.

[Black](https://black.readthedocs.io/){:target="_blank"} is the *uncompromising code formatter*. It's a no-brainer that takes care of making your code compliant to [PEP 8 - Style Guide for Python](https://peps.python.org/pep-0008/){:target="_blank"}. Black takes all the formatting decisions, and you can focus on your programming instead.

In this article we will look at how to configure PyCharm to auto-format your code with **black** and the **blackd** server.

## Prerequisites

Install *black* and the *blackd* HTTP server with pip:

`pip install 'black[d]'`

Now you're good to go, lets fix our favorite IDE to use **black**

## Configure PyCharm

Go to *Settings* -> *Plugins*.

Search and install the **BlackConnect** plugin.

![BlackConnect](/images/pycharm-blackconnect.png)

Lets configure the BlackConnect plugin to auto-format on file changes. 

Go to *Tools* -> *BlackConnect*

![BlackConnect](/images/pycharm-blackconnect-edit.png)

#### Trigger Settings:

- [x] Trigger when saving changed files 

#### Local instance (shared between projects):

- [x] Start local blackd instance when plugin loads

Click *Detect* to get the path to *blackd* 

(if not found you need to enter it manually. A simple `which blackd` in the terminal should give you the correct path.) 

Click *Start* to start the blackd server, then you're all set. Click *OK*

From now on, PyCharm will trigger auto-formatting your files via black when you save them. PyCharm will also make sure blackd is running when you restart PyCharm etc. Very nice!

(**Pro-tip**: find a nice repo and save, commit, push some files to quickly become the main contributor. Teammates will love you.)

`( •_•)>⌐■-■ (⌐■_■)`


