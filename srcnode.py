import json

spsrcnode ={
      "@context":{
        "@vocab":"http://schema.org/",
        "SRCNet":"http://example.org/SRCNet",
        "SRCNode":"http://example.org/SRCNode",
        "Place":"https://schema.org/Place",
        "Country":"https://schema.org/Country",
        "Region":"https://schema.org/Region",
        "Geo":"https://schema.org/Geo",
        "ContactPoint":"https://schema.org/ContactPoint",
        "Person":"https://schema.org/Person",
        "ResearchCentre":"https://schema.org/ResearchCentre",
        "Node":"http://example.org/Node",
        "Storage":"http://example.org/Storage",
        "DataType":"http://example.org/datatype",
        "DataCapabilities":"http://example.org/datacapabilities",
        "Cost":"http://example.org/cost",
        "PowerConsumption":"http://example.org/PowerConsumption",
        "Computing":"http://example.org/Computing",
        "CPU":"http://example.org/CPU",
        "RAM":"http://example.org/RAM",
        "Disck":"http://example.org/Disk",
        "Architecture":"http://example.org/Architecture",
        "Network":"http://example.org/Network",
        "Bandwidth":"http://example.org/Bandwidth",
        "AreaCoverage":"http://example.org/AreaCoverage",
        "Latency":"http://example.org/Latency",
        "CostsOfNetwork":"http://example.org/CostsOfNetwork",
        "SecurityPolicies":"http://example.org/SecurityPolicies",
        "Services":"http://example.org/Services",
        
    },

    "@type":"SRCNet",
    "isComposedBy":{
        "@type": "SRCNode",
        "name": "spSRC",
        "locatedIn":{
            "@type":"Place",
            "@id":"http://schema.org/Place/granada",
            "name":"Granada",
            "isInAcountry":{
                "@type": "Country",
                "@id": "http://schema.org/addressCountry/spain",
                "name": "Spain",
                "Locality":"Granada",
                "addressLocality":{
                    "type":"@postalAddress",
                    "address":"xxxxxxxxxxxxxxxx"
                    }
            },

            "isInAregion":{
                "@type":"region",
                "@id":"https://schema.org/DefinedRegion",
                "name":"andalucia",
                "postalCode":"",
                "addressRegion":""
                },

            "has_geo":{
                "@type": "GeoCoordinates",                          
                "@id":"http://schema.org/GeoCoordinates",
                "latitude":10.0000,
                "longitude": -1.0000
              },
            
            "has_contacts": {
                "@type": "ContactPoint",
                "@id":"http://schema.org/contactPoint/amigaGroup",
                "name": "spsrcTeam",
                "telephone": "+34 958121311",
                "email": "infospsrc@iaa.csic.es",
                "adress":"Gta de la Astronomía, s/n, Genil, 18008 ",
                "faxNumber":"+34 958814530",
                "URL":"iaa.csic.es"
            }
            
        },
        "has_PI":{
            "@type": "Person",
            "@id":"http://schema.org/Person/manu_parra",
            "name": "Manu Parra",
            "telephone": "XXXXXXXXXXXXX",
            "email": "xxxxxxxxxxxxxxx",
            "worksIn": {
                "@type": "Organization",
                "@id": "http://example.com/organization/iaa_csic",
                "name": "iaa_csic"
                },
        },
    "@type":"srcnode",
        "isComposedBy": {
            "@type":"Nodes",
            "hasComputing":{
                "@type": "Computing",
                "hasCPU":{
                    "@type": "CPU",
                    "cores":"",
                    "integratedGraphics":"",
                    "cacheMem":"",
                    "clock" : "1.4 GHz"
                },
                "hasMem":{
                    "@type":"Mem",
                    "size": "1TB",
                    "latency":"",
                    "speed":"",
                    "voltage":""
                },
                "hasDisk":{
                    "@type":"Disk",
                    "speed":"",
                    "size":"",
                    "interface":"",
                },
                "hasArch":{
                    "@type":"arch"
                    "dataPath",
                    "controlUnit":"",
                    "energyEfficiency":"",
                    "mem":"",
                },
                "hasPowerconsumption":{
                    "@type":"powerconsumption",
                    "idlePowerconsumption":" integer# Watts",
                    "activePowerConsumption":"integer#Watts",
                    "averagePower": "integer# Watts",
                    "powerSupplyEfficiency":"",
                    "temperatureAndCooling":"",
                    "electricityCost": "$0.10/kWh",
                    "annualEnergyConsumption":{
                        "@type": "QuantitativeValue",
                        "value": 2482,
                        "unitText": "kWh"
                        },
                    },

            },
            "has_storage":{
                "@type":"storage",
                "datatype":"",
                "has_data_cap":{
                    "capacityTB":"",
                    "access_time":{
                        "randon_access":"",
                        "cache_effects":"",
                        "transfer_time":"",
                        "seek_time":"",
                        "queue_depth":""
                    },
                    "data_transfer_rate":{
                        "write_rate":"",
                        "read_rate":"",
                    },
                },
            
                "has_cost":{
                    "@type":"cost",
                    "capacity_costs":"",
                    "data_transfer_costs":"",
                    "total_cost_of_ownwership":"",
                    "opportunity_costs":"",
                    },
                },

            

            "has_network":{
                "@type":"network",
                "has_bandwidth":{
                    "cost":"",
                    "mensurementUnits":"",
                    "throughput":"",
                    "network_congestion":"",
                    "simetry":""
                },
                "has_latency":{
                    "type":"",
                    "performance":"",
                    "jitter":"",
                    "distance":"",
                    "environmentalFactors":""
                },
                "has_area_covarage":{
                    "DeploymentDensity":"",
                    "covarageRadius":"",
                    "frequency-band":"",
                    "cost_of_expansion":"",
                    "signal_strength":""
                },
                "has_cost":{
                    "mantainenceCosts":"",
                    "OperationalCosts":"",
                    "equipmentCosts":"",
                    "licensingFees":"",
                    "CostOfdowntime":"",
                    "trainingCosts":""
                    },
                },
        
            
            "has_securityPolicies":{
                "@type":"securityPolicies",
                    "has_encryption":"",
                    "has_authorization":"",
                    "has_access_control":"",
                    "has_authentication":"",
                    "has_confidentiality":""
                    },

            "has_services":{
                "@type":"services",
                    "has_service1":"",
                    "has_service2":"",
                    "has_service3":"",
                    "has_serviceN":""
            },
         },
     },


 "@graph": [           

{

"@type":"SRCNet",
    "isComposedBy":{
        "@type": "SRCNode",
        "name": "ukSRC",
        "locatedIn":{
            "@type":"Place",
            "@id":"http://schema.org/Place/granada",
            "name":"Granada",
            "isInAcountry":{
                "@type": "Country",
                "@id": "http://schema.org/addressCountry/spain",
                "name": "Spain",
                "Locality":"Granada",
                "addressLocality":{
                    "type":"@postalAddress",
                    "address":"xxxxxxxxxxxxxxxx"
                    }
            },

            "isInAregion":{
                "@type":"region",
                "@id":"https://schema.org/DefinedRegion",
                "name":"andalucia",
                "postalCode":"",
                "addressRegion":""
                },

            "has_geo":{
                "@type": "GeoCoordinates",                          
                "@id":"http://schema.org/GeoCoordinates",
                "latitude":10.0000,
                "longitude": -1.0000
              },
            
            "has_contacts": {
                "@type": "ContactPoint",
                "@id":"http://schema.org/contactPoint/amigaGroup",
                "name": "spsrcTeam",
                "telephone": "+34 958121311",
                "email": "infospsrc@iaa.csic.es",
                "adress":"Gta de la Astronomía, s/n, Genil, 18008 ",
                "faxNumber":"+34 958814530",
                "URL":"iaa.csic.es"
            }
            
        },
        "has_PI":{
            "@type": "Person",
            "@id":"http://schema.org/Person/manu_parra",
            "name": "Manu Parra",
            "telephone": "XXXXXXXXXXXXX",
            "email": "xxxxxxxxxxxxxxx",
            "worksIn": {
                "@type": "Organization",
                "@id": "http://example.com/organization/iaa_csic",
                "name": "iaa_csic"
                },
        },
    "@type":"srcnode",
        "isComposedBy": {
            "@type":"Nodes",
            "hasComputing":{
                "@type": "Computing",
                "hasCPU":{
                    "@type": "CPU",
                    "cores":"",
                    "integratedGraphics":"",
                    "cacheMem":"",
                    "clock" : "1.4 GHz"
                },
                "hasMem":{
                    "@type":"Mem",
                    "size": "1TB",
                    "latency":"",
                    "speed":"",
                    "voltage":""
                },
                "hasDisk":{
                    "@type":"Disk",
                    "speed":"",
                    "size":"",
                    "interface":"",
                },
                "hasArch":{
                    "@type":"arch"
                    "dataPath",
                    "controlUnit":"",
                    "energyEfficiency":"",
                    "mem":"",
                },
                "hasPowerconsumption":{
                    "@type":"powerconsumption",
                    "idlePowerconsumption":" integer# Watts",
                    "activePowerConsumption":"integer#Watts",
                    "averagePower": "integer# Watts",
                    "powerSupplyEfficiency":"",
                    "temperatureAndCooling":"",
                    "electricityCost": "$0.10/kWh",
                    "annualEnergyConsumption":{
                        "@type": "QuantitativeValue",
                        "value": 2482,
                        "unitText": "kWh"
                        },
                    },

            },
            "has_storage":{
                "@type":"storage",
                "datatype":"",
                "has_data_cap":{
                    "capacityTB":"",
                    "access_time":{
                        "randon_access":"",
                        "cache_effects":"",
                        "transfer_time":"",
                        "seek_time":"",
                        "queue_depth":""
                    },
                    "data_transfer_rate":{
                        "write_rate":"",
                        "read_rate":"",
                    },
                },
            
                "has_cost":{
                    "@type":"cost",
                    "capacity_costs":"",
                    "data_transfer_costs":"",
                    "total_cost_of_ownwership":"",
                    "opportunity_costs":"",
                    },
                },

            

            "has_network":{
                "@type":"network",
                "has_bandwidth":{
                    "cost":"",
                    "mensurementUnits":"",
                    "throughput":"",
                    "network_congestion":"",
                    "simetry":""
                },
                "has_latency":{
                    "type":"",
                    "performance":"",
                    "jitter":"",
                    "distance":"",
                    "environmentalFactors":""
                },
                "has_area_covarage":{
                    "DeploymentDensity":"",
                    "covarageRadius":"",
                    "frequency-band":"",
                    "cost_of_expansion":"",
                    "signal_strength":""
                },
                "has_cost":{
                    "mantainenceCosts":"",
                    "OperationalCosts":"",
                    "equipmentCosts":"",
                    "licensingFees":"",
                    "CostOfdowntime":"",
                    "trainingCosts":""
                    },
                },
        
            
            "has_securityPolicies":{
                "@type":"securityPolicies",
                    "has_encryption":"",
                    "has_authorization":"",
                    "has_access_control":"",
                    "has_authentication":"",
                    "has_confidentiality":""
                    },

            "has_services":{
                "@type":"services",
                    "has_service1":"",
                    "has_service2":"",
                    "has_service3":"",
                    "has_serviceN":""
            },
         },
     }
}
 ]
}



# Serialize the dictionary to a JSON string
json_ld_string = json.dumps(spsrcnode, indent=2)

# Print the JSON-LD string
print(json_ld_string)

# (Optional) Write the JSON-LD string to a file
with open('json_code.jsonld', 'w') as jsonld_file:
    jsonld_file.write(json_ld_string)
  
