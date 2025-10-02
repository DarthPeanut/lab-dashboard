from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from . import parser
from . import database
import pytesseract
from PIL import Image
import shutil

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = FastAPI()

origin_regex = r"htp://127\.0\.0\.1:\d+"


app.add_middleware(
  CORSMiddleware,
  allow_origins=["null"],
  allow_origin_regex=origin_regex,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.post("/analyze")
async def analyze_report(
    patient_id: str = Form(...),
    file: UploadFile = File(...)
):
    temp_file_path = f"temp_{file.filename}"
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    try:
        extracted_text = pytesseract.image_to_string(Image.open(temp_file_path))
    except Exception as e:
        return {"error": f"OCR failed: {e}"}
    finally:
        # Clean up the temporary file
        import os
        os.remove(temp_file_path)

    previous_results = database.get_latest_report(patient_id)
    current_results = parser.process_lab_text(extracted_text)

    if current_results:
        database.save_lab_report(patient_id, current_results)

    return {
        "current_results": current_results,
        "previous_results": previous_results,
        "extracted_text": extracted_text # Also return the extracted text for debugging
    }