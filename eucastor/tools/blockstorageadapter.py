#!/bin/python

from abc import ABCMeta, abstractmethod


class BlockStorageAdapter:
    __metaclass__ = ABCMeta

    @abstractmethod
    def connect(self):
        pass

