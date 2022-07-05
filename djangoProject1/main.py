class SomeClass:
    list_of_items = [ ]

    def __init__(self, item):
        self.item = item
        SomeClass.list_of_items.append(item)

class AnotherClass(SomeClass):
    def __init__(self, item, second_item):
        SomeClass.__init__(self, item)
        self.second_item = second_item
print(AnotherClass)