# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/fort_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/fort_settings.proto',
  package='pogoprotos.settings',
  syntax='proto3',
  serialized_pb=_b('\n\'pogoprotos/settings/fort_settings.proto\x12\x13pogoprotos.settings\"\xc7\x02\n\x0c\x46ortSettings\x12 \n\x18interaction_range_meters\x18\x01 \x01(\x01\x12\"\n\x1amax_total_deployed_pokemon\x18\x02 \x01(\x05\x12#\n\x1bmax_player_deployed_pokemon\x18\x03 \x01(\x05\x12!\n\x19\x64\x65ploy_stamina_multiplier\x18\x04 \x01(\x01\x12 \n\x18\x64\x65ploy_attack_multiplier\x18\x05 \x01(\x01\x12$\n\x1c\x66\x61r_interaction_range_meters\x18\x06 \x01(\x01\x12\x14\n\x0c\x64isable_gyms\x18\x07 \x01(\x08\x12 \n\x18max_same_pokemon_at_fort\x18\x08 \x01(\x05\x12)\n!max_player_total_deployed_pokemon\x18\t \x01(\x05\x62\x06proto3')
)




_FORTSETTINGS = _descriptor.Descriptor(
  name='FortSettings',
  full_name='pogoprotos.settings.FortSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='interaction_range_meters', full_name='pogoprotos.settings.FortSettings.interaction_range_meters', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_total_deployed_pokemon', full_name='pogoprotos.settings.FortSettings.max_total_deployed_pokemon', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_player_deployed_pokemon', full_name='pogoprotos.settings.FortSettings.max_player_deployed_pokemon', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deploy_stamina_multiplier', full_name='pogoprotos.settings.FortSettings.deploy_stamina_multiplier', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deploy_attack_multiplier', full_name='pogoprotos.settings.FortSettings.deploy_attack_multiplier', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='far_interaction_range_meters', full_name='pogoprotos.settings.FortSettings.far_interaction_range_meters', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='disable_gyms', full_name='pogoprotos.settings.FortSettings.disable_gyms', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_same_pokemon_at_fort', full_name='pogoprotos.settings.FortSettings.max_same_pokemon_at_fort', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_player_total_deployed_pokemon', full_name='pogoprotos.settings.FortSettings.max_player_total_deployed_pokemon', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=392,
)

DESCRIPTOR.message_types_by_name['FortSettings'] = _FORTSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FortSettings = _reflection.GeneratedProtocolMessageType('FortSettings', (_message.Message,), dict(
  DESCRIPTOR = _FORTSETTINGS,
  __module__ = 'pogoprotos.settings.fort_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.FortSettings)
  ))
_sym_db.RegisterMessage(FortSettings)


# @@protoc_insertion_point(module_scope)
