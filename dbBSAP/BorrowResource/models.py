from django.db import models
from django.utils import timezone
# Create your models here.


class Resource(models.Model):
    resource_id = models.BigAutoField(primary_key=True)
    resource_quantity = models.IntegerField()
    resource_name = models.CharField(max_length=25, unique=True)
    is_available = models.BooleanField()

    def __str__(self):
        return self.resource_name

    class Meta:
        db_table = "Resource"


class BorrowResource(models.Model):
    borrow_resources_id = models.BigAutoField(primary_key=True)
    resident_id = models.ForeignKey("CreateAccount.Resident", on_delete=models.CASCADE, null=True, blank=True)
    org_id = models.ForeignKey("CreateAccount.Organization", on_delete=models.CASCADE, null=True, blank=True)
    resource_id = models.ForeignKey(Resource, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    borrow_date = models.DateField(default=timezone.now)
    return_date = models.DateField(default=timezone.now() + timezone.timedelta(days=7))
    approval = models.CharField(max_length=1, choices=[("A", "Approved"), ("P", "Pending"), ("R", "Rejected")],
                                default="P")

    def __str__(self):
        status = "Rejected" if self.approval == "R" else "Pending"
        if self.approval == "A":
            status = "Approved - Returned" if self.quantity == 0 else "Approved"
        return f"{status}"

    class Meta:
        db_table = "BorrowResource"

