#!/usr/bin/env bash
set -e

# Install Python dependencies
pip install fastapi uvicorn requests apache-beam dask torch

# Install Node.js dependencies for the Next.js frontend
cd "$(dirname "$0")/../frontend/web"
npm install

cd - >/dev/null

echo "Environment setup complete."

