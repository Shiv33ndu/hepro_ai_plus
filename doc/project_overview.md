# Dedicated Mentoring System for Students (HEPro AI+)

## 1. Overview

### Goal
The Dedicated Mentoring System for Students (HEPro AI+) is an AI-assisted mentoring platform designed to proactively support students across **academics, wellness, productivity, and career readiness**. The system focuses on early identification of at-risk patterns, structured mentor matching, and explainable interventions rather than reactive or opaque decision-making.

### Why This Matters
Traditional mentoring systems often suffer from being:
- Reactive instead of proactive
- Heavily manual and difficult to scale
- Opaque, making it hard for mentors and institutions to trust automated decisions

HEPro AI+ addresses these gaps by combining **interpretable rule-based logic** with **lightweight machine learning**, ensuring that every recommendation can be explained, audited, and improved over time.

### What This Project Builds
1. A realistic student profiling dataset spanning academic, behavioral, wellness, and career dimensions
2. Deterministic scoring models that quantify student readiness and risk
3. Unsupervised ML models for student segmentation and mentor matching
4. A rule-based intervention engine translating insights into actions
5. A feedback-driven loop for continuous system improvement

This project is intended for **educational analytics and mentoring support**, not as a replacement for human judgment.

---

## 2. System Architecture

The system follows a modular, pipeline-based architecture:

**Student Data → Feature Engineering → Scoring & ML Models → Intervention Logic → Mentor Actions → Feedback Loop**

Each module is designed to be independently extensible, allowing the system to evolve without large architectural changes.

---

## 3. Student Profiling Framework

### 3.1 Feature Dimensions

Each student is represented as a structured feature vector derived from the following dimensions:

- **Academic**: GPA, attendance, assignment completion
- **Behavioral**: engagement score, responsiveness proxies
- **Wellness**: stress level, sleep hours, mental wellbeing
- **Productivity**: productivity score, distraction level
- **Career**: career clarity, skill readiness

These features serve as the foundation for both rule-based scoring and machine learning models.

---

## 4. Student Archetypes

To design realistic mentoring logic, students are modeled using **behavioral archetypes** that reflect common real-world patterns. Archetypes are used during dataset design and are expected to re-emerge approximately during unsupervised clustering.

### Archetype 1: Academically Strong but Disengaged
- High GPA and assignment completion
- Low attendance and platform engagement
- Moderate stress and career clarity

**Mentoring Need:** Engagement-focused guidance rather than academic remediation.

---

### Archetype 2: Highly Engaged but Academically Struggling
- High engagement and attendance
- Low GPA and weak assignment performance
- High stress and low career clarity

**Mentoring Need:** Learning strategy correction and foundational academic support.

---

### Archetype 3: High Performer with Career Uncertainty
- Strong academics and consistent performance
- Low clarity regarding career direction
- Rising stress in advanced semesters

**Mentoring Need:** Career exploration, goal setting, and skill alignment.

---

### Archetype 4: Detached and Apathetic
- Low academic performance and engagement
- Low attendance and career clarity
- Low reported stress, indicating detachment rather than burnout

**Mentoring Need:** Motivation building and purpose-oriented mentoring.

---

## 5. Scoring Philosophy (Preview)

The system uses **deterministic, explainable scoring models** to maintain trust and transparency. Scores are normalized to a 0–100 scale and mapped to qualitative states (Green / Blue / Yellow / Red).

Planned core scores:
- Academic Performance Score (APS)
- Wellness & Wellbeing Score (WWS)
- Productivity & Time Management Score (PTMS)
- Career Readiness Score (CRS)

These scores combine to form a composite **Student Readiness Index (SRI)**, which acts as the primary trigger for interventions.

---

## 6. Role of Machine Learning

Machine learning is used to **augment**, not replace, rule-based logic.

Planned ML components:
- **Student Segmentation:** Unsupervised clustering (e.g., K-Means) on core scores to identify hidden behavior patterns
- **Mentor Matching:** Similarity-based matching between student and mentor feature vectors

ML outputs are always interpreted through the lens of scoring and rules to preserve explainability.

---

## 7. Intervention Framework

A rules engine translates scores and ML insights into structured actions:

- **Automated Guidance:** Nudges, reminders, study plans
- **Mentor Intervention:** Scheduled check-ins and targeted mentoring
- **Escalation:** Referral to senior mentors or counselors when risk is high

Rules are defined as readable conditional logic, ensuring auditability and ease of modification.

---

## 8. Evaluation Without Labels

Since labeled outcomes are not available, the system is evaluated using:
- Score distribution monitoring
- Cluster stability and interpretability
- Pre- vs post-intervention trend analysis
- Mentor feedback and student engagement changes

---


## 10. Key Takeaways

This project demonstrates:
- Hybrid AI system design (rules + ML)
- Explainable decision-making in sensitive domains
- Scalable mentoring intelligence
- Strong data-first engineering discipline

The HEPro AI+ mentoring system emphasizes **trust, transparency, and practical impact** over model complexity.

