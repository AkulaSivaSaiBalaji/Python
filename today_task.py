
#task-1 use getter and setter methods and also use public ,private,protected attributes 

class SamosaSecurityOfficer:

    def __init__(self, name, samosa_count, secret_samosa_code):
        # Public attribute
        self.name = name

        # Protected attribute
        self._samosa_count = samosa_count

        # Private attribute
        self.__secret_samosa_code = secret_samosa_code

    # Protected attribute - Getter
    def get_samosa_count(self):
        return self._samosa_count

    # Protected attribute - Setter
    def set_samosa_count(self, count):
        self._samosa_count = count

    # Private attribute - Getter
    def get_secret_samosa_code(self):
        return self.__secret_samosa_code

    # Private attribute - Setter
    def set_secret_samosa_code(self, code):
        self.__secret_samosa_code = code

#public

officer = SamosaSecurityOfficer("Yashaswi",10,"SAMOSA-007")
print(f"Officer Name: {officer.name}")
officer.name = "Super Yashaswi"
print(f"Updated Name: {officer.name}")
print(f"Samosas in Security: {officer.get_samosa_count()}")
officer.set_samosa_count(25)
print(f"Updated Samosas: {officer.get_samosa_count()}")



# private

print(f"Secret Code: {officer.get_secret_samosa_code()}")
officer.set_secret_samosa_code("SAMOSA-999")
print(f"Updated Secret Code: {officer.get_secret_samosa_code()}")


# task-2 convert same into hierarchical also make use of public,private along with class methods and class variables

class RBI:
    """Base Class"""

    # Public class variable
    cash = 10000000

    # Private class variable
    __secret_fund = 5000000

    def __init__(self, bank_name):
        # Public instance variable
        self.bank_name = bank_name

        # Private instance variable
        self.__security_code = "RBI@123"

    # Class method
    @classmethod
    def available_cash(cls):
        print(f"Available cash in {cls.__name__} is {cls.cash}")

    # Class method to access private class variable
    @classmethod
    def show_secret_fund(cls):
        return f"RBI Private Secret Fund is {cls.__secret_fund}"

    # Instance method to access private instance variable
    def show_security_code(self):
        print(f"Security code of {self.bank_name} is {self.__security_code}")


# Child Class 1
class SBI(RBI):
    """Derived Class"""

    cash = 5000000

    @classmethod
    def sbi_cash(cls):
        print(f"Available cash in SBI is {cls.cash}")
        print(f"Total cash with RBI and SBI is {RBI.cash + cls.cash}")


# Child Class 2
class HDFC(RBI):
    """Derived Class"""

    cash = 7000000

    @classmethod
    def hdfc_cash(cls):
        print(f"Available cash in HDFC is {cls.cash}")
        print(f"Total cash with RBI and HDFC is {RBI.cash + cls.cash}")



sbi = SBI("SBI")
print(f"Bank Name: {sbi.bank_name}")
print(f"SBI Cash: {sbi.cash}")
sbi.available_cash()
sbi.sbi_cash()
sbi.show_security_code()


hdfc = HDFC("HDFC")
print(f"Bank Name: {hdfc.bank_name}")
print(f"HDFC Cash: {hdfc.cash}")
hdfc.available_cash()
hdfc.hdfc_cash()
hdfc.show_security_code()

#RBI methods
rbi=RBI("Reserve Bank Of India")
print(f'{rbi.show_security_code()}')
RBI.available_cash()
RBI.show_secret_fund()

#task-2

