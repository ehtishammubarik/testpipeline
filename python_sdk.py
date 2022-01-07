from azureml.core import Workspace, Datastore, Dataset
from azureml.data.datapath import DataPath
from azureml.core.authentication import ServicePrincipalAuthentication

#cli_auth = AzureCliAuthentication()
svc_pr_password = "F.o7Q~XZfiPD45tisoQy2FF.Ohdl2U51xboXL"

svc_pr = ServicePrincipalAuthentication(
    tenant_id="8dfbdd82-ec8c-45dc-9f91-7e0b7441ca25",
    service_principal_id="36cfa292-9dd4-4789-a37b-09f7d5a0b7fb",
    service_principal_password=svc_pr_password)
ws = Workspace(subscription_id="3c338a15-cc11-4b45-8f5b-e0c10f624060",
        resource_group="eastUS",
        workspace_name="ustest",
        auth=svc_pr)
datastore = Datastore.get(ws, 'workspaceblobstore')
ds = Dataset.File.upload_directory(src_dir='./zipfile/',
           target=DataPath(datastore,  'UI'),
           show_progress=True)
ds = ds.register(workspace = ws, name = 'test2_secondfile',
                description = 'new upload zip from pipeline ', create_new_version = True)
