"""
Реализуйте класс исключений DomainException. Также реализуйте класс Domain для работы с доменами. Класс Domain должен поддерживать три способа создания своего экземпляра: напрямую через вызов класса, а также с помощью двух методов класса from_url() и from_email():

domain1 = Domain('pygen.ru')                       # непосредственно на основе домена
domain2 = Domain.from_url('https://pygen.ru')      # на основе url-адреса
domain3 = Domain.from_email('support@pygen.ru')    # на основе адреса электронной почты
При попытке создания экземпляра класса Domain на основе некорректных домена, url-адреса или адреса электронной почты должно быть возбуждено исключение DomainException с текстом:

Недопустимый домен, url или email
В качестве неформального строкового представления экземпляр класса Domain должен иметь собственный домен:

print(str(domain1))                                # pygen.ru
print(str(domain2))                                # pygen.ru
print(str(domain3))                                # pygen.ru
Примечание 1. Будем считать домен корректным, если он представляет собой последовательность из одной или более латинских букв, за которой следует точка, а затем снова одна или более латинских букв.

Примечание 2. Будем считать url-адрес корректным, если он представляет собой строку http:// или https://, за которой следует корректный домен.

Примечание 3. Будем считать адрес электронной почты корректным, если он представляет собой последовательность из одной или более латинских букв, за которой следует собачка (@), а затем корректный домен.

Примечание 4. Тестовые данные доступны по ссылкам:
"""
import re

re_domain =r'[A-Za-z]+\.[A-Za-z]+'
re_email = fr'^[A-Za-z]+@({re_domain})'
re_url = fr'^https?://({re_domain})'



class DomainException(Exception):
    pass

class Domain:
    def __init__(self, string: str):
            if re.fullmatch(re_domain,  string):
                self.domain = string
            else:
                raise DomainException('Недопустимый домен, url или email')

    def __repr__(self):
        return f'{self.domain}'

    @classmethod
    def from_url(cls, string: str):
        if ( m:= re.fullmatch(re_url, string)):
            return cls(m.group(1))
        else:
            raise DomainException('Недопустимый домен, url или email')

    @classmethod
    def from_email(cls, string:str):
        if ( m:= re.fullmatch(re_email, string)):
            return cls(m.group(1))
        else:
            raise DomainException('Недопустимый домен, url или email')

domains = ['nikitin..biz', '.org', 'katren.', 'kubanskaja.edu.', '.', 'i.p.com', 'ooo.info+']

for d in domains:
    try:
        domain = Domain(d)
    except DomainException as e:
        print(e)