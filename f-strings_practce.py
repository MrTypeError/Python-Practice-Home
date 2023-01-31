
'''Normally used f-strings '''

my_var = 5
print(f"The value of my variable is: {my_var}")

'''indexing in formatting strings '''

a = 1
b = 2
print(f"i am {1} with {0} and {2}").format(a, b, my_var)


'''
    using string formatting with **kwargs (key-value pair)
    and *args(lists) and nested value retrival 
'''


command = "I am "
config_data = {
    "afi": "ipv4",
    "destination": {
        "address": "192.0.4.0",
        "port_protocol": {"eq": "www"},
        "wildcard_bits": "0.0.0.255",
    },
    "dscp": "ef",
    "grant": "deny",
    "protocol": "tcp",
    "protocol_options": {"tcp": {"ack": True}},
    "sequence": 21,
    "source": {"address": "192.0.3.0", "wildcard_bits": "0.0.0.255"},
    "ttl": {"lt": 20},
}
if config_data["destination"].get("address"):
    command += " {address}".format(**config_data["destination"])
    if config_data["destination"].get("wildcard_bits"):
        command += " {wildcard_bits}".format(**config_data["destination"])

print(command)


'''
chaining string formatting (it is considered as a single string at the end )
'''


var_a = 2
var_b = 3
my_long_string = (
    "This is a very long string"
    f" that contains var_a: {var_a}"
    f" that contains var_a: {var_a}"
    f" that contains var_a: {var_a}"
    f" that contains var_a: {var_a}"
    f" that contains var_a: {var_a}"
    f" that contains var_a: {var_a}"
    f" that contains var_a: {var_a}"
    f" and var_b: {var_b}"
)
print(my_long_string)
