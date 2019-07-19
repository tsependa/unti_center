# Generated by Django 2.2.2 on 2019-07-21 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0002_dashboard_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExportFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_column', models.CharField(max_length=255, verbose_name='Название стобца')),
                ('name_url_arg', models.CharField(max_length=255, verbose_name='Название переменной в GET запросе')),
                ('name_verbose', models.CharField(max_length=255, verbose_name='Отображаемое имя фильтра')),
                ('placeholder', models.CharField(blank=True, default='Поле можно оставить пустым...', max_length=255, null=True, verbose_name='подсказка внутри поля ввода')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('operator', models.CharField(choices=[('==', '=='), ('!=', '!='), ('>', '>'), ('<', '<'), ('>=', '>='), ('<=', '<=')], max_length=255, verbose_name='оператор сравнения')),
                ('is_choices', models.BooleanField(default=False, verbose_name='сформировать choices из базы')),
                ('is_disabled', models.BooleanField(default=False, verbose_name='фильтр выключен')),
                ('data_type', models.CharField(choices=[('str', 'str'), ('int', 'int'), ('datetime', 'datetime')], max_length=255, verbose_name='Тип переменной')),
            ],
            options={
                'verbose_name': 'Фильтр данных',
                'verbose_name_plural': 'Фильтра данных',
            },
        ),
        migrations.CreateModel(
            name='DataExport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('sql', models.TextField(verbose_name='sql запрос к базе')),
                ('is_disabled', models.BooleanField(default=False, verbose_name='экспорт выключен')),
                ('result_file_name', models.CharField(default='result', max_length=255, verbose_name='имя файла для выгрузки')),
                ('filters', models.ManyToManyField(to='center.ExportFilter', verbose_name='фильтры данных при экспрте')),
            ],
            options={
                'verbose_name': 'Эксрорт данных',
                'verbose_name_plural': 'Эксрорт данных',
            },
        ),
    ]