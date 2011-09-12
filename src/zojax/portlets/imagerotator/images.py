##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
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
from zope.location import LocationProxy
from zope.publisher.interfaces import NotFound
from zope.publisher.interfaces import IPublishTraverse
from zope.security.proxy import removeSecurityProxy
from zope.component import getAdapters, queryMultiAdapter

from zojax.portlet.interfaces import IPortletManager, IPortletsExtension
from zojax.portlet.browser.interfaces import IPortletManagerPublicMarker
from zope.security.interfaces import Unauthorized

class Images(object):

    interface.implements(IPublishTraverse)

    __name__ = 'images'

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def publishTraverse(self, request, name):
        context = self.context
        try:
            return LocationProxy(context.images[int(name)-1], self.context, name)
        except ValueError, e:
            # 403 error
            raise Unauthorized("Access to images folder denied")
        except IndexError, e:
            # 404 error
            raise NotFound(self.context, self.__name__, request)
        except TypeError, e:
            raise

        raise NotFound(self.context, self.__name__, request)


class Buttons(Images):

    __name__ = 'buttons'

    def publishTraverse(self, request, name):
        context = self.context
        try:
            return LocationProxy(context.buttons[int(name)-1], self.context, name)
        except (TypeError, ValueError, IndexError), e:
            raise
        raise NotFound(self.context, self.__name__, request)
