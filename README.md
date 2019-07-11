<h1 align="center">
  <a href="https://github.com/f-prime/fist">Fist</a> python client</br>
  <sub>Python client library for Fist full text search</sub>
</h1>
  
<p align="center">
  <a href="https://travis-ci.org/dyne/fistpy">
    <img src="https://travis-ci.org/dyne/fistpy.svg?branch=master" alt="Build Status">
  </a>
  <a href="https://codecov.io/gh/dyne/fistpy">
    <img src="https://codecov.io/gh/dyne/fistpy/branch/master/graph/badge.svg" alt="Code coverage"/>
  </a>
  <a href="https://pypi.org/project/fistpy/">
    <img alt="PyPI" src="https://img.shields.io/pypi/v/fistpy.svg" alt="Latest release">
  </a>
  <a href="https://dyne.org">
    <img src="https://img.shields.io/badge/%3C%2F%3E%20with%20%E2%9D%A4%20by-Dyne.org-blue.svg" alt="Dyne.org">
  </a>
</p>

<br><br>

<h4 align="center">
  <a href="#floppy_disk-install">:floppy_disk: Install</a>
  <span> • </span>
  <a href="#video_game-quick-start">:video_game: Quick start</a>
  <span> • </span>
  <a href="#heart_eyes-acknowledgements">:heart_eyes: Acknowledgements</a>
  <span> • </span>
  <a href="#busts_in_silhouette-contributing">:busts_in_silhouette: Contributing</a>
  <span> • </span>
  <a href="#briefcase-license">:briefcase: License</a>
</h4>


:construction: [Fist](https://github.com/f-prime/fist) is a software in **ALPHA stage** and is heavily under development. So is this tiny wrapper.

This library attempts to provide a very simple wrapper around the [Fist](https://github.com/f-prime/fist) a fast full-text search and index server.
This library has also only been tested under Python 3.


<details>
 <summary><strong>:triangular_flag_on_post: Table of Contents</strong> (click to expand)</summary>

* [Install](#floppy_disk-install)
* [Quick start](#video_game-quick-start)
* [Acknowledgements](#heart_eyes-acknowledgements)
* [Contributing](#busts_in_silhouette-contributing)
* [License](#briefcase-license)
</details>

***
## :floppy_disk: Install

`pip install fistpy `

***
## :video_game: Quick start

```python

from fist.client import Fist

f = Fist(host="localhost", port=5575)
f.index("document_1 Some text that I want to index")
f.index("document_2 Some other text that I want to index")
result = f.search("text")

print(len(result), result) # 2 ['document_1', 'document_2']

```

***
## :heart_eyes: Acknowledgements

Copyright :copyright: 2019 by [Dyne.org](https://www.dyne.org) foundation, Amsterdam

Designed, written and maintained by Puria Nafisi Azizi.

Special thanks to the [Fist](https://github.com/f-prime/fist) authors and contributors.


***
## :busts_in_silhouette: Contributing

1.  :twisted_rightwards_arrows: [FORK IT](../../fork)
2.  Create your feature branch `git checkout -b feature/branch`
3.  Commit your changes `git commit -am 'Add some fooBar'`
4.  Push to the branch `git push origin feature/branch`
5.  Create a new Pull Request
6.  :pray: Thank you


***
## :briefcase: License
    Copyright 2019 Dyne.org foundation, Amsterdam
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
        http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
