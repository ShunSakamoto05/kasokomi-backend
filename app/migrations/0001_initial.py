# Generated by Django 3.2.9 on 2022-01-22 18:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=64, verbose_name='コメント')),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='部屋名')),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CoinMarketInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='NotFound', max_length=32, verbose_name='名前')),
                ('symbol', models.CharField(default='NotFound', max_length=32, verbose_name='シンボル')),
                ('rank', models.IntegerField(default='NotFound', verbose_name='ランク')),
                ('day_perchange', models.FloatField(default='NotFound', verbose_name='24h変化')),
                ('market_cap', models.FloatField(default='NotFound', verbose_name='マーケットキャップ')),
                ('last_updated', models.CharField(max_length=50, verbose_name='最終更新日')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.chatroom')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.chatmessage')),
            ],
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='room_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_name_chatmessage', to='app.chatroom'),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='username_chatmessage', to=settings.AUTH_USER_MODEL),
        ),
    ]
