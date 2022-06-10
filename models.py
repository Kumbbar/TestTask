from peewee import Model, SqliteDatabase, PrimaryKeyField, CharField, FloatField


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
