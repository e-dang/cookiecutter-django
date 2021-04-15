import pytest
from pytest_factoryboy import register

from {{ cookiecutter.project_slug }}.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


register(UserFactory)
