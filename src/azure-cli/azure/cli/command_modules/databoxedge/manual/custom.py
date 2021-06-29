# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=unused-argument

from azure.cli.core.util import sdk_no_wait


def databoxedge_device_create(client,
                              device_name,
                              resource_group_name,
                              location,
                              tags=None,
                              sku=None,
                              etag=None,
                              data_box_edge_device_status=None,
                              description=None,
                              model_description=None,
                              friendly_name=None,
                              no_wait=False):
    data_box_edge_device = {}
    data_box_edge_device['location'] = location
    data_box_edge_device['tags'] = tags
    data_box_edge_device['etag'] = etag
    data_box_edge_device['data_box_edge_device_status'] = data_box_edge_device_status
    data_box_edge_device['description'] = description
    data_box_edge_device['model_description'] = model_description
    data_box_edge_device['friendly_name'] = friendly_name
    if sku:
        data_box_edge_device['sku'] = {}
        data_box_edge_device['sku']['name'] = sku
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       device_name=device_name,
                       resource_group_name=resource_group_name,
                       data_box_edge_device=data_box_edge_device)


def databoxedge_device_update(client,
                              device_name,
                              resource_group_name,
                              tags=None):
    if tags is None:
        return client.get(device_name=device_name,
                          resource_group_name=resource_group_name)
    parameters = {'tags': tags}
    return client.update(device_name=device_name,
                         resource_group_name=resource_group_name,
                         parameters=parameters)


def databoxedge_bandwidth_schedule_update(instance,
                                          device_name,
                                          name,
                                          resource_group_name,
                                          start=None,
                                          stop=None,
                                          rate_in_mbps=None,
                                          days=None,
                                          no_wait=False):
    if start is not None:
        instance.start = start
    if stop is not None:
        instance.stop = stop
    if rate_in_mbps is not None:
        instance.rate_in_mbps = rate_in_mbps
    if days is not None:
        instance.days = days
    return instance


def databoxedge_order_create(client,
                             device_name,
                             resource_group_name,
                             address_line1,
                             postal_code,
                             city,
                             state,
                             country,
                             contact_person,
                             company_name,
                             phone,
                             email_list,
                             status=None,
                             comments=None,
                             address_line2=None,
                             address_line3=None,
                             no_wait=False):
    order = {}
    if status:
        order['current_status'] = {}
        order['current_status']['status'] = status
        order['current_status']['comments'] = comments
    order['shipping_address'] = {}
    order['shipping_address']['address_line1'] = address_line1
    order['shipping_address']['address_line2'] = address_line2
    order['shipping_address']['address_line3'] = address_line3
    order['shipping_address']['postal_code'] = postal_code
    order['shipping_address']['city'] = city
    order['shipping_address']['state'] = state
    order['shipping_address']['country'] = country
    order['contact_information'] = {}
    order['contact_information']['contact_person'] = contact_person
    order['contact_information']['company_name'] = company_name
    order['contact_information']['phone'] = phone
    order['contact_information']['email_list'] = email_list
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       device_name=device_name,
                       resource_group_name=resource_group_name,
                       order=order)
