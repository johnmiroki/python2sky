# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/CLR.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

from proto.common import common_pb2 as common_dot_common__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/CLR.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n0org.apache.skywalking.apm.network.language.agentP\001\252\002\032SkyWalking.NetworkProtocol',
  serialized_pb=b'\n\x10\x63ommon/CLR.proto\x1a\x13\x63ommon/common.proto\"\\\n\tCLRMetric\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12\x11\n\x03\x63pu\x18\x02 \x01(\x0b\x32\x04.CPU\x12\x12\n\x02gc\x18\x03 \x01(\x0b\x32\x06.ClrGC\x12\x1a\n\x06thread\x18\x04 \x01(\x0b\x32\n.ClrThread\"i\n\x05\x43lrGC\x12\x18\n\x10Gen0CollectCount\x18\x01 \x01(\x03\x12\x18\n\x10Gen1CollectCount\x18\x02 \x01(\x03\x12\x18\n\x10Gen2CollectCount\x18\x03 \x01(\x03\x12\x12\n\nHeapMemory\x18\x04 \x01(\x03\"\x8f\x01\n\tClrThread\x12&\n\x1e\x41vailableCompletionPortThreads\x18\x01 \x01(\x05\x12\x1e\n\x16\x41vailableWorkerThreads\x18\x02 \x01(\x05\x12 \n\x18MaxCompletionPortThreads\x18\x03 \x01(\x05\x12\x18\n\x10MaxWorkerThreads\x18\x04 \x01(\x05\x42Q\n0org.apache.skywalking.apm.network.language.agentP\x01\xaa\x02\x1aSkyWalking.NetworkProtocolb\x06proto3'
  ,
  dependencies=[common_dot_common__pb2.DESCRIPTOR,])




_CLRMETRIC = _descriptor.Descriptor(
  name='CLRMetric',
  full_name='CLRMetric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='CLRMetric.time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpu', full_name='CLRMetric.cpu', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gc', full_name='CLRMetric.gc', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='thread', full_name='CLRMetric.thread', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=133,
)


_CLRGC = _descriptor.Descriptor(
  name='ClrGC',
  full_name='ClrGC',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Gen0CollectCount', full_name='ClrGC.Gen0CollectCount', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Gen1CollectCount', full_name='ClrGC.Gen1CollectCount', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Gen2CollectCount', full_name='ClrGC.Gen2CollectCount', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='HeapMemory', full_name='ClrGC.HeapMemory', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=240,
)


_CLRTHREAD = _descriptor.Descriptor(
  name='ClrThread',
  full_name='ClrThread',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='AvailableCompletionPortThreads', full_name='ClrThread.AvailableCompletionPortThreads', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='AvailableWorkerThreads', full_name='ClrThread.AvailableWorkerThreads', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='MaxCompletionPortThreads', full_name='ClrThread.MaxCompletionPortThreads', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='MaxWorkerThreads', full_name='ClrThread.MaxWorkerThreads', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=243,
  serialized_end=386,
)

_CLRMETRIC.fields_by_name['cpu'].message_type = common_dot_common__pb2._CPU
_CLRMETRIC.fields_by_name['gc'].message_type = _CLRGC
_CLRMETRIC.fields_by_name['thread'].message_type = _CLRTHREAD
DESCRIPTOR.message_types_by_name['CLRMetric'] = _CLRMETRIC
DESCRIPTOR.message_types_by_name['ClrGC'] = _CLRGC
DESCRIPTOR.message_types_by_name['ClrThread'] = _CLRTHREAD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CLRMetric = _reflection.GeneratedProtocolMessageType('CLRMetric', (_message.Message,), {
  'DESCRIPTOR' : _CLRMETRIC,
  '__module__' : 'common.CLR_pb2'
  # @@protoc_insertion_point(class_scope:CLRMetric)
  })
_sym_db.RegisterMessage(CLRMetric)

ClrGC = _reflection.GeneratedProtocolMessageType('ClrGC', (_message.Message,), {
  'DESCRIPTOR' : _CLRGC,
  '__module__' : 'common.CLR_pb2'
  # @@protoc_insertion_point(class_scope:ClrGC)
  })
_sym_db.RegisterMessage(ClrGC)

ClrThread = _reflection.GeneratedProtocolMessageType('ClrThread', (_message.Message,), {
  'DESCRIPTOR' : _CLRTHREAD,
  '__module__' : 'common.CLR_pb2'
  # @@protoc_insertion_point(class_scope:ClrThread)
  })
_sym_db.RegisterMessage(ClrThread)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
