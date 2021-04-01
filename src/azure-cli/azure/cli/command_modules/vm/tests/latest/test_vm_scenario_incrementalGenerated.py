# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer
from .example_steps import step_cloud_service_create
from .example_steps import step_cloud_service_create2
from .example_steps import step_cloud_service_create3
from .example_steps import step_cloud_service_create4
from .example_steps import step_cloud_service_show_instance_view
from .example_steps import step_cloud_service_show
from .example_steps import step_cloud_service_list
from .example_steps import step_cloud_service_list_all
from .example_steps import step_cloud_service_delete_instance
from .example_steps import step_cloud_service_restart
from .example_steps import step_cloud_service_start
from .example_steps import step_cloud_service_power_off
from .example_steps import step_cloud_service_role_instance_show
from .example_steps import step_cloud_service_role
from .example_steps import step_cloud_service_role_instance_list
from .example_steps import step_cloud_service_role_instance_reimage
from .example_steps import step_cloud_service_role_instance_restart
from .example_steps import step_cloud_service_role_show
from .example_steps import step_cloud_service_role_list
from .example_steps import step_cloud_service_update
from .example_steps import step_cloud_service_update2
from .example_steps import step_cloud_service_update3
from .example_steps import step_cloud_service_delete
from .example_steps import step_disk_access_list_private_endpoint_connection
from .example_steps import step_disk_access_show_private_link_resource
from .example_steps import step_disk_access_delete
from .example_steps import step_disk_restore_point_show
from .example_steps import step_gallery_application_create
from .example_steps import step_gallery_application_show
from .example_steps import step_gallery_application_list
from .example_steps import step_gallery_application_version_list
from .example_steps import step_gallery_application_delete
from .example_steps import step_create
from .example_steps import step_show
from .example_steps import step_install_patch
from .example_steps import step_reimage
from .example_steps import step_vm_extension_create
from .example_steps import step_vm_extension_show
from .example_steps import step_vm_extension_list
from .example_steps import step_vm_run_list
from .example_steps import step_v_ms_retrieve_boot_diagnostic_data
from .. import (
    try_manual,
    raise_if,
    calc_coverage
)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Env setup_scenario
@try_manual
def setup_scenario(test):
    pass


# Env cleanup_scenario
@try_manual
def cleanup_scenario(test):
    pass


# Testcase: Scenario
@try_manual
def call_scenario(test):
    setup_scenario(test)
    step_cloud_service_create(test, checks=[
        test.check("name", "{myCloudService}", case_sensitive=False),
        test.check("location", "westus", case_sensitive=False),
        test.check("configuration", "{{ServiceConfiguration}}", case_sensitive=False),
        test.check("networkProfile.loadBalancerConfigurations[0].name", "contosolb", case_sensitive=False),
        test.check("networkProfile.loadBalancerConfigurations[0].properties.frontendIPConfigurations[0].name",
                   "contosofe", case_sensitive=False),
        test.check("networkProfile.loadBalancerConfigurations[0].properties.frontendIPConfigurations[0].properties.publ"
                   "icIPAddress.id", "/subscriptions/{subscription_id}/resourceGroups/{rg_4}/providers/Microsoft.Networ"
                   "k/publicIPAddresses/contosopublicip", case_sensitive=False),
        test.check("packageUrl", "{{PackageUrl}}", case_sensitive=False),
        test.check("upgradeMode", "Auto", case_sensitive=False),
    ])
    step_cloud_service_create2(test, checks=[
        test.check("name", "{myCloudService}", case_sensitive=False),
        test.check("location", "westus", case_sensitive=False),
        test.check("configuration", "{{ServiceConfiguration}}", case_sensitive=False),
        test.check("networkProfile.loadBalancerConfigurations[0].name", "myLoadBalancer", case_sensitive=False),
        test.check("networkProfile.loadBalancerConfigurations[0].properties.frontendIPConfigurations[0].name", "myfe",
                   case_sensitive=False),
        test.check("networkProfile.loadBalancerConfigurations[0].properties.frontendIPConfigurations[0].properties.publ"
                   "icIPAddress.id", "/subscriptions/{subscription_id}/resourceGroups/{rg_4}/providers/Microsoft.Networ"
                   "k/publicIPAddresses/myPublicIP", case_sensitive=False),
        test.check("packageUrl", "{{PackageUrl}}", case_sensitive=False),
        test.check("roleProfile.roles[0].name", "ContosoFrontend", case_sensitive=False),
        test.check("roleProfile.roles[0].sku.name", "Standard_D1_v2", case_sensitive=False),
        test.check("roleProfile.roles[0].sku.capacity", 1),
        test.check("roleProfile.roles[0].sku.tier", "Standard", case_sensitive=False),
        test.check("upgradeMode", "Auto", case_sensitive=False),
    ])
    step_cloud_service_create3(test, checks=[
        test.check("name", "{myCloudService}", case_sensitive=False),
        test.check("location", "westus", case_sensitive=False),
        test.check("configuration", "{{ServiceConfiguration}}", case_sensitive=False),
        test.check("networkProfile.loadBalancerConfigurations[0].name", "contosolb", case_sensitive=False),
        test.check("networkProfile.loadBalancerConfigurations[0].properties.frontendIPConfigurations[0].name",
                   "contosofe", case_sensitive=False),
        test.check("networkProfile.loadBalancerConfigurations[0].properties.frontendIPConfigurations[0].properties.publ"
                   "icIPAddress.id", "/subscriptions/{subscription_id}/resourceGroups/{rg_4}/providers/Microsoft.Networ"
                   "k/publicIPAddresses/contosopublicip", case_sensitive=False),
        test.check("packageUrl", "{{PackageUrl}}", case_sensitive=False),
        test.check("roleProfile.roles[0].name", "ContosoFrontend", case_sensitive=False),
        test.check("roleProfile.roles[0].sku.name", "Standard_D1_v2", case_sensitive=False),
        test.check("roleProfile.roles[0].sku.capacity", 1),
        test.check("roleProfile.roles[0].sku.tier", "Standard", case_sensitive=False),
        test.check("upgradeMode", "Auto", case_sensitive=False),
        test.check("osProfile.secrets[0].sourceVault.id", "/subscriptions/{subscription_id}/resourceGroups/{rg_4}/provi"
                   "ders/Microsoft.KeyVault/vaults/{{keyvault-name}}", case_sensitive=False),
        test.check("osProfile.secrets[0].vaultCertificates[0].certificateUrl", "https://{{keyvault-name}}.vault.azure.n"
                   "et:443/secrets/ContosoCertificate/{{secret-id}}", case_sensitive=False),
    ])
    step_cloud_service_create4(test, checks=[
        test.check("name", "{myCloudService}", case_sensitive=False),
        test.check("location", "westus", case_sensitive=False),
        test.check("configuration", "{{ServiceConfiguration}}", case_sensitive=False),
        test.check("networkProfile.loadBalancerConfigurations[0].name", "contosolb", case_sensitive=False),
        test.check("networkProfile.loadBalancerConfigurations[0].properties.frontendIPConfigurations[0].name",
                   "contosofe", case_sensitive=False),
        test.check("networkProfile.loadBalancerConfigurations[0].properties.frontendIPConfigurations[0].properties.publ"
                   "icIPAddress.id", "/subscriptions/{subscription_id}/resourceGroups/{rg_4}/providers/Microsoft.Networ"
                   "k/publicIPAddresses/contosopublicip", case_sensitive=False),
        test.check("packageUrl", "{{PackageUrl}}", case_sensitive=False),
        test.check("roleProfile.roles[0].name", "ContosoFrontend", case_sensitive=False),
        test.check("roleProfile.roles[0].sku.name", "Standard_D1_v2", case_sensitive=False),
        test.check("roleProfile.roles[0].sku.capacity", 1),
        test.check("roleProfile.roles[0].sku.tier", "Standard", case_sensitive=False),
        test.check("upgradeMode", "Auto", case_sensitive=False),
    ])
    step_cloud_service_show_instance_view(test, checks=[])
    step_cloud_service_show(test, checks=[
        test.check("name", "{myCloudService}", case_sensitive=False),
        test.check("configuration", "{{ServiceConfiguration}}", case_sensitive=False),
        test.check("networkProfile.loadBalancerConfigurations[0].name", "contosolb", case_sensitive=False),
        test.check("networkProfile.loadBalancerConfigurations[0].properties.frontendIPConfigurations[0].name",
                   "contosofe", case_sensitive=False),
        test.check("networkProfile.loadBalancerConfigurations[0].properties.frontendIPConfigurations[0].properties.publ"
                   "icIPAddress.id", "/subscriptions/{subscription_id}/resourceGroups/{rg_4}/providers/Microsoft.Networ"
                   "k/publicIPAddresses/contosopublicip", case_sensitive=False),
        test.check("upgradeMode", "Auto", case_sensitive=False),
    ])
    step_cloud_service_list(test, checks=[
        test.check('length(@)', 1),
    ])
    step_cloud_service_list_all(test, checks=[])
    step_cloud_service_delete_instance(test, checks=[])
    step_cloud_service_restart(test, checks=[])
    step_cloud_service_start(test, checks=[])
    step_cloud_service_power_off(test, checks=[])
    step_cloud_service_role_instance_show(test, checks=[])
    step_cloud_service_role(test, checks=[])
    step_cloud_service_role_instance_list(test, checks=[])
    step_cloud_service_role_instance_reimage(test, checks=[])
    step_cloud_service_role_instance_restart(test, checks=[])
    step_cloud_service_role_show(test, checks=[])
    step_cloud_service_role_list(test, checks=[])
    step_cloud_service_update(test, checks=[])
    step_cloud_service_update2(test, checks=[])
    step_cloud_service_update3(test, checks=[])
    step_cloud_service_delete(test, checks=[])
    step_disk_access_list_private_endpoint_connection(test, checks=[])
    step_disk_access_show_private_link_resource(test, checks=[])
    step_disk_access_delete(test, checks=[])
    step_disk_restore_point_show(test, checks=[])
    step_gallery_application_create(test, checks=[
        test.check("location", "West US", case_sensitive=False),
        test.check("description", "This is the gallery application description.", case_sensitive=False),
        test.check("eula", "This is the gallery application EULA.", case_sensitive=False),
        test.check("privacyStatementUri", "myPrivacyStatementUri}}", case_sensitive=False),
        test.check("releaseNoteUri", "myReleaseNoteUri", case_sensitive=False),
        test.check("supportedOSType", "Windows", case_sensitive=False),
        test.check("name", "{myGalleryApplication}", case_sensitive=False),
    ])
    step_gallery_application_show(test, checks=[
        test.check("location", "West US", case_sensitive=False),
        test.check("description", "This is the gallery application description.", case_sensitive=False),
        test.check("eula", "This is the gallery application EULA.", case_sensitive=False),
        test.check("privacyStatementUri", "myPrivacyStatementUri}}", case_sensitive=False),
        test.check("releaseNoteUri", "myReleaseNoteUri", case_sensitive=False),
        test.check("supportedOSType", "Windows", case_sensitive=False),
        test.check("name", "{myGalleryApplication}", case_sensitive=False),
    ])
    step_gallery_application_list(test, checks=[
        test.check('length(@)', 1),
    ])
    step_gallery_application_version_list(test, checks=[])
    step_gallery_application_delete(test, checks=[])
    step_create(test, checks=[
        test.check("location", "westus", case_sensitive=False),
        test.check("publicKey", "{{ssh-rsa public key}}", case_sensitive=False),
        test.check("name", "{mySshPublicKey}", case_sensitive=False),
    ])
    step_show(test, checks=[
        test.check("location", "westus", case_sensitive=False),
        test.check("publicKey", "{{ssh-rsa public key}}", case_sensitive=False),
        test.check("name", "{mySshPublicKey}", case_sensitive=False),
    ])
    step_install_patch(test, checks=[])
    step_reimage(test, checks=[])
    step_vm_extension_create(test, checks=[])
    step_vm_extension_show(test, checks=[])
    step_vm_extension_list(test, checks=[])
    step_vm_run_list(test, checks=[])
    step_v_ms_retrieve_boot_diagnostic_data(test, checks=[])
    cleanup_scenario(test)


# Test class for Scenario
@try_manual
class VmScenarioTest(ScenarioTest):
    def __init__(self, *args, **kwargs):
        super(VmScenarioTest, self).__init__(*args, **kwargs)
        self.kwargs.update({
            'subscription_id': self.get_subscription_id()
        })

        self.kwargs.update({
            'mySshPublicKey': 'mySshPublicKeyName',
            'myDiskAccess': 'myDiskAccess',
            'myDiskRestorePoint': 'TestDisk45ceb03433006d1baee0_b70cd924-3362-4a80-93c2-9415eaa12745',
            'myGalleryApplication': 'myGalleryApplicationName',
            'myCloudService': '{cs-name}',
        })

    @ResourceGroupPreparer(name_prefix='clitestvm_ConstosoRG'[:7], key='rg_4', parameter_name='rg_4')
    @ResourceGroupPreparer(name_prefix='clitestvm_myResourceGroup'[:7], key='rg', parameter_name='rg')
    @ResourceGroupPreparer(name_prefix='clitestvm_myResourceGroupName'[:7], key='rg_2', parameter_name='rg_2')
    @ResourceGroupPreparer(name_prefix='clitestvm_ResourceGroup'[:7], key='rg_3', parameter_name='rg_3')
    def test_vm_Scenario(self, rg_4, rg, rg_2, rg_3):
        call_scenario(self)
        calc_coverage(__file__)
        raise_if()
