from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='sunkylogger',
    version='0.0.1',
    description='Useful tools to work with Elastic stack in Python',
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
    'elasticsearch>=7.0.2'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)