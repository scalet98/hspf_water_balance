
import os
import sys

from setuptools import setup

# temporarily redirect config directory to prevent matplotlib importing
# testing that for writeable directory which results in sandbox error in
# certain easy_install versions
os.environ["MPLCONFIGDIR"] = "."


version = open("VERSION").readline().strip()

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist')
    os.system('twine upload dist/hspf_water_balance-{0}*'.format(version))
    sys.exit()

README = open("./README.rst").read()

version = open("./VERSION").readline().strip()

install_requires = [
    # http://packages.python.org/distribute/setuptools.html#declaring-dependencies
    'tstoolbox',
    'hspfbintoolbox'
]

setup_requires = []

setup(name='hspf_water_balance',
      version=version,
      description="Creates water balance table from HSPF models.",
      long_description=README,
      classifiers=[
          # Get strings from
          # http://pypi.python.org/pypi?%3Aaction=list_classifiers
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Science/Research',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'Environment :: Console',
          'License :: OSI Approved :: BSD License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Topic :: Scientific/Engineering :: Information Analysis',
          'Topic :: Scientific/Engineering',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='hydrology',
      author='Tim Cera, P.E.',
      author_email='tim@cerazone.net',
      url='http://timcera.bitbucket.io/hspf_water_balance/docsrc/index.html',
      packages=['hspf_water_balance'],
      include_package_data=True,
      zip_safe=False,
      setup_requires=setup_requires,
      install_requires=install_requires,
      entry_points={
          'console_scripts':
              ['hspf_water_balance=hspf_water_balance.hspf_water_balance:main']
      },
      test_suite='tests',
      python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*',
      )
