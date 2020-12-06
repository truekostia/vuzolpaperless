[ en | [de](README-de.md) | [el](README-el.md) ]

![Paperless](https://raw.githubusercontent.com/the-paperless-project/paperless/master/src/paperless/static/paperless/img/logo-dark.png)

[![Documentation](https://readthedocs.org/projects/paperless/badge/?version=latest)](https://paperless.readthedocs.org/)
[![Chat](https://badges.gitter.im/the-paperless-project/paperless.svg)](https://gitter.im/danielquinn/paperless)
[![Travis](https://travis-ci.org/the-paperless-project/paperless.svg?branch=master)](https://travis-ci.org/the-paperless-project/paperless)
[![Coverage Status](https://coveralls.io/repos/github/the-paperless-project/paperless/badge.svg?branch=master)](https://coveralls.io/github/the-paperless-project/paperless?branch=master)
[![StackShare](https://img.shields.io/badge/tech-stack-0690fa.svg?style=flat)](https://stackshare.io/the-paperless-project/the-paperless-project)
[![Thanks](https://img.shields.io/badge/THANKS-md-ff69b4.svg)](https://github.com/the-paperless-project/paperless/blob/master/THANKS.md)

Index and archive all of your scanned paper documents

## How it Works

Paperless does not control your scanner, it only helps you deal with what your scanner produces

1. Buy a document scanner that can write to a place on your network.  If you need some inspiration, have a look at the [scanner recommendations](https://paperless.readthedocs.io/en/latest/scanners.html) page.
2. Set it up to "scan to FTP" or something similar. It should be able to push scanned images to a server without you having to do anything.  Of course if your scanner doesn't know how to automatically upload the file somewhere, you can always do that manually.  Paperless doesn't care how the documents get into its local consumption directory.
3. Have the target server run the Paperless consumption script to OCR the file and index it into a local database.
4. Use the web frontend to sift through the database and find what you want.
5. Download the PDF you need/want via the web interface and do whatever you like with it.  You can even print it and send it as if it's the original. In most cases, no one will care or notice.

