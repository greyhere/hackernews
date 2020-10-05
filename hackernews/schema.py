import graphene

from links.schema import Query as LinksQuery


class Query(LinksQuery, graphene.ObjectType):
	pass


schema = graphene.Schema(query=Query)
