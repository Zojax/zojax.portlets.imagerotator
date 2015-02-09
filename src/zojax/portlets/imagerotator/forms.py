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

"""

$Id$
"""

from zope import interface
from zope.schema.fieldproperty import FieldProperty

from z3c.form.object import registerFactoryAdapter

from zojax.filefield.field import FileFieldProperty
from zojax.richtext.field import RichTextProperty

from interfaces import IImageRotatorImage, IImageRotatorButton, \
    IImageRotatorItem, IImageRotatorSimpleImage


class ImageRotatorItem(object):

    title = None

    image = FileFieldProperty(IImageRotatorItem['image'])

    text = RichTextProperty(IImageRotatorItem['text'])

    position = FieldProperty(IImageRotatorItem['position'])


class ImageRotatorImage(ImageRotatorItem):
    interface.implements(IImageRotatorImage)

    thumbnail = FileFieldProperty(IImageRotatorImage['thumbnail'])

    url = None


class ImageRotatorSimpleImage(object):
    interface.implements(IImageRotatorSimpleImage)

    title = None

    url = None

    image = FileFieldProperty(IImageRotatorItem['image'])

    position = FieldProperty(IImageRotatorItem['position'])

    text = RichTextProperty(IImageRotatorSimpleImage['text'])


class ImageRotatorButton(ImageRotatorItem):
    interface.implements(IImageRotatorButton)

    image = FileFieldProperty(IImageRotatorButton['image'])

    url = None


registerFactoryAdapter(IImageRotatorImage, ImageRotatorImage)

registerFactoryAdapter(IImageRotatorSimpleImage, ImageRotatorSimpleImage)

registerFactoryAdapter(IImageRotatorButton, ImageRotatorButton)
