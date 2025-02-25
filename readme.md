# Cloud Backup & Recovery with IBM Cloud Object Storage

This project is a simple **Cloud Backup & Recovery** web application that allows users to **upload, download, and delete files** using **IBM Cloud Object Storage (IBM COS)**. It is built with **Flask (Python)** and **IBM's boto3 SDK** for cloud storage interactions.

## Features
✅ Upload files to IBM Cloud Object Storage  
✅ List all stored files  
✅ Download files via a direct link  
✅ Delete files from cloud storage  

## Tech Stack
- **Backend**: Flask (Python)
- **Cloud Storage**: IBM Cloud Object Storage (COS)
- **Frontend**: HTML, CSS, JavaScript

---

## 🚀 Setup Instructions

### 1️⃣ Prerequisites
- Python 3.x installed
- IBM Cloud Object Storage account with bucket configured
- `pip install -r requirements.txt` installed dependencies

### 2️⃣ Clone the Repository
```
git clone https://github.com/Rohitkhot1718/cloud-backup
cd cloud-backup
```

### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables  
Create a **.env** file in the project root and add your IBM Cloud credentials:
```env
IBM_COS_API_KEY=your-api-key
IBM_COS_SERVICE_INSTANCE_ID=your-service-instance-id
IBM_COS_BUCKET_NAME=your-bucket-name
IBM_COS_REGION=your-region
IBM_COS_ENDPOINT=your-endpoint-url
```

### 5️⃣ Run the Application
```sh
python app.py
```
Visit `http://127.0.0.1:5000` in your browser.

---

## 📝 API Endpoints

| Method | Endpoint           | Description                  |
|--------|-------------------|------------------------------|
| GET    | `/`               | List all files               |
| POST   | `/upload`         | Upload a file               |
| GET    | `/download/<filename>` | Generate download link   |
| POST   | `/delete/<filename>` | Delete a file            |

---

## 📸 Screenshots
*Include screenshots of your app here.*

---

## 📜 License
This project is open-source and available under the **MIT License**.

---
