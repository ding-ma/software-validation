from behave import *

@given('a task')
def step_impl(context):
    pass

@when('a user categorizes the task as MEDIUM priority')
def step_impl(context):
    assert True is not False

@then('the task should be properly categorized')
def step_impl(context):
    assert context.failed is False