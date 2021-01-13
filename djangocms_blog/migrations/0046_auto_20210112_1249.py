from django.db import migrations
import django.db.models.deletion
import parler.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_blog', '0045_auto_20200421_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcategorytranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='djangocms_blog.BlogCategory'),
        ),
        migrations.AlterField(
            model_name='blogconfigtranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='djangocms_blog.BlogConfig'),
        ),
        migrations.AlterField(
            model_name='posttranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='djangocms_blog.Post'),
        ),
    ]
