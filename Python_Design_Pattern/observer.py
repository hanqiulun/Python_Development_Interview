# -*- coding: utf-8 -*-
'''
------------------------------------------------------------
File Name: Observer.py
Description : 
Project: Test
Last Modified: Monday, 18th March 2019 7:59:03 pm
-------------------------------------------------------------
'''
from typing import (
    List,
    Any,
    NoReturn
)
from dataclasses import (
    dataclass,
    field
)


@dataclass
class Subject:
    _observers: List[Any] = field(default_factory=list)

    def attach(self, observer: object) -> NoReturn:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: object) -> NoReturn:
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None) -> NoReturn:
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


# Example usage
@dataclass
class Data(Subject):
    name: str = ""
    _data: int = 0

    @property
    def data(self) -> Any:
        return self._data

    @data.setter
    def data(self, value) -> NoReturn:
        self._data = value
        self.notify()


class HexViewer:

    def update(self, subject) -> NoReturn:
        print(u'HexViewer: Subject %s has data 0x%x' %
              (subject.name, subject.data))


class DecimalViewer:

    def update(self, subject) -> NoReturn:
        print(u'DecimalViewer: Subject %s has data %d' %
              (subject.name, subject.data))


# Example usage...
def main() -> NoReturn:
    data1 = Data(name='Data 1')
    data2 = Data(name='Data 2')
    view1 = DecimalViewer()
    view2 = HexViewer()
    data1.attach(view1)
    data1.attach(view2)
    data2.attach(view2)
    data2.attach(view1)

    print(u"Setting Data 1 = 10")
    data1.data = 10
    print(u"Setting Data 2 = 15")
    data2.data = 15
    print(u"Setting Data 1 = 3")
    data1.data = 3
    print(u"Setting Data 2 = 5")
    data2.data = 5
    print(u"Detach HexViewer from data1 and data2.")
    data1.detach(view2)
    data2.detach(view2)
    print(u"Setting Data 1 = 10")
    data1.data = 10
    print(u"Setting Data 2 = 15")
    data2.data = 15


if __name__ == '__main__':
    main()
