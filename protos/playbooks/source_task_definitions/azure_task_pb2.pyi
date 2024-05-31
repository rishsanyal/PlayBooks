"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.wrappers_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Azure(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _TaskType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _TaskTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Azure._TaskType.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN: Azure._TaskType.ValueType  # 0
        FILTER_LOG_EVENTS: Azure._TaskType.ValueType  # 1

    class TaskType(_TaskType, metaclass=_TaskTypeEnumTypeWrapper): ...
    UNKNOWN: Azure.TaskType.ValueType  # 0
    FILTER_LOG_EVENTS: Azure.TaskType.ValueType  # 1

    @typing_extensions.final
    class FilterLogEvents(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        WORKSPACE_ID_FIELD_NUMBER: builtins.int
        FILTER_QUERY_FIELD_NUMBER: builtins.int
        TIMESPAN_FIELD_NUMBER: builtins.int
        @property
        def workspace_id(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        @property
        def filter_query(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        @property
        def timespan(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        def __init__(
            self,
            *,
            workspace_id: google.protobuf.wrappers_pb2.StringValue | None = ...,
            filter_query: google.protobuf.wrappers_pb2.StringValue | None = ...,
            timespan: google.protobuf.wrappers_pb2.StringValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["filter_query", b"filter_query", "timespan", b"timespan", "workspace_id", b"workspace_id"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["filter_query", b"filter_query", "timespan", b"timespan", "workspace_id", b"workspace_id"]) -> None: ...

    TYPE_FIELD_NUMBER: builtins.int
    FILTER_LOG_EVENTS_FIELD_NUMBER: builtins.int
    type: global___Azure.TaskType.ValueType
    @property
    def filter_log_events(self) -> global___Azure.FilterLogEvents: ...
    def __init__(
        self,
        *,
        type: global___Azure.TaskType.ValueType = ...,
        filter_log_events: global___Azure.FilterLogEvents | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["filter_log_events", b"filter_log_events", "task", b"task"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter_log_events", b"filter_log_events", "task", b"task", "type", b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["task", b"task"]) -> typing_extensions.Literal["filter_log_events"] | None: ...

global___Azure = Azure
