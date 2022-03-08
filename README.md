# greenely_tech_test
the technical test code for the junior position at Greenely

## Task Description and Requirement
- implementing a REST API
- must be developed using python
- make the /limit and /data endpoint document
- access restriction for other user

## main solution
- develop a REST API using "Django REST framework" which is a toolkit for building Web APIs.
- Restrict data viewing by logged-in users


## Enviroment and Installment
- CentOS7
- python3
- pyenv
- django
- Django REST framework
  -  A toolkit for building Web APIs.  
  -  https://www.django-rest-framework.org/

- django-filter
  - A toolkit for adding search function at Django Rest framework.
  - Describe Classes inherited from FilterSet at views.py

## demo project overview
I wrote the following files 
Models, Serializer, Vews and URL models.

- Models 
  - Days, Months and Users
- Serializer
  - In this project, ListAPIView 
  - Convert an object into format like JSON, YAML or XML
- Views
  - In this project, ListAPIView is used
  - This view is the one which concrete view for listing a queryset like Djangos Detail view.
- URL
  - Define APIs end points


## Endpoints
### Created Data and Limit endpoints 　

- http://〓IP adress〓/api/GET

- http://〓IP adress〓/api/LIMIT


### Data Endpoint 
- Returns the requested type and amount of data for the authenticated user.

- Solution 
  - To use DjangoFilterBackend class which enables field filtering
  - To do it, override get_queryset method

### Limit Endpoint 
- Returns the minimum and maximum value for a date, consumption and temperature for monthly and daily data.
- Solution
  - To modify Serializer and add extra fields
  - To do it, override the to_representation method
