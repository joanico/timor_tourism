from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

# Class ba field nebe fo naran body iha model konaba paragraph nian.
class TourismRichBlock(blocks.StructBlock): 
    """Text no align ba paragraph nebe atu add"""
    text = blocks.RichTextBlock(help_text='WYSIWYG text')
    align = blocks.ChoiceBlock(choices=(
               ('left', 'Left'), ('right', 'Right'),
               ('center', 'Center'), ('justify', 'Justify')),
               required=True, default=('left', 'Left')
     )

    class Meta:
        template = 'home/blocks/tourism_rich_block.html'


class BaseLinkBlock(blocks.StructBlock):
    """
    Base StructBlock class used to prevent DRY code.
    """
    display_text = blocks.CharBlock()


class ExternalLinkBlock(BaseLinkBlock):
    """
    Block that holds a link to any URL.
    """
    link = blocks.URLBlock()

    class Meta:
        template = 'home/menu/external_link_block.html'

class PageLinkBlock(BaseLinkBlock):
    """
    Block that holds a page.
    """
    page = blocks.PageChooserBlock()

    class Meta:
        template = 'home/menu/page_link_block.html'

class LinkChildrenBlock(blocks.StructBlock):
    """
    Base childblock for second level children.
    """
    children = blocks.StreamBlock(
            [
                ('external_link', ExternalLinkBlock()),
                ('page_link', PageLinkBlock()),
            ]
        )

class ExternalLinkWithChildrenBlock(LinkChildrenBlock, ExternalLinkBlock):
    """
    Uses LinkChildrenBlock as a mixin to create an ExternalLinkBlock that supports Children.
    """
    pass

class PageLinkWithChildrenBlock(LinkChildrenBlock, PageLinkBlock):
    """
    Uses LinkChildrenBlock as a mixin to create a PageLinkBlock that supports Children.
    """
    pass
