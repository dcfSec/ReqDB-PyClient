
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
    def __init__(self, title: str, description: str, extraType: int, children: list[dict] = [], id: int = 0):
        super().__init__(id)
        self.title: str = title
        self.description: str = description
        self.extraType: int = extraType
        self.children: list[dict] = children


class Requirement(Base):
    def __init__(self, key: str, title: str, description: str, tags: list[dict], parent: dict = None, visible: bool = True, id: int = 0):
        super().__init__(id)
        self.key: str = key
        self.title: str = title
        self.description: str = description
        self.visible: bool = visible
        self.tags: list = tags
        self.parent: dict = parent
        self.parentId: int = parent["id"] if parent is not None else None


class Tag(Base):
    def __init__(self, name: str, requirement: list[int] = [], id: int = 0):
        super().__init__(id)
        self.name = name
        self.requirement = requirement


class Topic(Base):
    def __init__(self, key: str, title: str, description: str, parent: int = None, id: int = 0):
        super().__init__(id)
        self.key: str = key
        self.title: str = title
        self.description: str = description
        self.parent: int = parent
        self.parentId: int = parent["id"] if parent is not None else None


class Catalogue(Base):
    def __init__(self, title: str, description: str, topics: str, id: int = None):
        super().__init__(id)
        self.title: str = title
        self.description: str = description
        self.topics: str = topics
