# Generated by Django 5.1.3 on 2024-11-30 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0010_rename_forumtopic_post_topic_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forummodel',
            old_name='description',
            new_name='ForumDescription',
        ),
        migrations.RenameField(
            model_name='forummodel',
            old_name='image',
            new_name='ForumImage',
        ),
        migrations.RenameField(
            model_name='forummodel',
            old_name='name',
            new_name='ForumTitile',
        ),
    ]
