from rest_framework import serializers
from manuscript_matcher.models import Journal

class JournalSerializer(serializers.ModelSerializer):
	class Meta:
		model = Journal
		fields = ('id', 'journal_name', 'jcr_category', 'jcr_rank', 'jcr_quartile', 'publisher', 'issn', 'eissn', 'jif')
					