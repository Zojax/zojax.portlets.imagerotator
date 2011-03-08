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
from rwproperty import setproperty, getproperty
"""

$Id$
"""
from zope import interface
from zope.component import queryUtility
from zope.app.component.hooks import getSite
from zojax.catalog.interfaces import ICatalog
from zojax.resourcepackage.library import include
from zojax.portlet.browser.portlet import publicAbsoluteURL

from interfaces import IImageRotatorPortlet


class ImageRotatorPortlet(object):

    def update(self):
        include('zojax.portlets.imagerotator')
        self.url = publicAbsoluteURL(self, self.request)
        
    def isAvailable(self):
        return bool(self.images)
    
    @getproperty
    def images(self):
        return self.__data__['images']
    
    @setproperty
    def images(self, value):
        old = self.__data__['images']
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
        self.__data__['images'] = old
                