# 📄 Pharmacovigilance Signal Extraction from PDF

## 📌 Objective
The **Pharmacovigilance Signal Extraction from PDF** project automates the detection and structured extraction of **critical safety information** from pharmacovigilance (PV) case reports in PDF format.  

This system enables safety teams to:
- **Identify** key patient, drug, and event information from unstructured narrative text.
- **Convert** PDFs into structured data for analytics and reporting.
- **Visualize** extracted entities for faster case assessment and signal detection.

---

## 🏗 System Architecture
```mermaid
flowchart TD
    A[PDF Case Reports] -->|Extract Text| B[PDF Text Extraction Module]
    B -->|Send to LLM| C[LangExtract Processing]
    C --> D[Entity Extraction: Patient Info, Drugs, AEs, etc.]
    D --> E[Structured Output - JSONL]
    E --> F[Visualization - HTML Report]
````

---

## 🛠 Tech Stack

**Programming Language**: Python 3.9+
**Core Libraries**:

* [`langextract`](https://pypi.org/project/langextract/) – LLM-powered structured extraction
* [`PyMuPDF`](https://pymupdf.readthedocs.io/) – PDF text extraction
* `textwrap`, `glob`, `os` – Python utilities

**Model Backend**:

* `gemini-2.5-flash` (compatible with OpenAI API key)

**Output Formats**:

* JSONL (Machine-readable structured data)
* HTML Visualization (Human-readable report)

---

## 📂 Project Structure

```
pv_signal_extraction/
│
├── main.py                      # Entry point
├── config.py                    # Configurations & constants
├── pdf_utils.py                 # PDF text extraction utilities
├── prompt_templates.py          # Domain-specific prompts & examples
├── extractor.py                 # Core LangExtract processing
├── requirements.txt             # Dependencies
├── pdf_inputs/                  # Folder containing PDF files
└── outputs/                     # JSONL and HTML output files
```

---

## ⚙️ Installation

1️⃣ **Clone the repository**

```bash
git clone https://github.com/your-username/pv_signal_extraction.git
cd pv_signal_extraction
```

2️⃣ **Install dependencies**

```bash
pip install -r requirements.txt
```

3️⃣ **Set API Key**

```bash
export OPENAI_API_KEY="your_api_key_here"
```

---

## 🚀 Usage

1. **Place PDFs** inside the `pdf_inputs/` folder.
2. **Run the extraction pipeline**:

```bash
python main.py
```

3. **Output Files**:

   * `extraction_results.jsonl` → Structured extraction results.
   * `visualization.html` → Clickable, color-coded view of extracted entities.

---

## 📊 Example Output

**Input PDF Narrative:**

> A 54-year-old female patient experienced severe headache and dizziness after starting DrugX 50mg daily. She was also taking Metformin for diabetes. The event was classified as serious due to hospitalization. Symptoms resolved after discontinuation. Reported by Dr. Smith on 15 Jan 2025.

**Extracted JSONL Example:**

```json
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
  "extraction_class": "adverse_event",
  "extraction_text": "severe headache and dizziness",
  "attributes": {"severity": "severe"}
}
```

**HTML Visualization Example:**

* Patient demographics → 🟦 Blue highlight
* Suspected drugs → 🟧 Orange highlight
* Adverse events → 🟥 Red highlight

---

## 📈 Benefits

* **Automates** manual PV case data entry.
* **Accelerates** signal detection workflows.
* **Minimizes errors** in critical safety reporting.
* **Enables analytics** by converting narrative text to structured format.

---

## 🔮 Future Enhancements

* Batch processing on **cloud-based infrastructure**.
* **Regulatory integration** with VigiBase / FAERS.
* Support for **multi-language case reports**.
* Integration with **AI signal prioritization**.

---

## 📜 License

Released under the **MIT License**.

---

## 📷 Screenshots
### HTML Visualization Output

![Visualization Example](LangExtract.png)

---

```
