from adminlte_full.models import MenuModel, MenuItemModel


def menu_deploy():
    """
    Создает базовые меню и пункты меню
    """
    MenuModel.objects.create(title='Стандартное меню', program_name='default_menu')
    MenuModel.objects.create(title='Меню сотрудников', program_name='admin_menu')
    MenuModel.objects.create(title='Меню клиентов', program_name='customer_menu')
    MenuModel.objects.create(title='Меню докторов', program_name='doctor_menu')
    MenuModel.objects.create(title='Меню фармацевтов', program_name='buyer_menu')

    MenuItemModel.objects.create(
        menu=MenuModel.objects.get(program_name='admin_menu'),
        title="Пользовательские меню",
        type='link',
        url='user_menu',
        endpoint='user_menu',
        endpoint_args='user_menu',
        endpoint_kwargs='user_menu',
        icon='fas fa-server',
        help="Пункт меню для создания новых пунктов меню"
    )

    MenuItemModel.objects.create(
        menu=MenuModel.objects.get(program_name='admin_menu'),
        title="Пользователи",
        type='link',
        url='user_search',
        endpoint='user_search',
        endpoint_args='user_search',
        endpoint_kwargs='user_menu',
        icon='fas fa-search',
        help="Пункт меню для просмотра данных пользователей"
    )
