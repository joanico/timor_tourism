from django.db import models


from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.rich_text import RichText
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

#import class sira husi block.py nian iha ne.
from .blocks import TourismRichBlock

# kria pajina dahuluk nia
class HomePage(Page):
    """Field ba imajen iha pajina dahuluk nia"""
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+')
    # Field ba body ka text iha pajina dahuluk nian
    body = StreamField(
            [
                ('paragraph', TourismRichBlock()) # paragraph refere kria pajina dahuluk nian no TourismRichBlock refere ba class husi block.py ba pajina dahuluk nian.
            ]
        )
    # contenet_panel refere ba field nebe kria ona iha leten.
    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        StreamFieldPanel('body'),
    ]
