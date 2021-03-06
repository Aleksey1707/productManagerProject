# Generated by Django 3.2.7 on 2021-09-10 13:09

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True, validators=[django.core.validators.MinLengthValidator(1, 'Наименование категории не может быть пустым')], verbose_name='Наименование')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='product.category', verbose_name='Родительская категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(1, 'Наименование продукта не может быть пустым')], verbose_name='Наименование')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='product.category')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'default_related_name': 'products',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(1, 'Наименование магазина не может быть пустым')], verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Магазин',
                'verbose_name_plural': 'Магазины',
                'default_related_name': 'shops',
            },
        ),
        migrations.CreateModel(
            name='ProductState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Количество товара не может быть ниже нуля')], verbose_name='Количество')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01'), 'Цена не может быть меньше 0.01 рубля')], verbose_name='Цена')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_states', to='product.product')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_states', to='product.shop')),
            ],
            options={
                'verbose_name': 'Статус товара',
                'verbose_name_plural': 'Статус товаров',
                'default_related_name': 'product_states',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='shops',
            field=models.ManyToManyField(related_name='products', through='product.ProductState', to='product.Shop'),
        ),
    ]
