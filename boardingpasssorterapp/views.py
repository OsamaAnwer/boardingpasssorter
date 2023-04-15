import json
from rest_framework.decorators import api_view
from rest_framework.response import Response

from boardingpasssorterapp.exceptions import InvalidJourneyException
from boardingpasssorterapp.services import sort_boarding_pass


@api_view(['POST'])
def sort(request):
    try:
        request_body = json.loads(request.body.decode('utf-8'))
        journey = sort_boarding_pass(request_body)
        return Response({"success": True, "journey": journey}, status=200)
    except json.JSONDecodeError:
        return Response({"success": False, "message": "Invalid Request"}, status=400)
    except InvalidJourneyException:
        return Response({"success": False, "message": "Invalid Journey"}, status=400)
