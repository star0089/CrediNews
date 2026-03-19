# CrediNews: AI-Assisted Fake News Detection System

## HOW TO RUN

1. Start the backend:
   ```bash
   cd backend
   pip install -r requirements.txt
   python train_model.py  # Wait for training to finish
   uvicorn app.main:app --reload
   ```

2. Start the frontend:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```
   Open `http://localhost:3000`

### OR Using Docker:
```bash
docker-compose up --build
```
