from models import db, Object


def create_tables() -> None:
    with db:
        db.create_tables([Object])


if __name__ == '__main__':
    create_tables()
