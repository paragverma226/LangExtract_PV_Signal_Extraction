import os
from glob import glob
from config import PDF_FOLDER, INTERMEDIATE_TEXT_FOLDER
from pdf_utils import extract_text_from_pdf, save_intermediate_text
from extraction_pipeline import prepare_example_objects, run_extraction_on_text, save_results_and_visualize

def main():
    pdf_files = glob(os.path.join(PDF_FOLDER, "*.pdf"))
    if not pdf_files:
        raise FileNotFoundError(f"No PDF files found in {PDF_FOLDER}/")

    examples = prepare_example_objects()
    all_results = []

    print("\n🔍 Extracting Pharmacovigilance Signals from PDFs...\n")

    for pdf_path in pdf_files:
        filename = os.path.splitext(os.path.basename(pdf_path))[0]
        print(f"📄 Processing file: {filename}")

        # Step 1: Extract text from PDF
        pdf_text = extract_text_from_pdf(pdf_path)

        # Step 2: Save intermediate text
        save_intermediate_text(pdf_text, INTERMEDIATE_TEXT_FOLDER, filename)

        # Step 3: Run extraction
        try:
            result = run_extraction_on_text(pdf_text, examples)
            all_results.append(result)
            print(f"✅ Extracted {len(result.extractions)} key entities from {filename}\n")
        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")

    # Step 4: Save results & visualization
    save_results_and_visualize(all_results)
    print("\n✅ Extraction complete!")
    print(f"📂 Saved structured data: extraction_results.jsonl")
    print(f"🌐 Open '{os.path.basename('visualization.html')}' in your browser to view the results.")

if __name__ == "__main__":
    main()
