import pyshark

shark_cap = pyshark.FileCapture('data/maccdc2010_00023_20100313211521.pcap')

for packet in shark_cap:
    import ipdb ; ipdb.set_trace()
