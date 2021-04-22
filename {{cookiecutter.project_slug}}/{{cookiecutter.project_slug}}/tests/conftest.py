from pathlib import Path

import pytest
from pytest_factoryboy import register as factory_register
from pytest_factoryboy.fixture import get_caller_module, get_model_name, make_fixture
{%- if cookiecutter.use_drf == "y" %}
from rest_framework.test import APIClient
{%- endif %}

from {{cookiecutter.project_slug}}.tests.factories import UserFactory


def json_fixture(request, factory_class):
    return factory_class.json()


def register(factory_class, _name=None, **kwargs):
    factory_register(factory_class, _name=_name, **kwargs)
    module = get_caller_module()
    model_name = get_model_name(factory_class) if _name is None else _name
    name = f"{model_name}_json"

    make_fixture(name, module, json_fixture, factory_class=factory_class)


register(UserFactory)


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath

{% if cookiecutter.use_drf == "y" %}
@pytest.fixture
def api_client() -> APIClient:
    return APIClient()


@pytest.fixture
def test_password() -> str:
    return "mytestpassword123"

{% endif %}
def pytest_collection_modifyitems(config, items):
    """Give tests a specific mark based on the test type directory they are in"""

    rootdir = Path(config.rootdir)
    for item in items:
        rel_path = Path(item.fspath).relative_to(rootdir)
        if "unit" in str(rel_path):
            item.add_marker("unit")
        elif "integration" in str(rel_path):
            item.add_marker("integration")
        elif "functional" in str(rel_path):
            item.add_marker("functional")
