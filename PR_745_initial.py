data = {
    "acls_data": [
        {
            "acls": [
                {
                    "aces": [
                        {
                            "destination": {
                                "host": "198.51.110.0",
                                "port_protocol": {
                                        "eq": "telnet"
                                }
                            },
                            "grant": "deny",
                            "protocol": "tcp",
                            "protocol_options": {
                                "tcp": {
                                        "ack": True
                                }
                            },
                            "sequence": 20,
                            "source": {
                                "host": "198.51.100.0"
                            }
                        }
                    ],
                    "acl_type": "extended",
                    "name": "110"
                },
                {
                    "aces": [
                        {
                            "destination": {
                                "address": "198.51.101.0",
                                "port_protocol": {
                                    "eq": "telnet"
                                },
                                "wildcard_bits": "0.0.0.255"
                            },
                            "grant": "deny",
                            "protocol": "tcp",
                            "protocol_options": {
                                "tcp": {
                                        "ack": True
                                }
                            },
                            "sequence": 10,
                            "source": {
                                "address": "198.51.100.0",
                                "wildcard_bits": "0.0.0.255"
                            },
                            "tos": {
                                "service_value": 12
                            }
                        },
                    ],
                    "acl_type": "extended",
                    "name": "123"
                },
                {
                    "aces": [
                        {
                            "grant": "deny",
                            "sequence": 10,
                            "source": {
                                "host": "192.168.1.200"
                            }
                        },
                        {
                            "grant": "deny",
                            "sequence": 20,
                            "source": {
                                "address": "192.168.2.0",
                                "wildcard_bits": "0.0.0.255"
                            }
                        }
                    ],
                    "acl_type": "standard",
                    "name": "std_acl"
                },
            ],
        },
        {
            "acls": [
                {
                    "aces": [
                        {
                            "destination": {
                                "any": True,
                                "port_protocol": {
                                    "eq": "telnet"
                                }
                            },
                            "dscp": "af11",
                            "grant": "deny",
                            "protocol": "tcp",
                            "protocol_options": {
                                    "tcp": {
                                        "ack": True
                                    }
                            },
                            "sequence": 10,
                            "source": {
                                "any": True,
                                "port_protocol": {
                                    "eq": "www"
                                }
                            }
                        }
                    ],
                    "name": "R1_TRAFFIC"
                }
            ],
            "afi": "ipv6"
        }
    ]
}


# data = {
#     "acls_data": [
#         {
#             "acls": [
#                 {
#                     "aces": [
#                         {
#                             "destination": {
#                                 "address": "192.0.3.0",
#                                 "wildcard_bits": "0.0.0.255"
#                             },
#                             "dscp": "ef",
#                             "grant": "deny",
#                             "protocol": "icmp",
#                             "protocol_options": {
#                                     "icmp": {
#                                         "traceroute": True
#                                     }
#                             },
#                             "sequence": 10,
#                             "source": {
#                                 "address": "192.0.2.0",
#                                 "wildcard_bits": "0.0.0.255"
#                             },
#                             "ttl": {
#                                 "eq": 10
#                             }
#                         },
#                         {
#                             "destination": {
#                                 "host": "198.51.110.0",
#                                 "port_protocol": {
#                                         "eq": "telnet"
#                                 }
#                             },
#                             "grant": "deny",
#                             "protocol": "tcp",
#                             "protocol_options": {
#                                 "tcp": {
#                                         "ack": True
#                                 }
#                             },
#                             "sequence": 20,
#                             "source": {
#                                 "host": "198.51.100.0"
#                             }
#                         }
#                     ],
#                     "acl_type": "extended",
#                     "name": "110"
#                 },
#                 {
#                     "aces": [
#                         {
#                             "destination": {
#                                 "address": "198.51.101.0",
#                                 "port_protocol": {
#                                     "eq": "telnet"
#                                 },
#                                 "wildcard_bits": "0.0.0.255"
#                             },
#                             "grant": "deny",
#                             "protocol": "tcp",
#                             "protocol_options": {
#                                         "tcp": {
#                                             "ack": True
#                                         }
#                             },
#                             "sequence": 10,
#                             "source": {
#                                 "address": "198.51.100.0",
#                                 "wildcard_bits": "0.0.0.255"
#                             },
#                             "tos": {
#                                 "service_value": 12
#                             }
#                         },
#                         {
#                             "destination": {
#                                 "address": "192.0.4.0",
#                                 "port_protocol": {
#                                     "eq": "www"
#                                 },
#                                 "wildcard_bits": "0.0.0.255"
#                             },
#                             "dscp": "ef",
#                                     "grant": "deny",
#                                     "protocol": "tcp",
#                                     "protocol_options": {
#                                 "tcp": {
#                                                 "ack": True
#                                 }
#                             },
#                             "sequence": 20,
#                             "source": {
#                                         "address": "192.0.3.0",
#                                         "wildcard_bits": "0.0.0.255"
#                             },
#                             "ttl": {
#                                         "lt": 20
#                             }
#                         }
#                     ],
#                     "acl_type": "extended",
#                     "name": "123"
#                 },
#                 {
#                     "aces": [
#                         {
#                             "grant": "deny",
#                             "sequence": 10,
#                             "source": {
#                                 "host": "192.168.1.200"
#                             }
#                         },
#                         {
#                             "grant": "deny",
#                             "sequence": 20,
#                             "source": {
#                                 "address": "192.168.2.0",
#                                 "wildcard_bits": "0.0.0.255"
#                             }
#                         }
#                     ],
#                     "acl_type": "standard",
#                     "name": "std_acl"
#                 },
#                 {
#                     "aces": [
#                         {
#                             "destination": {
#                                 "address": "192.0.3.0",
#                                 "port_protocol": {
#                                     "eq": "www"
#                                 },
#                                 "wildcard_bits": "0.0.0.255"
#                             },
#                             "grant": "deny",
#                             "option": {
#                                 "traceroute": True
#                             },
#                             "protocol": "tcp",
#                             "protocol_options": {
#                                         "tcp": {
#                                             "fin": True
#                                         }
#                             },
#                             "sequence": 10,
#                             "source": {
#                                 "address": "192.0.2.0",
#                                 "wildcard_bits": "0.0.0.255"
#                             },
#                             "ttl": {
#                                 "eq": 10
#                             }
#                         }
#                     ],
#                     "acl_type": "extended",
#                     "name": "test"
#                 }
#             ],
#             "afi": "ipv4"
#         },
#         {
#             "acls": [
#                 {
#                     "aces": [
#                         {
#                             "destination": {
#                                 "any": True,
#                                 "port_protocol": {
#                                     "eq": "telnet"
#                                 }
#                             },
#                             "dscp": "af11",
#                                     "grant": "deny",
#                                     "protocol": "tcp",
#                                     "protocol_options": {
#                                 "tcp": {
#                                                 "ack": True
#                                 }
#                             },
#                             "sequence": 10,
#                             "source": {
#                                         "any": True,
#                                         "port_protocol": {
#                                             "eq": "www"
#                                         }
#                             }
#                         }
#                     ],
#                     "name": "R1_TRAFFIC"
#                 }
#             ],
#             "afi": "ipv6"
#         }
#     ]
# }


vars = {
    "filter_options": {
        "match_all": True
    }
}

match_criteria = {
    "afi": "ipv4",
    "source_address": "192.0.2.0",
    "destination_address": "192.0.3.0"
}

# Thinking 2



match_temp, temp2 = [], []


def Solve(data, matching_critreria, vars):
    for key, val in match_criteria.items():
        match_temp.append(val)

    for key, val in data.items():
        if (type(val) == list):
            for j in val:
                if (isinstance(j, dict)):
                    acls = j.get("acls")
                    for aces in acls:
                        for ent, ent_val in aces.items():
                            if (isinstance(ent_val, dict) or (isinstance(ent_val, list))):
                                for sce_core_val in ent_val:
                                    for core, core_val in sce_core_val.items():
                                        if core == "source" or core == "destination":
                                            temp2.append(core_val)
                                            break
                                    for i in temp2:
                                        for tem_key, temp_val in i.items():
                                            if temp_val in match_temp:
                                                print(
                                                    temp_val, "matched", match_temp)


Solve(data, match_criteria, vars)
