"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.struct_pb2
import google.protobuf.wrappers_pb2
import protos.base_pb2
import protos.playbooks.playbook_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _WorkflowExecutionStatusType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _WorkflowExecutionStatusTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_WorkflowExecutionStatusType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNKNOWN_WORKFLOW_STATUS: _WorkflowExecutionStatusType.ValueType  # 0
    WORKFLOW_SCHEDULED: _WorkflowExecutionStatusType.ValueType  # 1
    WORKFLOW_RUNNING: _WorkflowExecutionStatusType.ValueType  # 2
    WORKFLOW_FINISHED: _WorkflowExecutionStatusType.ValueType  # 3
    WORKFLOW_FAILED: _WorkflowExecutionStatusType.ValueType  # 4
    WORKFLOW_CANCELLED: _WorkflowExecutionStatusType.ValueType  # 5

class WorkflowExecutionStatusType(_WorkflowExecutionStatusType, metaclass=_WorkflowExecutionStatusTypeEnumTypeWrapper): ...

UNKNOWN_WORKFLOW_STATUS: WorkflowExecutionStatusType.ValueType  # 0
WORKFLOW_SCHEDULED: WorkflowExecutionStatusType.ValueType  # 1
WORKFLOW_RUNNING: WorkflowExecutionStatusType.ValueType  # 2
WORKFLOW_FINISHED: WorkflowExecutionStatusType.ValueType  # 3
WORKFLOW_FAILED: WorkflowExecutionStatusType.ValueType  # 4
WORKFLOW_CANCELLED: WorkflowExecutionStatusType.ValueType  # 5
global___WorkflowExecutionStatusType = WorkflowExecutionStatusType

@typing_extensions.final
class WorkflowOneOffSchedule(google.protobuf.message.Message):
    """/////////////////// Workflow Scheduling /////////////////////"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___WorkflowOneOffSchedule = WorkflowOneOffSchedule

@typing_extensions.final
class WorkflowPeriodicSchedule(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DURATION_IN_SECONDS_FIELD_NUMBER: builtins.int
    INTERVAL_FIELD_NUMBER: builtins.int
    CRON_FIELD_NUMBER: builtins.int
    @property
    def duration_in_seconds(self) -> google.protobuf.wrappers_pb2.UInt64Value: ...
    @property
    def interval(self) -> google.protobuf.wrappers_pb2.UInt64Value: ...
    @property
    def cron(self) -> protos.base_pb2.TaskCronRule: ...
    def __init__(
        self,
        *,
        duration_in_seconds: google.protobuf.wrappers_pb2.UInt64Value | None = ...,
        interval: google.protobuf.wrappers_pb2.UInt64Value | None = ...,
        cron: protos.base_pb2.TaskCronRule | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["cron", b"cron", "duration_in_seconds", b"duration_in_seconds", "interval", b"interval"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cron", b"cron", "duration_in_seconds", b"duration_in_seconds", "interval", b"interval"]) -> None: ...

global___WorkflowPeriodicSchedule = WorkflowPeriodicSchedule

@typing_extensions.final
class WorkflowEntryPointApiConfig(google.protobuf.message.Message):
    """/////////////////// Workflow Entry Points Configurations /////////////////////"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___WorkflowEntryPointApiConfig = WorkflowEntryPointApiConfig

@typing_extensions.final
class WorkflowEntryPointSlackChannelAlertConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SLACK_CHANNEL_ID_FIELD_NUMBER: builtins.int
    SLACK_CHANNEL_NAME_FIELD_NUMBER: builtins.int
    SLACK_ALERT_TYPE_FIELD_NUMBER: builtins.int
    SLACK_ALERT_FILTER_STRING_FIELD_NUMBER: builtins.int
    @property
    def slack_channel_id(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def slack_channel_name(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def slack_alert_type(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def slack_alert_filter_string(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    def __init__(
        self,
        *,
        slack_channel_id: google.protobuf.wrappers_pb2.StringValue | None = ...,
        slack_channel_name: google.protobuf.wrappers_pb2.StringValue | None = ...,
        slack_alert_type: google.protobuf.wrappers_pb2.StringValue | None = ...,
        slack_alert_filter_string: google.protobuf.wrappers_pb2.StringValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["slack_alert_filter_string", b"slack_alert_filter_string", "slack_alert_type", b"slack_alert_type", "slack_channel_id", b"slack_channel_id", "slack_channel_name", b"slack_channel_name"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["slack_alert_filter_string", b"slack_alert_filter_string", "slack_alert_type", b"slack_alert_type", "slack_channel_id", b"slack_channel_id", "slack_channel_name", b"slack_channel_name"]) -> None: ...

global___WorkflowEntryPointSlackChannelAlertConfig = WorkflowEntryPointSlackChannelAlertConfig

@typing_extensions.final
class WorkflowEntryPointAlertConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _AlertType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _AlertTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[WorkflowEntryPointAlertConfig._AlertType.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN: WorkflowEntryPointAlertConfig._AlertType.ValueType  # 0
        SLACK_CHANNEL_ALERT: WorkflowEntryPointAlertConfig._AlertType.ValueType  # 1

    class AlertType(_AlertType, metaclass=_AlertTypeEnumTypeWrapper): ...
    UNKNOWN: WorkflowEntryPointAlertConfig.AlertType.ValueType  # 0
    SLACK_CHANNEL_ALERT: WorkflowEntryPointAlertConfig.AlertType.ValueType  # 1

    ALERT_TYPE_FIELD_NUMBER: builtins.int
    SLACK_CHANNEL_ALERT_CONFIG_FIELD_NUMBER: builtins.int
    alert_type: global___WorkflowEntryPointAlertConfig.AlertType.ValueType
    @property
    def slack_channel_alert_config(self) -> global___WorkflowEntryPointSlackChannelAlertConfig: ...
    def __init__(
        self,
        *,
        alert_type: global___WorkflowEntryPointAlertConfig.AlertType.ValueType = ...,
        slack_channel_alert_config: global___WorkflowEntryPointSlackChannelAlertConfig | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["alert_config", b"alert_config", "slack_channel_alert_config", b"slack_channel_alert_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["alert_config", b"alert_config", "alert_type", b"alert_type", "slack_channel_alert_config", b"slack_channel_alert_config"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["alert_config", b"alert_config"]) -> typing_extensions.Literal["slack_channel_alert_config"] | None: ...

global___WorkflowEntryPointAlertConfig = WorkflowEntryPointAlertConfig

@typing_extensions.final
class WorkflowActionWebhookNotificationConfig(google.protobuf.message.Message):
    """/////////////////// Workflow Actions /////////////////////"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ENDPOINT_FIELD_NUMBER: builtins.int
    METHOD_FIELD_NUMBER: builtins.int
    HEADERS_FIELD_NUMBER: builtins.int
    BODY_FIELD_NUMBER: builtins.int
    @property
    def endpoint(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def method(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def headers(self) -> google.protobuf.struct_pb2.Struct: ...
    @property
    def body(self) -> google.protobuf.struct_pb2.Struct: ...
    def __init__(
        self,
        *,
        endpoint: google.protobuf.wrappers_pb2.StringValue | None = ...,
        method: google.protobuf.wrappers_pb2.StringValue | None = ...,
        headers: google.protobuf.struct_pb2.Struct | None = ...,
        body: google.protobuf.struct_pb2.Struct | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["body", b"body", "endpoint", b"endpoint", "headers", b"headers", "method", b"method"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["body", b"body", "endpoint", b"endpoint", "headers", b"headers", "method", b"method"]) -> None: ...

global___WorkflowActionWebhookNotificationConfig = WorkflowActionWebhookNotificationConfig

@typing_extensions.final
class WorkflowActionSlackNotificationConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _MessageType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _MessageTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[WorkflowActionSlackNotificationConfig._MessageType.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN_SNT: WorkflowActionSlackNotificationConfig._MessageType.ValueType  # 0
        MESSAGE: WorkflowActionSlackNotificationConfig._MessageType.ValueType  # 1
        THREAD_REPLY: WorkflowActionSlackNotificationConfig._MessageType.ValueType  # 2

    class MessageType(_MessageType, metaclass=_MessageTypeEnumTypeWrapper): ...
    UNKNOWN_SNT: WorkflowActionSlackNotificationConfig.MessageType.ValueType  # 0
    MESSAGE: WorkflowActionSlackNotificationConfig.MessageType.ValueType  # 1
    THREAD_REPLY: WorkflowActionSlackNotificationConfig.MessageType.ValueType  # 2

    MESSAGE_TYPE_FIELD_NUMBER: builtins.int
    SLACK_CHANNEL_ID_FIELD_NUMBER: builtins.int
    THREAD_TS_FIELD_NUMBER: builtins.int
    message_type: global___WorkflowActionSlackNotificationConfig.MessageType.ValueType
    @property
    def slack_channel_id(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def thread_ts(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    def __init__(
        self,
        *,
        message_type: global___WorkflowActionSlackNotificationConfig.MessageType.ValueType = ...,
        slack_channel_id: google.protobuf.wrappers_pb2.StringValue | None = ...,
        thread_ts: google.protobuf.wrappers_pb2.StringValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["slack_channel_id", b"slack_channel_id", "thread_ts", b"thread_ts"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["message_type", b"message_type", "slack_channel_id", b"slack_channel_id", "thread_ts", b"thread_ts"]) -> None: ...

global___WorkflowActionSlackNotificationConfig = WorkflowActionSlackNotificationConfig

@typing_extensions.final
class WorkflowActionNotificationConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Type:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[WorkflowActionNotificationConfig._Type.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN: WorkflowActionNotificationConfig._Type.ValueType  # 0
        WEBHOOK: WorkflowActionNotificationConfig._Type.ValueType  # 1
        SLACK: WorkflowActionNotificationConfig._Type.ValueType  # 2

    class Type(_Type, metaclass=_TypeEnumTypeWrapper): ...
    UNKNOWN: WorkflowActionNotificationConfig.Type.ValueType  # 0
    WEBHOOK: WorkflowActionNotificationConfig.Type.ValueType  # 1
    SLACK: WorkflowActionNotificationConfig.Type.ValueType  # 2

    TYPE_FIELD_NUMBER: builtins.int
    WEBHOOK_CONFIG_FIELD_NUMBER: builtins.int
    SLACK_CONFIG_FIELD_NUMBER: builtins.int
    type: global___WorkflowActionNotificationConfig.Type.ValueType
    @property
    def webhook_config(self) -> global___WorkflowActionWebhookNotificationConfig: ...
    @property
    def slack_config(self) -> global___WorkflowActionSlackNotificationConfig: ...
    def __init__(
        self,
        *,
        type: global___WorkflowActionNotificationConfig.Type.ValueType = ...,
        webhook_config: global___WorkflowActionWebhookNotificationConfig | None = ...,
        slack_config: global___WorkflowActionSlackNotificationConfig | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["notification_config", b"notification_config", "slack_config", b"slack_config", "webhook_config", b"webhook_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["notification_config", b"notification_config", "slack_config", b"slack_config", "type", b"type", "webhook_config", b"webhook_config"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["notification_config", b"notification_config"]) -> typing_extensions.Literal["webhook_config", "slack_config"] | None: ...

global___WorkflowActionNotificationConfig = WorkflowActionNotificationConfig

@typing_extensions.final
class WorkflowSchedule(google.protobuf.message.Message):
    """/////////////////// Workflow Builder Proto /////////////////////"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Type:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[WorkflowSchedule._Type.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN: WorkflowSchedule._Type.ValueType  # 0
        ONE_OFF: WorkflowSchedule._Type.ValueType  # 1
        PERIODIC: WorkflowSchedule._Type.ValueType  # 2

    class Type(_Type, metaclass=_TypeEnumTypeWrapper): ...
    UNKNOWN: WorkflowSchedule.Type.ValueType  # 0
    ONE_OFF: WorkflowSchedule.Type.ValueType  # 1
    PERIODIC: WorkflowSchedule.Type.ValueType  # 2

    TYPE_FIELD_NUMBER: builtins.int
    ONE_OFF_FIELD_NUMBER: builtins.int
    PERIODIC_FIELD_NUMBER: builtins.int
    type: global___WorkflowSchedule.Type.ValueType
    @property
    def one_off(self) -> global___WorkflowOneOffSchedule: ...
    @property
    def periodic(self) -> global___WorkflowPeriodicSchedule: ...
    def __init__(
        self,
        *,
        type: global___WorkflowSchedule.Type.ValueType = ...,
        one_off: global___WorkflowOneOffSchedule | None = ...,
        periodic: global___WorkflowPeriodicSchedule | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["one_off", b"one_off", "periodic", b"periodic", "scheduler", b"scheduler"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["one_off", b"one_off", "periodic", b"periodic", "scheduler", b"scheduler", "type", b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["scheduler", b"scheduler"]) -> typing_extensions.Literal["one_off", "periodic"] | None: ...

global___WorkflowSchedule = WorkflowSchedule

@typing_extensions.final
class WorkflowEntryPoint(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Type:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[WorkflowEntryPoint._Type.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN: WorkflowEntryPoint._Type.ValueType  # 0
        API: WorkflowEntryPoint._Type.ValueType  # 1
        ALERT: WorkflowEntryPoint._Type.ValueType  # 2

    class Type(_Type, metaclass=_TypeEnumTypeWrapper): ...
    UNKNOWN: WorkflowEntryPoint.Type.ValueType  # 0
    API: WorkflowEntryPoint.Type.ValueType  # 1
    ALERT: WorkflowEntryPoint.Type.ValueType  # 2

    ID_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    API_CONFIG_FIELD_NUMBER: builtins.int
    ALERT_CONFIG_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> google.protobuf.wrappers_pb2.UInt64Value: ...
    type: global___WorkflowEntryPoint.Type.ValueType
    @property
    def api_config(self) -> global___WorkflowEntryPointApiConfig: ...
    @property
    def alert_config(self) -> global___WorkflowEntryPointAlertConfig: ...
    def __init__(
        self,
        *,
        id: google.protobuf.wrappers_pb2.UInt64Value | None = ...,
        type: global___WorkflowEntryPoint.Type.ValueType = ...,
        api_config: global___WorkflowEntryPointApiConfig | None = ...,
        alert_config: global___WorkflowEntryPointAlertConfig | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["alert_config", b"alert_config", "api_config", b"api_config", "config", b"config", "id", b"id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["alert_config", b"alert_config", "api_config", b"api_config", "config", b"config", "id", b"id", "type", b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["config", b"config"]) -> typing_extensions.Literal["api_config", "alert_config"] | None: ...

global___WorkflowEntryPoint = WorkflowEntryPoint

@typing_extensions.final
class WorkflowAction(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Type:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[WorkflowAction._Type.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN: WorkflowAction._Type.ValueType  # 0
        NOTIFY: WorkflowAction._Type.ValueType  # 1

    class Type(_Type, metaclass=_TypeEnumTypeWrapper): ...
    UNKNOWN: WorkflowAction.Type.ValueType  # 0
    NOTIFY: WorkflowAction.Type.ValueType  # 1

    ID_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    NOTIFICATION_CONFIG_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> google.protobuf.wrappers_pb2.UInt64Value: ...
    type: global___WorkflowAction.Type.ValueType
    @property
    def notification_config(self) -> global___WorkflowActionNotificationConfig: ...
    def __init__(
        self,
        *,
        id: google.protobuf.wrappers_pb2.UInt64Value | None = ...,
        type: global___WorkflowAction.Type.ValueType = ...,
        notification_config: global___WorkflowActionNotificationConfig | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["action", b"action", "id", b"id", "notification_config", b"notification_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["action", b"action", "id", b"id", "notification_config", b"notification_config", "type", b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["action", b"action"]) -> typing_extensions.Literal["notification_config"] | None: ...

global___WorkflowAction = WorkflowAction

@typing_extensions.final
class Workflow(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    CREATED_BY_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    IS_ACTIVE_FIELD_NUMBER: builtins.int
    SCHEDULE_FIELD_NUMBER: builtins.int
    PLAYBOOKS_FIELD_NUMBER: builtins.int
    ENTRY_POINTS_FIELD_NUMBER: builtins.int
    ACTIONS_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> google.protobuf.wrappers_pb2.UInt64Value: ...
    @property
    def name(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def description(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def created_by(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    created_at: builtins.int
    @property
    def is_active(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def schedule(self) -> global___WorkflowSchedule: ...
    @property
    def playbooks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[protos.playbooks.playbook_pb2.Playbook]: ...
    @property
    def entry_points(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___WorkflowEntryPoint]: ...
    @property
    def actions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___WorkflowAction]: ...
    def __init__(
        self,
        *,
        id: google.protobuf.wrappers_pb2.UInt64Value | None = ...,
        name: google.protobuf.wrappers_pb2.StringValue | None = ...,
        description: google.protobuf.wrappers_pb2.StringValue | None = ...,
        created_by: google.protobuf.wrappers_pb2.StringValue | None = ...,
        created_at: builtins.int = ...,
        is_active: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        schedule: global___WorkflowSchedule | None = ...,
        playbooks: collections.abc.Iterable[protos.playbooks.playbook_pb2.Playbook] | None = ...,
        entry_points: collections.abc.Iterable[global___WorkflowEntryPoint] | None = ...,
        actions: collections.abc.Iterable[global___WorkflowAction] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_by", b"created_by", "description", b"description", "id", b"id", "is_active", b"is_active", "name", b"name", "schedule", b"schedule"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["actions", b"actions", "created_at", b"created_at", "created_by", b"created_by", "description", b"description", "entry_points", b"entry_points", "id", b"id", "is_active", b"is_active", "name", b"name", "playbooks", b"playbooks", "schedule", b"schedule"]) -> None: ...

global___Workflow = Workflow

@typing_extensions.final
class UpdateWorkflowOp(google.protobuf.message.Message):
    """/////////////////// Workflow Update Ops Proto /////////////////////"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Op:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _OpEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[UpdateWorkflowOp._Op.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN: UpdateWorkflowOp._Op.ValueType  # 0
        UPDATE_WORKFLOW_NAME: UpdateWorkflowOp._Op.ValueType  # 1
        UPDATE_WORKFLOW_STATUS: UpdateWorkflowOp._Op.ValueType  # 2
        UPDATE_WORKFLOW: UpdateWorkflowOp._Op.ValueType  # 3
        UPDATE_WORKFLOW_ENTRY_POINT_STATUS: UpdateWorkflowOp._Op.ValueType  # 4
        UPDATE_WORKFLOW_ACTION_STATUS: UpdateWorkflowOp._Op.ValueType  # 5
        UPDATE_WORKFLOW_PLAYBOOK_STATUS: UpdateWorkflowOp._Op.ValueType  # 6

    class Op(_Op, metaclass=_OpEnumTypeWrapper): ...
    UNKNOWN: UpdateWorkflowOp.Op.ValueType  # 0
    UPDATE_WORKFLOW_NAME: UpdateWorkflowOp.Op.ValueType  # 1
    UPDATE_WORKFLOW_STATUS: UpdateWorkflowOp.Op.ValueType  # 2
    UPDATE_WORKFLOW: UpdateWorkflowOp.Op.ValueType  # 3
    UPDATE_WORKFLOW_ENTRY_POINT_STATUS: UpdateWorkflowOp.Op.ValueType  # 4
    UPDATE_WORKFLOW_ACTION_STATUS: UpdateWorkflowOp.Op.ValueType  # 5
    UPDATE_WORKFLOW_PLAYBOOK_STATUS: UpdateWorkflowOp.Op.ValueType  # 6

    @typing_extensions.final
    class UpdateWorkflowName(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        NAME_FIELD_NUMBER: builtins.int
        @property
        def name(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        def __init__(
            self,
            *,
            name: google.protobuf.wrappers_pb2.StringValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["name", b"name"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["name", b"name"]) -> None: ...

    @typing_extensions.final
    class UpdateWorkflowStatus(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        IS_ACTIVE_FIELD_NUMBER: builtins.int
        @property
        def is_active(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
        def __init__(
            self,
            *,
            is_active: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["is_active", b"is_active"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["is_active", b"is_active"]) -> None: ...

    @typing_extensions.final
    class UpdateWorkflow(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        WORKFLOW_FIELD_NUMBER: builtins.int
        @property
        def workflow(self) -> global___Workflow: ...
        def __init__(
            self,
            *,
            workflow: global___Workflow | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["workflow", b"workflow"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["workflow", b"workflow"]) -> None: ...

    @typing_extensions.final
    class UpdateWorkflowEntryPointStatus(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        ENTRY_POINT_ID_FIELD_NUMBER: builtins.int
        IS_ACTIVE_FIELD_NUMBER: builtins.int
        @property
        def entry_point_id(self) -> google.protobuf.wrappers_pb2.UInt64Value: ...
        @property
        def is_active(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
        def __init__(
            self,
            *,
            entry_point_id: google.protobuf.wrappers_pb2.UInt64Value | None = ...,
            is_active: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["entry_point_id", b"entry_point_id", "is_active", b"is_active"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["entry_point_id", b"entry_point_id", "is_active", b"is_active"]) -> None: ...

    @typing_extensions.final
    class UpdateWorkflowActionStatus(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        ACTION_ID_FIELD_NUMBER: builtins.int
        IS_ACTIVE_FIELD_NUMBER: builtins.int
        @property
        def action_id(self) -> google.protobuf.wrappers_pb2.UInt64Value: ...
        @property
        def is_active(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
        def __init__(
            self,
            *,
            action_id: google.protobuf.wrappers_pb2.UInt64Value | None = ...,
            is_active: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["action_id", b"action_id", "is_active", b"is_active"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["action_id", b"action_id", "is_active", b"is_active"]) -> None: ...

    @typing_extensions.final
    class UpdateWorkflowPlaybookStatus(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        PLAYBOOK_ID_FIELD_NUMBER: builtins.int
        IS_ACTIVE_FIELD_NUMBER: builtins.int
        @property
        def playbook_id(self) -> google.protobuf.wrappers_pb2.UInt64Value: ...
        @property
        def is_active(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
        def __init__(
            self,
            *,
            playbook_id: google.protobuf.wrappers_pb2.UInt64Value | None = ...,
            is_active: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["is_active", b"is_active", "playbook_id", b"playbook_id"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["is_active", b"is_active", "playbook_id", b"playbook_id"]) -> None: ...

    OP_FIELD_NUMBER: builtins.int
    UPDATE_WORKFLOW_NAME_FIELD_NUMBER: builtins.int
    UPDATE_WORKFLOW_STATUS_FIELD_NUMBER: builtins.int
    UPDATE_WORKFLOW_FIELD_NUMBER: builtins.int
    UPDATE_WORKFLOW_ENTRY_POINT_STATUS_FIELD_NUMBER: builtins.int
    UPDATE_WORKFLOW_ACTION_STATUS_FIELD_NUMBER: builtins.int
    UPDATE_WORKFLOW_PLAYBOOK_STATUS_FIELD_NUMBER: builtins.int
    op: global___UpdateWorkflowOp.Op.ValueType
    @property
    def update_workflow_name(self) -> global___UpdateWorkflowOp.UpdateWorkflowName: ...
    @property
    def update_workflow_status(self) -> global___UpdateWorkflowOp.UpdateWorkflowStatus: ...
    @property
    def update_workflow(self) -> global___UpdateWorkflowOp.UpdateWorkflow: ...
    @property
    def update_workflow_entry_point_status(self) -> global___UpdateWorkflowOp.UpdateWorkflowEntryPointStatus: ...
    @property
    def update_workflow_action_status(self) -> global___UpdateWorkflowOp.UpdateWorkflowActionStatus: ...
    @property
    def update_workflow_playbook_status(self) -> global___UpdateWorkflowOp.UpdateWorkflowPlaybookStatus: ...
    def __init__(
        self,
        *,
        op: global___UpdateWorkflowOp.Op.ValueType = ...,
        update_workflow_name: global___UpdateWorkflowOp.UpdateWorkflowName | None = ...,
        update_workflow_status: global___UpdateWorkflowOp.UpdateWorkflowStatus | None = ...,
        update_workflow: global___UpdateWorkflowOp.UpdateWorkflow | None = ...,
        update_workflow_entry_point_status: global___UpdateWorkflowOp.UpdateWorkflowEntryPointStatus | None = ...,
        update_workflow_action_status: global___UpdateWorkflowOp.UpdateWorkflowActionStatus | None = ...,
        update_workflow_playbook_status: global___UpdateWorkflowOp.UpdateWorkflowPlaybookStatus | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["update", b"update", "update_workflow", b"update_workflow", "update_workflow_action_status", b"update_workflow_action_status", "update_workflow_entry_point_status", b"update_workflow_entry_point_status", "update_workflow_name", b"update_workflow_name", "update_workflow_playbook_status", b"update_workflow_playbook_status", "update_workflow_status", b"update_workflow_status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["op", b"op", "update", b"update", "update_workflow", b"update_workflow", "update_workflow_action_status", b"update_workflow_action_status", "update_workflow_entry_point_status", b"update_workflow_entry_point_status", "update_workflow_name", b"update_workflow_name", "update_workflow_playbook_status", b"update_workflow_playbook_status", "update_workflow_status", b"update_workflow_status"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["update", b"update"]) -> typing_extensions.Literal["update_workflow_name", "update_workflow_status", "update_workflow", "update_workflow_entry_point_status", "update_workflow_action_status", "update_workflow_playbook_status"] | None: ...

global___UpdateWorkflowOp = UpdateWorkflowOp

@typing_extensions.final
class WorkflowExecutionLog(google.protobuf.message.Message):
    """/////////////////// Workflow Executions Proto /////////////////////"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    PLAYBOOK_EXECUTION_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> google.protobuf.wrappers_pb2.UInt64Value: ...
    @property
    def playbook_execution(self) -> protos.playbooks.playbook_pb2.PlaybookExecution: ...
    created_at: builtins.int
    def __init__(
        self,
        *,
        id: google.protobuf.wrappers_pb2.UInt64Value | None = ...,
        playbook_execution: protos.playbooks.playbook_pb2.PlaybookExecution | None = ...,
        created_at: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["id", b"id", "playbook_execution", b"playbook_execution"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["created_at", b"created_at", "id", b"id", "playbook_execution", b"playbook_execution"]) -> None: ...

global___WorkflowExecutionLog = WorkflowExecutionLog

@typing_extensions.final
class WorkflowExecution(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    WORKFLOW_RUN_ID_FIELD_NUMBER: builtins.int
    WORKFLOW_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    SCHEDULED_AT_FIELD_NUMBER: builtins.int
    EXPIRY_AT_FIELD_NUMBER: builtins.int
    INTERVAL_FIELD_NUMBER: builtins.int
    TOTAL_EXECUTIONS_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    STARTED_AT_FIELD_NUMBER: builtins.int
    FINISHED_AT_FIELD_NUMBER: builtins.int
    CREATED_BY_FIELD_NUMBER: builtins.int
    WORKFLOW_LOGS_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> google.protobuf.wrappers_pb2.UInt64Value: ...
    @property
    def workflow_run_id(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def workflow(self) -> global___Workflow: ...
    status: global___WorkflowExecutionStatusType.ValueType
    scheduled_at: builtins.int
    expiry_at: builtins.int
    @property
    def interval(self) -> google.protobuf.wrappers_pb2.UInt64Value: ...
    @property
    def total_executions(self) -> google.protobuf.wrappers_pb2.UInt64Value: ...
    created_at: builtins.int
    started_at: builtins.int
    finished_at: builtins.int
    @property
    def created_by(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def workflow_logs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___WorkflowExecutionLog]: ...
    def __init__(
        self,
        *,
        id: google.protobuf.wrappers_pb2.UInt64Value | None = ...,
        workflow_run_id: google.protobuf.wrappers_pb2.StringValue | None = ...,
        workflow: global___Workflow | None = ...,
        status: global___WorkflowExecutionStatusType.ValueType = ...,
        scheduled_at: builtins.int = ...,
        expiry_at: builtins.int = ...,
        interval: google.protobuf.wrappers_pb2.UInt64Value | None = ...,
        total_executions: google.protobuf.wrappers_pb2.UInt64Value | None = ...,
        created_at: builtins.int = ...,
        started_at: builtins.int = ...,
        finished_at: builtins.int = ...,
        created_by: google.protobuf.wrappers_pb2.StringValue | None = ...,
        workflow_logs: collections.abc.Iterable[global___WorkflowExecutionLog] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_by", b"created_by", "id", b"id", "interval", b"interval", "total_executions", b"total_executions", "workflow", b"workflow", "workflow_run_id", b"workflow_run_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["created_at", b"created_at", "created_by", b"created_by", "expiry_at", b"expiry_at", "finished_at", b"finished_at", "id", b"id", "interval", b"interval", "scheduled_at", b"scheduled_at", "started_at", b"started_at", "status", b"status", "total_executions", b"total_executions", "workflow", b"workflow", "workflow_logs", b"workflow_logs", "workflow_run_id", b"workflow_run_id"]) -> None: ...

global___WorkflowExecution = WorkflowExecution
