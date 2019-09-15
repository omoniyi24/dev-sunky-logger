from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='sunkylogger',
    version='0.0.3',
    description='Logging python SDK',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='Ilesanmi Omoniyi',
    author_email='omoniyi24@gmail.com',
    keywords=['Logger'],
    url='https://github.com/omoniyi24/dev-sunky-logger'
)

if __name__ == '__main__':
    setup(**setup_args)