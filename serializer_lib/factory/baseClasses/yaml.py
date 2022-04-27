from serializer_lib.factory.baseClasses.format import Format
import serializer_lib.formatters.yaml_format as YAMLParser


class Yaml(Format):
    """Base class for yaml format, contains all serializer methods."""
    def dump(self, obj, fp):
        """Call method dump from module yaml_format.
        Args:
            obj (object): object that should be serialized
            fp (str): name of file for serialized object

        Returns:
            YAMLFormat.dump(obj, fp): method serialize python object to file

        """
        return YAMLParser.dump(obj, fp)

    def dumps(self, obj):
        """Call method dumps from module yaml_format.
        Args:
            obj (object): object that should be serialized

        Returns:
            YAMLFormat.dumps(obj): method serialize python object to string

        """
        return YAMLParser.dumps(obj)

    def load(self, fp):
        """Call method load from module yaml_format.
        Args:
            fp (str): name of file for deserializing from

        Returns:
            YAMLFormat.load(fp): method deserialize python object from file

        """
        return YAMLParser.load(fp)

    def loads(self, s):
        """Call method loads from module yaml_format.
        Args:
            s (str): object that should be deserialized

        Returns:
            YAMLFormat.loads(s): method deserialize python object from string

        """
        return YAMLParser.loads(s)
