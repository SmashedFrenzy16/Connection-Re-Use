from urllib3 import HTTPConnectionPool

pool = HTTPConnectionPool('ajax.googleapis.com', maxsize=1)

r = pool.request('GET', '/ajax/services/search/web',
                 fields={'q': 'python', 'v': '1.0'})

print("Response Status: ")

print("Header: {}").format(r.headers['content-type'])

print("Python: {}").format(len(r.data))

r = pool.request('GET', '/ajax/services/search/web',
             fields={'q': 'php', 'v': '1.0'})

print("PHP: {}").format(r.data)

print("Number Of Connections: {}").format(pool.num_connections)

print("Number Of Requests: {}").format(pool.num_requests)

