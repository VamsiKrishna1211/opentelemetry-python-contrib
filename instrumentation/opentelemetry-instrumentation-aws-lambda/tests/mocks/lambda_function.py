# Copyright The OpenTelemetry Authors
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


def handler(event, context):
    return "200 ok"


def rest_api_handler(event, context):
    return {"statusCode": 200, "body": "200 ok"}


def handler_exc(event, context):
    # pylint: disable=broad-exception-raised
    raise Exception("500 internal server error")
