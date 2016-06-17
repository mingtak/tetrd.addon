# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from tetrd.addon.testing import TETRD_ADDON_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that tetrd.addon is properly installed."""

    layer = TETRD_ADDON_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if tetrd.addon is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'tetrd.addon'))

    def test_browserlayer(self):
        """Test that ITetrdAddonLayer is registered."""
        from tetrd.addon.interfaces import (
            ITetrdAddonLayer)
        from plone.browserlayer import utils
        self.assertIn(ITetrdAddonLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = TETRD_ADDON_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['tetrd.addon'])

    def test_product_uninstalled(self):
        """Test if tetrd.addon is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'tetrd.addon'))

    def test_browserlayer_removed(self):
        """Test that ITetrdAddonLayer is removed."""
        from tetrd.addon.interfaces import ITetrdAddonLayer
        from plone.browserlayer import utils
        self.assertNotIn(ITetrdAddonLayer, utils.registered_layers())
