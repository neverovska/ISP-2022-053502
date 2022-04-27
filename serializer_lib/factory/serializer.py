from serializer_lib.serializer.serializer import serialize_obj, deserialize_obj


class Serializer:
    """Class contain static methods for serializing and deserializing."""
    @staticmethod
    def serialize_obj(obj: object):
        """Call method serialize_obj from module serializer.serializer.
        Args:
            obj(object) : object that should be serialized

        Returns:
            serialize_obj(obj) : method serialize python object

        """
        return serialize_obj(obj)

    @staticmethod
    def deserialize_obj(obj: dict):
        """Call method serialize_obj from module serializer.serializer.
        Args:
            obj(dict) : dict with data that should be deserialized

        Returns:
            serialize_obj(obj) : method deserialize python object

        """
        return deserialize_obj(obj)
