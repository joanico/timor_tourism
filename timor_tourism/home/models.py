from django.db import models


from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.rich_text import RichText
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

#import class sira husi block.py nian iha ne.
from .blocks import TourismRichBlock 

""" Import models ba Menu"""
from django_extensions.db.fields import AutoSlugField
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import (
    MultiFieldPanel,
    InlinePanel,
    FieldPanel,
    PageChooserPanel,
)


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

"""Class sira iha menus/models.py"""

class MenuItem(Orderable):

    link_title = models.CharField(
        blank=True,
        null=True,
        max_length=50
    )
    link_url = models.CharField(
        max_length=500,
        blank=True
    )
    link_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.CASCADE,
    )
    open_in_new_tab = models.BooleanField(default=False, blank=True)

    page = ParentalKey("Menu", related_name="menu_items")

    panels = [
        FieldPanel("link_title"),
        FieldPanel("link_url"),
        PageChooserPanel("link_page"),
        FieldPanel("open_in_new_tab"),
    ]

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_url:
            return self.link_url
        return '#'

    @property
    def title(self):
        if self.link_page and not self.link_title:
            return self.link_page.title
        elif self.link_title:
            return self.link_title
        return 'Missing Title'


@register_snippet
class Menu(ClusterableModel):
    """The main menu clusterable model."""

    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="title", editable=True)
    # slug = models.SlugField()

    panels = [
        MultiFieldPanel([
            FieldPanel("title"),
            FieldPanel("slug"),
        ], heading="Menu"),
        InlinePanel("menu_items", label="Menu Item")
    ]

    def __str__(self):
        return self.title
