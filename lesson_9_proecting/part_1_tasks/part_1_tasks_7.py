"""
Класс Pagination
Реализуйте класс Pagination для обработки данных с разбивкой по страницам. Разбивка по страницам используется для разделения большого количества данных на части. Экземпляр класса Pagination должен создаваться на основе двух значений:

исходные данные, представленные в виде списка с произвольными элементами
размер страницы, то есть количество элементов, отображаемых на каждой странице
alphabet = list('abcdefghijklmnopqrstuvwxyz')

pagination = Pagination(alphabet, 4)
Для получения содержимого страницы должен использоваться метод get_visible_items():

print(pagination.get_visible_items())    # ['a', 'b', 'c', 'd']
Обратите внимание, содержимое страницы должно быть представлено в виде списка. Перемещение по страницам должно происходить с помощью следующих методов:

prev_page() — вернуться к предыдущей странице
next_page() — перейти к следующей странице
first_page() — вернуться к первой странице
last_page() — перейти к последней странице
go_to_page() — перейти к странице с указанным номером (1 — первая страница, 2 — вторая страница, и так далее)
pagination.next_page()
print(pagination.get_visible_items())    # ['e', 'f', 'g', 'h']

pagination.last_page()
print(pagination.get_visible_items())    # ['y', 'z']
Методы для перемещения по страницам должны быть применимы друг за другом:

pagination.first_page()
pagination.next_page().next_page()
print(pagination.get_visible_items())    # ['i', 'j', 'k', 'l']
С помощью атрибутов total_pages и current_page должна быть возможность получить общее количество страниц и текущую страницу соответственно:

print(pagination.total_pages)            # 7
print(pagination.current_page)           # 3
При нахождении на первой странице и перемещении к предыдущей странице, текущей страницей должна остаться первая страница. Аналогично при нахождении на последней странице и перемещении к следующей странице, текущей страницей должна остаться последняя страница:

pagination.first_page()
pagination.prev_page()
print(pagination.get_visible_items())    # ['a', 'b', 'c', 'd']

pagination.last_page()
pagination.next_page()
print(pagination.get_visible_items())    # ['y', 'z']
При перемещении к нулевой или менее странице, текущей страницей должна стать первая страница. Аналогично при перемещении к странице, номер которой превышает общее количество страниц, текущей страницей должна стать последняя страница:

pagination.go_to_page(-100)
print(pagination.get_visible_items())    # ['a', 'b', 'c', 'd']

pagination.go_to_page(100)
print(pagination.get_visible_items())    # ['y', 'z']
"""


class Pagination:
    def __init__(self, data: list, items_per_page: int):
        self.data = data
        self.items_per_page = items_per_page
        self._current_page = 1
        self._total_pages = max((len(data) + items_per_page - 1) // items_per_page, 1)

    def get_visible_items(self) -> list:
        start = (self._current_page - 1) * self.items_per_page
        end = start + self.items_per_page
        return self.data[start:end]

    def prev_page(self) -> 'Pagination':
        self._current_page = max(self._current_page - 1, 1)
        return self

    def next_page(self) -> 'Pagination':
        self._current_page = min(self._current_page + 1, self._total_pages)
        return self

    def first_page(self) -> 'Pagination':
        self._current_page = 1
        return self

    def last_page(self) -> 'Pagination':
        self._current_page = self._total_pages
        return self

    def go_to_page(self, page: int) -> 'Pagination':
        if page < 1:
            self._current_page = 1
        elif page > self._total_pages:
            self._current_page = self._total_pages
        else:
            self._current_page = page
        return self

    @property
    def total_pages(self) -> int:
        return self._total_pages

    @property
    def current_page(self) -> int:
        return self._current_page