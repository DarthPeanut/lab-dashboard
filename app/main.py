from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from . import parser

class LabReport(BaseModel):
	text:str

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

class LabReport(BaseModel):
  text: str

@app.post("/analyze")
def analyze_report(report: LabReport):
	
	processed_results = parser.process_lab_text(report.text)

	return {"input.text": report.text, "results": processed_results}
	
