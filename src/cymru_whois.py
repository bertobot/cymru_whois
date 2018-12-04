import socket


def lookup(ips):
    ok = False
    if isinstance(ips, list):
        ok = True
    elif isinstance(ips, str):
        return lookup([ips])
    else:
        ok = False

    if not ok:
        raise TypeError("invalid type")

    payload = '\r\n'.join(ips)
    command = '\r\n'.join(['begin', 'verbose', payload, 'end'])
    buffer = ''

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('whois.cymru.com', 43))
        s.sendall(command.encode())

        while True:
            data = s.recv(1024)
            buffer += data.decode('utf-8')
            if len(data) < 1024:
                break

    # now parse data

    result = []
    first = True

    for line in buffer.split('\n'):
        if first:
            first = False
            continue

        fields = line.split('|')

        if len(fields) < 7:
            continue

        result.append({
            'asn': fields[0].strip(),
            'subnet': fields[2].strip(),
            'country_code': fields[3].strip(),
            'since': fields[5].strip(),
            'owner': fields[6].strip()
        })

    return result
