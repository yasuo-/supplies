#!/bin/bash

# ReDocを使用してopenapi.jsonからHTMLファイルを生成
cat << EOF > ./docs/redoc.html
<!DOCTYPE html>
<html>
  <head>
    <title>API Documentation</title>
    <!-- ReDoc のCDN -->
    <script src="https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"></script>
  </head>
  <body>
    <redoc spec-url='./openapi.json'></redoc>
  </body>
</html>
EOF
