
# Student Dataset Dictionary 

- Column Name: `student_id`

  - Description: This a unique student identifier, it has no analytical meaning
  - Example: S001 
  - Scale : Categorical

- Column Name: `age`

  - Description: This column has student's age
  - Example: 20
  - Scale: Numeric  


- Column Name: `program`

  - Description: What discipline student is pursuing, program can directly impact career desicion making.
  - Example: B.Tech, MBA etc.
  - Scale: Categorical  

- Column Name: `semester`

  - Description: This shows the current progress of the program student pursuing, semester indicates **academic stage and pressure** *(Higher semester can mean Higher stress, career anxiety, Lower semester can mean exploration phase)*.
  - Example: 3, 5.
  - Scale: Numeric  

- Column Name: `gpa`

  - Description: Student's academic performance indicator that shows how well student is doing academically. GPA anchors **academic risk**, used heavily in **Academic Performance Score (APS)**
  - Example: 6.5, 7.8 etc.
  - Scale: 0-10 real numbers  

- Column Name: `attendance`

  - Description: Shows the participation of student in the chosen discipline as percentage out of totals days. Attendance is a **behavioral proxy**. Low attendance may signal: disengagement/stress/external constraints. This feature becomes defining in combination with other features. 
  - Example: 85, 76.8 etc.
  - Scale: 0-100 real numbers  

- Column Name: `assignment_completion`

  - Description: Percentage of completed assignments out of total given assignments.
  - Example: 85, 76.8 etc.
  - Scale: 0-100 real numbers  

- Column Name: `stress_level`

  - Description: Shows student's self reported psychological load. This is used to identify burnout risk and prioritize wellness interventions.
  - Example: 7 etc.
  - Scale: 1-10   

- Column Name: `sleep_hours`

  - Description: Student's average sleep time per night.
  - Example: 7 etc.
  - Scale: 0-10   

- Column Name: `mental_wellbeing`

  - Description: Student's indicator of overall psychological status, like how happy, motivated and determined student is in day-to-day life.
  - Example: 7.
  - Scale: 1-10   

- Column Name: `productivity_score`

  - Description: Reflects **time management & task execution**. This is inversely related to `distractions`
  - Example: 7.
  - Scale: 1-10   

- Column Name: `distractions`

  - Description: Student's distraction level (High value = negative outcome). Some features increase risk when high, others when low.
  - Example: 5.
  - Scale: 1-10   

- Column Name: `career_clarity`

  - Description: How much clarity student has for his future endeavours and choices for career (Lower career clarity means a *mentoring opportunity*).
  - Example: 4.
  - Scale: 1-10   

- Column Name: `skill_readiness`

  - Description: This score shows how job prepared student is, whether he has all the relevant skillset needed for job or not. Skill readiness ≠ GPA. Good GPA student can have low readiness.
  - Example: 6.
  - Scale: 1-10   

- Column Name: `engagement_score`

  - Description: This score shows how much engagement student makes with this platform. Engagement ≠ performance, Highly engaged students may still struggle academically.
  - Example: 70.
  - Scale: 1-100   

