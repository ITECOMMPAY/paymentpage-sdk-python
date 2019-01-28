from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='EcommPay Python SDK',
    version='1.0',
    url='https://github.com/ITECOMMPAY/paymentpage-sdk-python',
    license='MIT',
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
    long_description=open(join(dirname(__file__), 'README.rm')).read(),
)