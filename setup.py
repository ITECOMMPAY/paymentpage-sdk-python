import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name='ecommpay-sdk',
    version='1.0.3',
    url='https://github.com/ITECOMMPAY/paymentpage-sdk-python',
    license='MIT',
    long_description=README,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=['tests', 'tests.*']),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
