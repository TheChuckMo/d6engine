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

REQUIRES = ['Click', 'PyYaml', 'slugify', 'tornado']

setup(
    name='d6engine',
    version=version,
    description='',
    long_description=readme,
    author='Chuck Mo',
    author_email='chuck@d6engine.com',
    maintainer='Chuck Mo',
    maintainer_email='chuck@d6engine.com',
    url='https://gitlab.com/thechuckmo/d6engine',
    license='MIT/Apache-2.0',

    keywords=[
        'dice', 'character', 'game', 'opend6',
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
    package_data={'d6engine': ['data/*.yaml']},
    entry_points={
        'console_scripts': [
            'd6engine = d6engine.cli:d6engine',
        ],
    },
)
