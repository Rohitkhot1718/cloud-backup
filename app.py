import os
import ibm_boto3
from ibm_botocore.client import Config
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()

IBM_COS_API_KEY = os.getenv("IBM_COS_API_KEY")
IBM_COS_SERVICE_INSTANCE_ID = os.getenv("IBM_COS_SERVICE_INSTANCE_ID")
IBM_COS_BUCKET_NAME = os.getenv("IBM_COS_BUCKET_NAME")
IBM_COS_REGION = os.getenv("IBM_COS_REGION")
IBM_COS_ENDPOINT = os.getenv("IBM_COS_ENDPOINT")


cos = ibm_boto3.client(
    "s3",
    ibm_api_key_id=IBM_COS_API_KEY,
    ibm_service_instance_id=IBM_COS_SERVICE_INSTANCE_ID,
    config=Config(signature_version="s3v4"),  
    endpoint_url=IBM_COS_ENDPOINT
)

app = Flask(__name__)

@app.route('/')
def index():
    """List all files stored in IBM Cloud Object Storage."""
    try:
        response = cos.list_objects_v2(Bucket=IBM_COS_BUCKET_NAME)
        files = [obj['Key'] for obj in response.get('Contents', [])] if 'Contents' in response else []
    except Exception as e:
        files = []
        print(f"Error fetching files: {e}")
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    """Upload file to IBM Cloud Object Storage."""
    if 'file' not in request.files:
        return jsonify({"error": "No file selected!"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected!"}), 400

    try:
        cos.put_object(Bucket=IBM_COS_BUCKET_NAME, Key=file.filename, Body=file)
        return jsonify({"message": "File uploaded successfully", "filename": file.filename})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/download/<filename>')
def download_file(filename):
    """Generate a pre-signed URL for secure file download."""
    try:
        url = cos.generate_presigned_url(
            'get_object',
            Params={'Bucket': IBM_COS_BUCKET_NAME, 'Key': filename},
            ExpiresIn=3600  
        )
        return jsonify({"download_url": url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    """Delete a file from IBM Cloud Object Storage."""
    try:
        cos.delete_object(Bucket=IBM_COS_BUCKET_NAME, Key=filename)
        return jsonify({"message": "File deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
