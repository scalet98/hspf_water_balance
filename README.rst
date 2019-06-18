.. image:: https://travis-ci.org/timcera/hspf_water_balance.svg?branch=master
    :target: https://travis-ci.org/timcera/hspf_water_balance
    :height: 20

.. image:: https://coveralls.io/repos/timcera/hspf_water_balance/badge.png?branch=master
    :target: https://coveralls.io/r/timcera/hspf_water_balance?branch=master
    :height: 20

.. image:: https://img.shields.io/pypi/v/hspf_water_balance.svg
    :alt: Latest release
    :target: https://pypi.python.org/pypi/hspf_water_balance

.. image:: http://img.shields.io/badge/license-BSD-lightgrey.svg
    :alt: hspf_water_balance license
    :target: https://pypi.python.org/pypi/hspf_water_balance/

hspf_water_balance - Quick Guide
================================
The hspf_water_balance is a Python script to create a water balance from
Hydrological Simulation Program - FORTRAN (HSPF) or by function calls within
Python.  Uses pandas (http://pandas.pydata.org/) or numpy
(http://numpy.scipy.org) for any heavy lifting.

Requirements
------------
* tstoolbox - collected and installed by 'pip' or 'easy_install' command.

Installation
------------
Should be as easy as running ``pip install hspf_water_balance`` or
``easy_install hspf_water_balance`` at any command line.

Usage - Command Line
--------------------
Just run 'hspf_water_balance --help' to get a list of subcommands

usage: hspf_water_balance [-h]
                 {about,detailed,summary,mapping}
                 ...

    about               
        Display version number and system information.

    detailed          
        Create detailed water balance of each component.

    summary           
        Create a summary table of precipitation, runoff, evaporation.

    mapping           
        Create a table suitable for joining to a shapefile to map surface water
        balance components.

For the subcommands that output data it is printed to the screen and you can
then redirect to a file.

Usage - API
-----------
You can use all of the command line subcommands as functions.  The function
signature is identical to the command line subcommands.  The return is always
a PANDAS DataFrame.  Input can be a CSV or TAB separated file, or a PANDAS
DataFrame and is supplied to the function via the 'input_ts' keyword.

Simply import hspf_water_balance::

    from hspf_water_balance import hspf_water_balance

    # Then you could call the functions
    ntsd = hspf_water_balance.summary(method='linear', input_ts='tests/test_fill_01.csv')

    # Once you have a PANDAS DataFrame you can use that as input to other 
    # hspf_water_balance functions.
    ntsd = hspf_water_balance.aggregate(statistic='mean', agg_interval='daily', input_ts=ntsd)

