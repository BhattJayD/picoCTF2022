from os import system as s

s("tcpdump -A -r network-dump.flag.pcap  | grep -oE '{.*}' | tr -d ' ' |grep -oE 'picoCTF{.*}'")
