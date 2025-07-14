#!/bin/bash
set -e

./install.sh

echo "[INFO] Starting FastAPI app with Docker Compose..."
docker-compose up
