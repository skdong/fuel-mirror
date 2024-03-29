SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "definitions": {
        "DEB_REPO_SCHEMA": {
            "type": "object",
            "required": [
                "name",
                "uri",
                "suite",
                "section"
            ],
            "properties": {
                "name": {
                    "type": "string"
                },
                "type": {
                    "type": "string",
                    "enum": ["deb"]
                },
                "uri": {
                    "type": "string"
                },
                "priority": {
                    "anyOf": [
                        {
                            "type": "integer"
                        },
                        {
                            "type": "null"
                        }
                    ]
                },
                "suite": {
                    "type": "string"
                },
                "section": {
                    "type": "array",
                    "items": {"type": "string"}
                },
            }
        },
        "RPM_REPO_SCHEMA": {
            "type": "object",
            "required": [
                "name",
                "uri",
            ],
            "properties": {
                "name": {
                    "type": "string"
                },
                "type": {
                    "type": "string",
                    "enum": ["rpm"]
                },
                "uri": {
                    "type": "string"
                },
                "priority": {
                    "anyOf": [
                        {
                            "type": "integer"
                        },
                        {
                            "type": "null"
                        }
                    ]
                },
            }
        },
        "REPO_SCHEMA": {
            "anyOf":
            [
                {"$ref": "#/definitions/DEB_REPO_SCHEMA"},
                {"$ref": "#/definitions/RPM_REPO_SCHEMA"}
            ]
        },

        "REPOS_SCHEMA": {
            "type": "array", "items": {"$ref": "#/definitions/REPO_SCHEMA"}
        }
    },
    "type": "object",
    "required": [
        "groups",
    ],
    "properties": {
        "fuel_release_match": {
            "type": "object",
            "properties": {
                "operating_system": {
                    "type": "string"
                }
            },
            "required": [
                "operating_system"
            ]
        },
        "requirements": {
            "type": "object",
            "patternProperties": {
                "^[0-9a-z_-]+$": {
                    "type": "object",
                    "anyOf": [
                        {"required": ["packages"]},
                        {"required": ["repositories"]},
                        {"required": ["mandatory"]}
                    ],
                    "properties": {
                        "repositories": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "required": ["name"],
                                "properties": {
                                    "name": {
                                        "type": "string"
                                    },
                                    "excludes": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "patternProperties": {
                                                r"[a-z][\w_]*": {
                                                    "type": "string"
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "packages": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "required": ["name"],
                                "properties": {
                                    "name": {
                                        "type": "string"
                                    },
                                    "versions": {
                                        "type": "array",
                                        "items": {
                                            "type": "string",
                                            "pattern": "^([<>]=?|=)\s+.+$"
                                        }
                                    }
                                }
                            }
                        },
                        "mandatory": {
                            "enum": ["exact", "newest"]
                        }
                    }
                }
            },
            "additionalProperties": False,
        },
        "groups": {
            "type": "object",
            "patternProperties": {
                "^[0-9a-z_-]+$": {"$ref": "#/definitions/REPOS_SCHEMA"}
            },
            "additionalProperties": False,
        },
        "inheritance": {
            "type": "object",
            "patternProperties": {
                "^[0-9a-z_-]+$": {"type": "string"}
            },
            "additionalProperties": False,
        }
    }
}
