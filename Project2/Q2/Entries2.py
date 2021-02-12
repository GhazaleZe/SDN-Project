import httplib
import json

class StaticEntryPusher(object):

    def __init__(self , server , *args, **kwargs):
        self.server = server

    def get(self , data):
        ret = self.rest_call({} , 'GET')
        return json.loads(ret[2])

    def Set(self , data):
        ret = self.rest_call(data , 'POST')
        return ret[0] == 200

    def remove(self , objtype , data):
        ret = self.rest_call(data , 'DELETE')

    def rest_call(self , data , action):
        path = '/wm/staticentrypusher/json'
        header = {
            'Content-type' : 'application/json',
            'Accept' : 'application/json'
        }
        body = json.dumps(data)
        Conn = httplib.HTTPConnection(self.server , 8080)
        Conn.request(action , path , body , header)
        response = Conn.getresponse()
        ret = (response.status , response.reason , response.read())
        print(ret)
        Conn.close()
        return ret

pusher = StaticEntryPusher('127.0.0.1')

entry_s3 = {
    'switch' : '00:00:00:00:00:00:00:03',
    'name' : 'entry_s3',
    'eth_type' : "0x0800",
    "ipv4_src" : "10.0.0.9",
    "ipv4_dst" : "10.0.0.8",
    'priority' : "32768",
    "in_port" : "4",
    "active" : "true",
    "actions" : "output=1"
}

entry_s1 = {
    'switch' : '00:00:00:00:00:00:00:01',
    'name' : 'entry_s1',
    'eth_type' : "0x0800",
    "ipv4_src" : "10.0.0.9",
    "ipv4_dst" : "10.0.0.8",
    'priority' : "32768",
    "in_port" : "2",
    "active" : "true",
    "actions" : "output=3"
}

entry_s4 = {
    'switch' : '00:00:00:00:00:00:00:04',
    'name' : 'entry_s4',
    'eth_type' : "0x0800",
    "ipv4_src" : "10.0.0.9",
    "ipv4_dst" : "10.0.0.8",
    'priority' : "32768",
    "in_port" : "1",
    "active" : "true",
    "actions" : "output=6"
}

entry_s6 = {
    'switch' : '00:00:00:00:00:00:00:06',
    'name' : 'entry_s6',
    'eth_type' : "0x0800",
    "ipv4_src" : "10.0.0.9",
    "ipv4_dst" : "10.0.0.8",
    'priority' : "32768",
    "in_port" : "4",
    "active" : "true",
    "actions" : "output=2"
}

entry_s7 = {
    'switch' : '00:00:00:00:00:00:00:07',
    'name' : 'entry_s7',
    'eth_type' : "0x0800",
    "ipv4_src" : "10.0.0.9",
    "ipv4_dst" : "10.0.0.8",
    'priority' : "32768",
    "in_port" : "1",
    "active" : "true",
    "actions" : "output=3"
}

entry_s8 = {
    'switch' : '00:00:00:00:00:00:00:08',
    'name' : 'entry_s8',
    'eth_type' : "0x0800",
    "ipv4_src" : "10.0.0.9",
    "ipv4_dst" : "10.0.0.8",
    'priority' : "32768",
    "in_port" : "1",
    "active" : "true",
    "actions" : "output=4"
}

pusher.Set(entry_s3)
pusher.Set(entry_s1)
pusher.Set(entry_s4)
pusher.Set(entry_s6)
pusher.Set(entry_s7)
pusher.Set(entry_s8)
















