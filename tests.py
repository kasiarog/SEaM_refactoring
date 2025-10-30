from user_interface import UserInterface


def mock_multiple_inputs(inputs):
    input_iterator = iter(inputs)
    return lambda *args, **kwargs: next(input_iterator)


def test_employment_contract_1(monkeypatch, capsys):
    income = "1000"
    contract_type_input = "E"
    user_inputs = [income, contract_type_input]

    monkeypatch.setattr('builtins.input', mock_multiple_inputs(user_inputs))

    UserInterface().run_calculator()
    captured = capsys.readouterr()

    expected_output_fragment = "NET INCOME = 716.73"

    assert expected_output_fragment in captured.out
    assert captured.err == ""


def test_employment_contract_2(monkeypatch, capsys):
    income = "2000"
    contract_type_input = "E"
    user_inputs = [income, contract_type_input]

    monkeypatch.setattr('builtins.input', mock_multiple_inputs(user_inputs))

    UserInterface().run_calculator()
    captured = capsys.readouterr()

    expected_output_fragment = "NET INCOME = 1387.13"

    assert expected_output_fragment in captured.out
    assert captured.err == ""


def test_civil_contract_1(monkeypatch, capsys):
    income = "1000"
    contract_type_input = "C"
    user_inputs = [income, contract_type_input]

    monkeypatch.setattr('builtins.input', mock_multiple_inputs(user_inputs))

    UserInterface().run_calculator()
    captured = capsys.readouterr()

    expected_output_fragment = "NET INCOME = 670.40"

    assert expected_output_fragment in captured.out
    assert captured.err == ""


def test_civil_contract_2(monkeypatch, capsys):
    income = "2000"
    contract_type_input = "C"
    user_inputs = [income, contract_type_input]

    monkeypatch.setattr('builtins.input', mock_multiple_inputs(user_inputs))

    UserInterface().run_calculator()
    captured = capsys.readouterr()

    expected_output_fragment = "NET INCOME = 1340.80"

    assert expected_output_fragment in captured.out
    assert captured.err == ""
