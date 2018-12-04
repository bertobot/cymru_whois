# cymru whois

A simple python API for cymru's whois service.

## Synopsis

```python

from import cymru_whois import lookup 

ip_single = '8.8.8.8'
ip_multi = ['8.8.8.8', '1.1.1.1']

a1 = lookup(ip_single)
print(a1)
# [{'asn': '15169', 'subnet': '8.8.8.0/24', 'country_code': 'US', 'since': '1992-12-01', 'owner': 'GOOGLE - Google LLC, US'}]


a2 = lookup(ip_multi)
print(a2)
# [{'asn': '15169', 'subnet': '8.8.8.0/24', 'country_code': 'US', 'since': '1992-12-01', 'owner': 'GOOGLE - Google LLC, US'}, {'asn': '13335', 'subnet': '1.1.1.0/24', 'country_code': 'AU', 'since': '2011-08-11', 'owner': 'CLOUDFLARENET - Cloudflare, Inc., US'}]

``` 

## Description

*lookup(list_of_ips)*

Yields a list of dictionaries with the following properties:

* asn: the AS number,
* subnet: the subnet the IP belongs to,
* country_code: the country code the subnet is in,
* since: time the ASN was first observed,
* owner: the organization that owns the subnet / ASN






 
