from enum import Enum


class TaxRates:
    SOCIAL_SECURITY = 0.0976
    HEALTH_SOCIAL_SECURITY = 0.015
    SICKNESS_SOCIAL_SECURITY = 0.0245
    HEALTH_TAX_9 = 0.09
    HEALTH_TAX_7_75 = 0.0775
    ADVANCE_TAX = 0.18
    DEDUCTIBLE_EXPENSES_RATE = 0.20


class AmountConstants:
    TAX_FREE_INCOME = 46.33
    DEDUCTIBLE_EXPENSES = 111.25


class ContractType(str, Enum):
    EMPLOYMENT = "Employment"
    CIVIL = "Civil"
