# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


class Create(AAZCommand):
    """Create a network security group rule.

    :example: Create a basic "Allow" NSG rule with the highest priority.
        az network nsg rule create -g MyResourceGroup --nsg-name MyNsg -n MyNsgRule --priority 100

    :example: Create a "Deny" rule over TCP for a specific IP address range with the lowest priority.
        az network nsg rule create -g MyResourceGroup --nsg-name MyNsg -n MyNsgRule --priority 4096 --source-address-prefixes 208.130.28.0/24 --source-port-ranges 80 --destination-address-prefixes '*' --destination-port-ranges 80 8080 --access Deny --protocol Tcp --description "Deny from specific IP address ranges on 80 and 8080."

    :example: Create a security rule using service tags (https://aka.ms/servicetags).
        az network nsg rule create -g MyResourceGroup --nsg-name MyNsg -n MyNsgRuleWithTags --priority 400 --source-address-prefixes VirtualNetwork --destination-address-prefixes Storage --destination-port-ranges '*' --direction Outbound --access Allow --protocol Tcp --description "Allow VirtualNetwork to Storage."

    :example: Create a security rule using application security groups (https://aka.ms/applicationsecuritygroups).
        az network nsg rule create -g MyResourceGroup --nsg-name MyNsg -n MyNsgRuleWithAsg --priority 500 --source-address-prefixes Internet --destination-port-ranges 80 8080 --destination-asgs Web --access Allow --protocol Tcp --description "Allow Internet to Web ASG on ports 80,8080."
    """

    _aaz_info = {
        "version": "2022-01-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/networksecuritygroups/{}/securityrules/{}", "2022-01-01"],
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
        _args_schema.nsg_name = AAZStrArg(
            options=["--nsg-name"],
            help="Name of the network security group.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="Name of the network security group rule.",
            required=True,
        )
        _args_schema.access = AAZStrArg(
            options=["--access"],
            help="Network traffic is allowed or denied.",
            default="Allow",
            enum={"Allow": "Allow", "Deny": "Deny"},
        )
        _args_schema.description = AAZStrArg(
            options=["--description"],
            help="Description for this rule. Restricted to 140 chars.",
        )
        _args_schema.direction = AAZStrArg(
            options=["--direction"],
            help="Direction of the rule. The direction specifies if rule will be evaluated on incoming or outgoing traffic.",
            default="Inbound",
            enum={"Inbound": "Inbound", "Outbound": "Outbound"},
        )
        _args_schema.priority = AAZIntArg(
            options=["--priority"],
            help="Priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in the collection. The lower the priority number, the higher the priority of the rule.",
        )
        _args_schema.protocol = AAZStrArg(
            options=["--protocol"],
            help="Network protocol this rule applies to.",
            default="*",
            enum={"*": "*", "Ah": "Ah", "Esp": "Esp", "Icmp": "Icmp", "Tcp": "Tcp", "Udp": "Udp"},
        )

        # define Arg Group "Destination"

        _args_schema = cls._args_schema
        _args_schema.destination_address_prefix = AAZStrArg(
            options=["--destination-address-prefix"],
            arg_group="Destination",
            help="The destination address prefix. CIDR or destination IP range. Asterisk '*' can also be used to match all source IPs. Default tags such as 'VirtualNetwork', 'AzureLoadBalancer' and 'Internet' can also be used.",
        )
        _args_schema.destination_address_prefixes = AAZListArg(
            options=["--destination-address-prefixes"],
            arg_group="Destination",
            help="Space-separated list of CIDR prefixes or IP ranges. Alternatively, specify ONE of 'VirtualNetwork', 'AzureLoadBalancer', 'Internet' or '*' to match all IPs. Besides, it also supports all available Service Tags like 'ApiManagement', 'SqlManagement', 'AzureMonitor', etc.",
            default=["*"],
        )
        _args_schema.destination_application_security_groups = AAZListArg(
            options=["--destination-application-security-groups"],
            arg_group="Destination",
            help="Application security group specified as destination.",
        )
        _args_schema.destination_port_range = AAZStrArg(
            options=["--destination-port-range"],
            arg_group="Destination",
            help="The destination port or range. Integer or range between 0 and 65535. Asterisk '*' can also be used to match all ports.",
        )
        _args_schema.destination_port_ranges = AAZListArg(
            options=["--destination-port-ranges"],
            arg_group="Destination",
            help="Space-separated list of ports or port ranges between 0-65535. Use '*' to match all ports.",
            default=["80"],
        )

        destination_address_prefixes = cls._args_schema.destination_address_prefixes
        destination_address_prefixes.Element = AAZStrArg()

        destination_application_security_groups = cls._args_schema.destination_application_security_groups
        destination_application_security_groups.Element = AAZObjectArg()
        cls._build_args_application_security_group_create(destination_application_security_groups.Element)

        destination_port_ranges = cls._args_schema.destination_port_ranges
        destination_port_ranges.Element = AAZStrArg()

        # define Arg Group "SecurityRuleParameters"

        # define Arg Group "Source"

        _args_schema = cls._args_schema
        _args_schema.source_address_prefix = AAZStrArg(
            options=["--source-address-prefix"],
            arg_group="Source",
            help="The CIDR or source IP range. Asterisk '*' can also be used to match all source IPs. Default tags such as 'VirtualNetwork', 'AzureLoadBalancer' and 'Internet' can also be used. If this is an ingress rule, specifies where network traffic originates from.",
        )
        _args_schema.source_address_prefixes = AAZListArg(
            options=["--source-address-prefixes"],
            arg_group="Source",
            help="Space-separated list of CIDR prefixes or IP ranges. Alternatively, specify ONE of 'VirtualNetwork', 'AzureLoadBalancer', 'Internet' or '*' to match all IPs. Besides, it also supports all available Service Tags like 'ApiManagement', 'SqlManagement', 'AzureMonitor', etc.",
            default=["*"],
        )
        _args_schema.source_application_security_groups = AAZListArg(
            options=["--source-application-security-groups"],
            arg_group="Source",
            help="Application security group specified as source.",
        )
        _args_schema.source_port_range = AAZStrArg(
            options=["--source-port-range"],
            arg_group="Source",
            help="The source port or range. Integer or range between 0 and 65535. Asterisk '*' can also be used to match all ports.",
        )
        _args_schema.source_port_ranges = AAZListArg(
            options=["--source-port-ranges"],
            arg_group="Source",
            help="Space-separated list of ports or port ranges between 0-65535. Use '*' to match all ports.",
            default=["*"],
        )

        source_address_prefixes = cls._args_schema.source_address_prefixes
        source_address_prefixes.Element = AAZStrArg()

        source_application_security_groups = cls._args_schema.source_application_security_groups
        source_application_security_groups.Element = AAZObjectArg()
        cls._build_args_application_security_group_create(source_application_security_groups.Element)

        source_port_ranges = cls._args_schema.source_port_ranges
        source_port_ranges.Element = AAZStrArg()
        return cls._args_schema

    _args_application_security_group_create = None

    @classmethod
    def _build_args_application_security_group_create(cls, _schema):
        if cls._args_application_security_group_create is not None:
            _schema.id = cls._args_application_security_group_create.id
            _schema.location = cls._args_application_security_group_create.location
            _schema.tags = cls._args_application_security_group_create.tags
            return

        cls._args_application_security_group_create = AAZObjectArg()

        application_security_group_create = cls._args_application_security_group_create
        application_security_group_create.id = AAZResourceIdArg(
            options=["id"],
            help="Resource ID.",
            fmt=AAZResourceIdArgFormat(
                template="/subscriptions/{}/resourceGroups/{}/providers/Microsoft.Network/applicationSecurityGroups/{}",
            ),
        )
        application_security_group_create.location = AAZResourceLocationArg(
            options=["l", "location"],
            help="Resource location.",
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        application_security_group_create.tags = AAZDictArg(
            options=["tags"],
            help="Resource tags.",
        )

        tags = cls._args_application_security_group_create.tags
        tags.Element = AAZStrArg()

        _schema.id = cls._args_application_security_group_create.id
        _schema.location = cls._args_application_security_group_create.location
        _schema.tags = cls._args_application_security_group_create.tags

    def _execute_operations(self):
        self.pre_operations()
        yield self.SecurityRulesCreateOrUpdate(ctx=self.ctx)()
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

    class SecurityRulesCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkSecurityGroups/{networkSecurityGroupName}/securityRules/{securityRuleName}",
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
                    "networkSecurityGroupName", self.ctx.args.nsg_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "securityRuleName", self.ctx.args.name,
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
                    "api-version", "2022-01-01",
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
            _builder.set_prop("name", AAZStrType, ".name")
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("access", AAZStrType, ".access", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("description", AAZStrType, ".description")
                properties.set_prop("destinationAddressPrefix", AAZStrType, ".destination_address_prefix")
                properties.set_prop("destinationAddressPrefixes", AAZListType, ".destination_address_prefixes")
                properties.set_prop("destinationApplicationSecurityGroups", AAZListType, ".destination_application_security_groups")
                properties.set_prop("destinationPortRange", AAZStrType, ".destination_port_range")
                properties.set_prop("destinationPortRanges", AAZListType, ".destination_port_ranges")
                properties.set_prop("direction", AAZStrType, ".direction", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("priority", AAZIntType, ".priority")
                properties.set_prop("protocol", AAZStrType, ".protocol", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("sourceAddressPrefix", AAZStrType, ".source_address_prefix")
                properties.set_prop("sourceAddressPrefixes", AAZListType, ".source_address_prefixes")
                properties.set_prop("sourceApplicationSecurityGroups", AAZListType, ".source_application_security_groups")
                properties.set_prop("sourcePortRange", AAZStrType, ".source_port_range")
                properties.set_prop("sourcePortRanges", AAZListType, ".source_port_ranges")

            destination_address_prefixes = _builder.get(".properties.destinationAddressPrefixes")
            if destination_address_prefixes is not None:
                destination_address_prefixes.set_elements(AAZStrType, ".")

            destination_application_security_groups = _builder.get(".properties.destinationApplicationSecurityGroups")
            if destination_application_security_groups is not None:
                _CreateHelper._build_schema_application_security_group_create(destination_application_security_groups.set_elements(AAZObjectType, "."))

            destination_port_ranges = _builder.get(".properties.destinationPortRanges")
            if destination_port_ranges is not None:
                destination_port_ranges.set_elements(AAZStrType, ".")

            source_address_prefixes = _builder.get(".properties.sourceAddressPrefixes")
            if source_address_prefixes is not None:
                source_address_prefixes.set_elements(AAZStrType, ".")

            source_application_security_groups = _builder.get(".properties.sourceApplicationSecurityGroups")
            if source_application_security_groups is not None:
                _CreateHelper._build_schema_application_security_group_create(source_application_security_groups.set_elements(AAZObjectType, "."))

            source_port_ranges = _builder.get(".properties.sourcePortRanges")
            if source_port_ranges is not None:
                source_port_ranges.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.etag = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.id = AAZStrType()
            _schema_on_200_201.name = AAZStrType()
            _schema_on_200_201.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200_201.type = AAZStrType()

            properties = cls._schema_on_200_201.properties
            properties.access = AAZStrType(
                flags={"required": True},
            )
            properties.description = AAZStrType()
            properties.destination_address_prefix = AAZStrType(
                serialized_name="destinationAddressPrefix",
            )
            properties.destination_address_prefixes = AAZListType(
                serialized_name="destinationAddressPrefixes",
            )
            properties.destination_application_security_groups = AAZListType(
                serialized_name="destinationApplicationSecurityGroups",
            )
            properties.destination_port_range = AAZStrType(
                serialized_name="destinationPortRange",
            )
            properties.destination_port_ranges = AAZListType(
                serialized_name="destinationPortRanges",
            )
            properties.direction = AAZStrType(
                flags={"required": True},
            )
            properties.priority = AAZIntType()
            properties.protocol = AAZStrType(
                flags={"required": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.source_address_prefix = AAZStrType(
                serialized_name="sourceAddressPrefix",
            )
            properties.source_address_prefixes = AAZListType(
                serialized_name="sourceAddressPrefixes",
            )
            properties.source_application_security_groups = AAZListType(
                serialized_name="sourceApplicationSecurityGroups",
            )
            properties.source_port_range = AAZStrType(
                serialized_name="sourcePortRange",
            )
            properties.source_port_ranges = AAZListType(
                serialized_name="sourcePortRanges",
            )

            destination_address_prefixes = cls._schema_on_200_201.properties.destination_address_prefixes
            destination_address_prefixes.Element = AAZStrType()

            destination_application_security_groups = cls._schema_on_200_201.properties.destination_application_security_groups
            destination_application_security_groups.Element = AAZObjectType()
            _CreateHelper._build_schema_application_security_group_read(destination_application_security_groups.Element)

            destination_port_ranges = cls._schema_on_200_201.properties.destination_port_ranges
            destination_port_ranges.Element = AAZStrType()

            source_address_prefixes = cls._schema_on_200_201.properties.source_address_prefixes
            source_address_prefixes.Element = AAZStrType()

            source_application_security_groups = cls._schema_on_200_201.properties.source_application_security_groups
            source_application_security_groups.Element = AAZObjectType()
            _CreateHelper._build_schema_application_security_group_read(source_application_security_groups.Element)

            source_port_ranges = cls._schema_on_200_201.properties.source_port_ranges
            source_port_ranges.Element = AAZStrType()

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""

    @classmethod
    def _build_schema_application_security_group_create(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("id", AAZStrType, ".id")
        _builder.set_prop("location", AAZStrType, ".location")
        _builder.set_prop("tags", AAZDictType, ".tags")

        tags = _builder.get(".tags")
        if tags is not None:
            tags.set_elements(AAZStrType, ".")

    _schema_application_security_group_read = None

    @classmethod
    def _build_schema_application_security_group_read(cls, _schema):
        if cls._schema_application_security_group_read is not None:
            _schema.etag = cls._schema_application_security_group_read.etag
            _schema.id = cls._schema_application_security_group_read.id
            _schema.location = cls._schema_application_security_group_read.location
            _schema.name = cls._schema_application_security_group_read.name
            _schema.properties = cls._schema_application_security_group_read.properties
            _schema.tags = cls._schema_application_security_group_read.tags
            _schema.type = cls._schema_application_security_group_read.type
            return

        cls._schema_application_security_group_read = _schema_application_security_group_read = AAZObjectType()

        application_security_group_read = _schema_application_security_group_read
        application_security_group_read.etag = AAZStrType(
            flags={"read_only": True},
        )
        application_security_group_read.id = AAZStrType()
        application_security_group_read.location = AAZStrType()
        application_security_group_read.name = AAZStrType(
            flags={"read_only": True},
        )
        application_security_group_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        application_security_group_read.tags = AAZDictType()
        application_security_group_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_application_security_group_read.properties
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.resource_guid = AAZStrType(
            serialized_name="resourceGuid",
            flags={"read_only": True},
        )

        tags = _schema_application_security_group_read.tags
        tags.Element = AAZStrType()

        _schema.etag = cls._schema_application_security_group_read.etag
        _schema.id = cls._schema_application_security_group_read.id
        _schema.location = cls._schema_application_security_group_read.location
        _schema.name = cls._schema_application_security_group_read.name
        _schema.properties = cls._schema_application_security_group_read.properties
        _schema.tags = cls._schema_application_security_group_read.tags
        _schema.type = cls._schema_application_security_group_read.type


__all__ = ["Create"]
