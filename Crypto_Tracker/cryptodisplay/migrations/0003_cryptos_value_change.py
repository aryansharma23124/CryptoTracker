<<<<<<< HEAD
# Generated by Django 2.0.3 on 2018-03-26 17:05
=======
# Generated by Django 2.0.3 on 2018-03-26 15:21
>>>>>>> e83c084912856bed5ff778041cb7e6a9c433f426

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptodisplay', '0002_cryptos_crypto_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='cryptos',
            name='value_change',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]