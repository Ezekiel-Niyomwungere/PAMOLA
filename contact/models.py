from django.db import models


class ContactInquiry(models.Model):
    class InquiryType(models.TextChoices):
        GENERAL = "general", "General inquiry"
        PRODUCT = "product", "Product inquiry"
        PARTNERSHIP = "partnership", "Partnership"
        FARMER_SUPPLIER = "farmer_supplier", "Farmer/supplier"
        DISTRIBUTION = "distribution", "Distribution"
        TRAINING = "training", "Training"
        INVESTMENT = "investment", "Investment/support"
        OTHER = "other", "Other"

    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30, blank=True)
    organization = models.CharField(max_length=200, blank=True)
    inquiry_type = models.CharField(
        max_length=30,
        choices=InquiryType.choices,
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "contact inquiry"
        verbose_name_plural = "contact inquiries"

    def __str__(self):
        return f"{self.full_name} — {self.get_inquiry_type_display()}"
