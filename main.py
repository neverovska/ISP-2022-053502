from serializer_lib.factory.factory_method import FactoryMethod
from serializer_lib.factory.serializer import serialize_obj, deserialize_obj


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


parser = FactoryMethod.create_serializer("json")
#парсер является объектом класса джсон
file = "output.json"
parser.dump(serialize_obj(fact), file)
#сериализуем метод выше используя методы из фабричного
result = deserialize_obj(parser.load(file))
#соответственно десериализуем
print(result(6))
#арсений самая сладкая жопка
