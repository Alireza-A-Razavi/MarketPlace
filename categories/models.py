from django.db import models


class CustomeProperty(models.Model):
	title = models.CharField(max_length=32, verbose_name="نام")
	value = models.CharField(max_length=32, verbose_name="مقدار", null=True, blank=True)
	is_active = models.BooleanField(default=True)
	# category = models.OneToOneField('Category', related_name="custome property", on_delete=models.CASCADE)

	def __str__(self):
		return self.title

class StandardProperty(models.Model):
	title = models.CharField(max_length=32, verbose_name="نام")
	value = models.CharField(max_length=32, verbose_name="مقدار", null=True, blank=True)
	is_active = models.BooleanField(default=True)
	it_has = models.BooleanField(null=True, blank=True)

	def __str__(self):
		return self.title

#ROUND PER MINUTE
class RoundPerMinute(models.Model):
	value = models.CharField(max_length=32)

	def __str__(self):
		return f"rounde per meter: {self.value}"


#SIZE
class Size(models.Model):
	height = models.FloatField()
	length = models.FloatField()
	width = models.FloatField()

	def __str__(self):
		if self.height == 0:
			return f"length x width: {self.length} x {self.width}"
		else:
			return f"length x width x height: {self.length} x {self.width} x {self.height}"

#BOXING and Packing
class Boxing(models.Model):
	title = models.CharField(max_length=64)

	def __str__(self):
		return self.title

#MATERIAL
class Material(models.Model):
	title = models.CharField(max_length=64)
	resistance = models.CharField(max_length=32, null=True, blank=True)

	def __str__(self):
		return self.title



class Category(models.Model):
	title = models.CharField(max_length=64, verbose_name="نام دسته بندی")
	sub_category_of = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
	custome_property = models.ManyToManyField(CustomeProperty, null=True, blank=True)
	standar_properties = models.ManyToManyField(StandardProperty, null=True, blank=True)
	size = models.ManyToManyField(Size, null=True, blank=True)
	material = models.ManyToManyField(Material, null=True, blank=True)
	boxing = models.ManyToManyField(Boxing, null=True, blank=True)
	round_per_minute = models.ForeignKey(RoundPerMinute, on_delete=models.CASCADE, null=True, blank=True)
	description = models.TextField(null=True, blank=True)


	def __str__(self):
		if self.sub_category_of:
			return f"{self.sub_category_of.title} ---> {self.title}"
		else:
			return self.title
