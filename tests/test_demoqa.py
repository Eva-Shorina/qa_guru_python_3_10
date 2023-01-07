from demoqa.model.pages.practise_form import Form
from demoqa.data.user_data import alla

def test_submitting_form():

    user = alla
    form = Form()
    form.submit_form(user)

    form.validate_form(user)

