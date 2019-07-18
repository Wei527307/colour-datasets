# -*- coding: utf-8 -*-
"""
Defines unit tests for :mod:`colour_datasets.loaders.luo1999` module.
"""

from __future__ import division, unicode_literals

import numpy as np
import unittest

from colour_datasets.loaders import Luo1999DatasetLoader, build_Luo1999

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['TestLuo1999DatasetLoader', 'TestBuildLuo1999']


class TestLuo1999DatasetLoader(unittest.TestCase):
    """
    Defines :class:`colour_datasets.loaders.luo1999.Luo1999DatasetLoader`
    class unit tests methods.
    """

    def test_required_attributes(self):
        """
        Tests presence of required attributes.
        """

        required_attributes = ('ID', )

        for attribute in required_attributes:
            self.assertIn(attribute, dir(Luo1999DatasetLoader))

    def test_required_methods(self):
        """
        Tests presence of required methods.
        """

        required_methods = ('load', )

        for method in required_methods:
            self.assertIn(method, dir(Luo1999DatasetLoader))

    def test_load(self):
        """
        Tests :func:`colour_datasets.loaders.luo1999.Luo1999DatasetLoader.\
load` method.
        """

        dataset = Luo1999DatasetLoader()
        self.assertEqual(len(dataset.load().keys()), 37)

        np.set_printoptions(
            formatter={'float': '{:0.8f}'.format}, suppress=True)

        np.testing.assert_almost_equal(
            dataset.data['CSAJ-C - da'].XYZ_ct,
            np.array([
                [9.31000000, 7.33000000, 2.12000000],
                [8.85000000, 7.26000000, 1.73000000],
                [7.57000000, 6.72000000, 1.45000000],
                [6.93000000, 6.78000000, 1.81000000],
                [6.10000000, 6.41000000, 2.17000000],
                [5.89000000, 6.36000000, 2.65000000],
                [5.96000000, 6.24000000, 3.14000000],
                [6.60000000, 6.21000000, 3.24000000],
                [8.13000000, 6.74000000, 3.12000000],
                [9.29000000, 7.46000000, 2.71000000],
                [11.21000000, 7.78000000, 1.73000000],
                [9.76000000, 7.28000000, 1.07000000],
                [8.52000000, 7.32000000, 0.89000000],
                [6.48000000, 6.77000000, 1.10000000],
                [4.75000000, 5.99000000, 1.93000000],
                [4.28000000, 5.55000000, 2.83000000],
                [4.88000000, 5.80000000, 3.97000000],
                [6.15000000, 5.98000000, 4.26000000],
                [8.85000000, 6.81000000, 3.74000000],
                [10.74000000, 7.76000000, 2.68000000],
                [13.58000000, 8.66000000, 1.58000000],
                [3.88000000, 5.80000000, 1.83000000],
                [3.14000000, 4.99000000, 3.10000000],
                [3.83000000, 5.35000000, 4.93000000],
                [5.73000000, 5.80000000, 5.43000000],
                [9.92000000, 7.23000000, 4.52000000],
                [12.28000000, 7.66000000, 2.66000000],
                [25.06000000, 20.96000000, 6.42000000],
                [24.39000000, 20.65000000, 5.50000000],
                [22.85000000, 20.46000000, 5.04000000],
                [20.84000000, 19.87000000, 5.33000000],
                [19.00000000, 19.45000000, 6.67000000],
                [18.49000000, 19.08000000, 7.53000000],
                [19.44000000, 19.34000000, 8.58000000],
                [20.25000000, 18.84000000, 8.35000000],
                [23.50000000, 20.47000000, 8.20000000],
                [24.98000000, 21.02000000, 7.25000000],
                [28.00000000, 21.26000000, 5.27000000],
                [27.66000000, 21.94000000, 4.20000000],
                [23.88000000, 20.89000000, 3.26000000],
                [19.65000000, 19.72000000, 3.75000000],
                [16.48000000, 18.87000000, 6.21000000],
                [15.78000000, 18.46000000, 8.10000000],
                [16.39000000, 17.92000000, 9.86000000],
                [18.81000000, 17.89000000, 9.97000000],
                [24.53000000, 20.27000000, 9.32000000],
                [28.10000000, 21.73000000, 7.13000000],
                [36.31000000, 23.75000000, 4.25000000],
                [32.47000000, 23.05000000, 2.04000000],
                [25.96000000, 22.33000000, 1.40000000],
                [16.94000000, 19.34000000, 1.51000000],
                [11.51000000, 17.13000000, 5.43000000],
                [10.66000000, 16.24000000, 9.11000000],
                [11.81000000, 15.73000000, 13.45000000],
                [16.48000000, 16.69000000, 14.05000000],
                [26.75000000, 20.01000000, 11.24000000],
                [35.94000000, 23.61000000, 7.31000000],
                [51.48000000, 44.17000000, 13.98000000],
                [52.10000000, 44.99000000, 12.77000000],
                [49.35000000, 44.23000000, 11.47000000],
                [45.88000000, 43.36000000, 11.77000000],
                [42.03000000, 42.04000000, 14.30000000],
                [38.92000000, 39.17000000, 14.89000000],
                [41.21000000, 40.22000000, 16.66000000],
                [45.21000000, 41.75000000, 17.15000000],
                [48.11000000, 42.48000000, 16.43000000],
                [51.28000000, 44.35000000, 15.45000000],
                [55.86000000, 44.57000000, 11.95000000],
                [56.48000000, 46.28000000, 10.25000000],
                [50.94000000, 45.06000000, 8.49000000],
                [44.30000000, 43.47000000, 8.99000000],
                [37.51000000, 40.86000000, 13.42000000],
                [35.35000000, 39.12000000, 16.03000000],
                [37.26000000, 38.70000000, 18.63000000],
                [43.24000000, 40.67000000, 19.79000000],
                [49.20000000, 41.81000000, 17.63000000],
                [55.55000000, 45.18000000, 15.45000000],
                [63.57000000, 47.85000000, 11.77000000],
                [59.61000000, 46.66000000, 7.81000000],
                [52.37000000, 45.89000000, 6.15000000],
                [41.84000000, 42.37000000, 7.00000000],
                [33.71000000, 40.09000000, 12.81000000],
                [30.22000000, 36.68000000, 16.27000000],
                [33.26000000, 37.35000000, 21.58000000],
                [41.99000000, 40.27000000, 23.06000000],
                [53.44000000, 44.07000000, 20.61000000],
                [63.08000000, 47.24000000, 15.10000000],
            ]) / 100,
            decimal=7)

        self.assertEqual(
            dataset.data['CSAJ-C - da'].metadata['Experimental Method'],
            'Haploscopic')


class TestBuildLuo1999(unittest.TestCase):
    """
    Defines :func:`colour_datasets.loaders.luo1999.build_Luo1999`
    definition unit tests methods.
    """

    def test_build_Luo1999(self):
        """
        Tests :func:`colour_datasets.loaders.luo1999.build_Luo1999`
        definition.
        """

        self.assertIs(build_Luo1999(), build_Luo1999())


if __name__ == '__main__':
    unittest.main()
