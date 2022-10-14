from setuptools import setup

setup(
    tests_require=[
        'astronomer-certified-extensions[test]',
    ],
    extras_require={
        'test': [
            'pytest',
            'pytest-flask',
            'pytest-mock',
            'pytest-flake8<1.1.1',
        ],
    },
)
