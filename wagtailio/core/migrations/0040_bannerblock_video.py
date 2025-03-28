# Generated by Django 2.2.24 on 2021-07-22 13:26

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtail.snippets.blocks
import wagtailmedia.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_homepage_brands'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('banner', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=128)), ('sub_title', wagtail.core.blocks.CharBlock(max_length=128)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('video', wagtailmedia.blocks.VideoChooserBlock(required=False)), ('background', wagtail.images.blocks.ImageChooserBlock(required=False)), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock()), ('link_text_bold', wagtail.core.blocks.CharBlock(required=False)), ('link_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('link_url', wagtail.core.blocks.CharBlock(required=False))], icon='link')))])), ('brands', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('brands2', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock())])))])), ('features', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('subtitle', wagtail.core.blocks.CharBlock(required=False)), ('all_features_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('features', wagtail.core.blocks.ListBlock(wagtail.snippets.blocks.SnippetChooserBlock('features.FeatureDescription')))])), ('testimonials', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.TextBlock()), ('author', wagtail.core.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.core.blocks.URLBlock(required=False))]), icon='group')), ('code', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('subtitle', wagtail.core.blocks.CharBlock(required=False)), ('code', wagtail.core.blocks.StructBlock([('language', wagtail.core.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('django', 'Django templating language'), ('html', 'HTML'), ('javascript', 'Javascript'), ('python', 'Python'), ('scss', 'SCSS')])), ('code', wagtail.core.blocks.TextBlock())])), ('link', wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock()), ('link_text_bold', wagtail.core.blocks.CharBlock(required=False)), ('link_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('link_url', wagtail.core.blocks.CharBlock(required=False))]))])), ('showcases', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('subtitle', wagtail.core.blocks.CharBlock(required=False)), ('more_link', wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock()), ('link_text_bold', wagtail.core.blocks.CharBlock(required=False)), ('link_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('link_url', wagtail.core.blocks.CharBlock(required=False))], required=False)), ('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('subtitle', wagtail.core.blocks.CharBlock(required=False)), ('link_url', wagtail.core.blocks.URLBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock())])))])), ('promo_texts', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('texts', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('text', wagtail.core.blocks.RichTextBlock())])))]))]),
        ),
    ]
