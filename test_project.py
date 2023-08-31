from project import choice_menu, print_menu, clear_screen, Input, datetime
import pytest

def test_choice_menu():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        choice_menu(None, True)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == None

def test_print_menu():
    assert print_menu(None, True) == 0

def test_clear_screen():
    assert clear_screen(True) == 0

def test_input_choice():
    with pytest.raises(ValueError):
        Input.check.choice("5")
    assert Input.check.choice("1") == "1"
    assert Input.check.choice("9") == "9"

def test_input_title():
    with pytest.raises(ValueError):
        Input.check.title("")
    with pytest.raises(ValueError):
        Input.check.title("a" * 60)
    assert Input.check.title("a" * 59) == "a" * 59
    assert Input.check.title("test32") == "test32"

def test_input_priority():
    with pytest.raises(ValueError):
        Input.check.priority("")
    with pytest.raises(ValueError):
        Input.check.priority("10")
    assert Input.check.priority("1") == 1
    assert Input.check.priority("9") == 9

def test_due_date():
    with pytest.raises(ValueError):
        Input.check.due_date("2308-01")
    with pytest.raises(ValueError):
        Input.check.due_date("12")
    with pytest.raises(ValueError):
        Input.check.due_date("2023-13-1")
    print(Input.check.due_date("2023-08-1"))
    assert Input.check.due_date("2023-08-1") == datetime(2023, 8, 1, 0, 0)
    assert Input.check.due_date("2023-12-01") == datetime(2023, 12, 1, 0, 0)
