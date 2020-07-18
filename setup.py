from setuptools import setup, find_packages
import os

setup_packages = [f"mask_detector.{package}" for package in find_packages(where=os.path.join(os.path.dirname(__file__), 'src'))]
setup_packages.append("mask_detector")

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    requirements = [line.strip() for line in f.read().splitlines()]

setup(
    name='mask_detector',
    version="1.3",
    packages=setup_packages,
    include_package_data=True,
    package_dir={"mask_detector": "src"},
    url='https://github.com/javibg96/mask_detector/',
    author='Javier Blasco',
    install_requires=requirements,
    author_email="blascogarcia.javier@outlook.com",
    description=' '
)
