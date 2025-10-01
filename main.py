from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import parser

class LabReport(BaseModel):
	text:str

app = FastAPI()

origins = [
  "null"
  "http://127.0.0.1.5500"

]

app.add.middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)

class LabReport(BaseModel):
  text: str

@app.post("/analyze")
def analyze_report(report: LabReport):
	
	processed_results = parser.process_lab_text(report.text)

	return {"input.text": report.text, "results": processed_results}
	
