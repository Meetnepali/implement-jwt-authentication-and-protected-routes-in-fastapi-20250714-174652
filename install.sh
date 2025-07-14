#!/bin/bash
set -e

# Build Docker image and prepare environment

echo "[INFO] Building Docker image..."
docker-compose build

echo "[INFO] Installing dependencies in Docker container (this is automatic on build)"
echo "[INFO] Setup complete."
