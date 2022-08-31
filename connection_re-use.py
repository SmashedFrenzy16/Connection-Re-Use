from urllib3 import HTTPConnectionPool

pool = HTTPConnectionPool('ajax.googleapis.com', maxsize=1)

r = pool.request('GET', '/ajax/services/search/web',
                 fields={'q': 'python', 'v': '1.0'})

print("Response Status: ")

print("Header: {}").format(r.headers['content-type'])

print("Python: {}").format(len(r.data))

s = pool.request('GET', '/ajax/services/search/web',
             fields={'q': 'php', 'v': '1.0'})

print("PHP: {}").format(s.data)

print("Number Of Connections: {}").format(pool.num_connections)

