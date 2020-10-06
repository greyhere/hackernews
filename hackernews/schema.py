import graphene
import graphql_jwt

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
	token_auth = graphql_jwt.ObtainJSONWebToken.Field()
	verify_token = graphql_jwt.Verify.Field()
	refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
