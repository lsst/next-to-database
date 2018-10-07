import distutils
from distutils.core import setup

bin_files = ["bin.src/csv2pq"]

# The main call
setup(name='csv2pq',
      version='1.0.1',
      license="GPL",
      description="csv/parquet utilities",
      author="Andrew Hanushevsky",
      author_email="abh@slac.stanford.edu",
      packages=['next_to_database'],
      package_dir={'': 'python'},
      scripts=bin_files,
      data_files=[('tests', ['tests/data/testfile1.csv',
                             'tests/data/testfile2.csv',
                             'tests/data/test.schema'])
)
