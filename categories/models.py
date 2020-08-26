from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=64)
    upper_category = models.ForeignKey('self', on_delete=models.CASCADE,
                                       null=True, blank=True, related_name="sub_category_of")
    def __str__(self):
        return self.title



class Variation(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)  # size , round per meter


    class Meta:
        unique_together = (
            ('category', 'name')
        )

    def __str__(self):
        return self.name


class CategoryVariation(models.Model):
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE)
    value = models.CharField(max_length=50, null=True, blank=True)  # S, M, L
    attachment = models.ImageField(blank=True, null=True)
    selectable = models.BooleanField(default=False, blank=True, null=True)
    yes_or_no = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        unique_together = (
            ('variation', 'value')
        )

    def __str__(self):
        return self.value
