from abc import ABCMeta, abstractmethod

from HelloWorld.advancedOOP.adv_oop_project.database import Database


class Saveable(metaclass=ABCMeta):
    @abstractmethod
    def to_dict(self):
        pass

    def save(self):
        Database.insert(self.to_dict())