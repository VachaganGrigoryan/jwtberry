from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

__version__ = '0.2.0'


setup(
    name='jwtberry',
    version=__version__,
    description='Jwt authentication for Django Strawberry GraphQl',
    long_description=long_description,
    long_description_content_type='text/markdown',

    author='Vachagan Grigoryan',
    author_email='vachagan.grigoryan@outlook.com',
    url='https://github.com/VachaganGrigoryan/jwtberry',

    install_requires=[
        "django>=4.2.6",
        "strawberry-graphql>=0.211.1",
        "pyjwt>=2.8.0",
    ],
    extras_require={
        'test': ['pytest'],
    },
)
