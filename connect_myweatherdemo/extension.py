# -*- coding: utf-8 -*-
#
# Copyright (c) 2021, Education Team
# All rights reserved.
#

from connect.eaas.extension import (
    Extension,
    ProcessingResponse,
    ValidationResponse,
)

import requests
import json

class MyweatherdemoExtension(Extension):
    def approve_asset_request(self, request, template_id):
        self.logger.info(f'request_id={request["id"]} - template_id={template_id}')
        self.client.requests[request['id']]('approve').post(
            {
                'template_id': template_id,
            }
        )
        self.logger.info(f"Approved request {request['id']}")

    def process_asset_purchase_request(self, request):
        self.logger.info(f"Obtained request from company {request['asset']['tiers']['customer']['name']}")
        company = request['asset']['tiers']['customer']['name']

        self.logger.info(
            f"Received event for request {request['id']} in status {request['status']}"
        )

        if request['status'] == 'pending':
            for param in request['asset']['params']:
                if (param['id'] == 'unitofmeasure'):
                    unitofmeasure = param['value']

            citieslimit = 0
            for item in request['asset']['items']:
                if (item['mpn'] == 'citieslimit'):
                    citieslimit = item['quantity']

            newCompany = {
                'name': company,
                'unitofmeasure': unitofmeasure,
                'citieslimit': citieslimit
            }

            session = requests.Session()
            session.headers.update({'content-type': 'application/json', 'x-provider-token': 'osamwd'})
            vendorDataResponse = session.post('http://myweatherdemo.learn-cloudblue.com/api/company/', data = json.dumps(newCompany))

            self.logger.info(
                f"Received vendor response as: {vendorDataResponse.content}"
            )

            vendorData = vendorDataResponse.json() 

            self.logger.info(
                f"Received event for request id {vendorData['token']} with username {vendorData['username']} and password {vendorData['password']}"
            )

            self.client.requests[request['id']].update(
                {
                    "asset": {
                        "params": [
                            {
                                "id": "id",
                                "value": vendorData['token']
                            },
                            {
                                "id": "password",
                                "value": vendorData['password']
                            },
                            {
                                "id": "username",
                                "value": vendorData['username']
                            }
                        ]
                    }
                }
            )
            self.logger.info("Updating fulfillment parameters as follows:"
                                f"name to {company}, unitofmeasure to {unitofmeasure} and citieslimit to {citieslimit}")

            template_id = self.config['ASSET_REQUEST_APPROVE_TEMPLATE_ID']
            self.approve_asset_request(request, template_id)

        return ProcessingResponse.done()

    def process_asset_change_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ProcessingResponse.done()

    def process_asset_cancel_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ProcessingResponse.done()

    def process_asset_adjustment_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ProcessingResponse.done()

    def validate_asset_purchase_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ValidationResponse.done(request)

    def validate_asset_change_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ValidationResponse.done(request)

    