from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from manuscript_matcher.models import Journal
from manuscript_matcher.serializers import JournalSerializer

@csrf_exempt 
def journal_list(request):
	"""
	simply list all of the valid journals
	"""
	if request.method == "GET":
		journals = Journal.objects.all()
		serializer = JournalSerializer(journals, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == "POST":
		data = JSONParser().parse(request)
		serializer = JournalSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def journal_detail(request, pk):
    """
    Retrieve, update or delete a journal.
    """
    try:
        journal = Journal.objects.get(pk=pk)
    except Journal.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = JournalSerializer(journal)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = JournalSerializer(journal, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        journal.delete()
        return HttpResponse(status=204)