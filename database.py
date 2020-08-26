from peewee import SqliteDatabase, Model, IntegerField, BooleanField
from playhouse.migrate import SqliteMigrator, migrate


connection = SqliteDatabase('mafia_helper_bot.sqlite')
migrator = SqliteMigrator(connection)


class BaseModel(Model):
    class Meta:
        database = connection


class User(BaseModel):
    id = IntegerField(column_name='id', primary_key=True)
    user_id = IntegerField(column_name='user_id', unique=True)
    wait_for_selector = BooleanField(column_name='wait_for_selector', null=True)
    wait_for_card = BooleanField(column_name='wait_for_card', null=True)

    @staticmethod
    def migrate_column(field_name: str, field):
        migrate(
                migrator.add_column('user', field_name, field)
        )

    @staticmethod
    def add_new_user(user_id: int) -> None:
        User.insert(user_id=user_id)

    @staticmethod
    def get_all_users_ids() -> list:
        return [user_id['user_id'] for user_id in User.select(User.user_id).dicts().execute()]

    class Meta:
        table_name = 'User'


connection.create_tables([User])
print('Database created and connected')
