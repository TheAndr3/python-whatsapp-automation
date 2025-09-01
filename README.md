# Bulk WhatsApp Messaging Tool

This project provides a Python script to send personalized WhatsApp messages in bulk to a list of contacts from a CSV file. It uses the Evolution API as the backend service for sending messages, which is managed via Docker Compose.

## Features

- **Bulk Messaging**: Sends messages to multiple contacts from a CSV file.
- **Personalization**: Customizes messages using contact names (`{nome}`).
- **Adjustable Timer**: Sets a configurable delay between messages to avoid blocking.
- **Error Handling**: Detects failed messages (e.g., number doesn't have WhatsApp) and logs them to a `wrong_numbers.csv` file without crashing the script.

## Prerequisites

- [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/)
- [Python 3](https://www.python.org/downloads/)
- Read the [EvolutionAPI](https://doc.evolution-api.com/v1/pt/get-started/introduction) documentation to understand how the things work.

## Setup and Configuration

Follow these steps to set up and run the project.

### 1. Prepare the Project Files

If you have cloned a git repository, you can skip this. Otherwise, make sure all project files (`app.py`, `docker-compose.yml`, etc.) are in the same directory.

### 2. Configure Environment Variables

The project uses a `.env` file to manage all necessary credentials and configurations. Create a file named `.env` in the root of the project directory and add the following content:

```env
# Evolution API Docker Settings
# This password must be the same in the docker-compose.yml file
POSTGRES_PASSWORD=postgres

# Evolution API Connection Settings
# These are the credentials for the API itself.
# The base URL should point to your Docker container's port.
EVO_BASE_URL=http://localhost:8080
EVO_INSTANCE_NAME=my-instance
AUTHENTICATION_API_KEY=your-very-secret-api-key
```

**Important:**
- Replace `your-very-secret-api-key` with a strong, unique key of your choice.
- The `EVO_BASE_URL` should match the port you exposed in your `docker-compose.yml` file (default is `8080`).

### 3. Prepare the Contacts CSV
Remember write something here

- The header row must contain `@whatsapp` and `nome`.

### 4. Install Python Dependencies

This project requires a few Python packages. While a `requirements.txt` is not yet present, you can install them manually:

```sh
pip install requests python-dotenv
```

## Running the Application

The application consists of two main parts: the backend services (Evolution API) running in Docker and the Python script that sends the messages.

### 1. Start the Backend Services

Open a terminal in the project directory and run the following command to start the Evolution API, the database, and Redis in the background:

```sh
docker-compose up -d
```

Wait a few minutes for all services to start up completely. You can check the status of the containers with `docker-compose ps`.

### 2. Run the Messaging Script

Once the backend services are running, you can run the Python script to start sending messages:

```sh
python app.py
```

The script will print the status of each message in the console. Any numbers that result in an error will be logged in `wrong_numbers.csv`.

## Project Structure

```
.
├── .env                  # Environment variables (you need to create this)
├── app.py                # Main Python script for sending messages
├── docker-compose.yml    # Defines and configures the backend services
├── README.md             # This file
├── services/             # Service package for API communication
│   ├── __init__.py
│   └── evolution_api.py
└── wzap.csv              # Contacts CSV file
```
