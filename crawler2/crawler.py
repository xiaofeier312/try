import requests
from sqlalchemy import create_engine, MetaData, Table

from crawler2.sql_config import SQLConfig

engine = create_engine(SQLConfig.con, echo=True)
# DBSession = sessionmaker(bind=engine)
# session = DBSession()
metaData = MetaData(engine)
crawlerTable = Table('el', metaData, autoload=True)
print('Table \'elong\': {}'.format(crawlerTable))
conn = engine.connect()

urllist = ['https://www.baidu.com', 'https://www.elong.com', 'https://www.sina.com', 'http://www.126.com']
urllist.reverse()


def crawle_url(url):
    r = requests.get(url)
    r_text = r.text
    print('Length of r.text: {}'.format(len(r_text)))
    if url:
        conn.execute(crawlerTable.insert(), {'address': url, 'get_text': r_text})
    #print(r_text)
    

if __name__ == '__main__':
    for i in urllist:
        crawle_url(i)
