# jwtberry

<div align="center">
<img alt="jwtberry Logo" height="300" src="https://raw.githubusercontent.com/VachaganGrigoryan/jwtberry/master/jwtberry_logo.png" width="300"/>
</div>

**jwtberry** is a Python package that simplifies JWT (JSON Web Token) authentication for Django Strawberry GraphQL projects. It provides easy-to-use tools for implementing JWT authentication within your Strawberry-based GraphQL API.

## Features

- Seamless integration with Django Strawberry GraphQL.
- Simplified JWT authentication setup for your API.
- Customizable token generation and validation.

## Installation

You can install **jwtberry** using `pip`:

```bash
pip install jwtberry
```

## Usage
1. Add 'jwtberry.blackberry' app to your Django INSTALLED_APPS in the settings.py file:
```python
INSTALLED_APPS = [
    # ...
    'jwtberry.blackberry',
]
```

2. Configure your Django project's AUTHENTICATION_BACKENDS in settings.py to include the JwtAuthBackend from jwtberry:
```python
AUTHENTICATION_BACKENDS = [
    "jwtberry.backends.JwtAuthBackend",
    "django.contrib.auth.backends.ModelBackend",
]
```

3. Update your project's urls.py by importing JwtAsyncGraphQLView from jwtberry.views and adding a path for the GraphQL endpoint:

```python
from jwtberry.views import JwtAsyncGraphQLView

urlpatterns = [
    # ...
    path("graphql/", JwtAsyncGraphQLView.as_view(schema=schema)),
]
```

4. In your schema.py (where you define your GraphQL schema), make the following changes to include JWT-based authentication:

```python
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

schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
)
```
`IsAuthenticated` is a permission class that checks whether the user has authenticated by verifying the Authorization header.

For more detailed information and examples, check the [example](example) project.
