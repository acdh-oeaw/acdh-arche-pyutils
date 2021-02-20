import requests
import yaml


def camel_to_snake(s):
    """ converts CamelCase string to camel_case\
        taken from https://stackoverflow.com/a/44969381

        :param s: some string
        :type s: str:

        :return: a camel_case string
        :rtype: str:
    """
    no_camel = ''.join(['_'+c.lower() if c.isupper() else c for c in s]).lstrip('_')
    return no_camel.replace('__', '_')


class ArcheApiClient():
    """Main Class to interact with ARCHE-API """

    def __init__(
        self,
        arche_endpoint
    ):
        """ initializes the class
        :param arche_endpoint: The ARCHE endpoint e.g. `https://arche-dev.acdh-dev.oeaw.ac.at/api/`
        :type endpoint: str

        :return: A ArcheApiClient instance
        :rtype: class:`achd_arch_pyutils.client.ArcheApiClient`
        """
        super().__init__()
        self.endpoint = arche_endpoint
        self.describe_url = f"{arche_endpoint}describe"
        self.info = requests.get(self.describe_url)
        self.description = yaml.load(self.info.text, Loader=yaml.FullLoader)
