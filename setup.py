from setuptools import setup, find_packages

setup(
    name='finbox',
    version='0.0.1',
    description='A python client for finance related jobs',
    author='Yiheng Li',
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python :: 3'
    ],
    install_requires=[
        'backtrader',
        'colorlog',
        'pandas',
        'requests',
        'pyecharts',
        'pyecharts-snapshot',
        'pyfolio',
        'tqdm',
        'seaborn'
    ]
)
