from serializer_lib.factory.baseClasses.format import Format
import serializer_lib.formatters.toml_format as TOMLFormat


class Toml(Format):
    """Base class for toml format, contains all serializer methods."""
    def dump(self, obj, fp):
        """Call method dump from module toml_format.
        Args:
            obj (object): object that should be serialized
            fp (str): name of file for serialized object

        Returns:
            TOMLFormat.dump(obj, fp): method serialize python object to file

        """
        return TOMLFormat.dump(obj, fp)

    def dumps(self, obj):
        """Call method dumps from module toml_format.
        Args:
            obj (object): object that should be serialized

        Returns:
            TOMLFormat.dumps(obj): method serialize python object to string

        """
        return TOMLFormat.dumps(obj)

    def load(self, fp):
        """Call method load from module toml_format.
        Args:
             fp (str): name of file for deserializing from

        Returns:
            TOMLFormat.load(fp): method deserialize python object from file

        """
        return TOMLFormat.load(fp)

    def loads(self, s):
        """Call method loads from module toml_format.
        Args:
            s (str): object that should be deserialized

        Returns:
            TOMLFormat.loads(s): method deserialize python object from string

        """
        return TOMLFormat.loads(s)
