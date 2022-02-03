# greenely_tech_test
the technical test code for the junior position at Greenely

# abstruct

Implementing a REST API using Python/Django

# Time
- Technical research : 2 and half hour 
- Implementing : 5 and half hour


# Enviroment and Installment
- CentOS7
- python3
- django
- Django REST framework
  - A toolkit for building Web APIs.
  - https://www.django-rest-framework.org/

- django-filter
  - A toolkit for adding search function at Django Rest framework.
  - Describe Classes inherited from FilterSet at views.py


# Files
These following filres are created to get the test data from Data Base and deal with them as JSON

- models.py
  - Defines the type of data stored in the database

- serializer.py
  - This file is a one to serialize data from database
  - Define fields which are not included in Models, such as searching fields


- views.py
  - This fire is for API Views
  - Classes here are inherited rest_framework.viewsets.ModelViewSet

# Endpoints
- Create Data and Limit endpoints
　- http://〓IP adress〓/api/GET
  - http://〓IP adress〓/api/LIMIT


- Restriction of data access from other users
  - Implemented so as to get data filtered with login user id
  - login application has not implemented yet 

- About Data endpoint
  - Added search field for timestamp of Days
  - I intended to implement a function to switch the data type between daysmonths, but I haven't implemented it yet.

- About Limit endpoint
  - Aggregate the maximum / minimum power consumption of days and months associated with the User model
  - Query which get timestamp of the maximum / minimum power consumption should be described with Windows function, 
    but it is being verified.
