# Generated by Django 4.0.2 on 2022-03-07 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_account_birth_date'),
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='comment_like', to='users.Account'),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='post_like', to='users.Account'),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matn', models.CharField(blank=True, max_length=50)),
                ('vaqt', models.DateTimeField(auto_now_add=True)),
                ('media', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='feed.media')),
                ('qabul', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_qabul', to='users.account')),
                ('yuboruvchi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_yuboruvchi', to='users.account')),
            ],
        ),
    ]