# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from tetrd.addon import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from z3c.relationfield.schema import RelationList, RelationChoice
from plone.app.textfield import RichText
from plone.app.vocabularies.catalog import CatalogSource


class ITetrdAddonLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class ICover(Interface):

    title = schema.TextLine(
        title=_(u"Title"),
        required=True,
    )

    description = schema.Text(
        title=_(u"Description"),
        required=False,
    )

    heros = RelationList(
        title=_(u"Heros"),
        description=_(u"Rleated images for hero section"),
        value_type=RelationChoice(title=_(u"Related"),
                                  source=CatalogSource(portal_type='Image'),),
        required=True,
    )

    hotNews = RelationList(
        title=_(u"Hot News"),
        description=_(u"Rleated news for home page hot news list"),
        value_type=RelationChoice(title=_(u"Related"),
                                  source=CatalogSource(portal_type='News Item'),),
        required=True,
    )

