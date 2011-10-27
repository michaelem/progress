from django.db import models

class Book( models.Model ):
    page_count = models.IntegerField()
    title = models.CharField(max_length = 2048)
    
    def __unicode__( self ):
        return "%s, %d pages" % (self.title, self.page_count)