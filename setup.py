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

REQUIRES = ['Click', 'PyYaml', 'slugify', 'tornado', 'pydotenv', 'mkdocs']
BUILD_REQUIRES = []
TEST_REQUIRES = ['coverage', 'pytest']

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
    license='GPLv3',

    keywords=['dice', 'character', 'game', 'opend6'],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        #'Development Status :: 3 - Alpha',
        #'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Other Audience',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Framework :: Pytest',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    install_requires=REQUIRES,
    tests_require=TEST_REQUIRES,

    packages=find_packages(),
    package_data={'d6engine': ['data/*.yaml']},
    entry_points={
        'console_scripts': [
            'd6engine = d6engine.cli:d6engine',
        ],
    },
)
