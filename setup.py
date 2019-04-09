from io import open

from setuptools import find_packages, setup

with open('d6engine/__init__.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.strip().split('=')[1].strip(' \'"')
            break
    else:
        version = '0.0.1'

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

REQUIRES = []

setup(
    name='d6engine',
    version=version,
    description='',
    long_description=readme,
    author='Chuck Mo',
    author_email='chuck@moosejudge.com',
    maintainer='Chuck Mo',
    maintainer_email='chuck@moosejudge.com',
    url='https://gitlab.com/thechuckmo/d6engine',
    license='MIT/Apache-2.0',

    keywords=[
        '',
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    install_requires=REQUIRES,
    tests_require=['coverage', 'pytest'],

    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'd6engine = d6engine.cli:d6engine',
        ],
    },
)
