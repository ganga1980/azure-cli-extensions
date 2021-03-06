# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from .vendored_sdks.azure_mgmt_webpubsub.models import (
    RegenerateKeyParameters
)


def webpubsub_key_list(client, webpubsub_name, resource_group_name):
    return client.list_keys(resource_group_name, webpubsub_name)


def webpubsub_key_regenerate(client, webpubsub_name, resource_group_name, key_type):
    poller = client.begin_regenerate_key(resource_group_name, webpubsub_name, RegenerateKeyParameters(key_type=key_type))
    poller.wait()
    return webpubsub_key_list(client, webpubsub_name, resource_group_name)
