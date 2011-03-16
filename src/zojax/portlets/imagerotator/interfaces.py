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


class IImageRotatorItem(interface.Interface):

    title = schema.TextLine(title=_(u'Title'), 
                            description=_(u'Rotated image alternative text'), 
                            required=False)
    
    image = ImageField(title=_(u'Picture'), required=False)
    
    text = RichText(title=_(u'Text'), required=True)

    image.mimeTypes = ('image/jpeg', 'image/gif', 'image/png', 'application/octet-stream')
    
    
class IImageRotatorImage(IImageRotatorItem):

    thumbnail = ImageField(title=_(u'Thumbnail'), required=False)
    
    thumbnail.mimeTypes = IImageRotatorItem['image'].mimeTypes


class IImageRotatorButton(IImageRotatorItem):
    
    title = schema.TextLine(title=_(u'Title'), 
                            description=_(u'Button text'), 
                            required=True)
    
    url = schema.TextLine(title=_(u'URL'), 
                          description=_(u'Learn more... url'), required=True)
    

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
    
    height = schema.Int(
        title = _(u'Height'),
        default = 302,
        required = True)
    
    images = schema.List(title=_(u"Images"),
                         value_type=schema.Object(title=_(u'image'),
                                                  schema=IImageRotatorImage),
                         default=[],
                         required=False)
    
    buttons = schema.List(title=_(u"Buttons"),
                         value_type=schema.Object(title=_(u'button'),
                                                  schema=IImageRotatorButton),
                         default=[],
                         required=False)