##############################################################################
#
# Copyright (c) 2008 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
""" google ads portlet interfaces

$Id$
"""
from zope import schema, interface
from zope.i18nmessageid import MessageFactory

from zojax.filefield.field import ImageField
from zojax.richtext.field import RichText

_ = MessageFactory('"zojax.portlets.imagerotator"')


class IImageRotatorImage(interface.Interface):

    title = schema.TextLine(title=_(u'Title'), required=False)
    
    text = RichText(title=_(u'Text'), required=False)
    
    detailText = RichText(title=_(u'Detail text'), required=False)
    
    image = ImageField(title=_(u'Picture'), required=False)
    
    detailImage = ImageField(title=_(u'Detail picture'), required=False)
    
    thumbnail = ImageField(title=_(u'Thumbnail'), required=False)
    
    image.mimeTypes = thumbnail.mimeTypes = ('image/jpeg', 'image/gif', 'image/png', 'application/octet-stream')


class IImageRotatorPortlet(interface.Interface):
    """ portlet interface """
    
    label = schema.TextLine(
        title = _(u'Label'),
        default = u'',
        required = False)

    decoration = schema.Bool(
        title = _(u'Portlet decoration'),
        description = _(u'Show portlet decoration, or just html.'),
        default = True,
        required = False)

    cssClass = schema.TextLine(
        title = _(u'CSS class'),
        required = False)
    
    images = schema.List(title=_(u"Images"),
                         value_type=schema.Object(title=_(u'image'),
                                                  schema=IImageRotatorImage),
                         default=[],
                         required=False)