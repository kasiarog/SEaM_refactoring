# A simple tax calculator - refactor

### 1. Naming convention
In the original program there was an unclear and chaotic naming. I changed the naming of variables and methods in order to make them more meaningful. For example:
- `t_health1` -> `health_tax_9_percent`
- `t_advance` -> `advance_tax`
- `calculateOtherTaxes` -> `_calculate_social_contributions`


### 2. File splitting
The whole program was divided into files. Smaller chunks of code were separated into different files to make the program more clear and transparent. There are 4 main python files responsible for the main functionality: 
 - `main.py` - in this file there is only the main function running the calculator,
 - `calculator.py` - this is the core computing unit, all the computing methods are included here,
 - `printer.py` - with the functionality of printing calculation results,
 - `user_interface.py` - it gives the possibility to interact with user - it takes input and prints output accordingly.

Moreover, there is a file `config.py` which includes all the configurable variables that can be changed or expanded.

The last file `tests.py` consists of tests checking the correct operation of the program.


### 3. Classes
Every functionality that could be separated was divided into classes. There are 5 main classes:

---
#### `TaxCalculator`
This is the class responsible for main computations of taxes and parameters. This is a base class for other classes which will inherit its functionality. The class has all necessary attributes for calculating the taxes. They are initialized with the creation of a class. The class uses a supporting dataclass `TaxReport` which enables data exchange (of the results) with another classes.

#### `EmploymentContractTaxCalculator` and `CivilContractTaxCalculator`
These classes are derived from `TaxCalculator` which is due to division on contract type. These classes were created to assure slightly different computations that happens while computing the taxes. Mostly, these methods overwrite the `_set_contract_specific_values` method which is specific to each contract. These classes will be used after a call from a user.

#### `TaxReportPrinter`
The responsibility of this class is to print the result of calculations properly. This functionality was separated to a class in order to change or expand the possibilities of printing the results.

#### `UserInterface`
This class is responsible for interacting with a user. It takes care of an input and output and their dependency. It orders the execution of calculation depending on the user input. It also takes care about the error handling.

---

In addition to that, in the `config.py` file there are three supporting, configurable classes:
- `TaxRates` - it stores the configurable variables for tax rates, that can be changed in the future,
- `AmountConstants` - the same as previous, but storing some amount constants,
- `ContractType` - this is a crucial Enum class that stores the serviced contract types. Based on this Enum, the appropriate calculations are performed. It can be expanded or changed in the future.


### 4. Methods
Implemented classes are full of methods. I will cover the most important ones - from the `calculator` module. 

The methods are mainly computing the taxes. Each method is responsible for computing different, important sets of values. Sample methods:
- `_calculate_social_contributions()`,
- `_calculate_health_taxes()`,
- `_calculate_advance_paid_tax()`.

These methods are used in further computations like `_calculate_net_income()` or `_calculate_common_taxes()`. What is interesting is a method `_set_contract_specific_values()`. This is a "configurable" method, that is invented to be changed in child classes. It is responsible for custom computation specific to different contract types. The main method and used by another classes, running the whole computations is `run()`.