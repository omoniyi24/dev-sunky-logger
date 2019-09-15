from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='sunkylogger',
    version='0.0.5',
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

install_requires = [
    'python>=3.6'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)