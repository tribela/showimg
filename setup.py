from os import path

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup


def cwd():
    return path.abspath(path.dirname(__file__))


def readme():
    with open(path.join(cwd(), 'README.rst')) as fp:
        return fp.read()


setup(
    name='showimg',
    version='0.1.0',
    description='Show image on 256-coloured terminal.',
    long_description=readme(),
    url='https://github.com/kjwon15/showimg',
    author='Kjwon15',
    license='MIT',
    py_modules=['showimg'],
    install_requires=[
        'Pillow>=4.0.0',
        'requests>=2.12.5',
    ],
    entry_points={
        'console_scripts': [
            'showimg=showimg:main'
        ],
    }
)
