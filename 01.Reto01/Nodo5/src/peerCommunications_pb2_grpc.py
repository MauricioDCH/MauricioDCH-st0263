# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import peerCommunications_pb2 as peerCommunications__pb2

GRPC_GENERATED_VERSION = '1.66.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in peerCommunications_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class Peer2PeerServiceStub(object):
    """Servicios
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.HandleBootstrap = channel.unary_unary(
                '/peerCommunications.Peer2PeerService/HandleBootstrap',
                request_serializer=peerCommunications__pb2.BootstrapRequest.SerializeToString,
                response_deserializer=peerCommunications__pb2.BootstrapResponse.FromString,
                _registered_method=True)
        self.GetData = channel.unary_unary(
                '/peerCommunications.Peer2PeerService/GetData',
                request_serializer=peerCommunications__pb2.GetDataRequest.SerializeToString,
                response_deserializer=peerCommunications__pb2.GetDataResponse.FromString,
                _registered_method=True)
        self.QueryFingerTable = channel.unary_unary(
                '/peerCommunications.Peer2PeerService/QueryFingerTable',
                request_serializer=peerCommunications__pb2.FTRequest.SerializeToString,
                response_deserializer=peerCommunications__pb2.FTResponse.FromString,
                _registered_method=True)
        self.QueryFileList = channel.unary_unary(
                '/peerCommunications.Peer2PeerService/QueryFileList',
                request_serializer=peerCommunications__pb2.FileListRequest.SerializeToString,
                response_deserializer=peerCommunications__pb2.FileListResponse.FromString,
                _registered_method=True)
        self.UploadFile = channel.unary_unary(
                '/peerCommunications.Peer2PeerService/UploadFile',
                request_serializer=peerCommunications__pb2.UploadFileRequest.SerializeToString,
                response_deserializer=peerCommunications__pb2.UploadFileResponse.FromString,
                _registered_method=True)
        self.DownloadFile = channel.unary_unary(
                '/peerCommunications.Peer2PeerService/DownloadFile',
                request_serializer=peerCommunications__pb2.DownloadFileRequest.SerializeToString,
                response_deserializer=peerCommunications__pb2.DownloadFileResponse.FromString,
                _registered_method=True)
        self.Ping = channel.unary_unary(
                '/peerCommunications.Peer2PeerService/Ping',
                request_serializer=peerCommunications__pb2.PingRequest.SerializeToString,
                response_deserializer=peerCommunications__pb2.PingResponse.FromString,
                _registered_method=True)


class Peer2PeerServiceServicer(object):
    """Servicios
    """

    def HandleBootstrap(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryFingerTable(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryFileList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UploadFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DownloadFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Ping(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_Peer2PeerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'HandleBootstrap': grpc.unary_unary_rpc_method_handler(
                    servicer.HandleBootstrap,
                    request_deserializer=peerCommunications__pb2.BootstrapRequest.FromString,
                    response_serializer=peerCommunications__pb2.BootstrapResponse.SerializeToString,
            ),
            'GetData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetData,
                    request_deserializer=peerCommunications__pb2.GetDataRequest.FromString,
                    response_serializer=peerCommunications__pb2.GetDataResponse.SerializeToString,
            ),
            'QueryFingerTable': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryFingerTable,
                    request_deserializer=peerCommunications__pb2.FTRequest.FromString,
                    response_serializer=peerCommunications__pb2.FTResponse.SerializeToString,
            ),
            'QueryFileList': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryFileList,
                    request_deserializer=peerCommunications__pb2.FileListRequest.FromString,
                    response_serializer=peerCommunications__pb2.FileListResponse.SerializeToString,
            ),
            'UploadFile': grpc.unary_unary_rpc_method_handler(
                    servicer.UploadFile,
                    request_deserializer=peerCommunications__pb2.UploadFileRequest.FromString,
                    response_serializer=peerCommunications__pb2.UploadFileResponse.SerializeToString,
            ),
            'DownloadFile': grpc.unary_unary_rpc_method_handler(
                    servicer.DownloadFile,
                    request_deserializer=peerCommunications__pb2.DownloadFileRequest.FromString,
                    response_serializer=peerCommunications__pb2.DownloadFileResponse.SerializeToString,
            ),
            'Ping': grpc.unary_unary_rpc_method_handler(
                    servicer.Ping,
                    request_deserializer=peerCommunications__pb2.PingRequest.FromString,
                    response_serializer=peerCommunications__pb2.PingResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'peerCommunications.Peer2PeerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('peerCommunications.Peer2PeerService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Peer2PeerService(object):
    """Servicios
    """

    @staticmethod
    def HandleBootstrap(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/peerCommunications.Peer2PeerService/HandleBootstrap',
            peerCommunications__pb2.BootstrapRequest.SerializeToString,
            peerCommunications__pb2.BootstrapResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/peerCommunications.Peer2PeerService/GetData',
            peerCommunications__pb2.GetDataRequest.SerializeToString,
            peerCommunications__pb2.GetDataResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def QueryFingerTable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/peerCommunications.Peer2PeerService/QueryFingerTable',
            peerCommunications__pb2.FTRequest.SerializeToString,
            peerCommunications__pb2.FTResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def QueryFileList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/peerCommunications.Peer2PeerService/QueryFileList',
            peerCommunications__pb2.FileListRequest.SerializeToString,
            peerCommunications__pb2.FileListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UploadFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/peerCommunications.Peer2PeerService/UploadFile',
            peerCommunications__pb2.UploadFileRequest.SerializeToString,
            peerCommunications__pb2.UploadFileResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DownloadFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/peerCommunications.Peer2PeerService/DownloadFile',
            peerCommunications__pb2.DownloadFileRequest.SerializeToString,
            peerCommunications__pb2.DownloadFileResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/peerCommunications.Peer2PeerService/Ping',
            peerCommunications__pb2.PingRequest.SerializeToString,
            peerCommunications__pb2.PingResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
