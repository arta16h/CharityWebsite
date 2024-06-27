def make_image_path(instance, filename=None):
	image_path = f"images/users/{str(instance.first_name + '_' + instance.last_name)}/{filename}"
	return image_path