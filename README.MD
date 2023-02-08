# Hotel app management website

## End points

## BaseUrl ======>>> <http://127.0.0.1:8000/>

## admin end point ======>> <http://127.0.0.1:8000/>

this url point to the admin dasboard where activities and data of the backend can be managed. In the admin, a CUSTOM USER model is present and this will give you the list of all the users that have be created in the database.

## api end point ======>> <http://127.0.0.1:8000/api/user>

This endpoint accept a post request for creating users.

## auth endpoint  =====>> <http://127.0.0.1:8000/api/auth/>

This is the base endpoint for user authentication

## login endpoint  =====>> <http://127.0.0.1:8000/api/auth/token/>

this is the login end point which accept a post request and return an access token, expiring time and other data. To login, the email feed is required but it's denoted as username. viz the structure goes like this...

"username":"youremail@gmail.com",
"password":password,
"grant_type":"password",
"client_id":"zzIwMGlLylde7hzAUx193jyYX2Fb5uR7ZfHyhzIW",
"client_secret":"HRO42j5WuE8SIZKut02jQCR4EHlKfdZyOLJ3OSycCJygZF37k4JeddSyuZ6bIknpV2U7NSg1yELxfirXbPdeXNzHjIeu7tiXSYn0Kh8I7lzUA5e3mp6acP0YHcdk1beS"

NOTE: the grant_type, client_id and the client_secret should be left like that. the only thing to be provided by user aree thier email and password

bellow is an example ["auth sample"](./auth.JPG)
