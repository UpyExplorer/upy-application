from setuptools import find_packages, setup

with open('requirements.txt') as requirements_file:
    REQUIREMENTS = [r.replace('\n', '') for r in requirements_file.readlines()]

setup(
    name='upy_explorer',
    version='1.0.0',
    description='IndexOffy API',
    author='IndexOffy',
    author_email='upyexplorer@gmail.com',
    url='http://www.upyexplorer.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=REQUIREMENTS,
    zip_safe=False
)