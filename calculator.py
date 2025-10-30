from dataclasses import dataclass

from config import TaxRates, AmountConstants, ContractType
from printer import TaxReportPrinter


@dataclass
class TaxReport:
    contract_type: str
    income: float
    social_security_tax: float
    health_social_security_tax: float
    sickness_social_security_tax: float
    income_after_social_contributions: float
    health_tax_9_percent: float
    health_tax_7_percent: float
    deductible_expenses: float
    taxable_income: float
    advance_tax: float
    tax_free_income: float
    advance_paid_tax: float
    net_income: float


class TaxCalculator:
    def __init__(self, income: float = 0.0, contract_type: ContractType = None):
        self.income = income
        self.contract_type = contract_type

        self.social_security_tax = 0
        self.health_social_security_tax = 0
        self.sickness_social_security_tax = 0

        self.health_tax_9_percent = 0
        self.health_tax_7_percent = 0

        self.advance_tax = 0
        self.advance_paid_tax = 0
        self.deductible_expenses = AmountConstants.DEDUCTIBLE_EXPENSES
        self.tax_free_income = AmountConstants.TAX_FREE_INCOME

        self.income_after_social_contributions = 0
        self.net_income = 0

    def _calculate_social_contributions(self) -> None:
        self.social_security_tax = self.income * TaxRates.SOCIAL_SECURITY
        self.health_social_security_tax = self.income * TaxRates.HEALTH_SOCIAL_SECURITY
        self.sickness_social_security_tax = self.income * TaxRates.SICKNESS_SOCIAL_SECURITY

        self.income_after_social_contributions = self.income - (self.social_security_tax + self.health_social_security_tax + self.sickness_social_security_tax)

    def _calculate_health_taxes(self) -> None:
        self.health_tax_9_percent = self.income * TaxRates.HEALTH_TAX_9
        self.health_tax_7_percent = self.income * TaxRates.HEALTH_TAX_7_75

    def _calculate_advance_tax(self) -> None:
        self.advance_tax = self.income * TaxRates.ADVANCE_TAX

    def _calculate_advance_paid_tax(self) -> None:
        self.advance_paid_tax = self.advance_tax - self.health_tax_7_percent - self.tax_free_income

    def _calculate_net_income(self) -> float:
        all_deductions = (
                self.social_security_tax
                + self.health_social_security_tax
                + self.sickness_social_security_tax
                + self.health_tax_9_percent
                + self.advance_paid_tax
        )
        self.net_income = self.income - all_deductions
        return self.net_income

    def _calculate_common_taxes(self) -> None:
        self._calculate_social_contributions()
        self._calculate_health_taxes()
        self._calculate_advance_tax()
        self._calculate_advance_paid_tax()
        self._calculate_net_income()

    def _set_contract_specific_values(self) -> None: ...

    def calculate_taxes(self):
        self._set_contract_specific_values()
        self._calculate_common_taxes()
        return TaxReport(
            contract_type=self.contract_type,
            income=self.income,
            social_security_tax=self.social_security_tax,
            health_social_security_tax=self.health_social_security_tax,
            sickness_social_security_tax=self.sickness_social_security_tax,
            income_after_social_contributions=self.income_after_social_contributions,
            health_tax_9_percent=self.health_tax_9_percent,
            health_tax_7_percent=self.health_tax_7_percent,
            deductible_expenses=self.deductible_expenses,
            taxable_income=self.income_after_social_contributions - self.deductible_expenses,
            advance_tax=self.advance_tax,
            tax_free_income=self.tax_free_income,
            advance_paid_tax=self.advance_paid_tax,
            net_income=self.net_income,
        )

    def run(self) -> None:
        tax_report = self.calculate_taxes()
        TaxReportPrinter.print_tax_report(tax_report)


class EmploymentContractTaxCalculator(TaxCalculator):
    ...


class CivilContractTaxCalculator(TaxCalculator):
    def _set_contract_specific_values(self):
        self.tax_free_income = 0
        self._calculate_social_contributions()
        self.deductible_expenses = self.income_after_social_contributions * TaxRates.DEDUCTIBLE_EXPENSES_RATE
