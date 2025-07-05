#!/bin/bash

# Step 1: Rename the folder if it exists
if [ -d "RishikaRobot" ]; then
  mv RishikaRobot RishikaRobot
  echo "✅ Folder renamed: RishikaRobot → RishikaRobot"
fi

# Step 2: Replace all mentions in files
find . -type f -exec sed -i 's|RishikaRobot|RishikaRobot|g' {} +
echo "✅ All 'RishikaRobot' references updated in files"

# Step 3: Re-init git if corrupted
if [ -f ".git/index" ]; then
  rm -f .git/index
  git reset
fi

# Step 4: Git push
git add .
git commit -m "?? Renamed 'RishikaRobot' to 'RishikaRobot' and updated references"
git push

echo "?? Push completed to GitHub!"
