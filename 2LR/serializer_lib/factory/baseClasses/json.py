from serializer_lib.factory.baseClasses.format import Format
import serializer_lib.formatters.json_format as json_format
from typing import Any


class Json(Format):
    """Base class for json format, contains all serializer methods."""
    def dump(self, obj: Any, fp: str) -> None:
        """Call method dump from module json_format.
        Args:
            obj (object): object that should be serialized
            fp (str): name of file for serialized object

        Returns:
            JSONFormat.dump(obj, fp): method serialize python object to file

        """
        return json_format.dump(obj, fp)

    def dumps(self, obj: Any) -> str:
        """Call method dumps from module json_format.
        Args:
            obj (object): object that should be serialized

        Returns:
            JSONFormat.dumps(obj): method serialize python object to string

        """
        return json_format.dumps(obj)

    def load(self, fp: str):
        """Call method load from module json_format.
        Args:
            fp (str): name of file for deserializing from

        Returns:
            JSONFormat.load(fp): method deserialize python object from file

        """
        return json_format.load(fp)

    def loads(self, s: str):
        """Call method loads from module json_format.
        Args:
            s (str): object that should be deserialized

        Returns:
            JSONFormat.loads(s): method deserialize python object from string

        """
        return json_format.loads(s)
