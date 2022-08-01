# Generated by Django 3.2.8 on 2022-03-02 20:56

import django.db.models.deletion
from django.db import migrations, models

import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0066_collection_management_permissions"),
    ]

    operations = [
        migrations.CreateModel(
            name="SiteWideAlertSettings",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sitewide_alert_enabled",
                    models.BooleanField(
                        default=False, verbose_name="Enable sitewide alert"
                    ),
                ),
                (
                    "sitewide_alert_text",
                    wagtail.core.fields.RichTextField(
                        blank=True, verbose_name="Alert text"
                    ),
                ),
                (
                    "site",
                    models.OneToOneField(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wagtailcore.site",
                    ),
                ),
            ],
            options={
                "verbose_name": "Sitewide alert",
            },
        ),
    ]
