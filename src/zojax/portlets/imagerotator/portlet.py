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
from rwproperty import setproperty, getproperty

from zojax.portlet.browser.portlet import publicAbsoluteURL
from zojax.resourcepackage.library import include


class ImageRotatorPortlet(object):

    def update(self):
        include('zojax.portlets.imagerotator')
        self.url = publicAbsoluteURL(self, self.request)

    def isAvailable(self):
        return bool(self.images)

    @getproperty
    def images(self):
        return self.__data__.get('images', [])

    @setproperty
    def images(self, value):
        old = self.images
        if value is not None:
            if len(value) > len(old):
                old.extend(value[len(old):])
            else:
                old = old[:len(value)]
        else:
            self.__data__['images'] = []
            return
        for k, v in enumerate(value):
            ov = old[k]
            if v.image.data:
                ov.image = v.image
            if v.thumbnail.data:
               ov.thumbnail = v.thumbnail
            ov.title = v.title
            ov.text = v.text
            ov.url = v.url
            ov.position = v.position

        # NOTE: sort by position
        old = sorted(old, key=lambda x: x.position)
        self.__data__['images'] = old

    @getproperty
    def buttons(self):
        return self.__data__.get('buttons', [])

    @setproperty
    def buttons(self, value):
        old = self.buttons
        if value is not None:
            if len(value) > len(old):
                old.extend(value[len(old):])
            else:
                old = old[:len(value)]
        else:
            self.__data__['buttons'] = []
            return
        for k, v in enumerate(value):
            ov = old[k]
            if v.image.data:
                ov.image = v.image
            ov.title = v.title
            ov.text = v.text
            ov.url = v.url
            ov.position = v.position

        # NOTE: sort by position
        old = sorted(old, key=lambda x: x.position)
        self.__data__['buttons'] = old


class ImageRotatorSimplePortlet(object):
    """ """

    def update(self):
        include('zojax.portlets.imagerotator')
        include('jflow.plus')
        self.url = publicAbsoluteURL(self, self.request)

    def isAvailable(self):
        return bool(self.images)

    @getproperty
    def images(self):
        return self.__data__.get('images', [])

    @setproperty
    def images(self, value):
        old = self.images
        if value is not None:
            if len(value) > len(old):
                old.extend(value[len(old):])
            else:
                old = old[:len(value)]
        else:
            self.__data__['images'] = []
            return
        for k, v in enumerate(value):
            ov = old[k]
            if v.image.data:
                ov.image = v.image
            ov.title = v.title
            ov.url = v.url
            ov.position = v.position

        # NOTE: sort by position
        old = sorted(old, key=lambda x: x.position)
        self.__data__['images'] = old
