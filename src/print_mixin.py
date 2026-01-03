class PrintMixin:
    ID = 1

    def __init__(self):
        self.id = self.ID
        PrintMixin.ID += 1
        print(repr(self))

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(Продукт{self.id}: {self.name}, Описание продукта: {self.description}, "
            f"{self.price}, {self.quantity})"
        )
