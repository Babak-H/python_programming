# Dependency Inversion Principle (NOT related to dependency injection)
# high level classes/modules should not depend on low level modules, instead they should depend on abstraction (abstract)
# this is because if we change low level class, it will break the code in high level module

from abc import abstractmethod
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBILING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        pass



class Relationships(RelationshipBrowser):
    """LOW LEVEL CLASS"""
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


class Research:
    """HIGH LEVEL CLASS"""
    def __init__(self, browser):  
        # browser is an implementation of RelationshipBrowser class
        # we know all of its child classes implement find_all_children_of() method
        for p in browser.find_all_children_of("John"):
            print(p)


parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)
