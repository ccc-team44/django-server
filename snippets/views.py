import os

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from cloudant.client import CouchDB
import pycouchdb
@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)

"""
EXAMPLE DATABASE CRUD
"""

@csrf_exempt
def list_tweets(request):
    """
    query couch db
    """
    
    user = os.environ['COUCH_DB_USER']
    password = os.environ['COUCH_DB_PASSWORD']
    db_host = os.environ['COUCH_DB_ADDRESS']
    
    dummy_data = {"data":[{"State": "AL", "Under 5 Years": 310504, "5 to 13 Years": 552339, "14 to 17 Years": 259034, "18 to 24 Years": 450818, "25 to 44 Years": 1231572, "45 to 64 Years": 1215966, "65 Years and Over": 641667}, {"State": "AK", "Under 5 Years": 52083, "5 to 13 Years": 85640, "14 to 17 Years": 42153, "18 to 24 Years": 74257, "25 to 44 Years": 198724, "45 to 64 Years": 183159, "65 Years and Over": 50277}, {"State": "AZ", "Under 5 Years": 515910, "5 to 13 Years": 828669, "14 to 17 Years": 362642, "18 to 24 Years": 601943, "25 to 44 Years": 1804762, "45 to 64 Years": 1523681, "65 Years and Over": 862573}, {"State": "AR", "Under 5 Years": 202070, "5 to 13 Years": 343207, "14 to 17 Years": 157204, "18 to 24 Years": 264160, "25 to 44 Years": 754420, "45 to 64 Years": 727124, "65 Years and Over": 407205}, {"State": "CA", "Under 5 Years": 2704659, "5 to 13 Years": 4499890, "14 to 17 Years": 2159981, "18 to 24 Years": 3853788, "25 to 44 Years": 10604510, "45 to 64 Years": 8819342, "65 Years and Over": 4114496}, {"State": "CO", "Under 5 Years": 358280, "5 to 13 Years": 587154, "14 to 17 Years": 261701, "18 to 24 Years": 466194, "25 to 44 Years": 1464939, "45 to 64 Years": 1290094, "65 Years and Over": 511094}, {"State": "CT", "Under 5 Years": 211637, "5 to 13 Years": 403658, "14 to 17 Years": 196918, "18 to 24 Years": 325110, "25 to 44 Years": 916955, "45 to 64 Years": 968967, "65 Years and Over": 478007}]}
    

    if request.method == 'GET':
        server = pycouchdb.Server("http://" + user + ":" + password + "@" + db_host, authmethod="basic")
        db = server.database("tweets")
        
        # CREATE
        doc_in = db.save(dummy_data)
        
        # READ
        doc_out = db.get(doc_in["_id"])
        
        return JsonResponse(doc_out["data"], safe=False)
