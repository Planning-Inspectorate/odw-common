from odw_common.private_endpoint.private_endpoint_manager import PrivateEndpointManager


class KeyVaultPrivateEndpointManager(PrivateEndpointManager):
    def get_resource_type(self):
        return "Microsoft.Keyvault/vaults"
