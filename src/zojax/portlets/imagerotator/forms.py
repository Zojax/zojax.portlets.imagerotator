from zope import component, interface, schema
from z3c.form.object import registerFactoryAdapter
from zojax.filefield.field import FileFieldProperty

from interfaces import _, IImageRotatorImage


class ImageRotatorImage(object):
    interface.implements(IImageRotatorImage)

    title = None
    
    image = FileFieldProperty(IImageRotatorImage['image'])
    
    thumbnail = FileFieldProperty(IImageRotatorImage['thumbnail'])

    def __init__(self, title=None, image=None, thumbnail=None):
        self.title = title
        self.image = image
        self.thumbnail = thumbnail


registerFactoryAdapter(IImageRotatorImage, ImageRotatorImage)
