# End-to-End Mentoring System Flow

## Objective

Explain how student data is transformed into actionable mentoring recommendations through rule-based scoring, machine learning, and matching logic.

---

## Step 1 — Dataset Design & Student Profiling

A synthetic student dataset was generated to represent academic performance, wellness, productivity, engagement, and career readiness dimensions.

Each student record includes behavioral and psychological indicators such as GPA, attendance, stress level, sleep, productivity, and career clarity.

These features simulate real-world student profiles with diverse needs.

---

## Step 2 — Rule-Based Scoring System

Raw features were converted into interpretable scores:

- Academic Performance Score (APS)
- Wellness & Wellbeing Score (WWS)
- Productivity & Time Management Score (PTMS)
- Career Readiness Score (CRS)

These scores were combined to compute the Student Readiness Index (SRI), which categorizes students into:

- Green — Thriving
- Blue — Stable
- Yellow — Needs attention
- Red — High risk

This layer provides an interpretable baseline assessment.

---

## Step 3 — Machine Learning Segmentation

K-Means clustering was applied on engineered scores (APS, WWS, PTMS, CRS) to identify hidden student groups.

Three meaningful clusters emerged:

- Academic Performers with Moderate Risk
- Disengaged & Directionless Students
- Burnout / High-Stress At-Risk Students

Clustering revealed structural differences within the same risk levels, enabling root-cause-aware interventions.

---

## Step 4 — Intervention Design

Each cluster was mapped to targeted mentoring strategies:

- Optimization-focused guidance for high performers
- Direction-building support for disengaged students
- Wellness stabilization for burnout cases

Monitoring intensity and escalation rules were defined accordingly.

---

## Step 5 — Mentor Dataset & Capacity Constraints

A mentor dataset was created capturing:

- Expertise domains (academic, career, productivity, wellness)
- Capacity limits
- Availability
- Risk-handling capability

This enables realistic resource-aware matching.

---

## Step 6 — Mentor Matching Logic

Each student is matched to one mentor using a hierarchical decision process:

1. Determine primary need based on cluster
2. Consider risk level for urgency
3. Filter mentors by expertise and availability
4. Apply capacity constraints
5. Use fallback logic when exact matches are unavailable

If no mentor has remaining capacity, the student is placed in a pending assignment queue.

---

## Step 7 — Alert Generation

High-risk students trigger alerts:

- Red risk category
- Burnout cluster membership

These alerts prioritize immediate intervention.

---

## Step 8 — Final Recommendation Output

The system produces a recommendation table containing:

- Student profile indicators
- Assigned mentor (or pending status)
- Intervention type
- Alert flag
- Assignment status

This table represents actionable mentoring decisions.

---

## Key Insight

The system demonstrates how data-driven analytics, machine learning, and operational constraints can be integrated to support scalable personalized mentoring.

