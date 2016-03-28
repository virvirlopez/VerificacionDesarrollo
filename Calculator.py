# Calculator two numbers int between 0 and 100
class Calculatora:

    def __init__(self, dbConnector):
        self.dbConnector = dbConnector

    def get_mail_from_calculation(self, element1, element2, operation):
        result = self.calculate(element1, element2, operation)
        return self.dbConnector.get_mail(result)

    def remove_mail_from_calculation(self, element1, element2, operation):
        result = self.calculate(element1, element2, operation)
        return self.dbConnector.remove_mail(result)

    def get_user_from_calculation(self, element1, element2, operation):
        result = self.calculate(element1, element2, operation)
        return self.dbConnector.get_user(result)

    def remove_user_from_calculation(self, element1, element2, operation):
        result = self.calculate(element1, element2, operation)
        return self.dbConnector.remove_user(result)


    @staticmethod
    def calculate(element1, element2, operation):

        if element1.__class__.__name__ != "int" or element2.__class__.__name__ != "int" \
                or operation.__class__.__name__ != "str":
            raise Exception

        if element1 > 100 or element2 > 100:
            raise Exception

        if element1 < 0 or element2 < 0:
            raise Exception

        result = 0

        if operation != "+" and operation != "-" and operation != "*" and operation != "/":
            raise Exception

        if operation == "+":
            result = element1 + element2

        if operation == "-":
            result = element1 - element2

        if operation == "*":
            result = element1 * element2

        if operation == "/":
            result = element1 / element2

        return result