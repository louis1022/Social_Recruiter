# DBのセットアップ用スクリプト
import psycopg2

class psql_save(object):
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="my_db",
            port="5432",
            user="rui",
            password="password"
        )
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()



    def recreate_tables(self):
        self.cursor.execute('CREATE SCHEMA social_recruit')
        self.cursor.execute('DROP TABLE IF EXISTS social_recruit.user_info')
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS social_recruit.user_info (
                    user_id BIGINT,
                    screen_name TEXT,
                    location TEXT,
                    url TEXT,
                    discription TEXT,
                    friends_count INT,
                    followers_count INT,
                    listed_count INT,
                    favourites_count INT,
                    statuses_count INT,
                    created_at TIMESTAMP WITH TIME ZONE,
                    PRIMARY KEY(user_id)
                )
            ''')

        self.cursor.execute('DROP TABLE IF EXISTS social_recruit.status_info')
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS social_recruit.status_info (
                    user_id BIGINT,
                    screen_name TEXT,
                    status_id BIGINT,
                    status_text TEXT,
                    PRIMARY KEY(status_id)
                )
            ''')


    def insert_user_info(self, user):
        col_num = 11
        tmp = ', '.join(['%s' for _ in range(col_num)])
        self.cursor.execute(
            '''INSERT INTO social_recruit.user_info VALUES ({0})'''.format(tmp),
            (
                user['id'],
                user['screen_name'],
                user['location'],
                user['url'],
                user['description'],
                user['friends_count'],
                user['followers_count'],
                user['listed_count'],
                user['favourites_count'],
                user['statuses_count'],
                user['created_at']
            )
        )

    def insert_status(self, user_id, screen_name, status_id, text):
        self.cursor.execute(
            '''INSERT INTO twitter.status_info VALUES (%s, %s, %s, %s)''',
            (
                user_id,
                screen_name,
                status_id,
                text
            )
        )


    def close_section(self):
        self.cursor.close()
        self.conn.close()
