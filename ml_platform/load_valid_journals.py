import sys, os, csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ml_platform.settings")

import django
django.setup()

from manuscript_matcher.models import Journal 


def save_journal_from_row(file_row):
    journal = Journal()
    journal.id            = file_row[0]
    journal.journal_name  = file_row[1]
    journal.jcr_category  = file_row[2]
    journal.jcr_rank      = file_row[3]
    journal.jcr_quartile  = file_row[4]
    journal.publisher     = file_row[5]
    journal.issn          = file_row[6]
    journal.eissn         = file_row[7]
    journal.jif           = file_row[8]
    journal.save()
    
    
if __name__ == "__main__":
      
    if len(sys.argv) == 2:
        print "Reading from file " + str(sys.argv[1])

        with open(sys.argv[1], 'rb') as csvfile:
            filereader = csv.reader(csvfile, delimiter='\t')
            next(filereader, None) # Skip header
            for row in filereader:
                save_journal_from_row(row)
                #print ', '.join(row)  
        print "There are {} journals".format(Journal.objects.count())
        
    else:
        print "Please, provide file path to valid_journals"