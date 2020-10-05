import graphene

from links.schema import (
	Query as LinksQuery,
	Mutation as LinksMutation,
)


class Query(LinksQuery, graphene.ObjectType):
	pass


class Mutation(LinksMutation, graphene.ObjectType):
	pass


schema = graphene.Schema(query=Query, mutation=Mutation)
