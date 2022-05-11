from serializer_lib.factory.baseClasses.json import Json
from serializer_lib.factory.baseClasses.toml import Toml
from serializer_lib.factory.baseClasses.yaml import Yaml
from typing import Union

EXTENSIONS = {
    "json": Json,
    "toml": Toml,
    "yaml": Yaml
}


class FactoryMethod:
    """Class contain method for creating new serializer."""
    @staticmethod
    def create_serializer(file_format: str) -> Union[Json, Toml, Yaml, None]:
        """Call method loads from module toml_format.
        Args:
            file_format (str): format of new serializer

        Raises:
            ValueError: file format is not supported

        Returns:
            new_format(): new chosen class object

        """
        new_format = EXTENSIONS.get(file_format.lower(), None)
        if not new_format:
            raise ValueError(f'File format \'{file_format}\' is not supported.')
        return new_format()
