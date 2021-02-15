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
#***************A**to**D
# route from h12 to h8(TOS=1): h12->s9->s8->s10->s6->h8 ******************
Entry1_S9 = {
    'switch' : '00:00:00:00:00:00:00:09',
    'name' : 'Entry1_S9',
    'eth_type' : "0x0800",
    "ipv4_src" : "10.0.0.12",
    "ipv4_dst" : "10.0.0.8",
    'priority' : "32768",
    "ip_tos": "1",
    "in_port" : "2",
    "active" : "true",
    "actions" : "push_mpls=0x8847,set_field=mpls_label->7,output=1"
}

Entry1_S8 = {
    'switch' : '00:00:00:00:00:00:00:08',
    'name' : 'Entry1_S8',
    'eth_type' : "0x8847",
    'priority' : "32768",
    "mpls_label":"7",
    "in_port" : "4",
    "active" : "true",
    "actions" : "set_field=mpls_label->8,output=5"
}

Entry1_S10 = {
    'switch' : '00:00:00:00:00:00:00:0a',
    'name' : 'Entry1_S10',
    'eth_type' : "0x8847",
    'priority' : "32768",
    "mpls_label":"8",
    "in_port" : "6",
    "active" : "true",
    "actions" : "set_field=mpls_label->9,output=1"
}

Entry1_S6 = {
    'switch' : '00:00:00:00:00:00:00:06',
    'name' : 'Entry1_S6',
    'eth_type' : "0x8847",
    'priority' : "32768",
    "mpls_label":"9",
    "in_port" : "3",
    "active" : "true",
    "actions" : "pop_mpls=0x0800,output=2"
}

# route from h12 to h8(TOS=2): h12->s9->s8->s10->s6->h8 ******************
Entry2_S9 = {
    'switch' : '00:00:00:00:00:00:00:09',
    'name' : 'Entry2_S9',
    'eth_type' : "0x0800",
    "ipv4_src" : "10.0.0.12",
    "ipv4_dst" : "10.0.0.8",
    'priority' : "32768",
    "ip_tos": "2",
    "in_port" : "2",
    "active" : "true",
    "actions" : "push_mpls=0x8847,set_field=mpls_label->11,output=4"
}

Entry2_S10 = {
    'switch' : '00:00:00:00:00:00:00:0a',
    'name' : 'Entry2_S10',
    'eth_type' : "0x8847",
    'priority' : "32768",
    "mpls_label":"11",
    "in_port" : "2",
    "active" : "true",
    "actions" : "set_field=mpls_label->12,output=5"
}

Entry2_S3 = {
    'switch' : '00:00:00:00:00:00:00:03',
    'name' : 'Entry2_S3',
    'eth_type' : "0x8847",
    'priority' : "32768",
    "mpls_label":"12",
    "in_port" : "4",
    "active" : "true",
    "actions" : "set_field=mpls_label->13,output=3"
}

Entry2_S6 = {
    'switch' : '00:00:00:00:00:00:00:06',
    'name' : 'Entry2_S6',
    'eth_type' : "0x8847",
    'priority' : "32768",
    "mpls_label":"13",
    "in_port" : "1",
    "active" : "true",
    "actions" : "pop_mpls=0x0800,output=2"
}

#*********************B**to**E***********************
# route from h11 to h14(TOS=1): h11 -> s7 -> s5 -> s6 -> s10 ->h14
Entry3_S7 = {
    'switch' : '00:00:00:00:00:00:00:07',
    'name' : 'Entry3_S7',
    'eth_type' : "0x0800",
    "ipv4_src" : "10.0.0.11",
    "ipv4_dst" : "10.0.0.14",
    'priority' : "32768",
    "ip_tos": "1",
    "in_port" : "4",
    "active" : "true",
    "actions" : "push_mpls=0x8847,set_field=mpls_label->15,output=1"
}

Entry3_S5 = {
    'switch' : '00:00:00:00:00:00:00:05',
    'name' : 'Entry3_S5',
    'eth_type' : "0x8847",
    'priority' : "32768",
    "mpls_label":"15",
    "in_port" : "2",
    "active" : "true",
    "actions" : "set_field=mpls_label->16,output=3"
}

Entry3_S6 = {
    'switch' : '00:00:00:00:00:00:00:06',
    'name' : 'Entry3_S6',
    'eth_type' : "0x8847",
    'priority' : "32768",
    "mpls_label":"16",
    "in_port" : "6",
    "active" : "true",
    "actions" : "set_field=mpls_label->17,output=3"
}


Entry3_S10 = {
    'switch' : '00:00:00:00:00:00:00:0a',
    'name' : 'Entry3_S10',
    'eth_type' : "0x8847",
    'priority' : "32768",
    "mpls_label":"17",
    "in_port" : "1",
    "active" : "true",
    "actions" : "pop_mpls=0x0800,output=4"
}

# route from h11 to h14(TOS=2): h11 -> s7 -> s5 -> s4 -> s3 -> s10->h14
Entry4_S7 = {
    'switch' : '00:00:00:00:00:00:00:07',
    'name' : 'Entry4_S7',
    'eth_type' : "0x0800",
    "ipv4_src" : "10.0.0.11",
    "ipv4_dst" : "10.0.0.14",
    'priority' : "32768",
    "ip_tos": "2",
    "in_port" : "4",
    "active" : "true",
    "actions" : "push_mpls=0x8847,set_field=mpls_label->20,output=1"
}

Entry4_S5 = {
    'switch' : '00:00:00:00:00:00:00:05',
    'name' : 'Entry4_S5',
    'eth_type' : "0x8847",
    'priority' : "32768",
    "mpls_label":"20",
    "in_port" : "2",
    "active" : "true",
    "actions" : "set_field=mpls_label->21,output=1"
}

Entry4_S4 = {
    'switch' : '00:00:00:00:00:00:00:04',
    'name' : 'Entry4_S4',
    'eth_type' : "0x8847",
    'priority' : "32768",
    "mpls_label":"21",
    "in_port" : "2",
    "active" : "true",
    "actions" : "set_field=mpls_label->22,output=1"
}

Entry4_S3 = {
    'switch' : '00:00:00:00:00:00:00:03',
    'name' : 'Entry4_S3',
    'eth_type' : "0x8847",
    'priority' : "32768",
    "mpls_label":"22",
    "in_port" : "2",
    "active" : "true",
    "actions" : "set_field=mpls_label->23,output=4"
}

Entry4_S10 = {
    'switch' : '00:00:00:00:00:00:00:0a',
    'name' : 'Entry4_S10',
    'eth_type' : "0x8847",
    'priority' : "32768",
    "mpls_label":"23",
    "in_port" : "5",
    "active" : "true",
    "actions" : "pop_mpls=0x0800,output=4"
}

#*********************C**to**F***********************
# route from h3 to h9(TOS=1): h3 -> s2 -> s3 -> s4 -> s5 -> s6 -> h9
Entry5_S2 = {
    'switch' : '00:00:00:00:00:00:00:02',
    'name' : 'Entry5_S2',
    'eth_type' : "0x0800",
    "ipv4_src" : "10.0.0.3",
    "ipv4_dst" : "10.0.0.9",
    'priority' : "32768",
    "ip_tos": "1",
    "in_port" : "3",
    "active" : "true",
    "actions" : "push_mpls=0x8847,set_field=mpls_label->30,output=2"
}

Entry5_S3 = {
    'switch' : '00:00:00:00:00:00:00:03',
    'name' : 'Entry5_S3',
    'eth_type' : "0x8847",
    'priority' : "32768",
    "mpls_label":"30",
    "in_port" : "1",
    "active" : "true",
    "actions" : "set_field=mpls_label->31,output=2"
}

Entry5_S4 = {
    'switch' : '00:00:00:00:00:00:00:04',
    'name' : 'Entry5_S4',
    'eth_type' : "0x8847",
    'priority' : "32768",
    "mpls_label":"31",
    "in_port" : "1",
    "active" : "true",
    "actions" : "set_field=mpls_label->32,output=2"
}

Entry5_S5 = {
    'switch' : '00:00:00:00:00:00:00:05',
    'name' : 'Entry5_S5',
    'eth_type' : "0x8847",
    'priority' : "32768",
    "mpls_label":"32",
    "in_port" : "1",
    "active" : "true",
    "actions" : "set_field=mpls_label->33,output=3"
}

Entry5_S6 = {
    'switch' : '00:00:00:00:00:00:00:06',
    'name' : 'Entry5_S6',
    'eth_type' : "0x8847",
    'priority' : "32768",
    "mpls_label":"33",
    "in_port" : "6",
    "active" : "true",
    "actions" : "pop_mpls=0x0800,output=4"
}

# route from h3 to h9(TOS=2): h3 -> s2 -> s3 -> s10 -> s6 -> h9
Entry6_S2 = {
    'switch' : '00:00:00:00:00:00:00:02',
    'name' : 'Entry6_S2',
    'eth_type' : "0x0800",
    "ipv4_src" : "10.0.0.3",
    "ipv4_dst" : "10.0.0.9",
    'priority' : "32768",
    "ip_tos": "2",
    "in_port" : "3",
    "active" : "true",
    "actions" : "push_mpls=0x8847,set_field=mpls_label->40,output=2"
}

Entry6_S3 = {
    'switch' : '00:00:00:00:00:00:00:03',
    'name' : 'Entry6_S3',
    'eth_type' : "0x8847",
    'priority' : "32768",
    "mpls_label":"40",
    "in_port" : "1",
    "active" : "true",
    "actions" : "set_field=mpls_label->41,output=4"
}

Entry6_S10 = {
    'switch' : '00:00:00:00:00:00:00:0a',
    'name' : 'Entry6_S10',
    'eth_type' : "0x8847",
    'priority' : "32768",
    "mpls_label":"41",
    "in_port" : "5",
    "active" : "true",
    "actions" : "set_field=mpls_label->42,output=1"
}

Entry6_S6 = {
    'switch' : '00:00:00:00:00:00:00:06',
    'name' : 'Entry6_S6',
    'eth_type' : "0x8847",
    'priority' : "32768",
    "mpls_label":"42",
    "in_port" : "3",
    "active" : "true",
    "actions" : "pop_mpls=0x0800,output=4"
}


pusher.Set(Entry1_S9)
pusher.Set(Entry1_S8)
pusher.Set(Entry1_S10)
pusher.Set(Entry1_S6)
pusher.Set(Entry2_S9)
pusher.Set(Entry2_S10)
pusher.Set(Entry2_S3)
pusher.Set(Entry2_S6)
pusher.Set(Entry3_S7)
pusher.Set(Entry3_S5)
pusher.Set(Entry3_S6)
pusher.Set(Entry3_S10)
pusher.Set(Entry4_S7)
pusher.Set(Entry4_S5)
pusher.Set(Entry4_S4)
pusher.Set(Entry4_S3)
pusher.Set(Entry4_S10)
pusher.Set(Entry5_S2)
pusher.Set(Entry5_S3)
pusher.Set(Entry5_S4)
pusher.Set(Entry5_S5)
pusher.Set(Entry5_S6)
pusher.Set(Entry6_S2)
pusher.Set(Entry6_S3)
pusher.Set(Entry6_S10)
pusher.Set(Entry6_S6)
