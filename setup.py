from setuptools import find_packages, setup



def parse_requirements(filename):
    lines = (line.strip() for line in open(filename))
    return [line for line in lines if line and not line.startswith("#")]



setup(
    name="EffiSync",
    version = "0.1",
    py_modules=["app"],
    description="",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    readme="README.md",
    python_requires="",
    author="EffiSync team",
    url="",
    license="MIT",
    packages=find_packages(include=["app", "app.*"], exclude=["tests*"]),
    install_requires=parse_requirements("requirements.txt"),
    include_package_data=True,
    extras_require={"dev": ["pytest", "ruff", "black"]},
)
