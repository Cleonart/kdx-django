
from drf_yasg import openapi


def openAPIParamsInHeaderAsStr(name: str, description: str, required: bool = False):
    return openapi.Parameter(
        name,
        openapi.IN_HEADER,
        description=description,
        type=openapi.TYPE_STRING,
        required=required)


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


def openAPIHeadersCompanyCode(required: bool = True):
    return openapi.Parameter(
        'X-Company-Code',
        openapi.IN_HEADER,
        description="Company code for filtering",
        type=openapi.TYPE_STRING,
        required=required)
