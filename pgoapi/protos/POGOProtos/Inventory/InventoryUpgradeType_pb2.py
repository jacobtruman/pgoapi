# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Inventory/InventoryUpgradeType.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Inventory/InventoryUpgradeType.proto',
  package='POGOProtos.Inventory',
  syntax='proto3',
  serialized_pb=_b('\n/POGOProtos/Inventory/InventoryUpgradeType.proto\x12\x14POGOProtos.Inventory*b\n\x14InventoryUpgradeType\x12\x11\n\rUPGRADE_UNSET\x10\x00\x12\x19\n\x15INCREASE_ITEM_STORAGE\x10\x01\x12\x1c\n\x18INCREASE_POKEMON_STORAGE\x10\x02\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_INVENTORYUPGRADETYPE = _descriptor.EnumDescriptor(
  name='InventoryUpgradeType',
  full_name='POGOProtos.Inventory.InventoryUpgradeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UPGRADE_UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCREASE_ITEM_STORAGE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCREASE_POKEMON_STORAGE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=73,
  serialized_end=171,
)
_sym_db.RegisterEnumDescriptor(_INVENTORYUPGRADETYPE)

InventoryUpgradeType = enum_type_wrapper.EnumTypeWrapper(_INVENTORYUPGRADETYPE)
UPGRADE_UNSET = 0
INCREASE_ITEM_STORAGE = 1
INCREASE_POKEMON_STORAGE = 2


DESCRIPTOR.enum_types_by_name['InventoryUpgradeType'] = _INVENTORYUPGRADETYPE


# @@protoc_insertion_point(module_scope)