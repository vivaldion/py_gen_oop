"""еализуйте функцию is_context_manager(), которая принимает один аргумент:

obj — произвольный объект
Функция должна возвращать True, если объект obj является контекстным менеджером, или False в противном случае.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_context_manager(), но не код, вызывающий ее."""

def is_context_manager(obj:object):
    if "__exit__" in dir(obj) and "__enter__" in dir(obj):
        return True
    else:
        return False