#!/bin/bash

# Check if a commit message was provided
if [ -z "$1" ]
then
    echo "🚨 Error: Bhai, commit message toh daal Huzaifa! (e.g., lazygit 'updated script')"
    exit 1
fi

echo "📦 [INVYRAX] Gathering all files..."
git add .

echo "💾 [INVYRAX] Saving version checkpoint..."
git commit -m "$1"

echo "🚀 [INVYRAX] Blasting code to GitHub..."
git push

echo "✅ Jhakas! Syncing complete, Boss."
