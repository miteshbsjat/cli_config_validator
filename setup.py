import setuptools
from setuptools.command.test import test as TestCommand
# from .version import __version__
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
exec(open('mitesh/version.py').read())


class Run_TestSuite(TestCommand):
    def run_tests(self):
        import os
        import sys

        py_version = sys.version_info[0]
        print('Python version from setup.py is', py_version)
        run_string = "echo hi"
        os.system(run_string)


setuptools.setup(
    name='cli_config_validator',                                  # should match the package folder
    packages=['cli_config_validator'],                            # should match the package folder
    version=__version__,                            # important for updates
    license='Apache License 2.0',                   # should match your chosen license
    description='Validate configuration from multiple configuration files against a Python pydantic class Model',
    long_description=long_description,              # loads your README.md
    long_description_content_type="text/x-md",     # README.rst is of type 'x-rst'
    author='Mitesh Singh Jat',
    author_email="@".join(["mitesh.singh.jat", "gmail" + ".com"]),
    url='https://github.com/miteshbsjat/cli_config_validator', 
    project_urls = {                                # Optional
        "Bug Tracker": "https://github.com/miteshbsjat/cli_config_validator/issues"
    },
    install_requires=[
        "pydantic>=2.10.6"
        "pyyaml>=5.4.1"
        "toml>=0.10.2"
    ],                            # list all packages that your package uses
    entry_points='''
        [console_scripts]
        cli_config_validator=cli_config_validator:main
    ''',
    keywords=["pypi", "cli_config_validator", "yaml", "json", "toml"],           #descriptive meta-data
    classifiers=[                                   # https://pypi.org/classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Software Development :: Documentation',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System',
        'Topic :: System :: Operating System',
        'Topic :: System :: Shells',
        'Topic :: System :: System Shells',
        'Topic :: System :: Systems Administration',
        'Topic :: Text Processing',
        'Topic :: Utilities',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    
    download_url="https://github.com/miteshbsjat/cli_config_validator/archive/refs/tags/0.0.0.tar.gz",
    cmdclass={'test': Run_TestSuite},
)