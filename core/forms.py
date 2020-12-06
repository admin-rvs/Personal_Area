from crispy_forms.bootstrap import AppendedText, PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from django import forms
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _

from . import msgs

# Лэйблы
from .choices import SEX_CHOICES, REGION_CHOICES

ROLE_LABEL = _(u"Роль")
IDENTIFICATION_METHOD = _(u"Метод идентификации")

FIRST_NAME_LABEL = _(u"Ім")
LAST_NAME_LABEL = _(u"Фамилия")
MIDDLE_NAME_LABEL = _(u"Отчество")

# Вспомогательный текст

ROLE_HELP = _(u"")
IDENTIFICATION_HELP = _(
    u"С помощью номера договора или другого метода идентификации мы узнаем ваше "
    u"имя и предоставим всю нужную информацию")


class RoleForm(forms.Form):
    ROLE_CHOICES = (
        (0, 'Не выбрано'),
        (1, 'Клиент'),
        (2, 'Доктор'),
        (3, 'Фармацевт')
    )
    IDENTIFICATION_CHOICES = (
        (0, 'По номеру договора'),
        (1, 'По паспорту'),
        (2, 'По другому документу')
    )

    role = forms.ChoiceField(
        label=ROLE_LABEL,
        choices=ROLE_CHOICES,
        help_text="""Это поле сделано для теста, чтобы вы могли проверить как работают группы пользователей 
        в зависимости от роли, в будущем я думаю, что это вводить будет не нужно, а по номеру договора или другому 
        идентификатору мы будем определять группу пользователя."""
    )

    identification_method = forms.ChoiceField(
        label=IDENTIFICATION_METHOD,
        choices=IDENTIFICATION_CHOICES,
        help_text="""Это поле сейчас никак не работает, оно здесь стоит для примера, чтобы показать такую модель 
        взаимодействия с интерфейсом. Человек идентифицируется, например, по номеру договора и так определяется его роль
        и интерфейс, который он видит"""
    )

    @property
    def helper(self):
        helper = FormHelper()
        helper.form_show_labels = True
        helper.form_tag = False
        helper.layout = Layout(
            'role',
            'identification_method'
        )
        return helper

    def clean_role(self):
        """
        Проверка роли
        """

        role = self.cleaned_data.get('role')
        if role == '':
            raise forms.ValidationError(msgs.ROLE_ERROR)

        return role


class KostylForm(forms.Form):
    is_data_filled = forms.CharField()

    def helper(self):
        helper = FormHelper()
        helper.form_show_labels = True
        helper.form_tag = False
        helper.layout = Layout(
            AppendedText(
                'is_data_filled',
                mark_safe('<span class="fas fa-keyboard" id="is_data_filled"></span>'),
            )
        )
        return helper


class ModalWindowForm(forms.Form):
    """
    Персональные данные
    """
    first_name = forms.CharField(
        label='Ім\'я',
        max_length=50,
        required=True
    )
    last_name = forms.CharField(
        label='Прізвище',
        max_length=50,
        required=True
    )
    middle_name = forms.CharField(
        label='По батькові',
        max_length=50,
        required=True
    )
    email = forms.EmailField(
        label='Email',
        required=True
    )
    date_of_birth = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date'}
        ),
        label='Дата народження',
        help_text='Наприклад 18.01.1994',
        required=True,

    )
    sex = forms.ChoiceField(
        label='Стать',
        choices=SEX_CHOICES,
        required=True
    )
    region = forms.ChoiceField(
        label='Область',
        choices=REGION_CHOICES,
        required=True
    )
    city = forms.CharField(
        label='Місто',
        max_length=50,
        required=True
    )
    street = forms.CharField(
        label='Вулиця',
        max_length=50,
        required=True
    )
    house = forms.CharField(
        label='Дім',
        max_length=50,
        required=True
    )
    apartment = forms.CharField(
        label='Квартира',
        max_length=50,
        required=True

    )
    zip_code = forms.CharField(
        label='Індекс',
        max_length=50,
        required=True
    )
    series = forms.CharField(
        label='Серія',
        max_length=50,
        required=False,
        help_text='Якщо у вас паспорт зразка 1994 року'
    )
    number = forms.CharField(
        label='Номер',
        max_length=50,
        required=True,
        help_text='Для паспортів нового та старого зразку'
    )
    tax_number = forms.CharField(
        label='Налоговий номер',
        max_length=50,
        required=True,
        help_text='У паспортах нового зразку вказано як РНКОПП'
    )
    organization = forms.CharField(
        label='Установа',
        max_length=50,
        required=False
    )
    position = forms.CharField(
        label='Посада',
        max_length=50,
        required=False
    )

    @property
    def helper(self):
        helper = FormHelper()
        helper.form_show_labels = True
        helper.form_tag = False
        helper.layout = Layout(
            PrependedText('first_name',
                          '<input type="checkbox" checked="checked" value="" id="" name="first_name" '
                          'class="textinput textInput form-control-sm">',
                          active=True),
            'first_name',
            'last_name',
            'middle_name',
            'email',
            'date_of_birth',
            'sex',
            'region',
            'city',
            'street',
            'house',
            'apartment',
            'zip_code',
            'series',
            'number',
            'tax_number',
            'organization',
            'position',

        )
        return helper
