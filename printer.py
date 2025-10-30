from config import ContractType

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from calculator import TaxReport


class TaxReportPrinter:
    @staticmethod
    def print_tax_report(tax_report: 'TaxReport'):
        contract_type = tax_report.contract_type

        print(f"\n--- {contract_type.upper()} CONTRACT ---\n")
        print(f"Income: {tax_report.income:.2f}")
        print(f"Social security tax: {tax_report.social_security_tax:.2f}")
        print(f"Health social security tax: {tax_report.health_social_security_tax:.2f}")
        print(f"Sickness social security tax:  {tax_report.sickness_social_security_tax:.2f}")
        print(f"Income basis for health security tax:  {tax_report.income_after_social_contributions:.2f}")
        print(
            "Health social security tax:"
            f"\n - 9% = {tax_report.health_tax_9_percent:.2f}"
            f"\n - 7,75% = {tax_report.health_tax_7_percent:.2f}"
        )
        print(f"Tax deductible expenses: {tax_report.deductible_expenses:.2f}")
        print(f"Income to be taxed:  {tax_report.taxable_income} (rounded: {round(tax_report.taxable_income)})")
        print(f"Advance tax 18%: {tax_report.advance_tax:.1f}")

        if contract_type == ContractType.EMPLOYMENT:
            print(f"Tax free income: {tax_report.tax_free_income:.2f}")
            print(f"Reduced tax = {tax_report.advance_tax - tax_report.tax_free_income:.2f}")
            print(f"Advance paid tax = {tax_report.advance_paid_tax:.2f} (rounded: {round(tax_report.advance_paid_tax)})")
        elif contract_type == ContractType.CIVIL:
            print(f"Already paid tax = {tax_report.advance_tax:.2f}")
            print(f"Advance tax = {tax_report.advance_paid_tax:.2f} (rounded: {round(tax_report.advance_paid_tax)})")

        print()
        print(f"NET INCOME = {tax_report.net_income:.2f}")
        print()
