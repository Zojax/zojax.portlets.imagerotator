from zope import component, interface, schema
from z3c.form.object import registerFactoryAdapter
from zojax.filefield.field import FileFieldProperty

from interfaces import _, IImageRotatorImage, IImageRotatorButton, IImageRotatorItem
from zojax.persistent.fields.fields import RichText
from zojax.richtext.field import RichTextProperty


class ImageRotatorItem(object):
    
    title = None
    
    image = FileFieldProperty(IImageRotatorItem['image'])
        
    text = RichTextProperty(IImageRotatorItem['text'])


class ImageRotatorImage(ImageRotatorItem):
    interface.implements(IImageRotatorImage)

    thumbnail = FileFieldProperty(IImageRotatorImage['thumbnail'])
    
    url = None


class ImageRotatorButton(ImageRotatorItem):
    
    interface.implements(IImageRotatorButton)
    
    image = FileFieldProperty(IImageRotatorButton['image'])
    
    url = None
    

registerFactoryAdapter(IImageRotatorImage, ImageRotatorImage)

registerFactoryAdapter(IImageRotatorButton, ImageRotatorButton)
