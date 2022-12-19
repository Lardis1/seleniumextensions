from setuptools import setup

# Strip version and long description
with open('VERSION') as version_file:
    version_=version_file.read().strip()
with open('README.md') as readme_file:
    long_description_=readme_file.read()

setup(
    name='seleniumextensions',
    version=version_,
    description='Extended functionality for automated testing with Selenium Python.',
    long_description=long_description_,
    long_description_content_type='text/markdown',
    author='Alex Lardis',
    author_email='alexlardis@outlook.com',
    url='https://github.com/Lardis1/seleniumextensions',
    license='MIT',
    keywords="selenium, page object model, pom, pages, page factory",
    packages=['seleniumextensions'],
    install_requires=[
        'selenium',
    ]
)