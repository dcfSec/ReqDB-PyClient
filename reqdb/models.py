
class Base():
    def __init__(self, id: int = 0):
        self.id: int = id


class ExtraEntry(Base):
    def __init__(self, content: str, extraTypeId: int, requirementId: int, id: int = 0):
        super().__init__(id)
        self.content: str = content
        self.extraTypeId: int = extraTypeId
        self.requirementId: int = requirementId


class ExtraType(Base):
    def __init__(self, title: str, description: str, extraType: int, children: list[int] = [], id: int = 0):
        super().__init__(id)
        self.title: str = title
        self.description: str = description
        self.extraType: int = extraType
        self.children: list[int] = children


class Requirement(Base):
    def __init__(self, key: str, title: str, description: str, parentId: int = None, visible: bool = True, id: int = 0):
        super().__init__(id)
        self.key: str = key
        self.title: str = title
        self.description: str = description
        self.visible: bool = visible
        self.parentId: int = parentId


class Tag(Base):
    def __init__(self, name: str, requirement: list[int] = [], id: int = 0):
        super().__init__(id)
        self.name = name
        self.requirement = requirement


class Topic(Base):
    def __init__(self, key: str, title: str, description: str, parentId: int = None, id: int = 0):
        super().__init__(id)
        self.key: str = key
        self.title: str = title
        self.description: str = description
        self.parentId: int = parentId


class Catalogue(Base):
    def __init__(self, title: str, topics: str, id: int = None):
        super.__init__(id)
        self.title: str = title
        self.topics: str = topics
