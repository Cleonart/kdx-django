
from drf_yasg import openapi


def openAPIParamsInQueryAsStr(name: str, description: str):
    return openapi.Parameter(
        name,
        openapi.IN_QUERY,
        description=description,
        type=openapi.TYPE_STRING)


def openAPIParamsInQueryAsInt(name: str, description: str):
    return openapi.Parameter(
        name,
        openapi.IN_QUERY,
        description=description,
        type=openapi.TYPE_INTEGER)
