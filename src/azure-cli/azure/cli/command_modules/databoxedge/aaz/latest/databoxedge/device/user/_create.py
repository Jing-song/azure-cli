# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "databoxedge device user create",
)
class Create(AAZCommand):
    """Create user on a Data Box Edge/Data Box Gateway device.

    :example: Create user
        az databoxedge device user create -g rg --device-name name --user-type Share -n username --encrypted-password "{value:xxx,encryptionCertThumbprint:xxx,encryptionAlgorithm:AES256}"
    """

    _aaz_info = {
        "version": "2023-07-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.databoxedge/databoxedgedevices/{}/users/{}", "2023-07-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.device_name = AAZStrArg(
            options=["--device-name"],
            help="The device name.",
            required=True,
        )
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="The user name.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.encrypted_password = AAZObjectArg(
            options=["--encrypted-password"],
            arg_group="Properties",
            help="The password details.",
        )
        _args_schema.user_type = AAZStrArg(
            options=["--user-type"],
            arg_group="Properties",
            help="Type of the user.",
            required=True,
            enum={"ARM": "ARM", "LocalManagement": "LocalManagement", "Share": "Share"},
        )

        encrypted_password = cls._args_schema.encrypted_password
        encrypted_password.encryption_algorithm = AAZStrArg(
            options=["encryption-algorithm"],
            help="The algorithm used to encrypt \"Value\".",
            required=True,
            enum={"AES256": "AES256", "None": "None", "RSAES_PKCS1_v_1_5": "RSAES_PKCS1_v_1_5"},
        )
        encrypted_password.encryption_cert_thumbprint = AAZStrArg(
            options=["encryption-cert-thumbprint"],
            help="Thumbprint certificate used to encrypt \"Value\". If the value is unencrypted, it will be null.",
        )
        encrypted_password.value = AAZStrArg(
            options=["value"],
            help="The value of the secret.",
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.UsersCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class UsersCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/users/{name}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "deviceName", self.ctx.args.device_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "name", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-07-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True, "client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("encryptedPassword", AAZObjectType, ".encrypted_password")
                properties.set_prop("userType", AAZStrType, ".user_type", typ_kwargs={"flags": {"required": True}})

            encrypted_password = _builder.get(".properties.encryptedPassword")
            if encrypted_password is not None:
                encrypted_password.set_prop("encryptionAlgorithm", AAZStrType, ".encryption_algorithm", typ_kwargs={"flags": {"required": True}})
                encrypted_password.set_prop("encryptionCertThumbprint", AAZStrType, ".encryption_cert_thumbprint", typ_kwargs={"flags": {"secret": True}})
                encrypted_password.set_prop("value", AAZStrType, ".value", typ_kwargs={"flags": {"required": True}})

            return self.serialize_content(_content_value)

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.encrypted_password = AAZObjectType(
                serialized_name="encryptedPassword",
            )
            properties.share_access_rights = AAZListType(
                serialized_name="shareAccessRights",
                flags={"read_only": True},
            )
            properties.user_type = AAZStrType(
                serialized_name="userType",
                flags={"required": True},
            )

            encrypted_password = cls._schema_on_200.properties.encrypted_password
            encrypted_password.encryption_algorithm = AAZStrType(
                serialized_name="encryptionAlgorithm",
                flags={"required": True},
            )
            encrypted_password.encryption_cert_thumbprint = AAZStrType(
                serialized_name="encryptionCertThumbprint",
                flags={"secret": True},
            )
            encrypted_password.value = AAZStrType(
                flags={"required": True},
            )

            share_access_rights = cls._schema_on_200.properties.share_access_rights
            share_access_rights.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.share_access_rights.Element
            _element.access_type = AAZStrType(
                serialized_name="accessType",
                flags={"required": True},
            )
            _element.share_id = AAZStrType(
                serialized_name="shareId",
                flags={"required": True},
            )

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            return cls._schema_on_200


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]
