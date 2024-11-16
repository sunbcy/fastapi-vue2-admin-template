import socket
import subprocess

import psutil
from app.databases.schema import getDatabases
from app.databases.schema import get_DbTables
from fastapi import APIRouter
from fastapi import Request
from utils import get_os_type
from utils import responses as resp
from utils.responses import response_with

SQLALCHEMY_DATABASE_URI_COMMON = f'mysql+pymysql://root:12345678@127.0.0.1:3306'
router = APIRouter()

# 常见数据库的进程名称和默认端口
DATABASES = {
    'MySQLD': {'process_name': 'mysqld', 'port': 3306},
    'MySQL': {'process_name': 'mysql', 'port': 3306},
    'MySQLD_SAFE': {'process_name': 'mysqld_safe', 'port': 3306},
    'PostgreSQL': {'process_name': 'postgres', 'port': 5432},
    # 'SQLite': {'process_name': 'sqlite3', 'port': None},  # SQLite 不监听端口
    'Redis': {'process_name': 'redis-server', 'port': 6379},
    'MongoDB': {'process_name': 'mongod', 'port': 27017},
    'Elasticsearch': {'process_name': 'elasticsearch', 'port': 9200},
    'Kibana': {'process_name': 'kibana', 'port': 5601},
    'Neo4j': {'process_name': 'neo4j', 'port': 7474},
    'Cassandra': {'process_name': 'cassandra', 'port': 9042},
    'CouchDB': {'process_name': 'couchdb', 'port': 5984},
    'RabbitMQ': {'process_name': 'rabbitmq-server', 'port': 5672},
    'Riak': {'process_name': 'riak', 'port': 8087},
    'InfluxDB': {'process_name': 'influxd', 'port': 8086},
    'TimescaleDB': {'process_name': 'postgres', 'port': 5432},
    'CockroachDB': {'process_name': 'cockroach', 'port': 26257},
    'ArangoDB': {'process_name': 'arangod', 'port': 8529},
    'HBase': {'process_name': 'hbase', 'port': 16000},  # HBase 使用多个端口，这里只列出一个
    'ZooKeeper': {'process_name': 'zookeeper', 'port': 2181}
}

COMMON_DATABASES = {
    'MySQLD': {'process_name': 'mysqld', 'port': 3306},
    'MySQL': {'process_name': 'mysql', 'port': 3306},
    'MySQLD_SAFE': {'process_name': 'mysqld_safe', 'port': 3306},
    # 'PostgreSQL': {'process_name': 'postgres', 'port': 5432},
    'Redis': {'process_name': 'redis-server', 'port': 6379},
    'MongoDB': {'process_name': 'mongod', 'port': 27017},
}


def is_process_running(process_name):
    """检查给定的进程名是否在运行"""
    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name'] == process_name:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def is_port_open(port):
    """检查给定的端口是否开放"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('127.0.0.1', port)) == 0


def check_databases():
    """检测常见的数据库是否在运行"""
    results = {}

    for db_name, db_info in COMMON_DATABASES.items():
        process_name = db_info['process_name']
        port = db_info['port']

        if process_name and is_process_running(process_name):
            results[db_name] = "Running (Process)"
        elif port and is_port_open(port):
            results[db_name] = "Running (Port)"
        else:
            results[db_name] = "Not Running"

    return results


@router.get('/get_db_info')
def get_db_info():  # 获取 db 信息
    os_type = get_os_type()
    n_results = {}
    if os_type == 'MacOS' or os_type == 'Android':
        results = check_databases()
        for _ in results:
            if _ in ['MySQLD', 'MySQL', 'MySQLD_SAFE']:
                pass
            else:
                n_results[_] = results[_]
        if ('Not' not in results['MySQLD']) or ('Not' not in results['MySQL']) or ('Not' not in results['MySQLD_SAFE']):
            n_results['MySQL'] = 'Running'
        else:
            n_results['MySQL'] = 'Not Running'
        value = {'searchResults': [{'dbName': i, 'status': 'ON' if 'Not' not in results[i] else 'OFF'} for i in n_results]}
    else:
        results = check_databases()
        value = {'searchResults': [{'dbName': i, 'status': 'ON' if 'Not' not in results[i] else 'OFF'} for i in results]}
    # print(results)
    return response_with(resp.SUCCESS_200, value=value)


@router.post('/switch_db')
async def switch_db(request: Request):  # 获取 db 信息
    data = await request.json()  # 前端请求的参数
    print(data)
    dbName, status = data['dbName'], data['status']
    os_type = get_os_type()
    if dbName == 'Redis':
        if status == 'ON':
            pass
        else:
            pass
    elif dbName == 'MySQL':
        if os_type == 'MacOS':
            if status == 'ON':
                # password = ''  # 替换为你的实际密码  # 0828
                #
                # # 使用 sudo -S 并传递密码
                # process = subprocess.Popen(
                #     ['echo', password],
                #     stdout=subprocess.PIPE
                # )
                # p = subprocess.Popen(['sudo', 'mysqld_safe', '--skip-grant-tables', '&'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                # output, error = p.communicate(input=b'\n')
                # print(output, error)

                print(f'手动输入下面命令:\n\tsudo mysqld_safe --skip-grant-tables &')
            else:
                p = subprocess.Popen(['mysqladmin', '-u', 'root', '-p', 'shutdown'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output, error = p.communicate(input=b'\n\n')
                print(output, error)
        else:
            if status == 'ON':  # 12345678 connect
                # p = subprocess.Popen(['mysqld_safe', '--skip-grant-tables', '&'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                # output, error = p.communicate(input=b'\n\n')
                # print(output, error)
                print(f'手动输入下面命令:\n\tmysqld_safe --skip-grant-tables &\nOR\n\tnohup mysqld &')
            else:  # Android termux 关闭MySQL已实现
                p = subprocess.Popen(['mysqladmin', '-u', 'root', '-p', 'shutdown'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output, error = p.communicate(input=b'\n\n')
                print(output, error)

                # p = subprocess.Popen(['kill', '-9', '`pgrep', 'mysqld`'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                # output, error = p.communicate()
                # print(output, error)
    elif dbName == 'MongoDB':
        if status == 'ON':
            pass
        else:
            pass
    value = {'searchResults': 'OK'}
    return response_with(resp.SUCCESS_200, value=value)


# @databases_bp.route('/get_db_tables', methods=['GET'])
# def get_db_tables():  # 获取 db 信息
#     tables = get_DbTables()
#     # print(tables)
#     value = {'searchResults': [{'tableName': i} for i in tables]}
#     return response_with(resp.SUCCESS_200, value=value)

@router.post('/get_db_tables')
async def get_db_tables(request: Request):  # 获取 db 信息
    data = await request.json()  # 前端请求的参数
    db_name = data['req']
    print(db_name)
    tables = get_DbTables(SQLALCHEMY_DATABASE_URI_COMMON + '/' + db_name)
    value = {'searchResults': [i for i in tables]}  # {'name': i}
    return response_with(resp.SUCCESS_200, value=value)


@router.get('/get_databases')
def get_databases():  # 获取 db 信息
    dbs = getDatabases()
    print(dbs)
    value = {'searchResults': [i for i in dbs]}  # {'name': i}
    return response_with(resp.SUCCESS_200, value=value)


# if __name__ == "__main__":
#     # for proc in psutil.process_iter(['name']):
#     #     print(proc.info['name'])  #
#
#     results = check_databases()
#     for db_name, status in results.items():
#         print(f"{db_name}: {status}")
