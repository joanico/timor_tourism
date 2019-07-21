from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TourismRichBlock(blocks.StructBlock): 
    text = blocks.RichTextBlock(help_text='WYSIWYG text')
    align = blocks.ChoiceBlock(choices=(
               ('left', 'Left'), ('right', 'Right'),
               ('center', 'Center'), ('justify', 'Justify')),
               required=True, default=('left', 'Left')
     )

    class Meta:
        template = 'home/blocks/tourism_rich_block.html'
