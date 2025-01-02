from setuptools import setup, find_packages

setup(
    name="OptiBench",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scipy"
    ],
    entry_points={
        "console_scripts": [
            "optibench=optibench.cli:main"
        ]
    }
)