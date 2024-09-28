# Jarkomfinal: Single-threading vs Multi-threading Server 🚀

This repository contains a project that demonstrates the differences between a single-threading server and a multi-threading server. The project showcases how each server handles multiple client requests, focusing on performance, concurrency, and resource management.

## Table of Contents 📚
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Introduction 💡

This project compares two types of servers:
1. **Single-threading server**: Handles one client request at a time in a sequential manner.
2. **Multi-threading server**: Utilizes threads to handle multiple client requests concurrently, allowing for better performance under high load.

## Features ✨
- **Single-threading server implementation**: Processes one client request at a time in `Single Threading.py`.
- **Multi-threading server implementation**: Handles multiple client requests simultaneously in `Multi Threading.py`.
- **Client simulation**: A `client.py` file is provided to simulate client connections and test server performance.
- **Web interface**: An `index.html` file serves as a simple web interface for interaction with the servers.
- **Performance analysis**: Compare the server performance in handling multiple requests under different threading models.

## Requirements 📦
- Python 3.x
- Required libraries: `threading`, `socket`

## Installation ⚙️

To set up the project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/FaustaAkbar/jarkomfinal.git
    ```
2. Navigate to the project directory:
    ```bash
    cd jarkomfinal
    ```
## Usage 🚀

### Single-threading Server
To run the single-threading server:
```bash
python "Single Threading.py"
```
### Multi-threading Server
To run the multi-threading server:
```bash
python "Multi Threading.py"
```
### Client
To simulate client connections:
```bash
python client.py
```
### Web Interface
You can open the index.html file in a web browser to interact with the servers via a simple web interface.

## Project Structure 🗂️
- **Single Threading.py**: Implements the single-threaded server.
- **Multi Threading.py**: Implements the multi-threaded server.
- **client.py**: Simulates client connections to the server.
- **index.html**: Simple web interface for server interaction.
- **README.md**: Project overview (this file).

## License 📝
This project is licensed under the MIT License - see the [MIT License](LICENSE) file for details.
