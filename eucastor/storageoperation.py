#!/bin/python


class StorageOperation:

    StorageAdapter = None
    OperationName = None
    OperationConfig = None
    JsonConfig = None

    def __init__(self, config):
        self.JsonConfig = config

    def execute(self):
        pass


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
