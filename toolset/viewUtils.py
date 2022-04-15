
from rest_framework.response import Response


def ajaxResponse(context=None, success=True):
    if not context:
        context = {}

    return {"success": True if success else False, "result": context}


def ajaxErrorResponse(errMsg, errCode=None):
    context = {"errMsg": errMsg}
    if errCode is not None:
        context["errCode"] = errCode

    return ajaxResponse(context, False)


def viewResponse(context=None, content_type=None):
    if not context:
        context = {}

    return Response(ajaxResponse(context if context else {}), content_type=content_type)


def viewErrorResponse(errMsg, errCode=None):
    return Response(ajaxErrorResponse(errMsg, errCode))