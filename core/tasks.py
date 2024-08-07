from celery import shared_task
from.models import Rental

@shared_task
def calculate_rental_cost(rental_id):
    rental = Rental.objects.get(id=rental_id)
    # calculate cost here
    rental.cost = cost
    rental.save()