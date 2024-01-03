
from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'c2064645' # Must be replaced by your <storage_account_name>
    account_key = 'vuj4vqZysdMrrVMlPo5B51TkbPR3Tw5+Fif/NUm9hower41n0t+PJqCuhQefkH4mPPTBHOeYS86D+AStBQ9iHQ==' 
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'c2064645' 
    account_key = 'vuj4vqZysdMrrVMlPo5B51TkbPR3Tw5+Fif/NUm9hower41n0t+PJqCuhQefkH4mPPTBHOeYS86D+AStBQ9iHQ==' 
    azure_container = 'static'
    expiration_secs = None