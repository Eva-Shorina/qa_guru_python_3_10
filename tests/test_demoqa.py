from demoqa.model.pages.practise_form import Form
from demoqa.data.user_data import alla

def test_submitting_form():

    form = Form()
    form.submit_form(alla)

    form.validate_form(alla)

