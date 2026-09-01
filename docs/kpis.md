# Smart Rental Tracking System — KPIs

This document defines the operational and AI/analytics KPIs
used by the Smart Rental Tracking System.

The KPIs are designed to answer four core questions:

1. Where is each asset?
2. How is each asset being used?
3. What requires attention?
4. What equipment will be needed next?

---

# Operational KPIs

## 1. Total Assets

### Purpose

Measures the total number of equipment assets registered in the system.

### Formula

COUNT(asset_id)

### Example

If the system contains:

- EQX1001
- EQX1002
- EQX1003
- EQX1004
- EQX1005
- EQX1006
- EQX1007

Then:

Total Assets = 7

### Data Source

`assets` table

---

## 2. Active Rentals

### Purpose

Measures the number of assets currently rented and in an active
rental lifecycle.

### Formula

COUNT(rentals WHERE status = 'ACTIVE')

### Example

If 5 assets are currently rented:

Active Rentals = 5

### Data Source

`rentals` table

---

## 3. Available Assets

### Purpose

Measures the number of assets currently available for allocation
or rental.

### Formula

COUNT(assets WHERE status = 'AVAILABLE')

### Example

If 2 assets are available:

Available Assets = 2

### Data Source

`assets` table

---

## 4. Asset Utilization

### Purpose

Measures how effectively rented equipment is being used.

### Formula

Utilization % =
Runtime Hours / Available Operating Hours × 100

### Example

Runtime = 8 hours
Available Operating Hours = 10 hours

Utilization =
8 / 10 × 100

= 80%

### Interpretation

- High utilization → asset is being used effectively
- Low utilization → asset may be underutilized
- Very low utilization → investigate reassignment or return

### Data Source

`telemetry` table

---

## 5. Idle Hours

### Purpose

Measures the amount of time equipment remains powered or available
without productive operation.

### Example

Asset: EQX1004

Runtime = 2 hours
Idle Hours = 9 hours

The asset has significantly more idle time than operating time.

### Interpretation

High idle hours may indicate:

- Low utilization
- Inefficient equipment deployment
- Operator inactivity
- Equipment waiting at a site
- Potential unnecessary rental duration

### Data Source

`telemetry` table

---

## 6. Overdue Assets

### Purpose

Identifies rented assets that have passed their expected return date
without being checked back in.

### Formula

Current Date > Expected Return Date
AND rental status != 'RETURNED'

### Example

Expected Return Date = September 5
Current Date = September 8
Rental Status = ACTIVE

Result:

Asset = OVERDUE

### Data Source

`rentals` and `asset_events` tables

---

## 7. Anomaly Count

### Purpose

Measures the number of asset conditions or events that require
investigation.

### Anomaly Types

The system can detect:

- Missing operator
- Missing site assignment
- Excessive idle hours
- Zero runtime
- Unexpected asset movement
- Unusual usage patterns
- Overdue return
- Invalid telemetry

### Example

Missing operator = 3
High idle = 4
Zero runtime = 2
Unexpected movement = 1

Total Anomalies = 10

### Data Source

`alerts` table

---

# AI & Analytics KPIs

## 8. Forecast Accuracy

### Purpose

Measures how accurately the demand forecasting model predicts
future equipment requirements.

### Metrics

#### MAE — Mean Absolute Error

Measures the average absolute difference between predicted and
actual demand.

MAE = Average(|Actual - Predicted|)

#### RMSE — Root Mean Squared Error

Penalizes larger forecasting errors more heavily.

RMSE =
√(Average((Actual - Predicted)²))

#### MAPE — Mean Absolute Percentage Error

Measures prediction error as a percentage.

MAPE =
Average(|Actual - Predicted| / Actual) × 100

### Example

Predicted demand = 5 excavators
Actual demand = 6 excavators

Absolute Error = 1

The model's performance will be evaluated across multiple
historical observations rather than a single prediction.

### Data Source

Historical rental/demand data

### Model Output

Predicted equipment demand by:

- Equipment type
- Site
- Time period

---

## 9. Anomalies Detected

### Purpose

Measures the number of abnormal asset events detected by the
analytics layer.

### Definition

An anomaly is an asset condition or event that significantly
deviates from expected operational behavior.

### Example

EQX1007:

Runtime = 0 hours
Idle = 12 hours
Site = NULL
Operator = NULL

The system identifies this as an anomaly.

### Output

Anomaly:

UNASSIGNED_AND_UNUSED_ASSET

Severity:

HIGH

### Data Source

`telemetry`, `assets`, `operators`, `sites`

### Analytics Approach

The system may use:

- Rule-based thresholds
- Statistical analysis
- Machine learning anomaly detection

---

## 10. Estimated Cost Avoided

### Purpose

Estimates potential rental cost savings resulting from system
recommendations.

### Example

Unused asset rental cost = ₹5,000/day

Unnecessary rental duration identified = 3 days

Estimated Cost Avoided =
₹5,000 × 3

= ₹15,000

### Possible Cost-Saving Actions

The system may estimate savings from:

- Returning unused equipment
- Reassigning underutilized equipment
- Reducing unnecessary rental duration
- Preventing overdue rentals
- Pre-positioning equipment to avoid operational delays

### Important Note

Cost figures used in the prototype may be simulated estimates if
actual Caterpillar rental pricing is unavailable.

All such values will be explicitly labelled:

"Estimated Cost Avoided"

rather than being presented as actual Caterpillar financial data.

---

# KPI Dashboard Summary

The main control-tower dashboard should display the following:

| KPI | Purpose |
|---|---|
| Total Assets | Overall asset inventory |
| Active Rentals | Current rental activity |
| Available Assets | Equipment available for allocation |
| Utilization % | Equipment usage efficiency |
| Idle Hours | Potential underutilization |
| Overdue Assets | Rental return risk |
| Anomaly Count | Assets requiring attention |
| Forecast Accuracy | Quality of demand predictions |
| Anomalies Detected | AI/analytics activity |
| Estimated Cost Avoided | Potential financial impact |

---

# KPI → Business Decision Mapping

| KPI | Business Question | Possible Action |
|---|---|---|
| Total Assets | How many assets are being managed? | Monitor inventory |
| Active Rentals | How many assets are currently rented? | Monitor rental portfolio |
| Available Assets | What can be deployed? | Assign or rent |
| Utilization % | Are assets being used effectively? | Reassign / optimize |
| Idle Hours | Which assets may be underutilized? | Investigate / return |
| Overdue Assets | Which rentals need attention? | Follow up / return |
| Anomaly Count | What requires investigation? | Investigate |
| Forecast Accuracy | Can we trust demand predictions? | Improve model |
| Anomalies Detected | What unusual behavior exists? | Investigate |
| Estimated Cost Avoided | What financial value can actions create? | Prioritize actions |

---

# Core KPI Philosophy

The system should not stop at displaying a KPI.

Each important KPI should lead to an operational decision.

Example:

Low Utilization
→ Identify asset
→ Investigate reason
→ Recommend reassignment or return
→ Track outcome

Similarly:

Forecasted Demand
→ Compare with available assets
→ Identify shortage
→ Recommend repositioning
→ Track utilization improvement

The objective is:

DATA → INSIGHT → ACTION → MEASURABLE OUTCOME