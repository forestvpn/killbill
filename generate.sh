#!/bin/bash

swagger-codegen generate -l python -i swagger.json -o . \
  --git-user-id=forestvpn \
  --git-repo-id=killbill \
  --additional-properties="packageName=killbill,projectName=forestvpn-killbill,packageVersion=0.0.3"
