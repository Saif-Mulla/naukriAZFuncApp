# naukriAZFuncApp

An Azure Function-based automation solution to run scheduled tasks (e.g., data processing, job fetching) every day at 8 AM IST. This project leverages Azure's serverless compute and timer trigger to automate backend workflows efficiently.

## 🚀 Features

- Scheduled execution using Azure Timer Trigger
- Serverless, scalable, and cost-efficient architecture
- Python-based logic with modular script integration
- Easily configurable schedule via `function.json`
- Logging and monitoring enabled through Azure portal

## 🛠️ Tech Stack

- Python 3.10
- Azure Functions
- Timer Trigger
- Azure CLI
- Visual Studio Code

## 🗓️ Schedule

The function is configured to run daily at **8 AM IST** using the CRON expression in `function.json`.

```json
"schedule": "0 2 * * *" // UTC time (8 AM IST)
