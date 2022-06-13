from peewee import Model, SqliteDatabase, PrimaryKeyField, CharField, FloatField
from exceptions import ObjectAlreadyExistsError, ObjectDoesNotExistError

db = SqliteDatabase('db.sqlite3')


class Object(Model):
    id = PrimaryKeyField(unique=True)
    title = CharField(max_length=100)
    longitude = FloatField()
    latitude = FloatField()

    class Meta:
        database = db
        order_by = 'id'
        db_table = 'objects'

    @classmethod
    def check_object_exists(cls, title: str) -> None:
        items_titles = [row.title for row in Object.select()]
        if title in items_titles:
            raise ObjectAlreadyExistsError(f'Object {title} already exists, try another title')

    @classmethod
    def check_object_not_exists(cls, title: str) -> None:
        items_titles = [row.title for row in Object.select()]
        if title not in items_titles:
            raise ObjectDoesNotExistError(f'Object {title} does not exist, try another title')

