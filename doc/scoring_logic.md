# Activity 2: Student Scoring System (Rule-Based Intelligence)

## Objective

The goal of Activity 2 is to convert raw student-level data into interpretable, actionable performance scores that mentors can easily understand and use for decision-making. The scoring framework is fully rule-based, transparent, and designed to support mentoring interventions rather than automated

## Overview of Scoring Framework

Each student is evaluated across four key dimensions: academics, wellness, productivity, and career readiness. These dimensions are computed independently and then combined into a single Student Readiness Index

### 1. Academic Performance Score (APS)

APS measures academic strength using GPA, assignment completion, and attendance. GPA anchors academic outcomes, assignments reflect application of learning, and attendance provides behavioral

**Formula:**
`APS = 0.5 × GPA(normalized) + 0.3 × Assignment Completion + 0.2 × Attendance`


### 2. Wellness & Wellbeing Score (WWS)

WWS captures the sustainability of a student's mental and physical state. Stress is treated as a negative signal, while sleep and mental wellbeing act as protective

**Formula:**
`WWS = 0.4 × Stress(inverted) + 0.3 × Sleep(normalized) + 0.3 × Mental Wellbeing(normalized)`



### 3. Productivity & Time Management Score (PTMS)

PTMS evaluates a student's ability to execute tasks consistently. Productivity is treated as a positive signal, while distractions are penalized through

**Formula:**
`PTMS = 0.6 × Productivity(normalized) + 0.4 × Distractions(inverted)`




### 4. Career Readiness Score (CRS)

CRS reflects how prepared a student is for future career decisions. It balances clarity of career direction with practical skill readiness, ensuring that strong academics alone do not dominate career

**Formula:**
`CRS = 0.5 × Career Clarity(normalized) + 0.5 × Skill Readiness(normalized)`




### 5. Student Readiness Index (SRI)

SRI is a weighted combination of all four scores and serves as the primary indicator for mentoring

**Formula:**
`SRI = 0.30 × APS + 0.25 × WWS + 0.20 × PTMS + 0.25 × CRS`




## Risk Classification Thresholds

Based on the SRI, students are categorized into four mentoring risk levels:

- **Green:** SRI ≥ 80 (Doing well, monitoring only)
- **Blue:** 65 ≤ SRI < 80 (Stable, light guidance)
- **Yellow:** 45 ≤ SRI < 65 (At risk, active mentoring required)
- **Red:** SRI < 45 (High risk, immediate intervention required)

## Conclusion

This scoring framework is intentionally conservative and interpretable. It ensures that mentoring interventions are driven by holistic student readiness rather than isolated metrics. The rule-based design allows mentors to trust, audit, and refine the system over