#!/bin/bash
TOKEN=$(curl -X POST "https://iam.cloud.ibm.com/identity/token" \
  --header "Content-Type: application/x-www-form-urlencoded" \
  --data "apikey=$IBM_API_KEY&grant_type=urn:ibm:params:oauth:grant-type:apikey" | jq -r '.access_token')

curl -X POST "$IBM_AGENT_URL" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"input": {"text": "Hello Agent"}}'
