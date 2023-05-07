from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='colititato',
    version='0.1.1',
    author='Giannis Tiakas',
    author_email='giannis@tiakas.com',
    description='A CLI implementation of the classic Tic Tac Toe game',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/tiakas/colititato',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'colititato=colititato.cli:main'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Games/Entertainment :: Board Games',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    keywords='cli, tic-tat-toe, game',
    install_requires=[
    ],
    python_requires='>=3.6',
)
