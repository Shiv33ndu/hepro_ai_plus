# Student Dataset Dictionary

This document defines the schema, meaning, scale, and decision relevance of
each feature used in the student mentoring dataset.

---

### Column: `student_id`
- **Description:** Unique identifier for each student. Used only for tracking and
  reference; has no analytical or predictive meaning.
- **Example:** S001
- **Scale:** Categorical (ID)

---

### Column: `age`
- **Description:** Age of the student in years.
- **Example:** 20
- **Scale:** Numeric (integer)

---

## Column: `program`
- **Description:** Academic program or discipline the student is pursuing.
  Program context can influence academic pressure, skill expectations, and
  career decision-making.
- **Example:** B.Tech, MBA
- **Scale:** Categorical

---

## `semester`
- **Description:** Current stage of the academic program. Semester indicates
  academic progression and contextual pressure—higher semesters often correlate
  with increased academic load and career-related anxiety, while lower semesters
  reflect exploration phases.
- **Example:** 3, 5
- **Scale:** Numeric (integer)

---

## `gpa`
- **Description:** Academic performance indicator summarizing overall academic
  outcomes. GPA anchors academic risk assessment and is a primary input to the
  **Academic Performance Score (APS)**.
- **Example:** 6.5, 7.8
- **Scale:** 0–10 (real-valued)

---

## `attendance`
- **Description:** Percentage of classes attended. Attendance acts as a
  **behavioral proxy** for engagement and discipline. Low attendance may signal
  disengagement, stress, or external constraints, especially when combined with
  other features.
- **Example:** 85, 76.8
- **Scale:** 0–100 (percentage)

---

## `assignment_completion`
- **Description:** Percentage of assigned coursework completed. This reflects the
  student’s ability to apply learned concepts and is a strong indicator of
  execution and follow-through.
- **Example:** 85, 76.8
- **Scale:** 0–100 (percentage)

---

## `stress_level`
- **Description:** Self-reported psychological stress level. Used to identify
  burnout risk and prioritize wellness-focused interventions.
- **Example:** 7
- **Scale:** 1–10

---

## `sleep_hours`
- **Description:** Average number of hours the student sleeps per night. Sleep
  duration is a key wellness indicator and is often inversely related to stress.
- **Example:** 7
- **Scale:** 0–10 (hours)

---

## `mental_wellbeing`
- **Description:** Overall psychological wellbeing score capturing motivation,
  emotional state, and day-to-day mental health.
- **Example:** 7
- **Scale:** 1–10

---

## `productivity_score`
- **Description:** Composite indicator of time management and task execution.
  Higher values indicate effective use of time and consistent work habits.
  Typically inversely related to `distractions`.
- **Example:** 7
- **Scale:** 1–10

---

## `distractions`
- **Description:** Degree of distraction or lack of focus. Higher values indicate
  a negative outcome. Some features increase risk when high (e.g., stress,
  distractions), while others increase risk when low (e.g., GPA, attendance).
- **Example:** 5
- **Scale:** 1–10

---

## `career_clarity`
- **Description:** Degree of clarity regarding career goals and future direction.
  Lower values represent uncertainty and signal a **mentoring opportunity** rather
  than failure.
- **Example:** 4
- **Scale:** 1–10

---

## `skill_readiness`
- **Description:** Job-readiness indicator reflecting practical skills and
  employability. Skill readiness is not equivalent to GPA; students with strong
  academic performance may still lack applied skills.
- **Example:** 6
- **Scale:** 1–10

---

## `engagement_score`
- **Description:** Level of interaction with the mentoring platform (sessions,
  check-ins, activities). Engagement does not directly imply academic success;
  highly engaged students may still struggle academically.
- **Example:** 70
- **Scale:** 1–100

---