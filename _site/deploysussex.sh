#!/bin/bash

# Deploy Jekyll site to Sussex Unix server
# Usage: ./deploy.sh [your-username]

# Configuration
SERVER_HOST="unix.sussex.ac.uk"
SERVER_PATH="public_html/meml"
LOCAL_SITE_DIR="_site/"

# Get username from command line argument or prompt
if [ -z "$1" ]; then
    read -p "Enter your Sussex username: " USERNAME
else
    USERNAME="$1"
fi

echo "Deploying to $USERNAME@$SERVER_HOST:$SERVER_PATH"
echo "============================================"

# Build Jekyll site with correct baseurl for the meml subfolder
echo "Building Jekyll site..."
bundle exec jekyll build --baseurl "/~ck84/meml/"

if [ $? -ne 0 ]; then
    echo "Error: Jekyll build failed!"
    exit 1
fi

echo "Build complete. Starting upload..."

# Upload to server using rsync
# -a: archive mode (preserves permissions, times, etc.)
# -v: verbose output
# -z: compress file data during transfer
# --delete: delete files on server that don't exist locally
# --exclude: exclude certain files/folders
rsync -avz --delete \
    --exclude='.DS_Store' \
    --exclude='Thumbs.db' \
    --exclude='.git*' \
    $LOCAL_SITE_DIR $USERNAME@$SERVER_HOST:$SERVER_PATH/

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Deployment successful!"
    echo "Your site should be available at:"
    echo "https://unix.sussex.ac.uk/~$USERNAME/meml/"
else
    echo ""
    echo "❌ Deployment failed!"
    echo "Check your network connection and server credentials."
    exit 1
fi
