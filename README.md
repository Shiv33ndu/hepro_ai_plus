# Dedicated Mentoring System for Students (HEPro AI+)

An **AI-assisted, explainable mentoring system** designed to proactively support students across academics, wellness, productivity, and career readiness using a hybrid **rules + machine learning** approach.

---

## 🚀 Project Summary

HEPro AI+ is a data-first mentoring intelligence system that models student behavior, identifies risk patterns early, and recommends structured mentor interventions. The system prioritizes **interpretability, scalability, and real-world usability** over black-box complexity.

This repository is built as part of an **internship project** and follows professional ML engineering practices: clear data modeling, modular code structure, validation notebooks, and transparent decision logic.

---

## 🎯 Key Objectives

- Design a **realistic student mentoring dataset** spanning academic, wellness, productivity, and career dimensions
- Build **deterministic scoring models** to quantify student readiness
- Use **unsupervised ML** to discover student segments and assist mentor matching
- Translate insights into **actionable mentoring interventions**
- Maintain full **explainability and auditability** at every step

---

## 🧠 System Architecture (High Level)

Student Data → Feature Engineering → Scoring Models → ML Models → Intervention Rules → Mentor Actions → Feedback Loop

Each module is independently extensible and implemented using Python-first tooling.

---

## 👥 Student Archetypes (Design Foundation)

The system models students using behavior-driven archetypes discovered during dataset design:

- **Academically Strong but Disengaged** – High performance, low participation
- **Highly Engaged but Academically Struggling** – Effort present, outcomes weak
- **High Performer with Career Uncertainty** – Strong academics, unclear direction
- **Detached and Apathetic** – Low engagement, low stress, low direction

These archetypes guide synthetic data generation and are expected to re-emerge during clustering.

---

## 📁 Repository Structure

```
hepro-ai-mentoring-system/
│
├── data/
│   ├── raw/              # Synthetic student dataset
│   └── processed/        # Cleaned / transformed data
│
├── docs/                 # Design & documentation
│   ├── project_overview.md
│   └── data_dictionary.md
│
├── notebooks/            # Validation & analysis
│   └── 01_data_design_and_profiling.ipynb
│
├── src/                  # Production-ready code
│   ├── data/             # Data generation & preprocessing
│   ├── scoring/          # Rule-based scoring models
│   ├── models/           # ML components (clustering, matching)
│   └── rules/            # Intervention logic
│
├── tests/                # Basic tests & checks
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

- **Language:** Python
- **Data:** Pandas, NumPy
- **ML:** scikit-learn (unsupervised learning)
- **Visualization:** Matplotlib
- **Workflow:** Jupyter Notebooks + modular Python scripts

---

## 📌 How to Get Started

```bash
# Clone the repository
git clone https://github.com/Shiv33ndu/hepro_ai_plus.git
cd hepro-ai-plus

# Install dependencies
pip install -r requirements.txt

# Generate synthetic student data
python src/data/generate_students.py
```

---

## 📖 Documentation

- **Project Overview:** `docs/project_overview.md`
- **Data Dictionary:** `docs/data_dictionary.md`
- **Dataset Validation:** `notebooks/01_data_design_and_profiling.ipynb`

---

## ⚠️ Disclaimer

This project is intended for **educational and mentoring analytics only**. It is not a diagnostic or clinical tool and does not replace human judgment.

---

## 👤 Author

**Shivendu Kumar**  
Machine Learning Engineer Intern  

---

If you are a reviewer, start with [**`doc/project_overview.md`**](doc/data_dictionary.md) for a full system-level understanding.

