# Generated by Django 4.1.13 on 2024-06-19 07:18

from django.db import migrations

from protos.base_pb2 import SourceKeyType, SourceModelType, Source
from protos.connectors.connector_pb2 import Connector as ConnectorProto


def transform_remote_server_connectors(apps, schema_editor):
    Connector = apps.get_model("connectors", "Connector")
    ConnectorMetadataModelStore = apps.get_model("connectors", "ConnectorMetadataModelStore")

    for db_connector in Connector.objects.all():
        try:
            connector_proto: ConnectorProto = db_connector.unmasked_proto
            keys = connector_proto.keys
            host = None
            user = None
            for key in keys:
                if key.key_type == SourceKeyType.REMOTE_SERVER_USER:
                    user = key.key.value
                elif key.key_type == SourceKeyType.REMOTE_SERVER_HOST:
                    host = key.key.value
            if host and user:
                ssh_server = f'{user}@{host}'
                ConnectorMetadataModelStore.objects.update_or_create(account=db_connector.account,
                                                                     connector=db_connector,
                                                                     connector_type=Source.REMOTE_SERVER,
                                                                     model_type=SourceModelType.SSH_SERVER,
                                                                     model_uid=ssh_server,
                                                                     defaults={'is_active': True, 'metadata': None})
        except Exception as e:
            print('skip transformation for connector id: ', db_connector.id)
            continue


class Migration(migrations.Migration):
    dependencies = [
        ('connectors', '0014_alter_connector_connector_type_and_more'),
    ]

    operations = [
        migrations.RunPython(transform_remote_server_connectors, migrations.RunPython.noop)
    ]
