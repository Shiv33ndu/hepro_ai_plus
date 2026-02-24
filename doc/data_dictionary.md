# Data Dictionary - Datasets

This document explains Datasets and their features along with the relevance in decision making. 

## Student Dataset Schema

### Purpose 

This defines the schema, meaning, scale, and decision relevance of each feature used in the student mentoring dataset.
 

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

### Column: `program`
- **Description:** Academic program or discipline the student is pursuing.
  Program context can influence academic pressure, skill expectations, and
  career decision-making.
- **Example:** B.Tech, MBA
- **Scale:** Categorical

---

### Column: `semester`
- **Description:** Current stage of the academic program. Semester indicates
  academic progression and contextual pressure—higher semesters often correlate
  with increased academic load and career-related anxiety, while lower semesters
  reflect exploration phases.
- **Example:** 3, 5
- **Scale:** Numeric (integer)

---

### Column: `gpa`
- **Description:** Academic performance indicator summarizing overall academic
  outcomes. GPA anchors academic risk assessment and is a primary input to the
  **Academic Performance Score (APS)**.
- **Example:** 6.5, 7.8
- **Scale:** 0–10 (real-valued)

---

### Column: `attendance`
- **Description:** Percentage of classes attended. Attendance acts as a
  **behavioral proxy** for engagement and discipline. Low attendance may signal
  disengagement, stress, or external constraints, especially when combined with
  other features.
- **Example:** 85, 76.8
- **Scale:** 0–100 (percentage)

---

### Column: `assignment_completion`
- **Description:** Percentage of assigned coursework completed. This reflects the
  student’s ability to apply learned concepts and is a strong indicator of
  execution and follow-through.
- **Example:** 85, 76.8
- **Scale:** 0–100 (percentage)

---

### Column: `stress_level`
- **Description:** Self-reported psychological stress level. Used to identify
  burnout risk and prioritize wellness-focused interventions.
- **Example:** 7
- **Scale:** 1–10

---

### Column: `sleep_hours`
- **Description:** Average number of hours the student sleeps per night. Sleep
  duration is a key wellness indicator and is often inversely related to stress.
- **Example:** 7
- **Scale:** 0–10 (hours)

---

### Column: `mental_wellbeing`
- **Description:** Overall psychological wellbeing score capturing motivation,
  emotional state, and day-to-day mental health.
- **Example:** 7
- **Scale:** 1–10

---

### Column: `productivity_score`
- **Description:** Composite indicator of time management and task execution.
  Higher values indicate effective use of time and consistent work habits.
  Typically inversely related to `distractions`.
- **Example:** 7
- **Scale:** 1–10

---

### Column: `distractions`
- **Description:** Degree of distraction or lack of focus. Higher values indicate
  a negative outcome. Some features increase risk when high (e.g., stress,
  distractions), while others increase risk when low (e.g., GPA, attendance).
- **Example:** 5
- **Scale:** 1–10

---

### Column: `career_clarity`
- **Description:** Degree of clarity regarding career goals and future direction.
  Lower values represent uncertainty and signal a **mentoring opportunity** rather
  than failure.
- **Example:** 4
- **Scale:** 1–10

---

### Column: `skill_readiness`
- **Description:** Job-readiness indicator reflecting practical skills and
  employability. Skill readiness is not equivalent to GPA; students with strong
  academic performance may still lack applied skills.
- **Example:** 6
- **Scale:** 1–10

---

### Column: `engagement_score`
- **Description:** Level of interaction with the mentoring platform (sessions,
  check-ins, activities). Engagement does not directly imply academic success;
  highly engaged students may still struggle academically.
- **Example:** 70
- **Scale:** 1–100

---

## Mentor Dataset Scehma

### Purpose 

Represents available mentors, their expertise, capacity, and risk-level handling ability used for mentor-student matching.


### Column: `mentor_id`
- Description: Unique identifier for each mentor
- Example: M001
- Scale: Categorical

---

### Column: `name`
- Description: Mentor's name
- Example: Dr. Sharma
- Scale: Categorical

---

### Column: `expertise`
- Description: Primary mentoring specialization
- Possible values: academic, career, wellness, productivity
- Scale: Categorical

---

### Column: `max_capacity`
- Description: Primary mentoring specialization
- Possible values: academic, career, wellness, productivity
- Scale: Categorical

---

### Column: `current_load`
- Description: Number of students currently assigned to the mentor
- Example: 10
- Scale: Numeric

---

### Column: `availability_hours`
- Description: Estimated weekly hours available for mentoring
- Example: 15
- Scale: Numeric

---

### Column: `priority_levels`
- Description: Risk levels the mentor is trained to handle
- Example: Blue;Yellow;Red
- Scale: Categorical (multi-level)

---

