try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'The Prisoner Of Pyland',
    'author': 'Goran Nushkov',
    'url': 'https://github.com/nushkovg/the-prisoner-of-pyland',
    'download_url': 'https://github.com/nushkovg/the-prisoner-of-pyland',
    'author_email': 'gnuskov@protonmail.com',
    'version': '1.0',
    'packages': ['tpp_modules'],
    'scripts': ['bin/the-prisoner-of-pyland'],
    'name': 'the-prisoner-of-pyland',
}

setup(**config)
