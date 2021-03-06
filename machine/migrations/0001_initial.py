# Generated by Django 3.1 on 2020-08-20 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DbInfo',
            fields=[
                ('db_id', models.AutoField(primary_key=True, serialize=False)),
                ('ip', models.GenericIPAddressField()),
                ('ip_vpn', models.GenericIPAddressField()),
                ('port', models.IntegerField()),
                ('sid', models.CharField(max_length=32)),
                ('user', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=32)),
                ('db_model', models.CharField(max_length=32)),
                ('db_name', models.CharField(max_length=32)),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('uptime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='EnvInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_chinese_name', models.CharField(max_length=32)),
                ('service_name', models.CharField(max_length=32)),
                ('service_host', models.GenericIPAddressField()),
                ('service_port', models.IntegerField()),
                ('service_deploy_path', models.CharField(max_length=200)),
                ('service_url', models.CharField(max_length=50)),
                ('service_model', models.CharField(max_length=32)),
                ('env_model', models.CharField(max_length=32)),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('uptime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=6, null=True)),
                ('telephoneNum', models.IntegerField(null=True)),
            ],
        ),
    ]
