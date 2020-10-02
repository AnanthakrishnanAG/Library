from django.db import models





# database model for activity periods

class Library(models.Model):
      
    book_name=models.CharField(max_length=50,null=False)
    auther=models.CharField(max_length=50,null=False)
    count=models.IntegerField(null=False)
    class Meta:
      db_table = "Library"
    
    # def __str__(self):
    #   return self.name




# database model for Users
class User(models.Model):
    name=models.CharField(max_length=50,null=False)
    email=models.CharField(max_length=50,null=False)
    password=models.CharField(max_length=50,null=False)

    class Meta:
      db_table = "User"
    # def __str__(self):
    #   return self.name




def add_dummies():
  
  
  
  periods1=ActivityPeriod(start_time='2020-09-27 19:08:00',end_time='2020-09-27 19:08:00')
  periods2=ActivityPeriod(start_time='2020-09-27 23:08:00',end_time='2020-09-24 19:08:00')
  periods3=ActivityPeriod(start_time='2020-09-27 23:53:00',end_time='2020-09-26 23:49:00')


  periods1.save()
  periods2.save()
  periods3.save()

  user1=User(_id='W012A3CDE',real_name='Egon Spengler',tz='America/Los_Angeles')
  user1.save()
  user1.activity_periods.add(periods1,periods2,periods3)
  user1.save()
  user2=User(_id='W07QCRPA4"',real_name='Glinda Southgood',tz='Asia/Kolkata')
  user2.save()
  user2.activity_periods.add(periods2,periods1,periods3)
  user2.save()

  


