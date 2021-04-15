from django.db import migrations, models
import {{cookiecutter.project_slug}}.users.managers
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[
                ("objects", {{cookiecutter.project_slug}}.users.managers.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
        migrations.AddField(
            model_name="user",
            name="uuid",
            field=models.UUIDField(
                db_index=True,
                default=uuid.uuid4,
                editable=False,
                unique=True,
                verbose_name="Public lookup id",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                max_length=254, unique=True, verbose_name="Email address"
            ),
        ),
    ]
