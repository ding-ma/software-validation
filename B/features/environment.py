from behave import use_fixture
from features.fixture import app

def before_feature(context, tag):
    use_fixture(app, context)