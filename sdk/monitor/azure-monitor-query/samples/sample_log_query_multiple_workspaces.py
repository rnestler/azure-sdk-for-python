# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
import pandas as pd
from datetime import datetime
from msrest.serialization import UTC
from azure.monitor.query import LogsQueryClient
from azure.identity import DefaultAzureCredential

credential  = DefaultAzureCredential()

client = LogsQueryClient(credential)

# Response time trend 
# request duration over the last 12 hours. 
query = "union * | where TimeGenerated > ago(100d) | project TenantId | summarize count() by TenantId"

end_time = datetime.now(UTC())

# returns LogsQueryResult 
response = client.query(
    os.environ['LOG_WORKSPACE_ID'],
    query,
    additional_workspaces=[os.environ["SECONDARY_WORKSPACE_ID"]],
    )

try:
    table = response.tables[0]
    df = pd.DataFrame(table.rows, columns=[col.name for col in table.columns])
    print(df)
except TypeError:
    print(response.error)


