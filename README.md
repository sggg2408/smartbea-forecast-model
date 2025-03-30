# smartbea-forecast-model
this is important repo sample
# Dummy AWS Lambda API with CI/CD

This project sets up a basic AWS Lambda function with an API Gateway endpoint using the [Serverless Framework](https://www.serverless.com/). It includes a GitHub Actions workflow to automatically deploy changes to AWS whenever code is pushed to the `main` branch.

---

## Project Structure


---

## What It Does

- Deploys a simple API endpoint: `GET /hello`
- Returns a dummy message: `{"message": "Hello from dummy API!"}`
- Sets up CI/CD to automatically deploy on push to `main`

---

## Prerequisites

1. An AWS account with IAM user having Lambda, API Gateway, and CloudFormation permissions.
2. GitHub repo with the following **Secrets** set under `Settings > Secrets and Variables > Actions`:
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
   - `AWS_REGION` (e.g., `us-east-1`)

---

## Deploying Locally (Optional)

Install Serverless Framework and deploy manually:

```bash
npm install -g serverless
sls deploy
