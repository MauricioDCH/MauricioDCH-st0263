from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BootstrapRequest(_message.Message):
    __slots__ = ("node_ip", "node_port")
    NODE_IP_FIELD_NUMBER: _ClassVar[int]
    NODE_PORT_FIELD_NUMBER: _ClassVar[int]
    node_ip: str
    node_port: int
    def __init__(self, node_ip: _Optional[str] = ..., node_port: _Optional[int] = ...) -> None: ...

class BootstrapResponse(_message.Message):
    __slots__ = ("node_id_client", "id_chord_node", "node_id_predeccesor", "node_id_succesor", "node_status")
    NODE_ID_CLIENT_FIELD_NUMBER: _ClassVar[int]
    ID_CHORD_NODE_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_PREDECCESOR_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_SUCCESOR_FIELD_NUMBER: _ClassVar[int]
    NODE_STATUS_FIELD_NUMBER: _ClassVar[int]
    node_id_client: int
    id_chord_node: int
    node_id_predeccesor: int
    node_id_succesor: int
    node_status: bool
    def __init__(self, node_id_client: _Optional[int] = ..., id_chord_node: _Optional[int] = ..., node_id_predeccesor: _Optional[int] = ..., node_id_succesor: _Optional[int] = ..., node_status: bool = ...) -> None: ...

class GetDataRequest(_message.Message):
    __slots__ = ("node_id", "node_ip", "node_port")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_IP_FIELD_NUMBER: _ClassVar[int]
    NODE_PORT_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    node_ip: str
    node_port: int
    def __init__(self, node_id: _Optional[int] = ..., node_ip: _Optional[str] = ..., node_port: _Optional[int] = ...) -> None: ...

class GetDataResponse(_message.Message):
    __slots__ = ("node_id_client", "id_chord_node", "node_ip_chord_node", "node_id_predeccesor", "node_id_succesor", "node_ip_succesor", "node_port_succesor", "number_of_nodes_in_network")
    NODE_ID_CLIENT_FIELD_NUMBER: _ClassVar[int]
    ID_CHORD_NODE_FIELD_NUMBER: _ClassVar[int]
    NODE_IP_CHORD_NODE_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_PREDECCESOR_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_SUCCESOR_FIELD_NUMBER: _ClassVar[int]
    NODE_IP_SUCCESOR_FIELD_NUMBER: _ClassVar[int]
    NODE_PORT_SUCCESOR_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_NODES_IN_NETWORK_FIELD_NUMBER: _ClassVar[int]
    node_id_client: int
    id_chord_node: int
    node_ip_chord_node: str
    node_id_predeccesor: int
    node_id_succesor: int
    node_ip_succesor: str
    node_port_succesor: int
    number_of_nodes_in_network: int
    def __init__(self, node_id_client: _Optional[int] = ..., id_chord_node: _Optional[int] = ..., node_ip_chord_node: _Optional[str] = ..., node_id_predeccesor: _Optional[int] = ..., node_id_succesor: _Optional[int] = ..., node_ip_succesor: _Optional[str] = ..., node_port_succesor: _Optional[int] = ..., number_of_nodes_in_network: _Optional[int] = ...) -> None: ...

class FTRequest(_message.Message):
    __slots__ = ("number_of_nodes_in_network", "node_ids")
    NUMBER_OF_NODES_IN_NETWORK_FIELD_NUMBER: _ClassVar[int]
    NODE_IDS_FIELD_NUMBER: _ClassVar[int]
    number_of_nodes_in_network: int
    node_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, number_of_nodes_in_network: _Optional[int] = ..., node_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class FTResponse(_message.Message):
    __slots__ = ("node_ids", "node_urls")
    NODE_IDS_FIELD_NUMBER: _ClassVar[int]
    NODE_URLS_FIELD_NUMBER: _ClassVar[int]
    node_ids: _containers.RepeatedScalarFieldContainer[int]
    node_urls: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, node_ids: _Optional[_Iterable[int]] = ..., node_urls: _Optional[_Iterable[str]] = ...) -> None: ...

class FileListRequest(_message.Message):
    __slots__ = ("node_id_required", "node_ip_required", "node_port_required", "next_node_id", "next_node_ip", "next_node_port")
    NODE_ID_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    NODE_IP_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    NODE_PORT_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    NEXT_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NEXT_NODE_IP_FIELD_NUMBER: _ClassVar[int]
    NEXT_NODE_PORT_FIELD_NUMBER: _ClassVar[int]
    node_id_required: int
    node_ip_required: str
    node_port_required: int
    next_node_id: int
    next_node_ip: str
    next_node_port: int
    def __init__(self, node_id_required: _Optional[int] = ..., node_ip_required: _Optional[str] = ..., node_port_required: _Optional[int] = ..., next_node_id: _Optional[int] = ..., next_node_ip: _Optional[str] = ..., next_node_port: _Optional[int] = ...) -> None: ...

class FileListResponse(_message.Message):
    __slots__ = ("file_locations", "file_list")
    FILE_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    FILE_LIST_FIELD_NUMBER: _ClassVar[int]
    file_locations: str
    file_list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, file_locations: _Optional[str] = ..., file_list: _Optional[_Iterable[str]] = ...) -> None: ...

class UploadFileRequest(_message.Message):
    __slots__ = ("file_name", "file_location")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    file_location: str
    def __init__(self, file_name: _Optional[str] = ..., file_location: _Optional[str] = ...) -> None: ...

class UploadFileResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...

class DownloadFileRequest(_message.Message):
    __slots__ = ("node_id_required", "node_ip_required", "node_port_required", "file_name", "file_location")
    NODE_ID_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    NODE_IP_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    NODE_PORT_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    node_id_required: int
    node_ip_required: str
    node_port_required: int
    file_name: str
    file_location: str
    def __init__(self, node_id_required: _Optional[int] = ..., node_ip_required: _Optional[str] = ..., node_port_required: _Optional[int] = ..., file_name: _Optional[str] = ..., file_location: _Optional[str] = ...) -> None: ...

class DownloadFileResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...

class PingRequest(_message.Message):
    __slots__ = ("node_ip_required", "node_port_required")
    NODE_IP_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    NODE_PORT_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    node_ip_required: str
    node_port_required: int
    def __init__(self, node_ip_required: _Optional[str] = ..., node_port_required: _Optional[int] = ...) -> None: ...

class PingResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    def __init__(self, status: bool = ...) -> None: ...
