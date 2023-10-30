import strawberry

from jwtberry.mutations import auth_token
from jwtberry.permission import IsAuthenticated
from jwtberry.types import JwtAuthResponse


@strawberry.type
class Query:
    hi: str = strawberry.field(resolver=lambda: "Hello", permission_classes=[IsAuthenticated])


@strawberry.type
class Mutation:
    login: JwtAuthResponse = auth_token

    # refresh: JwtAuthResponse = refresh_token
    # logout = auth.logout()
    # register: UserType = auth.register(UserInput)


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
)
