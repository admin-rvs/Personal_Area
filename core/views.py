from datetime import datetime, timedelta
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.urls import reverse
# from django.contrib import auth, messages
from django.shortcuts import render
# from django import forms
# from django.http import JsonResponse
# from django.urls import reverse_lazy
from django.views import View
from adminlte_base import MenuLoader, Message,  Dropdown
# from adminlte_base import MenuItem, Notification, Task, ThemeColor
from .forms import RoleForm, ModalWindowForm, KostylForm
from adminlte_full.adminlte import manager
from adminlte_full.models import MenuModel
from .utils import menu_deploy

User = get_user_model()


class IndexView(View):
    template_name = 'core/index.html'
    form_class = RoleForm
    form_class_modal_window = ModalWindowForm
    form_class_kostyl_form = KostylForm

    @method_decorator(login_required)
    def get(self, request):
        user = User.objects.get(phone=self.request.user)
        is_data_filled = '0'
        if user.role == 1:
            if not user.first_name or not user.last_name or not user.middle_name \
                    or not user.date_of_birth or not user.email or not user.region \
                    or not user.city or not user.street or not user.house\
                    or not user.zip_code or not user.number or not user.tax_number:
                is_data_filled = '1'

        form_modal_window = self.form_class_modal_window(
            initial={
                'first_name': user.first_name,
                'last_name': user.last_name,
                'middle_name': user.middle_name,
                'sex': user.sex,
                'email': user.email,
                'date_of_birth': user.date_of_birth,
                'region': user.region,
                'city': user.city,
                'street': user.street,
                'house': user.house,
                'apartment': user.apartment,
                'zip_code': user.zip_code,
                'series': user.series,
                'number': user.number,
                'tax_number': user.tax_number,
                'organization': user.organization,
                'position': user.position,
            })
        kostyl_form = self.form_class_kostyl_form(
            initial={
                'is_data_filled': is_data_filled
            }
        )
        try:
            MenuModel.objects.get(program_name='default_menu')
        except MenuModel.DoesNotExist:
            menu_deploy()

        return render(request, self.template_name, {'form': self.form_class,
                                                    'form_modal_window': form_modal_window,
                                                    'kostyl_form': kostyl_form})

    def post(self, request):
        form = self.form_class(request.POST)
        form_modal_window = self.form_class_modal_window(request.POST)
        if form.is_valid():
            phone = request.user.get_username()
            user = User.objects.get(phone=phone)
            user.role = form.cleaned_data['role']
            user.save()
            return HttpResponseRedirect(
                reverse('index')
            )
        if form_modal_window.is_valid():
            user = User.objects.get(phone=self.request.user.phone)
            user.first_name = form_modal_window.cleaned_data['first_name']
            user.last_name = form_modal_window.cleaned_data['last_name']
            user.middle_name = form_modal_window.cleaned_data['middle_name']
            user.email = form_modal_window.cleaned_data['email']
            user.sex = form_modal_window.cleaned_data['sex']
            user.date_of_birth = form_modal_window.cleaned_data['date_of_birth']
            user.region = form_modal_window.cleaned_data['region']
            user.city = form_modal_window.cleaned_data['city']
            user.street = form_modal_window.cleaned_data['street']
            user.house = form_modal_window.cleaned_data['house']
            user.apartment = form_modal_window.cleaned_data['apartment']
            user.zip_code = form_modal_window.cleaned_data['zip_code']
            user.series = form_modal_window.cleaned_data['series']
            user.number = form_modal_window.cleaned_data['number']
            user.tax_number = form_modal_window.cleaned_data['tax_number']
            user.organization = form_modal_window.cleaned_data['organization']
            user.position = form_modal_window.cleaned_data['position']
            user.save()
            return render(request, self.template_name, {'form': form, 'form_modal_window': form_modal_window})
        return render(request, self.template_name, {'form': form, 'form_modal_window': form_modal_window})


@manager.menu_loader
class MyMenuLoader(MenuLoader):
    def __call__(self, user):
        if user.is_superuser:
            return MenuModel.objects.get(program_name='admin_menu')
        if user.role == 1:
            # CUSTOMER
            return MenuModel.objects.get(program_name='customer_menu')
        if user.role == 2:
            # DOCTOR
            return MenuModel.objects.get(program_name='doctor_menu')
        if user.role == 3:
            # BUYER
            return MenuModel.objects.get(program_name='buyer_menu')
        return MenuModel.objects.get(program_name='default_menu')

    def sidebar_menu(self):
        menu = self._create(self(user=self.context['request'].user), active_path=self.context['request'].path)
        return menu


@manager.messages_loader
def load_messages(context):
    now = datetime.now()
    sender = context['user']
    messages = Dropdown('#', 15)
    messages.add(Message(sender, 'Тестовое сообщение 1', '#', sent_at=now - timedelta(seconds=16)), )

    return messages
