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

from enum import Enum


class PathSetAccessControlRecursiveMode(str, Enum):

    set = "set"
    modify = "modify"
    remove = "remove"


class PathExpiryOptions(str, Enum):

    never_expire = "NeverExpire"
    relative_to_creation = "RelativeToCreation"
    relative_to_now = "RelativeToNow"
    absolute = "Absolute"


class ListBlobsIncludeItem(str, Enum):

    copy = "copy"
    deleted = "deleted"
    metadata = "metadata"
    snapshots = "snapshots"
    uncommittedblobs = "uncommittedblobs"
    versions = "versions"
    tags = "tags"


class ListBlobsShowOnly(str, Enum):

    deleted = "deleted"


class PathResourceType(str, Enum):

    directory = "directory"
    file = "file"


class PathRenameMode(str, Enum):

    legacy = "legacy"
    posix = "posix"


class PathUpdateAction(str, Enum):

    append = "append"
    flush = "flush"
    set_properties = "setProperties"
    set_access_control = "setAccessControl"
    set_access_control_recursive = "setAccessControlRecursive"


class PathLeaseAction(str, Enum):

    acquire = "acquire"
    break_enum = "break"
    change = "change"
    renew = "renew"
    release = "release"


class PathGetPropertiesAction(str, Enum):

    get_access_control = "getAccessControl"
    get_status = "getStatus"
