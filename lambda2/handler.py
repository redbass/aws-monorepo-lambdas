from lib.response import build_response


def handler(event, context):
    return build_response(2)