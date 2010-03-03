#!/usr/bin/env python

from distutils.core import setup

setup(
    name='nailbiter',
    version='1698c10c6eb8f3321f7825ac894fb2f4dbf6a1bf',
    description='thumbnail generation modeled after sorl-thumbnail, plays nice with storage backends',
    author='Matt Dennewitz (blackbrrr)',
    author_email='mattdennewitz@gmail.com',
    url='',
    packages = ['nailbiter',],
    package_dir = {'nailbiter':'nailbiter'},
)
