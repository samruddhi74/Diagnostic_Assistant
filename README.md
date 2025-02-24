# Diagnostic_Assistant
# Diagnostic Assistant: AI-Powered Medical Diagnosis

## Overview
This project is an AI-powered **Diagnostic Assistant** designed to analyze **medical images (MRI scans)** and **patient symptoms** to assist healthcare professionals in diagnosing diseases accurately and efficiently.

## Features
- **MRI Tumor Segmentation**: Uses a deep learning **ResUNet** model to detect brain tumors from MRI scans.
- **Web-Based Interface**: Built using **FastAPI (backend)** and **React.js (frontend)** for seamless interaction.

## Technologies Used
### **Machine Learning & AI**
- **ResUNet** for tumor segmentation

### **Web Application**
- **Frontend**: React.js, Tailwind CSS
- **Backend**: FastAPI (Python), OpenAI API integration
- **Database**: PostgreSQL 

## Installation & Setup
### **1. Clone the Repository**
```bash
 git clone https://github.com/samruddhi74/diagnostic-assistant.git
 cd diagnostic-assistant
```

### **2. Set Up the Backend**
1. Install dependencies:
```bash
cd backend
pip install -r requirements.txt
```
2. Set up environment variables in a `.env` file (inside `backend` folder):
```env
OPENAI_API_KEY=your_api_key
DATABASE_URL=your_database_url
```
3. Run the backend server:
```bash
uvicorn backend.main:app --reload
```

### **3. Set Up the Frontend**
1. Navigate to the frontend folder:
```bash
cd ../frontend
```
2. Install dependencies:
```bash
npm install
```
3. Start the development server:
```bash
npm start
```

## Usage
1. **Upload MRI Scans**: The AI model will segment tumors and provide results.
2. **Enter Symptoms**: The system analyzes input symptoms using fuzzy logic and suggests possible conditions.

## Alternate Approaches Considered
- **Rule-Based Symptom Analysis** (Replaced with **Fuzzy Logic** for better flexibility)
- **Centralized Model Training** (Replaced with **Federated Learning** for privacy preservation)
- **Traditional Image Processing** (Replaced with **Deep Learning** for better accuracy)

## Contributing
Feel free to fork this repository, create a new branch, and submit a pull request. Contributions, issues, and feature requests are welcome!

## Contact
For queries or collaborations, reach out via:
- Email: samruddhi.deshmukh2019@gmail.com

