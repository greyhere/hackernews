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
from links.schema_relay import (
	RelayQuery,
	RelayMutation,
)


class Query(
	UsersQuery,
	LinksQuery,
	RelayQuery,
	graphene.ObjectType
):
	pass


class Mutation(
	UsersMutation,
	LinksMutation,
	RelayMutation,
	graphene.ObjectType
):
	token_auth = graphql_jwt.ObtainJSONWebToken.Field()
	verify_token = graphql_jwt.Verify.Field()
	refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
