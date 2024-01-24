from setuptools import setup


setup(
    name='MyLibrary',                    # package name
    version='0.1',                          # version
    description='Package Description will be later',      # short description
    url='https://github.com/AnisimovMike/TestLibrary',               # package URL
    install_requires=[],                    # list of packages this package depends
                                            # on.
    packages=['MyLibrary'],              # List of module names that installing
                                            # this package will provide.
)
