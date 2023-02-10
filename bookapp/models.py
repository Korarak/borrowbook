from django.db import models

# Create your models here.
class tb_member(models.Model):
    m_id = models.AutoField(primary_key=True)
    m_user = models.CharField(max_length=50,null=True)
    m_pass = models.CharField(max_length=100,null=True)
    m_name = models.CharField(max_length=50,null=True)
    m_phone = models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.m_user

class tb_book(models.Model):
    b_id = models.CharField(primary_key=True, max_length=6)
    b_name = models.CharField(max_length=60,null=False)
    b_writer = models.CharField(max_length=50,null=True)
    b_category = models.IntegerField()
    b_price = models.IntegerField(null=False)
    def __str__(self):
        return self.b_id+" "+self.b_name

class tb_borrow_book(models.Model):
    br_id = models.AutoField(primary_key=True)
    br_date_br = models.DateField(auto_now=False, auto_now_add=False)
    br_date_rt = models.DateField(auto_now=False, auto_now_add=False ,null=True)
    b_id = models.ForeignKey(tb_book,null=True,on_delete=models.CASCADE)
    m_user = models.ForeignKey(tb_member,null=True,on_delete=models.CASCADE)
    br_fine = models.IntegerField()
    def __str__(self):
        return self.m_user.m_name+" "+self.b_id.b_name