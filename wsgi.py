service: flask-wsgi-api

provider:
  name: aws
  runtime: python3.9
  stage: ${opt:stage, 'dev'}
  region: ap-southeast-1
  iam:
    role: arn:aws:iam::405125190450:role/LookerActionExecutionRole
  logs:
    restApi: true
  lambdaHashingVersion: 20201221
  tags:
    Ownership: Data-Science
    Environment: ${opt:stage, 'dev'}
  apiGateway:
    shouldStartNameWithService: true

functions:
  app:
    handler: wsgi.handler
    events:
      - http: ANY /
      - http: 'ANY /{proxy+}'

plugins:
  - serverless-python-requirements
  - serverless-wsgi

custom:
  wsgi:
    app: my_app.app
    packRequirements: false
  pythonRequirements:
    dockerizePip: non-linux
