# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import register_rpc_pb2 as register__rpc__pb2
from . import login_rpc_pb2 as login__rpc__pb2
from . import get_user_data_rpc_pb2 as get__user__data__rpc__pb2
from . import update_user_data_rpc_pb2 as update__user__data__rpc__pb2
from . import forgot_password_rpc_pb2 as forgot__password__rpc__pb2
from . import reset_password_rpc_pb2 as reset__password__rpc__pb2
from . import set_discord_connection_data_rpc_pb2 as set__discord__connection__data__rpc__pb2
from . import set_stripe_connection_data_rpc_pb2 as set__stripe__connection__data__rpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x61pi_service.proto\x12\x03\x61pi\x1a\x1bgoogle/protobuf/empty.proto\x1a\x12register_rpc.proto\x1a\x0flogin_rpc.proto\x1a\x17get_user_data_rpc.proto\x1a\x1aupdate_user_data_rpc.proto\x1a\x19\x66orgot_password_rpc.proto\x1a\x18reset_password_rpc.proto\x1a%set_discord_connection_data_rpc.proto\x1a$set_stripe_connection_data_rpc.proto2\xc0\x04\n\x03\x41PI\x12\x36\n\x08Register\x12\x14.api.RegisterRequest\x1a\x12.api.LoginResponse\"\x00\x12\x30\n\x05Login\x12\x11.api.LoginRequest\x1a\x12.api.LoginResponse\"\x00\x12\x41\n\x0bGetUserData\x12\x16.google.protobuf.Empty\x1a\x18.api.GetUserDataResponse\"\x00\x12H\n\x0eUpdateUserData\x12\x1a.api.UpdateUserDataRequest\x1a\x18.api.GetUserDataResponse\"\x00\x12\x46\n\x0e\x46orgotPassword\x12\x1a.api.ForgotPasswordRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x44\n\rResetPassword\x12\x19.api.ResetPasswordRequest\x1a\x16.google.protobuf.Empty\"\x00\x12Z\n\x18SetDiscordConnectionData\x12$.api.SetDiscordConnectionDataRequest\x1a\x16.google.protobuf.Empty\"\x00\x12X\n\x17SetStripeConnectionData\x12#.api.SetStripeConnectionDataRequest\x1a\x16.google.protobuf.Empty\"\x00\x42\rZ\x0b./;grpc_apib\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\013./;grpc_api'
  _API._serialized_start=276
  _API._serialized_end=852
# @@protoc_insertion_point(module_scope)
