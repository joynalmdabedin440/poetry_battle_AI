# AI Poetry Collaboration System

An interactive poetry generation system where **two AI poets** collaborate to create a poem, and an **AI judge** evaluates which poet wrote the better verse.  
This project demonstrates the integration of **NLP, text generation, and semantic similarity** using the Hugging Face Transformers and SentenceTransformers libraries.

---

## Features

✅ Dual Poet Collaboration – Two independent text generation models create poetic verses in sequence.  
✅ Intelligent Judging – A transformer-based judge evaluates similarity, emotion, and richness of text.  
✅ Multi-format Input Support – Accepts text prompts from DOCX, PDF, or plain text files.  
✅ Audio Narration – Automatically converts the final poem into speech using Google Text-to-Speech (gTTS).  
✅ Organized Modular Structure – Easily replace or extend components (e.g., swap models).  

---

## Project Structure

```
AI-Poetry-Collaboration/
│
├── main.py                  # Main entry point for running the full pipeline
├── poem_pipeline.py         # Coordinates the two poets and judge
│
├── poets/
│   ├── poet1.py             # Poet 1 (GPT-2 Medium)
│   ├── poet2.py             # Poet 2 (GPT-Neo 125M)
│
├── judge/
│   └── judge.py             # Evaluates poem quality and similarity
│
├── utils/
│   ├── extractor.py         # Extracts text from PDF/DOCX
│   ├── audio.py             # Converts final poem to audio using gTTS
│
├── requirements.txt         # Project dependencies
└── README.md                # Documentation
```

---

## ⚙️ Installation

1. **Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/AI-Poetry-Collaboration.git
cd AI-Poetry-Collaboration
```

2. **Create a virtual environment (recommended)**

```bash
python -m venv venv
venv\Scripts\activate       # For Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## Models Used

| Role | Model | Description |
|------|--------|-------------|
| Poet 1 | `gpt2-medium` | Generates creative and coherent poetry lines |
| Poet 2 | `EleutherAI/gpt-neo-125M` | Offers alternative poetic interpretations |
| Judge | `all-MiniLM-L6-v2` | Evaluates semantic similarity and emotional depth |

---

## 🚀 How to Run

### Option 1: Run with default input
```bash
python main.py
```

### Option 2: Run with custom input file
```bash
python main.py --input poems/input.docx
```

You can use `.docx`, `.pdf`, or `.txt` files containing your poetic prompt or theme.

---

##  Example Output

```
--- Generated Poem ---
Poet 1: A quiet forest after rain, where whispers bloom in silver air.
Poet 2: The sun breaks softly through the mist, like hope reborn again.

 Verdict :
Judge's Verdict: Poet 2 wrote the better verse (similarity=0.82, richness=7.50, emotion=0.61)

Audio saved as poem_output.mp3
```

**Audio Output:** `poem_output.mp3` will be automatically saved in your project folder.

---


```
assets/
└── sample_output.png
```

Then reference in README:

```markdown
![Poem Output Example](assets/sample_output.png)
```

---

## Design Approach

### 1. Modular Architecture
Each major function (generation, judging, extraction, and audio) is separated for flexibility.

### 2. Poetic Generation
- Both poets use prompt continuation to build lines.
- Sampling techniques (`temperature`, `top_p`, `repetition_penalty`) enhance creativity.

### 3. Judging Logic
The judge model (`all-MiniLM-L6-v2`) measures:
- **Semantic Similarity:** Cosine similarity between poets’ lines.
- **Emotion:** Sentiment polarity (positive vs. neutral).

A composite score determines the winner.

### 4. Audio Narration
Final poem is read aloud using **gTTS**, enhancing the poetic experience.

---

## Example Prompt File (input.docx)

```
A quiet forest after rain.
The sun slowly breaks through the mist.
```

---

## Requirements

```
requests
transformers
torch
sentence-transformers
gtts
pdfplumber
python-docx
pytesseract
Pillow
```

Install them using:
```bash
pip install -r requirements.txt
```

---

## Contributors

**Md. Joynal Abedin**  
 BSc in CSE, Presidency University  
 Dhaka, Bangladesh  
 [GitHub](https://github.com/joynalmdabedin440)  
 [LinkedIn](https://www.linkedin.com/in/mdjoynal-abedin/)

---



## Future Improvements
 
- Add web UI (Gradio or Streamlit) for interactive use.  





