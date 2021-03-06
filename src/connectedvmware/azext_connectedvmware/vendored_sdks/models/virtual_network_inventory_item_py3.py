# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .inventory_item_properties_py3 import InventoryItemProperties


class VirtualNetworkInventoryItem(InventoryItemProperties):
    """The Virtual network inventory item.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param managed_resource_id: Gets or sets the tracked resource id
     corresponding to the inventory resource.
    :type managed_resource_id: str
    :param mo_ref_id: Gets or sets the MoRef (Managed Object Reference) ID for
     the inventory item.
    :type mo_ref_id: str
    :param mo_name: Gets or sets the vCenter Managed Object name for the
     inventory item.
    :type mo_name: str
    :ivar provisioning_state: Gets or sets the provisioning state.
    :vartype provisioning_state: str
    :param inventory_type: Required. Constant filled by server.
    :type inventory_type: str
    """

    _validation = {
        'provisioning_state': {'readonly': True},
        'inventory_type': {'required': True},
    }

    _attribute_map = {
        'managed_resource_id': {'key': 'managedResourceId', 'type': 'str'},
        'mo_ref_id': {'key': 'moRefId', 'type': 'str'},
        'mo_name': {'key': 'moName', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'inventory_type': {'key': 'inventoryType', 'type': 'str'},
    }

    def __init__(self, *, managed_resource_id: str=None, mo_ref_id: str=None, mo_name: str=None, **kwargs) -> None:
        super(VirtualNetworkInventoryItem, self).__init__(managed_resource_id=managed_resource_id, mo_ref_id=mo_ref_id, mo_name=mo_name, **kwargs)
        self.inventory_type = 'VirtualNetwork'
