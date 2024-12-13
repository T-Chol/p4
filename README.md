# p4
# P4 Project Setup and Git Workflow

### First Time Committing
If this is your first time setting up the project and committing changes, follow these steps:

1. **Create a Virtual Environment**  
   Set up a Python virtual environment:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
unset FLASK_APP [-----optional-----]
unset FLASK_RUN_PORT [-----optional-----] 
```
```bash
git checkout -b [branchName]
git checkout main
git pull origin main
git merge models
```




```bash
git checkout [branchName]
git add [. || files]
git commit -m"[your message]'
git checkout main
git pull origin main
git merge [branchName]
```