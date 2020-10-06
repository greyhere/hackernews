import graphene

from links.schema import (
	Query as LinksQuery,
	Mutation as LinksMutation,
)
from users.schema import (
	Query as UsersQuery,
	Mutation as UsersMutation,
)


class Query(UsersQuery, LinksQuery, graphene.ObjectType):
	pass


class Mutation(UsersMutation, LinksMutation, graphene.ObjectType):
	pass


schema = graphene.Schema(query=Query, mutation=Mutation)
