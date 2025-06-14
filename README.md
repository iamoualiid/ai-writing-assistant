# AI Writing Assistant with PDF Reference Matching

This project is a multi-agent AI system that helps generate summaries and extract insights from web articles, while cross-referencing related content from a local PDF document.

---

## 🚀 Features

- 🔍 Google search integration using Serper API
- 🌐 Web article scraping and text extraction
- 📝 Article summarization using Hugging Face (BART model)
- 🧠 Keyword extraction with KeyBERT and MiniLM
- 📄 PDF reading and page-by-page analysis (via PyMuPDF)
- 🔗 Semantic matching between article and PDF using Sentence Transformers
- 📦 Outputs a structured JSON file ready for reporting or use in other systems

---

## 🧰 Technologies Used

- Python 3.10
- Hugging Face Transformers
- KeyBERT
- Sentence Transformers
- PyMuPDF
- BeautifulSoup
- Serper.dev API

---

## 📂 Output Format

The final output is saved in `output.json` and looks like this:

```json
{
  "titre_article": "2025 : les tendances et innovations dans le domaine de l'énergie",
  "resume": "En 2025, le paysage énergétique mondial continue de se transformer...",
  "mots_cles": ["émissions carbone", "rénovation énergétique", ...],
  "liens_references_pdf": [
    {
      "extrait": "Sparse Representations\nMRR@10\nNotes...",
      "page": 3
    }
  ],
  "url_source": "https://..."
}
```


---

## 👤 Author

**Project created by [Oualid Benhamou](https://github.com/iamoualiid)**  
Built as part of an academic assignment on multi-agent AI systems.  
Shared publicly for learning, inspiration, and demonstration purposes.
