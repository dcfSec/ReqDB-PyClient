from marshmallow import EXCLUDE, validate, Schema, fields


class BaseSchema(Schema):
    id = fields.Integer()


class ExtraEntrySchema(BaseSchema):
    class Meta:
        include_relationships = True
        load_instance = True
        include_fk = True
        unknown = EXCLUDE

    content = fields.String(validate=validate.Length(min=1))
    extraTypeId = fields.Integer()
    requirementId = fields.Integer()


class ExtraTypeSchema(BaseSchema):
    class Meta:
        include_relationships = True
        load_instance = True
        include_fk = True
        unknown = EXCLUDE
    title = fields.String(validate=validate.Length(min=1, max=200))
    description = fields.String(validate=validate.Length(min=1))
    extraType = fields.Integer(validate=validate.Range(min=1, max=3))
    children = fields.List(fields.Nested(nested='ExtraEntrySchema', only=['id']))


class RequirementSchema(BaseSchema):
    class Meta:
        include_relationships = True
        load_instance = True
        include_fk = True
        unknown = EXCLUDE

    key = fields.String(validate=validate.Length(min=1, max=20))
    title = fields.String(validate=validate.Length(min=1, max=200))
    description = fields.String(validate=validate.Length(min=1))
    visible = fields.Boolean()
    parentId = fields.Integer(allow_none=True)
    tags = fields.List(fields.Nested(nested='TagSchema', only=['id']))
    extras = fields.List(fields.Nested(
        nested='ExtraEntrySchema', only=['id']))
    parent = fields.Nested(nested='TopicSchema', only=['id'])


class TagSchema(BaseSchema):
    class Meta:
        include_relationships = True
        load_instance = True
        include_fk = True
        unknown = EXCLUDE

    name = fields.String(validate=validate.Length(min=1, max=50))
    requirement = fields.Nested(nested='RequirementSchema', only=['id'],
                                many=True)


class TopicSchema(BaseSchema):
    class Meta:
        include_relationships = True
        load_instance = True
        include_fk = True
        unknown = EXCLUDE

    key = fields.String(validate=validate.Length(min=1, max=20))
    title = fields.String(validate=validate.Length(min=1, max=200))
    description = fields.String(validate=validate.Length(min=1))
    parentId = fields.Integer(allow_none=True)
    children = fields.List(fields.Nested(nested='TopicSchema'))
    requirements = fields.Nested(nested='RequirementSchema',
                                 only=['id'],
                                 many=True)
    parent = fields.Nested(nested='TopicSchema',
                           only=['id'], allow_none=True)
    catalogues = fields.List(fields.Integer(allow_none=True))


class CatalogueSchema(BaseSchema):
    """
    Catalogue schema with topics (id, title) as nested elements
    """
    class Meta:
        include_relationships = True
        load_instance = True
        include_fk = True
        unknown = EXCLUDE

    title = fields.String(validate=validate.Length(min=1, max=200))
    topics = fields.Nested(nested='TopicSchema', only=['id'],
                           many=True)
