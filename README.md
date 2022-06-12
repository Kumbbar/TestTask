***
# Test task for Stabilis
## Flask REST API
### Method - POST
### PATHS
* /objects/create
* /objects/get
* /objects/get_many
* /objects/edit
* /objects/delete
* /objects/calculate_distance

## Testing
### Deployed on [Heroku](https://test-task-stabilis.herokuapp.com/objects/get_many)
```
https://test-task-stabilis.herokuapp.com/objects/get_many
```
### Local testing
```
git clone https://github.com/Kumbbar/Test_task.git
```
```
python3 -m venv env
```
Windows
```
env\Scripts\activate.bat
```
Linux or MacOS
```
source env/bin/activate
```
<br>
<br>

```
pip install -r Test_task/requirements.txt
```
## JSON Example
### Create
```
{
    "title": "Moskow2",
    "longitude": 37.6158,
    "latitude": 55.7522
}
```
### Get
```
{
    "title": "Moskow2"
}
```

### Get many
```
Without json
```
### Edit
```
{
    "title": "Moskow2",
    "longitude": 37.6151,
    "latitude": 55.7528
}
```
### Delete
```
{
    "title": "Moskow2"
}
```
### Calculate distance
```
{
    "first_object_title": "Moskow",
    "second_object_title": "Tyumen"
}

```
***
