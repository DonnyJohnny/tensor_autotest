# Есть маркер @pytest.mark.id_check(1, 2, 3), нужно вывести на печать, то что в него передано
#
# >>> 1, 2, 3

import pytest


@pytest.fixture(autouse=True)
def get_param(request):
    """
    Фикстура для получения доступа к пользовательскому маркеру через объект запроса request
    :param request: специальная фикстура FixtureRequest, предоставляющая информацию о запрашиваемой тестовой функции
    """
    mark = request.node.get_closest_marker("id_check")
    print(", ".join([str(i) for i in mark.args]))


@pytest.mark.id_check(1, 2, 3)
def test():

    pass
