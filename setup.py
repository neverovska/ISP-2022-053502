from setuptools import setup

setup(
    name="serializer_lib",
    packages=[
        "serializer_lib",
        "serializer_lib/serializer",
        "serializer_lib/formatters",
        "serializer_lib/factory",
        "serializer_lib/factory/baseClasses",
        "serializer_lib/formatters/json",
        "serializer_lib/formatters/toml",
        "serializer_lib/formatters/yaml",
    ],
    version="1.0.0",
    author="rariramz",
    description='console serializer',
    scripts=["bin/console_serializer"]
)