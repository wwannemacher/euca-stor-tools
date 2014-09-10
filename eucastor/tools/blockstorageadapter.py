#!/bin/python

from abc import ABCMeta, abstractmethod


class BlockStorageAdapter(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def connect(self):
        pass


Adapters = {'NetappAdapter': "eucastor.adapters.netappadapter.NetappAdapter",
            'netapp': "eucastor.adapters.netappadapter.NetappAdapter",
            'EmcAdapter': "eucastor.adapters.emcadapter.EmcAdapter",
            'emc': "eucastor.adapters.emcadapter.EmcAdapter",
            'EquallogicAdapter': "eucastor.adapters.equallogicadapter.EquallogicAdapter",
            'equallogic': "eucastor.adapters.equallogicadapter.EquallogicAdapter"}

Operations = ["connect", "login"]

def adapter(x):
    return Adapters.get(x, None)


class ClazzFinder(object):

    ClassName = None
    Clazz = None

    def __init__(self, class_name):
        self.ClassName = class_name

    def load_class(self):
        parts = self.ClassName.split('.')
        module = ".".join(parts[:-1])
        m = __import__(module)
        for comp in parts[1:]:
            m = getattr(m, comp)
        self.Clazz = m

    def get_instance(self):
        if self.Clazz is None:
            self.load_class()
        return self.Clazz()
