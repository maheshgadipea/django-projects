# django-projects  
  
 ###### Note : To view Pages on GET API call  use query parameters along with URL
              example : http://localhost:8000/userInfo?page=1
              
 ###### Current Page size is 1 i.e only one user info is displayed per page ,to customize page size change value PAGE_SIZE to a number in REST_FRAMEWORK classes in settings.py file
          example: 
                REST_FRAMEWORK = {
                        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
                        'PAGE_SIZE': 3
                }
