# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""This class demonstrates how to create a local inventory datasource."""

# [START CreateFileLocalInventoryDatasource]
from examples.authentication import generate_user_credentials
from google.shopping.merchant_datasources_v1beta import CreateDataSourceRequest
from google.shopping.merchant_datasources_v1beta import DataSource
from google.shopping.merchant_datasources_v1beta import DataSourcesServiceClient
from google.shopping.merchant_datasources_v1beta import FileInput
from google.shopping.merchant_datasources_v1beta import LocalInventoryDataSource

# ENSURE you fill in the merchant account for the sample to work.
_ACCOUNT = "[INSERT_ACCOUNT_HERE]"
_PARENT = f"accounts/{_ACCOUNT}"


def create_file_local_inventory_data_source():
  """Creates a `DataSource` resource."""

  # Gets OAuth Credentials.
  credentials = generate_user_credentials.main()

  # Creates a client.
  client = DataSourcesServiceClient(credentials=credentials)

  # If FetchSettings are not set, then this will be an `UPLOAD` file type
  # that you must manually upload via the Merchant Center UI or via SFTP.
  file_input = FileInput()
  file_input.file_name = "British T-shirts Local Inventory Data.txt"

  # Creates a SupplementalProductDataSource.
  local_inventory_datasource = LocalInventoryDataSource()
  # As LocalInventoryDataSources are a type of file feed, wildcards are not
  # available. LocalInventoryDataSources can only be created for a specific
  # `feedLabel` and `contentLanguage` combination.
  local_inventory_datasource.content_language = "en"
  local_inventory_datasource.feed_label = "GB"

  # Creates a DataSource and populates its attributes.
  data_source = DataSource()
  data_source.display_name = "Example Local Inventory DataSource"
  data_source.local_inventory_data_source = local_inventory_datasource
  data_source.file_input = file_input

  # Creates the request.
  request = CreateDataSourceRequest(parent=_PARENT, data_source=data_source)

  # Makes the request and catches and prints any error messages.
  try:
    response = client.create_data_source(request=request)
    print(f"DataSource successfully created: {response}")
  except RuntimeError as e:
    print("DataSource creation failed")
    print(e)


# [END CreateFileLocalInventoryDatasource]

if __name__ == "__main__":
  create_file_local_inventory_data_source()