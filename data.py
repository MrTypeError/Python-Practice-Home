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
