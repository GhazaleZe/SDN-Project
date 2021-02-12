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

#h9 to h14

entry_s6_914 = {
    'switch' : '00:00:00:00:00:00:00:06',
    'name' : 'entry_s6_914',
    'eth_type' : "0x0800",
    "ipv4_src" : "10.0.0.9",
    "ipv4_dst" : "10.0.0.14",
    'priority' : "32768",
    "in_port" : "4",
    "active" : "true",
    "actions" : "output=1"
}


entry_s3_914 = {
    'switch' : '00:00:00:00:00:00:00:03',
    'name' : 'entry_s3_914',
    'eth_type' : "0x0800",
    "ipv4_src" : "10.0.0.9",
    "ipv4_dst" : "10.0.0.14",
    'priority' : "32768",
    "in_port" : "3",
    "active" : "true",
    "actions" : "output=4"
}

entry_s10_914 = {
    'switch' : '00:00:00:00:00:00:00:0a',
    'name' : 'entry_s10_914',
    'eth_type' : "0x0800",
    "ipv4_src" : "10.0.0.9",
    "ipv4_dst" : "10.0.0.14",
    'priority' : "32768",
    "in_port" : "5",
    "active" : "true",
    "actions" : "output=4"
}

#h14 to h5

entry_s10_145 = {
    'switch' : '00:00:00:00:00:00:00:0a',
    'name' : 'entry_s10_145',
    'eth_type' : "0x0800",
    "ipv4_src" : "10.0.0.14",
    "ipv4_dst" : "10.0.0.5",
    'priority' : "32768",
    "in_port" : "4",
    "active" : "true",
    "actions" : "output=2"
}

entry_s9_145 = {
    'switch' : '00:00:00:00:00:00:00:09',
    'name' : 'entry_s9_145',
    'eth_type' : "0x0800",
    "ipv4_src" : "10.0.0.14",
    "ipv4_dst" : "10.0.0.5",
    'priority' : "32768",
    "in_port" : "4",
    "active" : "true",
    "actions" : "output=1"
}


entry_s8_145 = {
    'switch' : '00:00:00:00:00:00:00:08',
    'name' : 'entry_s8_145',
    'eth_type' : "0x0800",
    "ipv4_src" : "10.0.0.14",
    "ipv4_dst" : "10.0.0.5",
    'priority' : "32768",
    "in_port" : "4",
    "active" : "true",
    "actions" : "output=1"
}

#h12 to h7

entry_s9_127 = {
    'switch' : '00:00:00:00:00:00:00:09',
    'name' : 'entry_s9_127',
    'eth_type' : "0x0800",
    "ipv4_src" : "10.0.0.12",
    "ipv4_dst" : "10.0.0.7",
    'priority' : "32768",
    "in_port" : "2",
    "active" : "true",
    "actions" : "output=4"
}

entry_s10_127 = {
    'switch' : '00:00:00:00:00:00:00:0a',
    'name' : 'entry_s10_127',
    'eth_type' : "0x0800",
    "ipv4_src" : "10.0.0.12",
    "ipv4_dst" : "10.0.0.7",
    'priority' : "32768",
    "in_port" : "2",
    "active" : "true",
    "actions" : "output=6"
}

entry_s8_127 = {
    'switch' : '00:00:00:00:00:00:00:08',
    'name' : 'entry_s8_127',
    'eth_type' : "0x0800",
    "ipv4_src" : "10.0.0.12",
    "ipv4_dst" : "10.0.0.7",
    'priority' : "32768",
    "in_port" : "5",
    "active" : "true",
    "actions" : "output=3"
}

#h7 to h11

entry_s8_711 = {
    'switch' : '00:00:00:00:00:00:00:08',
    'name' : 'entry_s8_711',
    'eth_type' : "0x0800",
    "ipv4_src" : "10.0.0.7",
    "ipv4_dst" : "10.0.0.11",
    'priority' : "32768",
    "in_port" : "3",
    "active" : "true",
    "actions" : "output=5"
}

entry_s10_711 = {
    'switch' : '00:00:00:00:00:00:00:0a',
    'name' : 'entry_s10_711',
    'eth_type' : "0x0800",
    "ipv4_src" : "10.0.0.7",
    "ipv4_dst" : "10.0.0.11",
    'priority' : "32768",
    "in_port" : "6",
    "active" : "true",
    "actions" : "output=5"
}

entry_s3_711 = {
    'switch' : '00:00:00:00:00:00:00:03',
    'name' : 'entry_s3_711',
    'eth_type' : "0x0800",
    "ipv4_src" : "10.0.0.7",
    "ipv4_dst" : "10.0.0.11",
    'priority' : "32768",
    "in_port" : "4",
    "active" : "true",
    "actions" : "output=2"
}

entry_s3_711 = {
    'switch' : '00:00:00:00:00:00:00:03',
    'name' : 'entry_s3_711',
    'eth_type' : "0x0800",
    "ipv4_src" : "10.0.0.7",
    "ipv4_dst" : "10.0.0.11",
    'priority' : "32768",
    "in_port" : "4",
    "active" : "true",
    "actions" : "output=2"
}

entry_s4_711 = {
    'switch' : '00:00:00:00:00:00:00:04',
    'name' : 'entry_s4_711',
    'eth_type' : "0x0800",
    "ipv4_src" : "10.0.0.7",
    "ipv4_dst" : "10.0.0.11",
    'priority' : "32768",
    "in_port" : "1",
    "active" : "true",
    "actions" : "output=2"
}

entry_s5_711 = {
    'switch' : '00:00:00:00:00:00:00:05',
    'name' : 'entry_s5_711',
    'eth_type' : "0x0800",
    "ipv4_src" : "10.0.0.7",
    "ipv4_dst" : "10.0.0.11",
    'priority' : "32768",
    "in_port" : "1",
    "active" : "true",
    "actions" : "output=2"
}

entry_s7_711 = {
    'switch' : '00:00:00:00:00:00:00:07',
    'name' : 'entry_s7_711',
    'eth_type' : "0x0800",
    "ipv4_src" : "10.0.0.7",
    "ipv4_dst" : "10.0.0.11",
    'priority' : "32768",
    "in_port" : "1",
    "active" : "true",
    "actions" : "output=4"
}

#h3 to h9

entry_s2_39 = {
    'switch' : '00:00:00:00:00:00:00:02',
    'name' : 'entry_s2_39',
    'eth_type' : "0x0800",
    "ipv4_src" : "10.0.0.3",
    "ipv4_dst" : "10.0.0.9",
    'priority' : "32768",
    "in_port" : "3",
    "active" : "true",
    "actions" : "output=2"
}

entry_s3_39 = {
    'switch' : '00:00:00:00:00:00:00:03',
    'name' : 'entry_s3_39',
    'eth_type' : "0x0800",
    "ipv4_src" : "10.0.0.3",
    "ipv4_dst" : "10.0.0.9",
    'priority' : "32768",
    "in_port" : "1",
    "active" : "true",
    "actions" : "output=3"
}

entry_s6_39 = {
    'switch' : '00:00:00:00:00:00:00:06',
    'name' : 'entry_s6_39',
    'eth_type' : "0x0800",
    "ipv4_src" : "10.0.0.3",
    "ipv4_dst" : "10.0.0.9",
    'priority' : "32768",
    "in_port" : "1",
    "active" : "true",
    "actions" : "output=4"
}


#h8 to h14

entry_s6_814 = {
    'switch' : '00:00:00:00:00:00:00:06',
    'name' : 'entry_s6_814',
    'eth_type' : "0x0800",
    "ipv4_src" : "10.0.0.8",
    "ipv4_dst" : "10.0.0.14",
    'priority' : "32768",
    "in_port" : "2",
    "active" : "true",
    "actions" : "output=1"
}

entry_s3_814 = {
    'switch' : '00:00:00:00:00:00:00:03',
    'name' : 'entry_s3_814',
    'eth_type' : "0x0800",
    "ipv4_src" : "10.0.0.8",
    "ipv4_dst" : "10.0.0.14",
    'priority' : "32768",
    "in_port" : "3",
    "active" : "true",
    "actions" : "output=4"
}

entry_s10_814 = {
    'switch' : '00:00:00:00:00:00:00:0a',
    'name' : 'entry_s10_814',
    'eth_type' : "0x0800",
    "ipv4_src" : "10.0.0.8",
    "ipv4_dst" : "10.0.0.14",
    'priority' : "32768",
    "in_port" : "5",
    "active" : "true",
    "actions" : "output=4"
}


pusher.Set(entry_s6_914)
pusher.Set(entry_s3_914)
pusher.Set(entry_s10_914)
pusher.Set(entry_s10_145)
pusher.Set(entry_s9_145)
pusher.Set(entry_s8_145)
pusher.Set(entry_s9_127)
pusher.Set(entry_s10_127)
pusher.Set(entry_s8_127)
pusher.Set(entry_s8_711)
pusher.Set(entry_s10_711)
pusher.Set(entry_s3_711)
pusher.Set(entry_s4_711)
pusher.Set(entry_s5_711)
pusher.Set(entry_s7_711)
pusher.Set(entry_s2_39)
pusher.Set(entry_s3_39)
pusher.Set(entry_s6_39)
pusher.Set(entry_s6_814)
pusher.Set(entry_s3_814)
pusher.Set(entry_s10_814)















