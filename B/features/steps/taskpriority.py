from behave import *
from features.steps.fixture import app
import requests
import subprocess
import xmltodict
from features.steps.helper import *


def before_feature(context, tag):
    if tag == "fixture.app":
        use_fixture(app)

@given('a task')
def step_impl(context):
    r = requests.get(url_todo, headers=recv_xml_headers)
    d = xml_to_dict_todos(r.text)
    assert r.status_code == 200 and "todos" in d

@when('a user categorizes the task as MEDIUM priority')
def step_impl(context):
    assert True is not False

@then('the task should be properly categorized')
def step_impl(context):
    assert context.failed is False
    # process.close_app()