import pymysql
import pandas as pd


class PandasLearn:
    def __init__(self):
        sql = 'SELECT * FROM Test'
        dbInfo = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': 'rootroot',
            'db': 'maoyan'
        }
        self.conn = pymysql.connect(
            host=dbInfo['host'],
            port=dbInfo['port'],
            user=dbInfo['user'],
            password=dbInfo['password'],
            db=dbInfo['db'],
            charset='utf8'
        )
        self.df = pd.read_sql(sql, self.conn)

    def Test(self):
        print(self.df)  # 1

        self.df.head(10)  # 2

        print(self.df['id'])  # 3

        self.df['id'].count()  # 4

        var = self.df[self.df['id'] < 1000][self.df['age'] > 30]  # 5

        self.df.drop_duplicates('age')[['id', 'age']].groupby('id').aggregate({'age': 'count'})  # 6

        # 7
        sql_movie = 'SELECT * FROM movie;'
        df_movie = pd.read_sql(sql_movie, self.conn)
        pd.merge(self.df, df_movie, how='inner', on='id')

        pd.concat([self.df, df_movie], join='outer').drop_duplicates()  # 8

        # 9
        self.df.drop(self.df[self.df['id'] == 10].index)

        # 10
        self.df.drop('sex', axis=1)


