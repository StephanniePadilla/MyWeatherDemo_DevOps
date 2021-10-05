# -*- coding: utf-8 -*-
#
# Copyright (c) 2021, Education Team
# All rights reserved.
#

from connect_myweatherdemo.extension import MyweatherdemoExtension


def test_process_asset_purchase_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = MyweatherdemoExtension(client, logger, config)
    result = ext.process_asset_purchase_request(request)
    assert result.status == 'success'


def test_process_asset_change_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = MyweatherdemoExtension(client, logger, config)
    result = ext.process_asset_change_request(request)
    assert result.status == 'success'


def test_process_asset_cancel_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = MyweatherdemoExtension(client, logger, config)
    result = ext.process_asset_cancel_request(request)
    assert result.status == 'success'


def test_process_asset_adjustment_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = MyweatherdemoExtension(client, logger, config)
    result = ext.process_asset_adjustment_request(request)
    assert result.status == 'success'


def test_validate_asset_purchase_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = MyweatherdemoExtension(client, logger, config)
    result = ext.validate_asset_purchase_request(request)
    assert result.status == 'success'
    assert result.data == request


def test_validate_asset_change_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = MyweatherdemoExtension(client, logger, config)
    result = ext.validate_asset_change_request(request)
    assert result.status == 'success'
    assert result.data == request
