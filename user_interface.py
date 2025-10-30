from typing import Any, Union

from calculator import EmploymentContractTaxCalculator, CivilContractTaxCalculator, TaxCalculator
from config import ContractType


class UserInterface:
    @staticmethod
    def _get_valid_float_input() -> Union[float, str]:
        try:
            return float(input("Enter income: "))
        except ValueError:
            return "Incorrect input! You must enter a number."

    @staticmethod
    def _get_valid_contract_type_input() -> Union[ContractType, str]:
        prompt = "Enter contract type - (E)mployment, (C)ivil: "

        try:
            input_contract_type = input(prompt)[0].lower()
            for contract_type in ContractType:
                if input_contract_type == contract_type.value[0] or input_contract_type == contract_type.value[0].lower():
                    return contract_type.value
            raise ValueError

        except (IndexError, ValueError):
            return "Incorrect contract type! You must enter one of the provided codes."

    @staticmethod
    def initialize_with_input_data() -> tuple[Any, Any]:
        income_result = UserInterface._get_valid_float_input()
        if isinstance(income_result, str):
            return income_result

        contract_result = UserInterface._get_valid_contract_type_input()
        try:
            ContractType(contract_result)
        except ValueError:
            return contract_result

        return income_result, contract_result

    @staticmethod
    def perform_contract_calculations(income: float, contract_type: ContractType) -> None:
        calculator_map = {
            ContractType.EMPLOYMENT: EmploymentContractTaxCalculator,
            ContractType.CIVIL: CivilContractTaxCalculator
        }

        calculator_class = calculator_map.get(contract_type, TaxCalculator)
        calculator = calculator_class(income, contract_type)
        calculator.run()

    def run_calculator(self):
        data_or_error = UserInterface.initialize_with_input_data()

        if isinstance(data_or_error, str):
            print(data_or_error)
            return

        income, contract_type = data_or_error
        self.perform_contract_calculations(income, contract_type)
