# API for Retrieving Movie and Cartoon Lists

This API is designed to retrieve lists of movies and cartoons.

## Example Movie

```json
{
    "name": "Toy Story",
    "genre": "adventure",
    "studio": "Pixar",
    "score": 8
}
```

## Provided API Functionality

1. Registration and account deletion
2. Retrieving movies

---

## Section 1: Registration and Account Deletion

### Registration

To register, you need to send a POST request to the URL:

```
http://localhost:8000/API/v1/registration
```

### Example Request Body

```json
{
    "mail": "some@gmail.com",
    "password": "YOUR PASSWORD"
}
```

### Code Examples

#### Python

```python
import requests

url = "http://localhost:8000/API/v1/registration"
data = {
    "mail": "some@gmail.com",
    "password": "YOUR PASSWORD"
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
```

#### JavaScript

```javascript
const url = "http://localhost:8000/API/v1/registration";
const data = {
    mail: "some@gmail.com",
    password: "YOUR PASSWORD"
};

fetch(url, {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));
```

#### PHP

```php
$url = "http://localhost:8000/API/v1/registration";
$data = array(
    "mail" => "some@gmail.com",
    "password" => "YOUR PASSWORD"
);

$options = array(
    'http' => array(
        'header'  => "Content-Type: application/json\r\n",
        'method'  => 'POST',
        'content' => json_encode($data),
    ),
);

$context  = stream_context_create($options);
$result = file_get_contents($url, false, $context);

if ($result === FALSE) { /* Error handling */ }

echo $result;
```

### Response Examples

#### On Successful Registration

```json
{
    "detail": "some@gmail.com",
    "error": "false"
}
```

#### If the Email Address Already Exists

```json
{
    "detail": "invalid mail address",
    "error": "true"
}
```

#### If Required Data is Missing

```json
{
    "mail": [
        "This field may not be blank."
    ]
}
```

### Account Deletion

To delete an account, you need to send a POST request to the URL:

```
http://localhost:8000/API/v1/delete
```

### Example Request Body

```json
{
    "mail": "some@gmail.com",
    "password": "YOUR PASSWORD"
}
```

### Code Examples

#### Python

```python
import requests

url = "http://localhost:8000/API/v1/delete"
data = {
    "mail": "some@gmail.com",
    "password": "YOUR PASSWORD"
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
```

#### JavaScript

```javascript
const url = "http://localhost:8000/API/v1/delete";
const data = {
    mail: "some@gmail.com",
    password: "YOUR PASSWORD"
};

fetch(url, {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));
```

#### PHP

```php
$url = "http://localhost:8000/API/v1/delete";
$data = array(
    "mail" => "some@gmail.com",
    "password" => "YOUR PASSWORD"
);

$options = array(
    'http' => array(
        'header'  => "Content-Type: application/json\r\n",
        'method'  => 'POST',
        'content' => json_encode($data),
    ),
);

$context  = stream_context_create($options);
$result = file_get_contents($url, false, $context);

if ($result === FALSE) { /* Error handling */ }

echo $result;
```

### Response Examples

#### On Successful Deletion

```json
{
    "detail": "deleted",
    "error": "false"
}
```

#### If the Data is Incorrect

```json
{
    "detail": "not correct data",
    "error": "true"
}
```

#### If Some Data is Missing

```json
{
    "detail": "not correct data",
    "error": "true"
}
```

---

## Section 2: Retrieving Movies

To retrieve a list of movies, you need to:

1. Register.
2. Send a POST request to the URL:

```
http://localhost:8000/API/v1/films
```

### Example Request Body

```json
{
    "mail": "some@gmail.com",
    "password": "YOUR PASSWORD"
}
```

### Code Examples

#### Python

```python
import requests

url = "http://localhost:8000/API/v1/films"
data = {
    "mail": "some@gmail.com",
    "password": "YOUR PASSWORD"
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
```

#### JavaScript

```javascript
const url = "http://localhost:8000/API/v1/films";
const data = {
    mail: "some@gmail.com",
    password: "YOUR PASSWORD"
};

fetch(url, {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));
```

#### PHP

```php
$url = "http://localhost:8000/API/v1/films";
$data = array(
    "mail" => "some@gmail.com",
    "password" => "YOUR PASSWORD"
);

$options = array(
    'http' => array(
        'header'  => "Content-Type: application/json\r\n",
        'method'  => 'POST',
        'content' => json_encode($data),
    ),
);

$context  = stream_context_create($options);
$result = file_get_contents($url, false, $context);

if ($result === FALSE) { /* Error handling */ }

echo $result;
```

### Response Examples

#### On Successful Request

```json
{
    "detail": [
        {
            "name": "Toy Story",
            "genre": "adventure",
            "studio": "Pixar",
            "score": 8
        },
        {
            "name": "The Lion King",
            "genre": "Adventure",
            "studio": "Walt Disney",
            "score": 8
        }
    ],
    "error": "false"
}
```

#### If the Account is Incorrect

```json
{
    "detail": "not accept account",
    "error": "true"
}
```

#### If the Request Body is Incorrect

```json
{
    "detail": "not correct data",
    "error": "true"
}
```

 