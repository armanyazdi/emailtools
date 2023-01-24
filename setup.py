from setuptools import setup

with open('./README.md', 'r') as f:
    readme = f.read()

setup(
    name='emailtools',
    version='0.0.4',
    packages=['emailtools'],
    include_package_data=True,
    url='https://github.com/armanyazdi/emailtools',
    license='MIT',
    author='Arman Yazdi',
    description='A Python library for email suggestions and validations.',
    long_description=readme,
    long_description_content_type='text/markdown',
    keywords='email generator, email suggester, email validator, email',
    install_requires=['persian-names'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Persian',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Localization'
    ],
    project_urls={
        'Source': 'https://github.com/armanyazdi/emailtools',
        'Documentation': 'https://pypi.org/project/emailtools',
    },
)
