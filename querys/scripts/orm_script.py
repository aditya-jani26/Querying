from django.db import connection
from models import Restaurant , Rating
from django.utils import timezone
from django.contrib.auth.models import User
    # resturant = Restaurant()
    # resturant.name = 'test'
    # resturant.latitude = 50.2
    # resturant.longitude = 50.2
    # resturant.date_open = timezone.now()
    # resturant.resturant_type = Restaurant.TypreChoices.ITALIAN
   
   
#    resturant = Restaurant.objects.all()
#    print(resturant)
    

    # restaurant= Restaurant.objects.all()[0:5]
    # print(restaurant)

    #    resturant = Restaurant.objects.all(-1)
    #    print(resturant)
    # This will not work as it dose not support
    
    # print(connection.queries)

    # restaurant = Restaurant.objects.First()
    # print(restaurant)
    # print(connection.queries)
#  restaurant = Restaurant.objects.first()
#  user = User.objects.first()
#  print(Restaurant.objects.last())
#  print(connection.queries)
 
#  Rating.objects.create(user=user, rastaurant=restaurant, rating=3)

#  print(Rating.objects.filter(rating=3))
#  print(Rating.objects.filter(rating=5))
def run():
    pass

