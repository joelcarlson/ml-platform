from manuscript_matcher.models import Journal
from manuscript_matcher.serializers import JournalSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO

# Populate a couple of journals
journal = Journal(journal_name = "PHYSICS IN MEDICINE AND BIOLOGY",
	jcr_category="radiology;medical imaging",
	jcr_rank = "1/20;25/26",
	jcr_quartile = "Q1;Q4",
	publisher = "Applesauceland publishing",
	issn = "1002-1234",
	eissn = "1002-4312",
	jif = "1.72")
journal.save()

journal = Journal(journal_name = "MEDICAL PHYSICS",
	jcr_category="radiology;medical imaging",
	jcr_rank = "13/20;23/26",
	jcr_quartile = "Q3;Q4",
	publisher = "Applesauceland publishing",
	issn = "1002-1234",
	eissn = "1002-4312",
	jif = "0.72")
journal.save()

# We've now got a few snippet instances to play with. 
# Let's take a look at serializing one of those instances.
serializer = JournalSerializer(journal)
serializer.data

# At this point we've translated the model instance into Python native datatypes. 
# To finalize the serialization process we render the data into json.
content = JSONRenderer().render(serializer.data)
content

# Deserialization is similar. First we parse a stream into Python native datatypes:
stream = BytesIO(content)
data = JSONParser().parse(stream)

# then we restore those native datatypes into a fully populated object instance.
serializer = JournalSerializer(data=data)
serializer.is_valid()
# True
serializer.validated_data
serializer.save()