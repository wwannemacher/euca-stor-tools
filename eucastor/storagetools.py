#!/bin/python

import fileinput
import json
from eucastor.storageoperation import OperationSet


class StorageTools(object):

    Description = 'Eucalyptus Storage Tools'
    JSON = ''

    def __init__(self):
        pass

    def run(self):
        for line in fileinput.input():
            self.read_json(line)
        fileinput.close()
        operations = self.parse_json()
        for op in operations.get_operations():
            op.execute()

    def read_json(self, line):
        self.JSON += line

    def parse_json(self):
        parsed = json.loads(self.JSON)
        return OperationSet(parsed)

if __name__ == '__main__':
    StorageTools().run()
