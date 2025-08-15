import os
import langextract as lx
from config import PV_PROMPT, EXAMPLES, OUTPUT_JSONL, OUTPUT_HTML

def prepare_example_objects():
    """Convert EXAMPLES dict into LangExtract ExampleData objects."""
    return [
        lx.data.ExampleData(
            text=ex["text"],
            extractions=[
                lx.data.Extraction(
                    extraction_class=e["extraction_class"],
                    extraction_text=e["extraction_text"],
                    attributes=e.get("attributes", {})
                ) for e in ex["extractions"]
            ]
        ) for ex in EXAMPLES
    ]

def run_extraction_on_text(text: str, examples, model_id="gemini-2.5-flash"):
    """Run LangExtract extraction for a given text input."""
    return lx.extract(
        text_or_documents=text,
        prompt_description=PV_PROMPT,
        examples=examples,
        model_id=model_id
    )

def save_results_and_visualize(results):
    """Save extraction results to JSONL and generate HTML visualization."""
    lx.io.save_annotated_documents(results, output_name=OUTPUT_JSONL, output_dir=".")
    html_content = lx.visualize(OUTPUT_JSONL)
    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(str(html_content.data if hasattr(html_content, "data") else html_content))
