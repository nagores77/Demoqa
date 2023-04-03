import pytest

@pytest.mark.skup(reason='Причина пропуска')
def test_skip():
    assert True

@pytest.mark.xfail(condition=True,reason='причина, по которой тестовая функция помечена, как xfail')
def test_xfail_2():


    #Если тест упадет, он пометится, как skipped - тест пропущен
    #если тест пройдет, он пометится, как passed
    # в обоих случаях в отчет добавится тег "ожидаемый сбой"

    assert False

@pytest.mark.xfail(condition=True, reason='причина, по которой тестовая функция помечена, как xfail')
def test_xfail_2():
    assert True
