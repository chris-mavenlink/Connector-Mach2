# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: connector.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='connector.proto',
  package='grpc',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0f\x63onnector.proto\x12\x04grpc\"n\n\x06\x41\x63tion\x12\x14\n\x0c\x64isplay_name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x1b\n\x06inputs\x18\x03 \x03(\x0b\x32\x0b.grpc.Field\x12\x1c\n\x07outputs\x18\x04 \x03(\x0b\x32\x0b.grpc.Field\"\x8d\x01\n\rActionRequest\x12\x1c\n\x06\x61\x63tion\x18\x01 \x01(\x0b\x32\x0c.grpc.Action\x12/\n\x06params\x18\x02 \x03(\x0b\x32\x1f.grpc.ActionRequest.ParamsEntry\x1a-\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xe4\x01\n\x0e\x41\x63tionResponse\x12+\n\x06status\x18\x01 \x01(\x0e\x32\x1b.grpc.ActionResponse.Status\x12\x32\n\x07outputs\x18\x02 \x03(\x0b\x32!.grpc.ActionResponse.OutputsEntry\x12\x15\n\rerror_message\x18\x03 \x01(\t\x1a.\n\x0cOutputsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"*\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\t\n\x05\x45RROR\x10\x01\x12\x08\n\x04HALT\x10\x02\"q\n\x07Trigger\x12\x14\n\x0c\x64isplay_name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0f\n\x07\x61pp_key\x18\x03 \x01(\t\x12\x1c\n\x07outputs\x18\x04 \x03(\x0b\x32\x0b.grpc.Field\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\"\x91\x01\n\x0eTriggerRequest\x12\x1e\n\x07trigger\x18\x01 \x01(\x0b\x32\r.grpc.Trigger\x12\x30\n\x06params\x18\x02 \x03(\x0b\x32 .grpc.TriggerRequest.ParamsEntry\x1a-\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x95\x01\n\x0fTriggerResponse\x12,\n\x06status\x18\x01 \x01(\x0e\x32\x1c.grpc.TriggerResponse.Status\x12\x15\n\rerror_message\x18\x02 \x01(\t\x12\x1b\n\x06\x65vents\x18\x03 \x03(\x0b\x32\x0b.grpc.Event\" \n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\t\n\x05\x45RROR\x10\x01\"\"\n\x0e\x41\x63tionsRequest\x12\x10\n\x08whatever\x18\x01 \x01(\t\"0\n\x0f\x41\x63tionsResponse\x12\x1d\n\x07\x61\x63tions\x18\x01 \x03(\x0b\x32\x0c.grpc.Action\"*\n\x0fTriggersRequest\x12\x17\n\x0ftesting_trigger\x18\x01 \x01(\t\"3\n\x10TriggersResponse\x12\x1f\n\x08triggers\x18\x01 \x03(\x0b\x32\r.grpc.Trigger\"p\n\x05\x46ield\x12\x14\n\x0c\x64isplay_name\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x0f\n\x07\x61pp_key\x18\x06 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x10\n\x08required\x18\x05 \x01(\x08\"\x18\n\x05\x45vent\x12\x0f\n\x07payload\x18\x01 \x01(\t2\xfb\x01\n\tConnector\x12\x39\n\x08triggers\x12\x15.grpc.TriggersRequest\x1a\x16.grpc.TriggersResponse\x12>\n\x0fperform_trigger\x12\x14.grpc.TriggerRequest\x1a\x15.grpc.TriggerResponse\x12\x36\n\x07\x61\x63tions\x12\x14.grpc.ActionsRequest\x1a\x15.grpc.ActionsResponse\x12;\n\x0eperform_action\x12\x13.grpc.ActionRequest\x1a\x14.grpc.ActionResponseb\x06proto3'
)



_ACTIONRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='grpc.ActionResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HALT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=468,
  serialized_end=510,
)
_sym_db.RegisterEnumDescriptor(_ACTIONRESPONSE_STATUS)

_TRIGGERRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='grpc.TriggerResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=468,
  serialized_end=500,
)
_sym_db.RegisterEnumDescriptor(_TRIGGERRESPONSE_STATUS)


_ACTION = _descriptor.Descriptor(
  name='Action',
  full_name='grpc.Action',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='display_name', full_name='grpc.Action.display_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='grpc.Action.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inputs', full_name='grpc.Action.inputs', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='grpc.Action.outputs', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=25,
  serialized_end=135,
)


_ACTIONREQUEST_PARAMSENTRY = _descriptor.Descriptor(
  name='ParamsEntry',
  full_name='grpc.ActionRequest.ParamsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='grpc.ActionRequest.ParamsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='grpc.ActionRequest.ParamsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=234,
  serialized_end=279,
)

_ACTIONREQUEST = _descriptor.Descriptor(
  name='ActionRequest',
  full_name='grpc.ActionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='grpc.ActionRequest.action', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='params', full_name='grpc.ActionRequest.params', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ACTIONREQUEST_PARAMSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=279,
)


_ACTIONRESPONSE_OUTPUTSENTRY = _descriptor.Descriptor(
  name='OutputsEntry',
  full_name='grpc.ActionResponse.OutputsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='grpc.ActionResponse.OutputsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='grpc.ActionResponse.OutputsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=420,
  serialized_end=466,
)

_ACTIONRESPONSE = _descriptor.Descriptor(
  name='ActionResponse',
  full_name='grpc.ActionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='grpc.ActionResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='grpc.ActionResponse.outputs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='grpc.ActionResponse.error_message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ACTIONRESPONSE_OUTPUTSENTRY, ],
  enum_types=[
    _ACTIONRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=282,
  serialized_end=510,
)


_TRIGGER = _descriptor.Descriptor(
  name='Trigger',
  full_name='grpc.Trigger',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='display_name', full_name='grpc.Trigger.display_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='grpc.Trigger.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='app_key', full_name='grpc.Trigger.app_key', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='grpc.Trigger.outputs', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='grpc.Trigger.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=512,
  serialized_end=625,
)


_TRIGGERREQUEST_PARAMSENTRY = _descriptor.Descriptor(
  name='ParamsEntry',
  full_name='grpc.TriggerRequest.ParamsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='grpc.TriggerRequest.ParamsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='grpc.TriggerRequest.ParamsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=234,
  serialized_end=279,
)

_TRIGGERREQUEST = _descriptor.Descriptor(
  name='TriggerRequest',
  full_name='grpc.TriggerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='trigger', full_name='grpc.TriggerRequest.trigger', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='params', full_name='grpc.TriggerRequest.params', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_TRIGGERREQUEST_PARAMSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=628,
  serialized_end=773,
)


_TRIGGERRESPONSE = _descriptor.Descriptor(
  name='TriggerResponse',
  full_name='grpc.TriggerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='grpc.TriggerResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='grpc.TriggerResponse.error_message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='events', full_name='grpc.TriggerResponse.events', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TRIGGERRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=776,
  serialized_end=925,
)


_ACTIONSREQUEST = _descriptor.Descriptor(
  name='ActionsRequest',
  full_name='grpc.ActionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='whatever', full_name='grpc.ActionsRequest.whatever', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=927,
  serialized_end=961,
)


_ACTIONSRESPONSE = _descriptor.Descriptor(
  name='ActionsResponse',
  full_name='grpc.ActionsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='actions', full_name='grpc.ActionsResponse.actions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=963,
  serialized_end=1011,
)


_TRIGGERSREQUEST = _descriptor.Descriptor(
  name='TriggersRequest',
  full_name='grpc.TriggersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='testing_trigger', full_name='grpc.TriggersRequest.testing_trigger', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1013,
  serialized_end=1055,
)


_TRIGGERSRESPONSE = _descriptor.Descriptor(
  name='TriggersResponse',
  full_name='grpc.TriggersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='triggers', full_name='grpc.TriggersResponse.triggers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1057,
  serialized_end=1108,
)


_FIELD = _descriptor.Descriptor(
  name='Field',
  full_name='grpc.Field',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='display_name', full_name='grpc.Field.display_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='key', full_name='grpc.Field.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='grpc.Field.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='app_key', full_name='grpc.Field.app_key', index=3,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='grpc.Field.description', index=4,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='required', full_name='grpc.Field.required', index=5,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1110,
  serialized_end=1222,
)


_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='grpc.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='payload', full_name='grpc.Event.payload', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1224,
  serialized_end=1248,
)

_ACTION.fields_by_name['inputs'].message_type = _FIELD
_ACTION.fields_by_name['outputs'].message_type = _FIELD
_ACTIONREQUEST_PARAMSENTRY.containing_type = _ACTIONREQUEST
_ACTIONREQUEST.fields_by_name['action'].message_type = _ACTION
_ACTIONREQUEST.fields_by_name['params'].message_type = _ACTIONREQUEST_PARAMSENTRY
_ACTIONRESPONSE_OUTPUTSENTRY.containing_type = _ACTIONRESPONSE
_ACTIONRESPONSE.fields_by_name['status'].enum_type = _ACTIONRESPONSE_STATUS
_ACTIONRESPONSE.fields_by_name['outputs'].message_type = _ACTIONRESPONSE_OUTPUTSENTRY
_ACTIONRESPONSE_STATUS.containing_type = _ACTIONRESPONSE
_TRIGGER.fields_by_name['outputs'].message_type = _FIELD
_TRIGGERREQUEST_PARAMSENTRY.containing_type = _TRIGGERREQUEST
_TRIGGERREQUEST.fields_by_name['trigger'].message_type = _TRIGGER
_TRIGGERREQUEST.fields_by_name['params'].message_type = _TRIGGERREQUEST_PARAMSENTRY
_TRIGGERRESPONSE.fields_by_name['status'].enum_type = _TRIGGERRESPONSE_STATUS
_TRIGGERRESPONSE.fields_by_name['events'].message_type = _EVENT
_TRIGGERRESPONSE_STATUS.containing_type = _TRIGGERRESPONSE
_ACTIONSRESPONSE.fields_by_name['actions'].message_type = _ACTION
_TRIGGERSRESPONSE.fields_by_name['triggers'].message_type = _TRIGGER
DESCRIPTOR.message_types_by_name['Action'] = _ACTION
DESCRIPTOR.message_types_by_name['ActionRequest'] = _ACTIONREQUEST
DESCRIPTOR.message_types_by_name['ActionResponse'] = _ACTIONRESPONSE
DESCRIPTOR.message_types_by_name['Trigger'] = _TRIGGER
DESCRIPTOR.message_types_by_name['TriggerRequest'] = _TRIGGERREQUEST
DESCRIPTOR.message_types_by_name['TriggerResponse'] = _TRIGGERRESPONSE
DESCRIPTOR.message_types_by_name['ActionsRequest'] = _ACTIONSREQUEST
DESCRIPTOR.message_types_by_name['ActionsResponse'] = _ACTIONSRESPONSE
DESCRIPTOR.message_types_by_name['TriggersRequest'] = _TRIGGERSREQUEST
DESCRIPTOR.message_types_by_name['TriggersResponse'] = _TRIGGERSRESPONSE
DESCRIPTOR.message_types_by_name['Field'] = _FIELD
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Action = _reflection.GeneratedProtocolMessageType('Action', (_message.Message,), {
  'DESCRIPTOR' : _ACTION,
  '__module__' : 'connector_pb2'
  # @@protoc_insertion_point(class_scope:grpc.Action)
  })
_sym_db.RegisterMessage(Action)

ActionRequest = _reflection.GeneratedProtocolMessageType('ActionRequest', (_message.Message,), {

  'ParamsEntry' : _reflection.GeneratedProtocolMessageType('ParamsEntry', (_message.Message,), {
    'DESCRIPTOR' : _ACTIONREQUEST_PARAMSENTRY,
    '__module__' : 'connector_pb2'
    # @@protoc_insertion_point(class_scope:grpc.ActionRequest.ParamsEntry)
    })
  ,
  'DESCRIPTOR' : _ACTIONREQUEST,
  '__module__' : 'connector_pb2'
  # @@protoc_insertion_point(class_scope:grpc.ActionRequest)
  })
_sym_db.RegisterMessage(ActionRequest)
_sym_db.RegisterMessage(ActionRequest.ParamsEntry)

ActionResponse = _reflection.GeneratedProtocolMessageType('ActionResponse', (_message.Message,), {

  'OutputsEntry' : _reflection.GeneratedProtocolMessageType('OutputsEntry', (_message.Message,), {
    'DESCRIPTOR' : _ACTIONRESPONSE_OUTPUTSENTRY,
    '__module__' : 'connector_pb2'
    # @@protoc_insertion_point(class_scope:grpc.ActionResponse.OutputsEntry)
    })
  ,
  'DESCRIPTOR' : _ACTIONRESPONSE,
  '__module__' : 'connector_pb2'
  # @@protoc_insertion_point(class_scope:grpc.ActionResponse)
  })
_sym_db.RegisterMessage(ActionResponse)
_sym_db.RegisterMessage(ActionResponse.OutputsEntry)

Trigger = _reflection.GeneratedProtocolMessageType('Trigger', (_message.Message,), {
  'DESCRIPTOR' : _TRIGGER,
  '__module__' : 'connector_pb2'
  # @@protoc_insertion_point(class_scope:grpc.Trigger)
  })
_sym_db.RegisterMessage(Trigger)

TriggerRequest = _reflection.GeneratedProtocolMessageType('TriggerRequest', (_message.Message,), {

  'ParamsEntry' : _reflection.GeneratedProtocolMessageType('ParamsEntry', (_message.Message,), {
    'DESCRIPTOR' : _TRIGGERREQUEST_PARAMSENTRY,
    '__module__' : 'connector_pb2'
    # @@protoc_insertion_point(class_scope:grpc.TriggerRequest.ParamsEntry)
    })
  ,
  'DESCRIPTOR' : _TRIGGERREQUEST,
  '__module__' : 'connector_pb2'
  # @@protoc_insertion_point(class_scope:grpc.TriggerRequest)
  })
_sym_db.RegisterMessage(TriggerRequest)
_sym_db.RegisterMessage(TriggerRequest.ParamsEntry)

TriggerResponse = _reflection.GeneratedProtocolMessageType('TriggerResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRIGGERRESPONSE,
  '__module__' : 'connector_pb2'
  # @@protoc_insertion_point(class_scope:grpc.TriggerResponse)
  })
_sym_db.RegisterMessage(TriggerResponse)

ActionsRequest = _reflection.GeneratedProtocolMessageType('ActionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACTIONSREQUEST,
  '__module__' : 'connector_pb2'
  # @@protoc_insertion_point(class_scope:grpc.ActionsRequest)
  })
_sym_db.RegisterMessage(ActionsRequest)

ActionsResponse = _reflection.GeneratedProtocolMessageType('ActionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACTIONSRESPONSE,
  '__module__' : 'connector_pb2'
  # @@protoc_insertion_point(class_scope:grpc.ActionsResponse)
  })
_sym_db.RegisterMessage(ActionsResponse)

TriggersRequest = _reflection.GeneratedProtocolMessageType('TriggersRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRIGGERSREQUEST,
  '__module__' : 'connector_pb2'
  # @@protoc_insertion_point(class_scope:grpc.TriggersRequest)
  })
_sym_db.RegisterMessage(TriggersRequest)

TriggersResponse = _reflection.GeneratedProtocolMessageType('TriggersResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRIGGERSRESPONSE,
  '__module__' : 'connector_pb2'
  # @@protoc_insertion_point(class_scope:grpc.TriggersResponse)
  })
_sym_db.RegisterMessage(TriggersResponse)

Field = _reflection.GeneratedProtocolMessageType('Field', (_message.Message,), {
  'DESCRIPTOR' : _FIELD,
  '__module__' : 'connector_pb2'
  # @@protoc_insertion_point(class_scope:grpc.Field)
  })
_sym_db.RegisterMessage(Field)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), {
  'DESCRIPTOR' : _EVENT,
  '__module__' : 'connector_pb2'
  # @@protoc_insertion_point(class_scope:grpc.Event)
  })
_sym_db.RegisterMessage(Event)


_ACTIONREQUEST_PARAMSENTRY._options = None
_ACTIONRESPONSE_OUTPUTSENTRY._options = None
_TRIGGERREQUEST_PARAMSENTRY._options = None

_CONNECTOR = _descriptor.ServiceDescriptor(
  name='Connector',
  full_name='grpc.Connector',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1251,
  serialized_end=1502,
  methods=[
  _descriptor.MethodDescriptor(
    name='triggers',
    full_name='grpc.Connector.triggers',
    index=0,
    containing_service=None,
    input_type=_TRIGGERSREQUEST,
    output_type=_TRIGGERSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='perform_trigger',
    full_name='grpc.Connector.perform_trigger',
    index=1,
    containing_service=None,
    input_type=_TRIGGERREQUEST,
    output_type=_TRIGGERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='actions',
    full_name='grpc.Connector.actions',
    index=2,
    containing_service=None,
    input_type=_ACTIONSREQUEST,
    output_type=_ACTIONSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='perform_action',
    full_name='grpc.Connector.perform_action',
    index=3,
    containing_service=None,
    input_type=_ACTIONREQUEST,
    output_type=_ACTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CONNECTOR)

DESCRIPTOR.services_by_name['Connector'] = _CONNECTOR

# @@protoc_insertion_point(module_scope)
