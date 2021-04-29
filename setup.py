from setuptools import setup

setup(
    name='sherlock',
    version='0.14.0',
    packages = ["sherlock"],
    entry_points={
        'console_scripts': [
            'sherlock=sherlock.sherlock:main'
        ]
    }
)
