from typing import Any

from snowplow_tracker import payload

import business_logic


# The Lambda handler extracts needed information from the event
# object and invokes the business logic
def handler(event, context, statusCode=200, body=Any):
    # Extract needed information from event object payload = event[‘payload’]

    # Invoke business logic
    result = business_logic.opted_some_logic(payload)

    # Construct result for API Gateway
    return {
        statusCode: 200,
        body: result
    }


