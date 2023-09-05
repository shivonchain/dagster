from pathlib import Path
from typing import Dict

from setuptools import find_packages, setup


def get_version() -> str:
    version: Dict[str, str] = {}
    with open(Path(__file__).parent / "dagster_ext/version.py", encoding="utf8") as fp:
        exec(fp.read(), version)

    return version["__version__"]


ver = get_version()
# dont pin dev installs to avoid pip dep resolver issues
pin = "" if ver == "1!0+dev" else f"=={ver}"
setup(
    name="dagster-ext",
    version=get_version(),
    author="Elementl",
    author_email="hello@elementl.com",
    license="Apache-2.0",
    description="Toolkit for Dagster integrations with transform logic outside of Dagster",
    url="https://github.com/dagster-io/dagster/tree/master/python_modules/libraries/dagster-ext",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(exclude=["dagster_ext_tests*"]),
    extras_require={
        "test": [
            f"dagster{pin}",
            "boto3",
            "botocore",
            "moto[s3,server]",
        ],
    },
    zip_safe=False,
    entry_points={"console_scripts": ["dagster-graphql = dagster_graphql.cli:main"]},
)