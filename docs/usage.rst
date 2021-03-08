=====
Usage
=====


Post Data to Triple Store::

    import os
    from acdh_arche_pyutils.client import ArcheToTripleStore

    BGUSER = os.environ.get('BGUSER')
    BGPW = os.environ.get('BGPW')

    triple_store = "https://arche-sparql.acdh-dev.oeaw.ac.at/sparql"
    arche_endpoint = "https://arche-dev.acdh-dev.oeaw.ac.at/api/"
    client = ArcheToTripleStore(
        triple_store, arche_endpoint=arche_endpoint,
        user=BGUSER, pw=BGPW 
    )
    top_cols = client.post_all_resources()

Write RDF-Graph of an ARCHE-URI to file::

    from acdh_arche_pyutils.client import ArcheApiClient

    endpoint = "https://arche-dev.acdh-dev.oeaw.ac.at/api/"
    client = ArcheApiClient(endpoint)
    to_file = client.write_resource_to_file("https://arche-dev.acdh-dev.oeaw.ac.at/api/123")
    
    # returns the name of the saved file, e.g. `123.ttl`


Fetch all TopCollection URIs and Labels::

    from acdh_arche_pyutils.client import ArcheApiClient

    endpoint = "https://arche-dev.acdh-dev.oeaw.ac.at/api/"
    client = ArcheApiClient(endpoint)
    top_cols = client.top_col_ids()

    # returns something like:
    [
        (
            'https://arche-dev.acdh-dev.oeaw.ac.at/api/18243',
            'HistoGIS'
        ),
        (
            'https://arche-dev.acdh-dev.oeaw.ac.at/api/18293',
            'Downed Allied Air Crew Database Austria'
        ),
        (
            'https://arche-dev.acdh-dev.oeaw.ac.at/api/18270',
            'Die Korrespondenz von Leo von Thun-Hohenstein'
        )
    ]

Retrieve the API-Configuration::

    from acdh_arche_pyutils.client import ArcheApiClient

    endpoint = "https://arche-dev.acdh-dev.oeaw.ac.at/api/"
    client = ArcheApiClient(endpoint)
    client.description
    # returns something like:
    {
        'rest':
            {
                'headers': 
                    {
                        'metadataReadMode': 'X-METADATA-READ-MODE',
                        'metadataParentProperty': 'X-PARENT-PROPERTY',
                        'metadataWriteMode': 'X-METADATA-WRITE-MODE',
                        'transactionId': 'X-TRANSACTION-ID'
                    },
                'urlBase': 'https://arche-dev.acdh-dev.oeaw.ac.at',
                'pathBase': '/api/'
            },
        'schema':
            {
                'id': 'https://vocabs.acdh.oeaw.ac.at/schema#hasIdentifier',
                'parent': 'https://vocabs.acdh.oeaw.ac.at/schema#isPartOf',
                'label': 'https://vocabs.acdh.oeaw.ac.at/schema#hasTitle',
                ...
            }
        }
    }