import textwrap

# Folder paths
PDF_FOLDER = "pdf_inputs"
INTERMEDIATE_TEXT_FOLDER = "intermediate_text"
OUTPUT_JSONL = "extraction_results.jsonl"
OUTPUT_HTML = "visualization.html"

# Extraction prompt for Pharmacovigilance
PV_PROMPT = textwrap.dedent("""
    Extract patient demographics, suspected drugs, concomitant medications, reported adverse events, 
    seriousness criteria, event outcome, and reporting source from the narrative text.
    Use exact text from the report without paraphrasing.
    Provide meaningful attributes for each extracted entity to support signal detection.
""")

# Training example for the model
EXAMPLES = [
    {
        "text": """A 54-year-old female patient experienced severe headache and dizziness after starting DrugX 50mg daily. 
She was also taking Metformin for diabetes. The event was classified as serious due to hospitalization.
Symptoms resolved after discontinuation. Reported by Dr. Smith on 15 Jan 2025.""",
        "extractions": [
            {
                "extraction_class": "patient_info",
                "extraction_text": "54-year-old female",
                "attributes": {"age": "54", "sex": "female"}
            },
            {
                "extraction_class": "suspected_drug",
                "extraction_text": "DrugX 50mg daily",
                "attributes": {"dose": "50mg", "frequency": "daily"}
            },
            {
                "extraction_class": "concomitant_medication",
                "extraction_text": "Metformin",
                "attributes": {"indication": "diabetes"}
            },
            {
                "extraction_class": "adverse_event",
                "extraction_text": "severe headache and dizziness",
                "attributes": {"severity": "severe"}
            },
            {
                "extraction_class": "seriousness",
                "extraction_text": "hospitalization",
                "attributes": {"criteria": "hospitalization"}
            },
            {
                "extraction_class": "outcome",
                "extraction_text": "resolved after discontinuation",
                "attributes": {"status": "resolved"}
            },
            {
                "extraction_class": "report_source",
                "extraction_text": "Dr. Smith",
                "attributes": {"date_reported": "15 Jan 2025"}
            }
        ]
    }
]
