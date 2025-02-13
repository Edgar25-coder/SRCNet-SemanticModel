import json

spsrcnode = {
    "@context": {
        "@vocab": "http://schema.org/",
        "SRCNet": "http://example.org/SRCNet",
        "SRCNode": "http://example.org/SRCNode",
        "Place": "https://schema.org/Place",
        "Country": "https://schema.org/Country",
        "Region": "https://schema.org/Region",
        "Geo": "https://schema.org/Geo",
        "ContactPoint": "https://schema.org/ContactPoint",
        "Person": "https://schema.org/Person",
        "Organization": "https://schema.org/Organization",
        "Computing": "http://example.org/Computing",
        "CPU": "http://example.org/CPU",
        "Disk": "http://example.org/Disk",
        "Memory": "http://example.org/Memory",
        "qudt": "http://qudt.org/schema/qudt/",
        "Architecture": "http://example.org/Architecture",
        "Network": "http://example.org/Network",
        "Service": "http://example.org/Service",
       
    },
    "@graph": [
        {
            "@id":"http://example.org/spSRC1",
            "@type":"http://example.org/computing",
            "name": "Nodes",
            "isComposedBy": {
                "@type": "SRCNode",
                "name": "spSRC1",
                "locatedIn": {
                    "@type": "Place",
                    "name": "Granada",
                    "isInAcountry": {
                        "@type": "Country",
                        "name": "Spain",
                        "Locality":"Granada",
                        "addressLocality":{
                            "type":"@postalAddress",
                            "address":"xxxxxxxxxxxxxxxx"
                            }
                    },

                    "isInAregion":{
                        "@type":"region",
                        "name":"andalucia",
                        "postalCode":"",
                        "addressRegion":""
                },

                    "has_geo": {
                        "@type": "GeoCoordinates",
                        "latitude": 10.0000,
                        "longitude": -1.0000
                    },
                    "has_contacts": {
                        "@type": "ContactPoint",
                        "name": "Spsrc Team",
                        "telephone": "+34 958121311",
                        "email": "infospsrc@iaa.csic.es",
                        "adress":"Gta de la Astronomía, s/n, Genil, 18008 ",
                        "faxNumber":"+34 958814530",
                        "URL":"iaa.csic.es"
                    }
                },
                "has_PI": {
                    "@type": "Person",
                    "name": "Manu Parra",
                    "email": "manu@example.com",
                    "telephone":"xxxxxxxxxxx",
                     "worksIn": {
                         "@type": "Organization",
                         "name": "iaa_csic"
                         },
                },
                "isComposedBy": {
                    "@type": "Computing",
                    "hasCPU": {
                        "@type": "CPU",
                        "cores": 8,
                        "clock":{
                            "@type":"quantityValue",
                            "unit":"GHz",
                            "value":3.5,
                            
                            }
                    },

                    "hasMemory": {
                        "@type": "QuantityValue",
                         "unit": "http://qudt.org/vocab/unit/Gigabyte",
                         "value":32
                         },
                    
                    "hasDisk": {
                        "@type": "Disk",
                        "size":{
                            "@type":"QuantityValue",
                            "unit": "http://qudt.org/vocab/unit/Terabyte",
                            "value":1
                            
                            },
                        "type": "SSD"
                    },
                }
            }
        },

        {
            "@id":"http://example.org/spSRC2",
            "@type":"http://example.org/computing",
            "@type": "SRCNode",
            "name": "spSRC2",
            "locatedIn": {
                "@type": "Place",
                "name": "Madrid",
                "isInAcountry": {
                    "@type": "Country",
                    "name": "Spain",
                    "Locality":"Madrid Centro",
                        "addressLocality":{
                            "type":"@postalAddress",
                            "address":"xxxxxxxxxxxxxxxx"
                            }
                        },

                "has_geo": {
                    "@type": "GeoCoordinates",
                    "latitude": 40.4168,
                    "longitude": -3.7038
                },
                "has_contacts": {
                    "@type": "ContactPoint",
                    "name": "Support Team",
                    "telephone": "+34 912345678",
                    "email": "supportsrc@example.com",
                    "adress":"xxxxxxxxxxx",
                    "faxNumber":"+34 958172013",
                    "URL":"iaa.csic.es"
                }
            },
            "has_PI": {
                "@type": "Person",
                "name": "Julián Garrido",
                "email": "jgarrido@example.com",
                "telephone":"xxxxxxxxxxx",
                "worksIn": {
                    "@type": "Organization",
                    "name": "iaa_csic"
                    }
            },
            "isComposedBy": {
                "@type": "Computing",
                "hasCPU": {
                    "@type": "CPU",
                    "cores": 16,
                    "clock":{
                        "@type":"quantityValue",
                        "unit":"GHz",
                        "value":3.0,
                        
                    } 
                },
                "hasMemory": {
                    "@type": "QuantityValue",
                    "unit": "http://qudt.org/vocab/unit/Gigabyte",
                    "value":64
                    
                   
                },
                "hasDisk": {
                        "@type": "Disk",
                        "size":{
                            "@type":"QuantityValue",
                            "unit": "http://qudt.org/vocab/unit/Terabyte",
                            "value":2
                          
                        },
                        "type": "HDD"
                }
            }
        }
    ]
}

# Serialize the dictionary to a JSON string
json_ld_string = json.dumps(spsrcnode, indent=2)

# Print the JSON-LD string
print(json_ld_string)

# (Optional) Write the JSON-LD string to a file
with open('json_codeone.jsonld', 'w') as jsonld_file:
    jsonld_file.write(json_ld_string)
