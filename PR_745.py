data = {
    "acls_data": [
        {
            "acls": [
                {
                    "aces": [
                        {
                            "destination": {
                                "address": "192.0.3.0",
                                "wildcard_bits": "0.0.0.255"
                            },
                            "dscp": "ef",
                            "grant": "deny",
                            "protocol": "icmp",
                            "protocol_options": {
                                    "icmp": {
                                        "traceroute": True
                                    }
                            },
                            "sequence": 10,
                            "source": {
                                "address": "192.0.2.0",
                                "wildcard_bits": "0.0.0.255"
                            },
                            "ttl": {
                                "eq": 10
                            }
                        },
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
                        {
                            "destination": {
                                "address": "192.0.4.0",
                                "port_protocol": {
                                    "eq": "www"
                                },
                                "wildcard_bits": "0.0.0.255"
                            },
                            "dscp": "ef",
                                    "grant": "deny",
                                    "protocol": "tcp",
                                    "protocol_options": {
                                "tcp": {
                                                "ack": True
                                }
                            },
                            "sequence": 20,
                            "source": {
                                        "address": "192.0.3.0",
                                        "wildcard_bits": "0.0.0.255"
                            },
                            "ttl": {
                                        "lt": 20
                            }
                        }
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
                {
                    "aces": [
                        {
                            "destination": {
                                "address": "192.0.3.0",
                                "port_protocol": {
                                    "eq": "www"
                                },
                                "wildcard_bits": "0.0.0.255"
                            },
                            "grant": "deny",
                            "option": {
                                "traceroute": True
                            },
                            "protocol": "tcp",
                            "protocol_options": {
                                        "tcp": {
                                            "fin": True
                                        }
                            },
                            "sequence": 10,
                            "source": {
                                "address": "192.0.2.0",
                                "wildcard_bits": "0.0.0.255"
                            },
                            "ttl": {
                                "eq": 10
                            }
                        }
                    ],
                    "acl_type": "extended",
                    "name": "test"
                }
            ],
            "afi": "ipv4"
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


filter_operation = {
    "filter_options": {
        "match_all": True
    }
}

match_criteria = {
    "afi": "ipv4",
    "source_address": "192.0.2.0",
    "destination_address": "192.0.3.0"
}



def validator_func(each_ace, match_criteria, filter_operation, name, afi):
    check_list  , future_use = ["source" , "destination" , "afi"] , []
    for key , val in each_ace.items():
            if key not in check_list:
                if each_ace.get(key , "Not Found") == match_criteria.get(key , "Not Found"):
                     future_use.append(True)
                else :
                     future_use.append(False)
            elif(name == key ):
                future_use.append(True) if name == match_criteria.get(key) else future_use.append(False)

            elif(afi == key ):
                future_use.append(True) if name == match_criteria.get(key) else future_use.append(False)
            else:
                          
                     
               



def delete_aces(data, match_criteria, filter_operation):
    ace_v4, ace_v6 = [], []
    rem_ace_v4, rem_ace_v6 = [], []

    flinal_acls = {"acls": [{"aces": ace_v4, "afi": "ipv4"}], "acls": [
        {"aces": ace_v6, "afi": "ipv6"}]}
    rem_acls = {"acls": [{"aces": rem_ace_v4, "afi": "ipv4"}],
                "acls": [{"aces": rem_ace_v6, "afi": "ipv6"}]}

    remove_first_only = True if filter_operation.get(
        "match_all") is True else False

    for acls in data.get("acls_data"):
        afi = acls.get("afi")

        for acl in acls.get("acls"):
            aces_inner, acls_inner = [], {}
            remace_inner, remacls_inner = [], {}
            holt = True

            aces = acl.get("aces", [])

            name = acl.get("name", "No String")

            for each_ace in aces:
                temp = validator_func(each_ace, match_criteria, filter_operation, name, afi)


delete_aces(data, match_criteria, filter_operation)
