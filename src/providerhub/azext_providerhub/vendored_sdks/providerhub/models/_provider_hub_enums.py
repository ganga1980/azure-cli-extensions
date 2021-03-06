# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class ExtensionCategory(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOT_SPECIFIED = "NotSpecified"
    RESOURCE_CREATION_VALIDATE = "ResourceCreationValidate"
    RESOURCE_CREATION_BEGIN = "ResourceCreationBegin"
    RESOURCE_CREATION_COMPLETED = "ResourceCreationCompleted"
    RESOURCE_READ_VALIDATE = "ResourceReadValidate"
    RESOURCE_READ_BEGIN = "ResourceReadBegin"
    RESOURCE_PATCH_VALIDATE = "ResourcePatchValidate"
    RESOURCE_PATCH_COMPLETED = "ResourcePatchCompleted"
    RESOURCE_DELETION_VALIDATE = "ResourceDeletionValidate"
    RESOURCE_DELETION_BEGIN = "ResourceDeletionBegin"
    RESOURCE_DELETION_COMPLETED = "ResourceDeletionCompleted"
    RESOURCE_POST_ACTION = "ResourcePostAction"
    SUBSCRIPTION_LIFECYCLE_NOTIFICATION = "SubscriptionLifecycleNotification"
    RESOURCE_PATCH_BEGIN = "ResourcePatchBegin"
    RESOURCE_MOVE_BEGIN = "ResourceMoveBegin"
    RESOURCE_MOVE_COMPLETED = "ResourceMoveCompleted"

class ExtensionOptionType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOT_SPECIFIED = "NotSpecified"
    DO_NOT_MERGE_EXISTING_READ_ONLY_AND_SECRET_PROPERTIES = "DoNotMergeExistingReadOnlyAndSecretProperties"
    INCLUDE_INTERNAL_METADATA = "IncludeInternalMetadata"

class FeaturesPolicy(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ANY = "Any"
    ALL = "All"

class IdentityManagementTypes(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOT_SPECIFIED = "NotSpecified"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    ACTOR = "Actor"
    DELEGATED_RESOURCE_IDENTITY = "DelegatedResourceIdentity"

class LinkedAction(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOT_SPECIFIED = "NotSpecified"
    BLOCKED = "Blocked"
    VALIDATE = "Validate"
    ENABLED = "Enabled"

class LinkedOperation(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "None"
    CROSS_RESOURCE_GROUP_RESOURCE_MOVE = "CrossResourceGroupResourceMove"
    CROSS_SUBSCRIPTION_RESOURCE_MOVE = "CrossSubscriptionResourceMove"

class LoggingDetails(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "None"
    BODY = "Body"

class LoggingDirections(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "None"
    REQUEST = "Request"
    RESPONSE = "Response"

class ManifestResourceDeletionPolicy(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOT_SPECIFIED = "NotSpecified"
    CASCADE = "Cascade"
    FORCE = "Force"

class MessageScope(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOT_SPECIFIED = "NotSpecified"
    REGISTERED_SUBSCRIPTIONS = "RegisteredSubscriptions"

class NotificationMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOT_SPECIFIED = "NotSpecified"
    EVENT_HUB = "EventHub"
    WEB_HOOK = "WebHook"

class OperationsDefinitionActionType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOT_SPECIFIED = "NotSpecified"
    INTERNAL = "Internal"

class OperationsDefinitionOrigin(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOT_SPECIFIED = "NotSpecified"
    USER = "User"
    SYSTEM = "System"

class OptInHeaderType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOT_SPECIFIED = "NotSpecified"
    SIGNED_USER_TOKEN = "SignedUserToken"
    CLIENT_GROUP_MEMBERSHIP = "ClientGroupMembership"
    SIGNED_AUXILIARY_TOKENS = "SignedAuxiliaryTokens"
    UNBOUNDED_CLIENT_GROUP_MEMBERSHIP = "UnboundedClientGroupMembership"

class PreflightOption(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "None"
    CONTINUE_DEPLOYMENT_ON_FAILURE = "ContinueDeploymentOnFailure"
    DEFAULT_VALIDATION_ONLY = "DefaultValidationOnly"

class ProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOT_SPECIFIED = "NotSpecified"
    ACCEPTED = "Accepted"
    RUNNING = "Running"
    CREATING = "Creating"
    CREATED = "Created"
    DELETING = "Deleting"
    DELETED = "Deleted"
    CANCELED = "Canceled"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    MOVING_RESOURCES = "MovingResources"
    TRANSIENT_FAILURE = "TransientFailure"
    ROLLOUT_IN_PROGRESS = "RolloutInProgress"

class Regionality(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOT_SPECIFIED = "NotSpecified"
    GLOBAL_ENUM = "Global"
    REGIONAL = "Regional"

class ResourceDeletionPolicy(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOT_SPECIFIED = "NotSpecified"
    CASCADE_DELETE_ALL = "CascadeDeleteAll"
    CASCADE_DELETE_PROXY_ONLY_CHILDREN = "CascadeDeleteProxyOnlyChildren"

class ResourceProviderCapabilitiesEffect(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOT_SPECIFIED = "NotSpecified"
    ALLOW = "Allow"
    DISALLOW = "Disallow"

class ResourceProviderManagementResourceAccessPolicy(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOT_SPECIFIED = "NotSpecified"
    ACIS_READ_ALLOWED = "AcisReadAllowed"
    ACIS_ACTION_ALLOWED = "AcisActionAllowed"

class ResourceProviderType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOT_SPECIFIED = "NotSpecified"
    INTERNAL = "Internal"
    EXTERNAL = "External"
    HIDDEN = "Hidden"
    REGISTRATION_FREE = "RegistrationFree"
    LEGACY_REGISTRATION_REQUIRED = "LegacyRegistrationRequired"
    TENANT_ONLY = "TenantOnly"
    AUTHORIZATION_FREE = "AuthorizationFree"

class ResourceTypeMarketplaceType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOT_SPECIFIED = "NotSpecified"
    ADD_ON = "AddOn"
    BYPASS = "Bypass"
    STORE = "Store"

class ResourceTypeRegistrationPropertiesMarketplaceType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOT_SPECIFIED = "NotSpecified"
    ADD_ON = "AddOn"
    BYPASS = "Bypass"
    STORE = "Store"

class ResourceValidation(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOT_SPECIFIED = "NotSpecified"
    RESERVED_WORDS = "ReservedWords"
    PROFANE_WORDS = "ProfaneWords"

class RoutingType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    DEFAULT = "Default"
    PROXY_ONLY = "ProxyOnly"
    HOST_BASED = "HostBased"
    EXTENSION = "Extension"
    TENANT = "Tenant"
    FANOUT = "Fanout"
    LOCATION_BASED = "LocationBased"
    FAILOVER = "Failover"
    CASCADE_EXTENSION = "CascadeExtension"

class SkuLocationInfoType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOT_SPECIFIED = "NotSpecified"
    EDGE_ZONE = "EdgeZone"
    ARC_ZONE = "ArcZone"

class SkuScaleType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "None"
    MANUAL = "Manual"
    AUTOMATIC = "Automatic"

class SubscriptionNotificationOperation(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOT_DEFINED = "NotDefined"
    DELETE_ALL_RESOURCES = "DeleteAllResources"
    SOFT_DELETE_ALL_RESOURCES = "SoftDeleteAllResources"
    NO_OP = "NoOp"
    BILLING_CANCELLATION = "BillingCancellation"
    UNDO_SOFT_DELETE = "UndoSoftDelete"

class SubscriptionReregistrationResult(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOT_APPLICABLE = "NotApplicable"
    CONDITIONAL_UPDATE = "ConditionalUpdate"
    FORCED_UPDATE = "ForcedUpdate"
    FAILED = "Failed"

class SubscriptionState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOT_DEFINED = "NotDefined"
    ENABLED = "Enabled"
    WARNED = "Warned"
    PAST_DUE = "PastDue"
    DISABLED = "Disabled"
    DELETED = "Deleted"

class SubscriptionTransitioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    REGISTERED = "Registered"
    UNREGISTERED = "Unregistered"
    WARNED = "Warned"
    SUSPENDED = "Suspended"
    DELETED = "Deleted"
    WARNED_TO_REGISTERED = "WarnedToRegistered"
    WARNED_TO_SUSPENDED = "WarnedToSuspended"
    WARNED_TO_DELETED = "WarnedToDeleted"
    WARNED_TO_UNREGISTERED = "WarnedToUnregistered"
    SUSPENDED_TO_REGISTERED = "SuspendedToRegistered"
    SUSPENDED_TO_WARNED = "SuspendedToWarned"
    SUSPENDED_TO_DELETED = "SuspendedToDeleted"
    SUSPENDED_TO_UNREGISTERED = "SuspendedToUnregistered"

class TemplateDeploymentCapabilities(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    DEFAULT = "Default"
    PREFLIGHT = "Preflight"

class TemplateDeploymentPreflightOptions(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "None"
    VALIDATION_REQUESTS = "ValidationRequests"
    DEPLOYMENT_REQUESTS = "DeploymentRequests"
    TEST_ONLY = "TestOnly"
    REGISTERED_ONLY = "RegisteredOnly"

class ThrottlingMetricType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOT_SPECIFIED = "NotSpecified"
    NUMBER_OF_REQUESTS = "NumberOfRequests"
    NUMBER_OF_RESOURCES = "NumberOfResources"

class TrafficRegionCategory(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOT_SPECIFIED = "NotSpecified"
    CANARY = "Canary"
    LOW_TRAFFIC = "LowTraffic"
    MEDIUM_TRAFFIC = "MediumTraffic"
    HIGH_TRAFFIC = "HighTraffic"
    NONE = "None"
    REST_OF_THE_WORLD_GROUP_ONE = "RestOfTheWorldGroupOne"
    REST_OF_THE_WORLD_GROUP_TWO = "RestOfTheWorldGroupTwo"
