from setuptools import setup


setup(
    name='pre-commit-sqlfluff',
    description='pre-commit hook for sqlfluff',
    version='0.3.6',
    install_requires=[
        'sqlfluff==0.3.6'
    ],
)
