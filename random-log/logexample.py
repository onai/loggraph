import logging
from random import choice
import socket
import struct
import random

def gen_ip(count):
    return [socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff))) for i in range(count)]

def get_random_ip(ls):
    return random.choice(ls)

class ContextFilter(logging.Filter):
    """
    This is a filter which injects contextual information into the log.

    Rather than use actual contextual information, we just use random
    data in this demo.
    """

    USERS = ['jim', 'fred', 'sheila']
    IPS = gen_ip(40)
    IPS2 = gen_ip(40)

    def filter(self, record):

        record.ip = choice(ContextFilter.IPS)
        record.ip2 = choice(ContextFilter.IPS)
        record.user = choice(ContextFilter.USERS)
        return True

if __name__ == '__main__':
    levels = (logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL)
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)-15s %(name)-5s %(levelname)-8s IP: %(ip)-15s User: %(user)-8s IP2: %(ip2)-15s')
    a1 = logging.getLogger('a.b.c')
    a2 = logging.getLogger('d.e.f')

    f = ContextFilter()
    a1.addFilter(f)
    a2.addFilter(f)
    #a1.debug('A debug message')
    #a1.info('An info message with %s', 'some parameters')
    for x in range(200):
        lvl = choice(levels)
        lvlname = logging.getLevelName(lvl)
        a2.log(lvl, '%s %d %s', lvlname, 2, 'parameters')
