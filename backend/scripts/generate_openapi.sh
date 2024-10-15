#!/bin/bash

# FastAPI の OpenAPI JSON をエクスポート
curl -o ./docs/openapi.json http://localhost:8000/openapi.json
