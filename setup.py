from distutils.core import setup


setup(
    name='data-converter',
    packages=['data_converter'],
    version='0.0.1',
    description='Convert any data file to any other',
    author='Eddy Hintze',
    author_email="eddy@hintze.co",
    url="https://github.com/xtream1101/data-converter",
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    install_requires=[
                      ],
    entry_points = {
        'console_scripts': [
            'data-converter=data_converter:cli',
        ],
    },

)
