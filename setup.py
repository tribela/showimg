try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()


setup(
    name='showimg',
    py_modules=['showimg'],
    install_requires=[
        'Pillow>=4.0.0',
    ],
    entry_points={
        'console_scripts': [
            'showimg=showimg:showimg'
        ],
    }
)
