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
