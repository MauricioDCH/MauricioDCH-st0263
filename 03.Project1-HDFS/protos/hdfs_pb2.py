# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: protos/hdfs.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'protos/hdfs.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11protos/hdfs.proto\x12\x04hdfs\"\xa6\x01\n DataNodeDesignationClientRequest\x12\x16\n\x0enombre_archivo\x18\x01 \x01(\t\x12\x16\n\x0etamano_archivo\x18\x02 \x01(\x02\x12\x16\n\x0enombre_usuario\x18\x03 \x01(\t\x12\x13\n\x0burl_cliente\x18\x04 \x01(\t\x12%\n\x1dnumero_de_replicas_por_bloque\x18\x05 \x01(\x05\"\xb5\x01\n#DataNodeDesignationNameNodeResponse\x12 \n\x18lista_id_data_node_lider\x18\x01 \x03(\x05\x12#\n\x1blista_id_data_node_seguidor\x18\x02 \x03(\x05\x12!\n\x19lista_url_data_node_lider\x18\x03 \x03(\t\x12$\n\x1clista_url_data_node_seguidor\x18\x04 \x03(\t\"\xf9\x02\n\x1a\x42lockReportDataNodeRequest\x12\x14\n\x0cid_data_node\x18\x01 \x01(\x05\x12$\n\x1clista_rutas_bloques_seguidor\x18\x02 \x03(\t\x12!\n\x19lista_rutas_bloques_lider\x18\x03 \x03(\t\x12\x33\n+json_diccionario_metadatos_bloques_seguidor\x18\x04 \x01(\t\x12\x30\n(json_diccionario_metadatos_bloques_lider\x18\x05 \x01(\t\x12\x11\n\tid_bloque\x18\x06 \x01(\t\x12\x12\n\nruta_lider\x18\x07 \x01(\t\x12\x10\n\x08id_lider\x18\x08 \x01(\t\x12\x11\n\turl_lider\x18\t \x01(\t\x12\x16\n\x0eids_seguidores\x18\n \x03(\t\x12\x17\n\x0furls_seguidores\x18\x0b \x03(\t\x12\x18\n\x10rutas_seguidores\x18\x0c \x03(\t\"5\n\x1b\x42lockReportNameNodeResponse\x12\x16\n\x0e\x65stado_exitoso\x18\x01 \x01(\x08\"`\n\x19\x46ileLocationClientRequest\x12\x16\n\x0enombre_archivo\x18\x01 \x01(\t\x12\x16\n\x0enombre_usuario\x18\x02 \x01(\t\x12\x13\n\x0burl_cliente\x18\x03 \x01(\t\"\xf7\x01\n\x1c\x46ileLocationNameNodeResponse\x12#\n\x1blista_id_data_node_seguidor\x18\x01 \x03(\x05\x12 \n\x18lista_id_data_node_lider\x18\x02 \x03(\x05\x12$\n\x1clista_url_data_node_seguidor\x18\x03 \x03(\t\x12!\n\x19lista_url_data_node_lider\x18\x04 \x03(\t\x12$\n\x1clista_rutas_bloques_seguidor\x18\x05 \x03(\t\x12!\n\x19lista_rutas_bloques_lider\x18\x06 \x03(\t\"\xbe\x01\n\x1b\x42\x61\x63kUpNameNodeLeaderRequest\x12\x32\n*lista_todos_los_archivos_en_namenodeleader\x18\x01 \x03(\t\x12=\n5lista_todos_contenidos_los_archivos_en_namenodeleader\x18\x02 \x03(\t\x12,\n$lista_diccionario_metadatos_archivos\x18\x03 \x03(\t\"8\n\x1e\x42\x61\x63kUpNameNodeFollowerResponse\x12\x16\n\x0e\x65stado_exitoso\x18\x01 \x01(\x08\"H\n\x18HandShakeDataNodeRequest\x12\x14\n\x0c\x64\x61ta_node_ip\x18\x01 \x01(\t\x12\x16\n\x0e\x64\x61ta_node_port\x18\x02 \x01(\x05\"I\n\x19HandShakeNameNodeResponse\x12\x14\n\x0cid_data_node\x18\x01 \x01(\x05\x12\x16\n\x0e\x65stado_exitoso\x18\x02 \x01(\x08\"0\n\x18HeartBeatDataNodeRequest\x12\x14\n\x0cid_data_node\x18\x01 \x01(\x05\"F\n\x19HeartBeatNameNodeResponse\x12\x16\n\x0e\x65stado_exitoso\x18\x01 \x01(\x08\x12\x11\n\ttimestrap\x18\x02 \x01(\t\"\xa5\x01\n\x19\x44ownloadFileClientRequest\x12\x16\n\x0enombre_archivo\x18\x01 \x01(\t\x12\x16\n\x0enombre_usuario\x18\x02 \x01(\t\x12\x13\n\x0burl_cliente\x18\x03 \x01(\t\x12#\n\x1blista_id_data_node_seguidor\x18\x04 \x03(\x05\x12\x1e\n\x16rutas_bloques_seguidor\x18\x05 \x03(\t\"`\n\x1c\x44ownloadFileDataNodeResponse\x12(\n lista_contenido_bloques_seguidor\x18\x01 \x03(\x0c\x12\x16\n\x0e\x65stado_exitoso\x18\x02 \x01(\x08\"\x95\x02\n\x17UploadFileClientRequest\x12\x16\n\x0enombre_archivo\x18\x01 \x01(\t\x12\x16\n\x0enombre_usuario\x18\x02 \x01(\t\x12\x13\n\x0burl_cliente\x18\x03 \x01(\t\x12%\n\x1dlista_contenido_bloques_lider\x18\x04 \x03(\x0c\x12 \n\x18lista_id_data_node_lider\x18\x05 \x03(\x05\x12#\n\x1blista_id_data_node_seguidor\x18\x06 \x03(\x05\x12!\n\x19lista_url_data_node_lider\x18\x07 \x03(\t\x12$\n\x1clista_url_data_node_seguidor\x18\x08 \x03(\t\"4\n\x1aUploadFileDataNodeResponse\x12\x16\n\x0e\x65stado_exitoso\x18\x01 \x01(\x08\"\xb1\x02\n\x17\x44\x65leteFileClientRequest\x12\x16\n\x0enombre_archivo\x18\x01 \x01(\t\x12\x16\n\x0enombre_usuario\x18\x02 \x01(\t\x12\x13\n\x0burl_cliente\x18\x03 \x01(\t\x12\x1d\n\x15lista_id_bloque_lider\x18\x04 \x03(\x05\x12 \n\x18lista_id_bloque_seguidor\x18\x05 \x03(\x05\x12!\n\x19lista_url_data_node_lider\x18\x06 \x03(\t\x12$\n\x1clista_url_data_node_seguidor\x18\x07 \x03(\t\x12!\n\x19lista_rutas_bloques_lider\x18\x08 \x03(\t\x12$\n\x1clista_rutas_bloques_seguidor\x18\t \x03(\t\"4\n\x1a\x44\x65leteFileDataNodeResponse\x12\x16\n\x0e\x65stado_exitoso\x18\x01 \x01(\x08\"\xaf\x02\n\x15ReadFileClientRequest\x12\x16\n\x0enombre_archivo\x18\x01 \x01(\t\x12\x16\n\x0enombre_usuario\x18\x02 \x01(\t\x12\x13\n\x0burl_cliente\x18\x03 \x01(\t\x12\x1d\n\x15lista_id_bloque_lider\x18\x04 \x03(\x05\x12 \n\x18lista_id_bloque_seguidor\x18\x05 \x03(\x05\x12!\n\x19lista_url_data_node_lider\x18\x06 \x03(\t\x12$\n\x1clista_url_data_node_seguidor\x18\x07 \x03(\t\x12!\n\x19lista_rutas_bloques_lider\x18\x08 \x03(\t\x12$\n\x1clista_rutas_bloques_seguidor\x18\t \x03(\t\"\\\n\x18ReadFileDataNodeResponse\x12(\n lista_contenido_bloques_seguidor\x18\x01 \x03(\x0c\x12\x16\n\x0e\x65stado_exitoso\x18\x02 \x01(\x08\"\xb1\x01\n\x17PipeLineDataNodeRequest\x12\x16\n\x0enombre_archivo\x18\x01 \x01(\t\x12\x1a\n\x12id_data_node_lider\x18\x02 \x03(\x05\x12\x1d\n\x15id_data_node_seguidor\x18\x03 \x03(\x05\x12\x1f\n\x17\x63ontenido_bloques_lider\x18\x04 \x03(\x0c\x12\"\n\x1a\x63ontenido_bloques_seguidor\x18\x05 \x03(\x0c\"V\n\x18PipeLineDataNodeResponse\x12\x16\n\x0e\x65stado_exitoso\x18\x01 \x01(\x08\x12\"\n\x1a\x63ontenido_bloques_seguidor\x18\x02 \x03(\x0c\"3\n\x19\x44\x65leteFileDataNodeRequest\x12\x16\n\x0enombre_archivo\x18\x01 \x01(\t\"4\n\x1a\x44\x65leteFileNameNodeResponse\x12\x16\n\x0e\x65stado_exitoso\x18\x01 \x01(\x08\"|\n\x1dPipeLineForGetDataNodeRequest\x12\x16\n\x0enombre_archivo\x18\x01 \x01(\t\x12#\n\x1blista_id_data_node_seguidor\x18\x02 \x03(\x05\x12\x1e\n\x16rutas_bloques_seguidor\x18\x03 \x03(\t\"b\n\x1ePipeLineForGetDataNodeResponse\x12(\n lista_contenido_bloques_seguidor\x18\x01 \x03(\x0c\x12\x16\n\x0e\x65stado_exitoso\x18\x02 \x01(\x08\"{\n PipeLineForDeleteDataNodeRequest\x12\x16\n\x0enombre_archivo\x18\x01 \x01(\t\x12\x1d\n\x15lista_id_bloque_lider\x18\x02 \x03(\x05\x12 \n\x18lista_id_bloque_seguidor\x18\x03 \x03(\x05\";\n!PipeLineForDeleteDataNodeResponse\x12\x16\n\x0e\x65stado_exitoso\x18\x01 \x01(\x08\x32\xbb\x0b\n\x0c\x46ullServices\x12v\n!DataNodeDesignationNameNodeClient\x12&.hdfs.DataNodeDesignationClientRequest\x1a).hdfs.DataNodeDesignationNameNodeResponse\x12\x62\n\x1b\x42lockReportNameNodeDataNode\x12 .hdfs.BlockReportDataNodeRequest\x1a!.hdfs.BlockReportNameNodeResponse\x12\x61\n\x1a\x46ileLocationNameNodeClient\x12\x1f.hdfs.FileLocationClientRequest\x1a\".hdfs.FileLocationNameNodeResponse\x12o\n$BackUpNameNodeFollowerNameNodeLeader\x12!.hdfs.BackUpNameNodeLeaderRequest\x1a$.hdfs.BackUpNameNodeFollowerResponse\x12\\\n\x19HandShakeNameNodeDataNode\x12\x1e.hdfs.HandShakeDataNodeRequest\x1a\x1f.hdfs.HandShakeNameNodeResponse\x12\\\n\x19HeartBeatNameNodeDataNode\x12\x1e.hdfs.HeartBeatDataNodeRequest\x1a\x1f.hdfs.HeartBeatNameNodeResponse\x12\x61\n\x1a\x44ownloadFileDataNodeClient\x12\x1f.hdfs.DownloadFileClientRequest\x1a\".hdfs.DownloadFileDataNodeResponse\x12[\n\x18UploadFileDataNodeClient\x12\x1d.hdfs.UploadFileClientRequest\x1a .hdfs.UploadFileDataNodeResponse\x12[\n\x18\x44\x65leteFileDataNodeClient\x12\x1d.hdfs.DeleteFileClientRequest\x1a .hdfs.DeleteFileDataNodeResponse\x12U\n\x16ReadFileDataNodeClient\x12\x1b.hdfs.ReadFileClientRequest\x1a\x1e.hdfs.ReadFileDataNodeResponse\x12h\n\'PipeLineDataNodeResponseDataNodeRequest\x12\x1d.hdfs.PipeLineDataNodeRequest\x1a\x1e.hdfs.PipeLineDataNodeResponse\x12_\n\x1a\x44\x65leteFileNameNodeDataNode\x12\x1f.hdfs.DeleteFileDataNodeRequest\x1a .hdfs.DeleteFileNameNodeResponse\x12z\n-PipeLineForGetDataNodeResponseDataNodeRequest\x12#.hdfs.PipeLineForGetDataNodeRequest\x1a$.hdfs.PipeLineForGetDataNodeResponse\x12\x83\x01\n0PipeLineForDeleteDataNodeResponseDataNodeRequest\x12&.hdfs.PipeLineForDeleteDataNodeRequest\x1a\'.hdfs.PipeLineForDeleteDataNodeResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.hdfs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_DATANODEDESIGNATIONCLIENTREQUEST']._serialized_start=28
  _globals['_DATANODEDESIGNATIONCLIENTREQUEST']._serialized_end=194
  _globals['_DATANODEDESIGNATIONNAMENODERESPONSE']._serialized_start=197
  _globals['_DATANODEDESIGNATIONNAMENODERESPONSE']._serialized_end=378
  _globals['_BLOCKREPORTDATANODEREQUEST']._serialized_start=381
  _globals['_BLOCKREPORTDATANODEREQUEST']._serialized_end=758
  _globals['_BLOCKREPORTNAMENODERESPONSE']._serialized_start=760
  _globals['_BLOCKREPORTNAMENODERESPONSE']._serialized_end=813
  _globals['_FILELOCATIONCLIENTREQUEST']._serialized_start=815
  _globals['_FILELOCATIONCLIENTREQUEST']._serialized_end=911
  _globals['_FILELOCATIONNAMENODERESPONSE']._serialized_start=914
  _globals['_FILELOCATIONNAMENODERESPONSE']._serialized_end=1161
  _globals['_BACKUPNAMENODELEADERREQUEST']._serialized_start=1164
  _globals['_BACKUPNAMENODELEADERREQUEST']._serialized_end=1354
  _globals['_BACKUPNAMENODEFOLLOWERRESPONSE']._serialized_start=1356
  _globals['_BACKUPNAMENODEFOLLOWERRESPONSE']._serialized_end=1412
  _globals['_HANDSHAKEDATANODEREQUEST']._serialized_start=1414
  _globals['_HANDSHAKEDATANODEREQUEST']._serialized_end=1486
  _globals['_HANDSHAKENAMENODERESPONSE']._serialized_start=1488
  _globals['_HANDSHAKENAMENODERESPONSE']._serialized_end=1561
  _globals['_HEARTBEATDATANODEREQUEST']._serialized_start=1563
  _globals['_HEARTBEATDATANODEREQUEST']._serialized_end=1611
  _globals['_HEARTBEATNAMENODERESPONSE']._serialized_start=1613
  _globals['_HEARTBEATNAMENODERESPONSE']._serialized_end=1683
  _globals['_DOWNLOADFILECLIENTREQUEST']._serialized_start=1686
  _globals['_DOWNLOADFILECLIENTREQUEST']._serialized_end=1851
  _globals['_DOWNLOADFILEDATANODERESPONSE']._serialized_start=1853
  _globals['_DOWNLOADFILEDATANODERESPONSE']._serialized_end=1949
  _globals['_UPLOADFILECLIENTREQUEST']._serialized_start=1952
  _globals['_UPLOADFILECLIENTREQUEST']._serialized_end=2229
  _globals['_UPLOADFILEDATANODERESPONSE']._serialized_start=2231
  _globals['_UPLOADFILEDATANODERESPONSE']._serialized_end=2283
  _globals['_DELETEFILECLIENTREQUEST']._serialized_start=2286
  _globals['_DELETEFILECLIENTREQUEST']._serialized_end=2591
  _globals['_DELETEFILEDATANODERESPONSE']._serialized_start=2593
  _globals['_DELETEFILEDATANODERESPONSE']._serialized_end=2645
  _globals['_READFILECLIENTREQUEST']._serialized_start=2648
  _globals['_READFILECLIENTREQUEST']._serialized_end=2951
  _globals['_READFILEDATANODERESPONSE']._serialized_start=2953
  _globals['_READFILEDATANODERESPONSE']._serialized_end=3045
  _globals['_PIPELINEDATANODEREQUEST']._serialized_start=3048
  _globals['_PIPELINEDATANODEREQUEST']._serialized_end=3225
  _globals['_PIPELINEDATANODERESPONSE']._serialized_start=3227
  _globals['_PIPELINEDATANODERESPONSE']._serialized_end=3313
  _globals['_DELETEFILEDATANODEREQUEST']._serialized_start=3315
  _globals['_DELETEFILEDATANODEREQUEST']._serialized_end=3366
  _globals['_DELETEFILENAMENODERESPONSE']._serialized_start=3368
  _globals['_DELETEFILENAMENODERESPONSE']._serialized_end=3420
  _globals['_PIPELINEFORGETDATANODEREQUEST']._serialized_start=3422
  _globals['_PIPELINEFORGETDATANODEREQUEST']._serialized_end=3546
  _globals['_PIPELINEFORGETDATANODERESPONSE']._serialized_start=3548
  _globals['_PIPELINEFORGETDATANODERESPONSE']._serialized_end=3646
  _globals['_PIPELINEFORDELETEDATANODEREQUEST']._serialized_start=3648
  _globals['_PIPELINEFORDELETEDATANODEREQUEST']._serialized_end=3771
  _globals['_PIPELINEFORDELETEDATANODERESPONSE']._serialized_start=3773
  _globals['_PIPELINEFORDELETEDATANODERESPONSE']._serialized_end=3832
  _globals['_FULLSERVICES']._serialized_start=3835
  _globals['_FULLSERVICES']._serialized_end=5302
# @@protoc_insertion_point(module_scope)
