# Generated by Django 2.0.5 on 2018-05-23 19:08

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('peregrine', '0006_auto_20180418_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitepage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.TextBlock(icon='title', template='wagtailcontentstream/blocks/heading.html')), ('paragraph', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'ol', 'ul', 'monospace'], icon='pilcrow')), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='The image to display.')), ('caption', wagtail.core.blocks.TextBlock(help_text='The caption will appear under the image, if entered.', required=False)), ('credit', wagtail.core.blocks.TextBlock(help_text='The credit will appear under the image, if entered.', required=False)), ('align', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('center', 'Center'), ('full', 'Full Width')], help_text='How to align the image in the body of the page.'))])), ('document', wagtail.documents.blocks.DocumentChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='media')), ('table', wagtail.contrib.table_block.blocks.TableBlock(icon='table')), ('code', wagtail.core.blocks.StructBlock([('language', wagtail.core.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('diff', 'diff'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')], help_text='Coding language', label='Language')), ('code', wagtail.core.blocks.TextBlock(label='Code'))], icon='code'))], blank=True),
        ),
    ]