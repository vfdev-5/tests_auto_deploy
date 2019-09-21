[![Build Status](https://travis-ci.org/vfdev-5/tests_auto_deploy.svg?branch=master)](https://travis-ci.org/vfdev-5/tests_auto_deploy)

https://vfdev-5.github.io/tests_auto_deploy/

# Tests auto deploy


A repository to test artifacts auto build/upload on conda and pipy on tagging the code.

Deployment is executed with Travis. See [.travis.yml](.travis.yml)


## Installation

From `test.pypi`
```bash
pip install --index-url https://test.pypi.org/simple/ check-auto-deploy
```
and from conda
```bash
conda install -c vfdev-5 check-auto-deploy
```
