from sqlalchemy import create_engine, MetaData, text
from sqlalchemy.orm import sessionmaker

# engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=False)  # 创建引擎

# engine = create_engine(f'mysql+pymysql://root:12345678@127.0.0.1:3306')  # 创建引擎  127.0.0.1:3306
SQLALCHEMY_DATABASE_URI_COMMON = f'mysql+pymysql://root:12345678@127.0.0.1:3306'
engine = create_engine(SQLALCHEMY_DATABASE_URI_COMMON)  # 创建引擎
# engine = create_engine(f'mysql+pymysql://bcy:12345678@127.0.0.1:3306/test_20240403', echo=False)  # 创建引擎
# Base = declarative_base()  # 建立 sql rom基类
Session = sessionmaker(bind=engine)
session = Session()  # 创建会话


def get_DbTables(db_url: str=SQLALCHEMY_DATABASE_URI_COMMON+'/test_20240403'):
    engine = create_engine(db_url)
    # 获取元数据
    metadata = MetaData()
    metadata.reflect(bind=engine)
    # 获取所有表的名称
    table_names = metadata.tables.keys()
    # # 打印所有表的名称
    # for table_name in table_names:
    #     print(table_name)

    # 关闭会话
    # session.close()
    return table_names


def getDatabases():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SHOW DATABASES;"))
            # print(result)
            databases = [row[0] for row in result]
            return databases
    except Exception as e:
        return {'error': str(e)}

# r = getDatabases()
# print(r)
