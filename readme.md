# Development Setup 

1. Intall Python 3.5+
2. Install requirements using `pip install -r requirement.txt`
3. Create the database & apply migrations: `python manage.py migrate` from src folder
4. Run development server with `python manage.py runserver`

# API Endpoints

## Users
* /api/1.0/users/ - List of users. Only for administrators


##User Detail, Update and Destroy
* /api/1.0/users/**id**/ - Detail of user. Only for administrators or own user. Support *GET, PUT and 
DELETE*


## Blogs List
* /api/1.0/blogs/ - Public list of blogs. Only GET protocol supported. 
Also, it is possible search by username and ordering.
` /api/1.0/blogs/?search=VIRIATO&ordering=blog_name` 


## Blog Detail
* /api/1.0/blogs/detail/<id_owner>/ - Listing the posts list from a blog. It is possible search by
 title or body content and ordering by title or publish date.
`/api/1.0/blogs/detail/10/?search=millones&ordering=-publish_date`

## Post Creation
* /api/1.0/blogs/detail/ - POST protocol.

This endpoint must recieve a valid JSON like this example:
```json
    {
        "title": "Prueba",
        "intro": "prueba",
        "publish_date": "2017-10-10",
        "body": "esto es una prueba"
    }
```
The post will publish in the blog of the authenticated user.

## Post Detail, Update and Destroy
* /api/1.0/post/10/ - You can retrieve a post´s information with a GET petition.

If you are a superuser or the owner of this post, you can also update via PUT protocol the data 
or destroy the post via DELETE petition.