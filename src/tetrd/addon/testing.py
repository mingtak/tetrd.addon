# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import tetrd.addon


class TetrdAddonLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=tetrd.addon)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'tetrd.addon:default')


TETRD_ADDON_FIXTURE = TetrdAddonLayer()


TETRD_ADDON_INTEGRATION_TESTING = IntegrationTesting(
    bases=(TETRD_ADDON_FIXTURE,),
    name='TetrdAddonLayer:IntegrationTesting'
)


TETRD_ADDON_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(TETRD_ADDON_FIXTURE,),
    name='TetrdAddonLayer:FunctionalTesting'
)


TETRD_ADDON_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        TETRD_ADDON_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='TetrdAddonLayer:AcceptanceTesting'
)
