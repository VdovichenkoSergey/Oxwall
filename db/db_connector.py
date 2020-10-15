import pymysql.cursors


class OxwallDB:
    def __init__(self, **param):
        self.connection = pymysql.connect(  # Connect to the database
            **param,
            host='192.168.0.191/',
            user='root',  # уточнить у Паши
            password='mysql',  # уточнить у Паши
            db='oxwa824',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.connection.autocommit(True)

    def close(self):
        self.connection.close()

    def create_user(self, user):
        with self.connection.cursor() as cursor:
            # Create a new record
            sql = '''INSERT INTO 'ow_base_user', ('username', 'email', 'password')
                     VALUES (%s, %s, %s)'''
            cursor.execute(sql, ('test', 'webmaster@python.org', 'pass'))

    def get_users(self):
        with self.connection.cursor() as cursor:
            # Record a single record
            sql = "SELECT 'id', 'username', 'password', 'email' FROM 'ow_base_user'"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result


if __name__ == "__main__":
    db_obj = OxwallDB(host="192.168.0.191/", user="root")
