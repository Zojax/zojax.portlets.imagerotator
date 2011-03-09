from zope import component, interface, schema
from z3c.form.object import registerFactoryAdapter
from zojax.filefield.field import FileFieldProperty

from interfaces import _, IImageRotatorImage, IImageRotatorButton
from zojax.persistent.fields.fields import RichText
from zojax.richtext.field import RichTextProperty


class ImageRotatorItem(object):
    
    title = None
    
    image = FileFieldProperty(IImageRotatorImage['image'])
        
    text = RichTextProperty(IImageRotatorImage['text'])
    
    def __init__(self, **kw):
        map(lambda x:setattr(self, x[0], x[1]), kw.items())


class ImageRotatorImage(ImageRotatorItem):
    interface.implements(IImageRotatorImage)

    thumbnail = FileFieldProperty(IImageRotatorImage['thumbnail'])
    
    def __init__(self, **kw):
        map(lambda x:setattr(self, x[0], x[1]), kw.items())
        

class ImageRotatorButton(ImageRotatorItem):
    
    interface.implements(IImageRotatorButton)
    
    url = None
    

registerFactoryAdapter(IImageRotatorImage, ImageRotatorImage)

registerFactoryAdapter(IImageRotatorButton, ImageRotatorButton)
