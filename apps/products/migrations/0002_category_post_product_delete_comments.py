# Generated by Django 4.2.4 on 2023-08-02 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=128)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product/image')),
                ('name', models.CharField(max_length=128)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('descriptions', models.TextField(blank=True, null=True)),
                ('quantity', models.IntegerField()),
                ('category', models.ManyToManyField(related_name='product', to='products.category')),
            ],
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
