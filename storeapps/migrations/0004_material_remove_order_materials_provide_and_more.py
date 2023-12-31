# Generated by Django 4.2 on 2023-12-06 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapps', '0003_remove_order_user_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='materials_provide',
        ),
        migrations.AlterField(
            model_name='order',
            name='purpose',
            field=models.CharField(choices=[('place_order', 'Place Order'), ('return', 'Return'), ('enquiry', 'Enquiry')], max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='materials_provide',
            field=models.ManyToManyField(to='storeapps.material'),
        ),
    ]
