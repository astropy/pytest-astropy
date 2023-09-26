0.11.0 (2023-09-26)
===================

- Dropped ``pytest-openfiles`` as dependency. If you still use it,
  you can install it separately. See https://github.com/astropy/pytest-openfiles/pull/44
  for more information. [#52]

- ``-R`` is added as a short version for the command-line option
  ``--remote-data``. [#55]

- Require ``pytest-doctestplus`` 1.0.0 or later. [#56]

- Require ``pytest-remotedata`` 0.4.1 or later. [#56]

- Require ``pytest-astropy-header`` 0.2.2 or later. [#56]

- Require ``pytest-arraydiff`` 0.5 or later. [#56]

- Require ``pytest-filter-subpackage`` 0.1.2 or later. [#56]


0.10.0 (2022-04-21)
===================

- Dropped ``distutils`` as build dependency. [#47]

- Added plugin for cpu/memory intensive tests. See ``README.rst``. [#48]

0.9.0 (2021-09-21)
==================

- Added ``pytest-mock`` as dependency. [#31]

- Require ``pytest-cov`` 2.3.1 or later. [#41]

- Require ``pytest-doctestplus`` 0.11.0 or later. [#43]

- Dropped support for Python 3.6. [#43]

0.8.0 (2020-01-16)
==================

- Added ``pytest-filter-subpackage`` and ``pytest-cov`` as dependencies. [#29]

- Dropped support for Python 2.7 and 3.5. [#29]

- Require Hypothesis 5.1 or later. [#29]

0.7.0 (2019-12-10)
==================

- Added ``hypothesis` as a dependency. [#25]

0.6.0 (2019-10-25)
==================

- Added ``pytest-astropy-header`` as a dependency.

0.5.0 (2018-11-26)
==================

- Updates to ``pytest-remotedata``, ``pytest-doctestplus``, and
  ``pytest-openfiles``. [#14]

0.4.0 (2018-05-29)
==================

- Update ``pytest-remotedata`` to reflect new version. [#12]

0.3.0 (2018-04-20)
==================

- Explicitly pin ``pytest-arraydiff`` to version >= 0.1. [#10]

- Update dependencies on ``pytest-doctestplus``, ``pytest-remotedata``, and
  ``pytest-openfiles`` to reflect recent releases. [#11]

0.2.1 (2017-12-08)
==================

- Remove dependency on ``pytest-mpl`` since it introduces a dependency on
  ``matplotlib``, which is not always desirable.

0.2.0 (2017-12-07)
==================

- Update REAME. Use README as long description on PyPi. [#7]

- Update dependency versions of Astropy-specific plugins.

0.1 (2017-10-10)
================

- Alpha release.
