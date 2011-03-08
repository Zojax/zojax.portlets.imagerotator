from zope import component, interface, schema
from z3c.form.object import registerFactoryAdapter
from zojax.filefield.field import FileFieldProperty

from interfaces import _, IImageRotatorImage
from zojax.persistent.fields.fields import RichText
from zojax.richtext.field import RichTextProperty


class ImageRotatorImage(object):
    interface.implements(IImageRotatorImage)

    title = None
    
    image = FileFieldProperty(IImageRotatorImage['image'])
    
    detailImage = FileFieldProperty(IImageRotatorImage['detailImage'])
    
    thumbnail = FileFieldProperty(IImageRotatorImage['thumbnail'])
    
    text = RichTextProperty(IImageRotatorImage['text'])
    
    detailText = RichTextProperty(IImageRotatorImage['detailText'])

    def __init__(self, **kw):
        map(lambda x:setattr(self, x[0], x[1]), kw.items())

registerFactoryAdapter(IImageRotatorImage, ImageRotatorImage)
