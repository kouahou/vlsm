import math
import socket
import struct
import ipaddress


def get_mask(nb_machine):
    return 32 - math.ceil(math.log2(nb_machine))


def pgcd(ri, q):
    if ri < q:
        return 0
    return (ri // q) * q


def dec_mask(mask_length):
    mask = (1 << 32) - (1 << 32 >> mask_length)
    return socket.inet_ntoa(struct.pack(">L", mask))


def assignable_range(ip, mask):
    net4 = ipaddress.ip_network(f'{ip}/{mask}')
    hosts = list(net4.hosts())
    return hosts


def last_and_first_assignable_range(ip, mask):
    hosts = assignable_range(ip, mask)
    return f'{hosts[0]}-{hosts[-1]}'


def get_broadcast(ip, mask):
    net4 = ipaddress.ip_network(f'{ip}/{mask}')
    return str(net4.broadcast_address)


class IPService:
    def __init__(self, ip, mask):
        self.ip = ip
        self.mask = int(mask)

        self.table = {
            32: 1,
            31: 2,
            30: 4,
            29: 8,
            28: 16,
            27: 32,
            26: 64,
            25: 128,
        }

        self.sub_networks = {}

    def set_sub_network(self, sub_networks):
        self.sub_networks = sub_networks
        self.order_network()

    def sub_all_network(self):
        first = list(self.sub_networks.values())[0]
        mask = get_mask(first)

        if not self.is_full(mask):
            list_n = []
            base_ip = self.ip
            for key, val in self.get_base_mask().items():
                list_n.append({key: [base_ip, val]})
                base_ip = self.get_next_network(base_ip, val)
            return list_n

    def get_next_network(self, ip, mask):
        i, q = self.get_q(mask)
        tab_ip = [int(i) for i in ip.split(".")][::-1]

        while tab_ip[i] + q > 255:
            tab_ip[i] = 0
            i = i + 1
            q = 1
        tab_ip[i] = pgcd(tab_ip[i], q) + q
        tab_ip = [str(i) for i in tab_ip][::-1]
        return ".".join(tab_ip)

    def order_network(self):
        self.sub_networks = dict(sorted(self.sub_networks.items(), key=lambda item: item[1], reverse=True))

    def get_base_mask(self):
        return dict(zip(self.sub_networks.keys(),
                        list(map(get_mask, self.sub_networks.values()))))

    def get_base_q_and_position(self):
        return dict(zip(self.sub_networks.keys(), list(map(self.get_q, self.get_base_mask().values()))))

    def get_q(self, mask):
        i = 0
        while mask < 25:
            mask = mask + 8
            i = i + 1
        return i, self.table.get(mask)

    def is_full(self, mask):
        return self.mask > mask

    def get_address(self, name):
        return [k.get(name) for k in self.sub_all_network() if name in k.keys()][0]

    def result(self):
        subnets = [[
            k,
            s,
            2**math.ceil(math.log2(s)),
            *self.get_address(k),
            dec_mask(self.get_base_mask().get(k)),
            last_and_first_assignable_range(*self.get_address(k)),
            get_broadcast(*self.get_address(k))
        ]
                   for k, s in self.sub_networks.items()]
        return subnets


if __name__ == '__main__':
    ip_service = IPService('172.16.0.0', 21)
    sub = {
        "ADMIN": 400,
        "GUEST": 200,
        "IMP": 300,
        "ANT": 45,
        "USERS": 120,
        "INVT": 1030
    }

    ip_service.set_sub_network(sub)

    print(ip_service.sub_networks)

    print(ip_service.get_base_mask())

    print(ip_service.get_base_q_and_position())

    print(ip_service.sub_all_network())

    print(ip_service.result())
