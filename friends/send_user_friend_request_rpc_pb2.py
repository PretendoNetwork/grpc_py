# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: send_user_friend_request_rpc.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"send_user_friend_request_rpc.proto\x12\x07\x66riends\"R\n\x1cSendUserFriendRequestRequest\x12\x0e\n\x06sender\x18\x01 \x01(\r\x12\x11\n\trecipient\x18\x02 \x01(\r\x12\x0f\n\x07message\x18\x03 \x01(\t\"0\n\x1dSendUserFriendRequestResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x42\x11Z\x0f./;grpc_friendsb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'send_user_friend_request_rpc_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\017./;grpc_friends'
  _SENDUSERFRIENDREQUESTREQUEST._serialized_start=47
  _SENDUSERFRIENDREQUESTREQUEST._serialized_end=129
  _SENDUSERFRIENDREQUESTRESPONSE._serialized_start=131
  _SENDUSERFRIENDREQUESTRESPONSE._serialized_end=179
# @@protoc_insertion_point(module_scope)
