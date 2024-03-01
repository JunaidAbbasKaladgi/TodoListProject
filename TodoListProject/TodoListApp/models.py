from django.db import models

class taskTable(models.Model):
            Tasktitle=models.CharField(max_length=20)
            Taskdesc=models.TextField()
            Tasktime=models.DateTimeField(auto_now_add=True)

            def __str__(self):
                    return self.Tasktitle
