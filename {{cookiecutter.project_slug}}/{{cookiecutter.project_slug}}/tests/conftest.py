import pytest
from pytest_factoryboy import register as factory_register
from pytest_factoryboy.fixture import get_caller_module, get_model_name, make_fixture

from {{cookiecutter.project_slug}}.tests.factories import UserFactory


def json_fixture(request, factory_class):
    return factory_class.json()


def register(factory_class, _name=None, **kwargs):
    factory_register(factory_class, _name=_name, **kwargs)
    module = get_caller_module()
    model_name = get_model_name(factory_class) if _name is None else _name
    name = f'{model_name}_json'

    make_fixture(name, module, json_fixture, factory_class=factory_class)


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


register(UserFactory)
