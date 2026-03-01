from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("bd_models", "0014_alter_ball_options_alter_ballinstance_options_and_more")]

    operations = [
        # Add F1-specific fields to Ball (driver)
        migrations.AddField(
            model_name="ball",
            name="nationality",
            field=models.CharField(blank=True, help_text="Driver's nationality", max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="ball",
            name="car_number",
            field=models.IntegerField(blank=True, help_text="Driver's race car number", null=True),
        ),
        migrations.AddField(
            model_name="ball",
            name="championships",
            field=models.IntegerField(default=0, help_text="Number of Formula 1 World Championships won"),
        ),
        # Rename Regime → Constructor in admin display
        migrations.AlterModelOptions(
            name="regime",
            options={
                "managed": True,
                "verbose_name": "Constructor",
                "verbose_name_plural": "Constructors",
            },
        ),
        # Rename Economy → Engine Supplier in admin display
        migrations.AlterModelOptions(
            name="economy",
            options={
                "managed": True,
                "verbose_name": "Engine Supplier",
                "verbose_name_plural": "Engine Suppliers",
            },
        ),
    ]
