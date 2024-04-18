from deep_functions import check_answer


def test_check_answer():
    assert check_answer("42") == "Yes"
    assert check_answer(" 42") == "Yes"
    assert check_answer("forty two") == "Yes"
    assert check_answer("forty-two") == "Yes"
    assert check_answer("5") == "No"

