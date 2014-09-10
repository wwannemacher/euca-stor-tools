#!/bin/python
from eucastor.tools.blockstorageadapter import ClazzFinder
from tools import blockstorageadapter


class StorageOperation:

    StorageAdapter = None
    OperationConfig = None
    Json = None
    Config = None
    Operations = None

    def __init__(self, json):
        self.Json = json

    def get_from_config(self, key_name):
        if self.Config is None and self.Json is not None and isinstance(self.Json, dict):
            for key in self.Json.keys():
                normalized = key.lower()
                if normalized.startswith("config"):
                    self.Config = self.Json[key]
        if self.Config is not None:
            return self.Config[key_name]
        else:
            raise Exception("unable to find the configuration stanza of the input, "
                            "you must have a configuration section in the input")

    def get_operations(self):
        if self.Operations is None and self.Json is not None and isinstance(self.Json, dict):
            for key in self.Json.keys():
                normalized = key.lower()
                if normalized.startswith("op"):
                    self.Operations = self.Json[key]
        if self.Operations is not None:
            return self.Operations
        else:
            raise Exception("unable to find the operation stanza of the input, "
                            "you must have an operation section in the input")

    def choose_adapter(self):
        adaptertypename = self.get_from_config("type")
        adaptertype = blockstorageadapter.adapter(adaptertypename)
        if adaptertype is not None:
            finder = ClazzFinder(adaptertype)
        else:
            finder = ClazzFinder(adaptertypename)
        self.StorageAdapter = finder.get_instance()

    def parse_operation(self):
        ops = self.get_operations()

    def execute(self):
        self.choose_adapter()
        self.parse_operation()
        print str(self)

    def __str__(self):
        s = "operations: "
        if self.Operations is not None and isinstance(self.Operations, list):
            for op in self.Operations:
                s += op['command'] + ","
        else:
            s += 'None'
        s += ' using storage adapter: '
        if self.StorageAdapter is not None:
            s += self.StorageAdapter.__class__.__name__
        else:
            s += 'None'
        return s


class OperationSet(object):

    Config = None

    def __init__(self, config):
        self.Config = config

    def get_operations(self):
        if isinstance(self.Config, dict):
            op = StorageOperation(self.Config)
            return [op]
        elif isinstance(self.Config, list):
            ops = []
            for config in self.Config:
                op = StorageOperation(config)
                ops.append(op)
            return ops
        raise Exception("unable to iterate over configuration, must be either a dict or a list")
