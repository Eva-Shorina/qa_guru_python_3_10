from allure_commons.types import Severity

from demoqa.model.pages.practise_form import Form
from demoqa.data.user_data import alla
import allure

def test_submitting_form(setup_browser):
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.NORMAL)
    allure.dynamic.label('owner', 'eva.shorina')
    allure.dynamic.feature('Проверка отправки формы')


    form = Form()

    with allure.step('Заполняем данные формы'):
        form.submit_form(alla)

    with allure.step('Проверяем, что данные формы есть в результирующей таблице'):
        form.validate_form(alla)

