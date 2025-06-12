"""лассы bool и NoneType не могут быть родительскими, то есть от них нельзя наследоваться, и при попытке сделать это будет возбуждено исключение"""

class UpperPrintString(str):
    def __str__(self):
        return f'{super().__str__().upper()}'
