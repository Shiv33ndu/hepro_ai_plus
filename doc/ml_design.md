# Machine Learning Design

## Objective

Using K-Means unsupervised ML to find the hidden Students pattern in the `students_scored.csv`. The features used for the clustering are `"APS", "WWS", "PTMS", "CRS"`. This clustering is used as a comparison with Rule-Based Risk Interpretation.


## Feature Selection

I chose `"APS", "WWS", "PTMS", "CRS"` as they are indicators of different dimension of a student's learning, mental, and overall awareness of the career endeavours, using raw features like `GPA, Wellness Score` can increase the dimensionality and also weakens the signal strength compared to engieered features.


## Preprocessing

Evne though, the scores are on 0-100 scale, I have opted for StandardScaler to make the features more consistent for the distance based unsupervised ML algo like K-Means.


## Model Choice

The student data here is unstructured and unlabeled which makes it perfect for unsupervised ML, also to make the interpretability the priority I chose K-Means clustering for finding the pattern.


## Choosing K

Using the Elbow and Silhuoette method, I got two options for K which is 3 and 4 (Highest Silhuoette Score). I chose K=3 that gives me Clustering themes like (Academic Performers / Burnout Students / Disengaged Students).


## Cluster Profiles

Cluster 0:
- High APS (Strong academics)
- Moderate WWS (Moderate wellness)
- Moderate-High PTMS (Decent productivity) 
- Moderate CRS (Average career clarity)

**Cluster 0 vs Risk Cross Table**

| risk_category | Blue | Green | Red | Yellow |
|---------------|------|-------|-----|--------|
| cluster 0     | 43   | 1     | 0   | 76     |

**Observation**: This cluster is **Academic Performers with Moderate Risk** (Blue & Yellow Group).

--- 

Cluster 1:
- Low APS (Poor academics)
- High WWS (High Mental Wellness)
- Very Low PTMS (Very Low Productivity)
- Very Low CRS (Extremely Low Career Clarity)

**Cluster 1 vs Risk Cross Table**

| risk_category | Blue | Green | Red | Yellow |
|---------------|------|-------|-----|--------|
| cluster 1     |  0   |   0   | 27  | 13     |

**Observation**: This cluster is **Comfortable but Directionless / Disengaged** (Comfortable Red & few Blue group).

---

Cluster 2:
- Moderate APS (Academically average)
- Very Low WWS (Extremely Low wellness)
- Low PTMS (Low productivity)
- Low CRS (Low career clarity)

**Cluster 2 vs Risk Cross Table**

| risk_category | Blue | Green | Red | Yellow |
|---------------|------|-------|-----|--------|
| cluster 2     |  0   |   0   | 33  |  7     |

**Observation**: This cluster is **High-Risk Burnout Group** (Risky Red & few Borderline Yellow)


## ML vs Rule-Based Comparison

The rule-based SRI system groups students primarily by overall readiness score.

However, clustering reveals structural differences within high-risk populations.

Specifically, ML identifies two distinct Red groups:

1. Burnout-driven risk (Cluster 2)
2. Directionless disengagement (Cluster 1)

While SRI classifies both as high risk, clustering differentiates the underlying causes.

This demonstrates the added value of ML-based segmentation in mentoring systems.


## Key Takeaways

- Even though Rule-Based Risk modeling gives high signal, but it somehow misses the sub-grouping of the data
- ML Clustering is successfully taking care of the sub-groups and the patterns. 