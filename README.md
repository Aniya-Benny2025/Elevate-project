# 🛒 E-commerce Return Rate Reduction Analysis

## 📌 Objective
The goal of this project is to identify **why customers return products** and how **return rates vary** by category, geography, and marketing channel.  
We also use **logistic regression** to predict the probability of returns and build a **Power BI dashboard** to visualize return risk.

---

## 🛠️ Tools & Technologies
- **Python**: Data cleaning, analysis, predictive modeling  
- **SQL**: Data extraction & transformation  
- **Power BI**: Interactive dashboard with drill-through filters  
- **Logistic Regression**: Predicting probability of product returns  

---

## 📂 Repository Structure
```
Ecommerce-Return-Rate-Analysis/
│── data/
│   ├── orders.csv
│   ├── returns.csv
│   └── high_risk_products.csv
│
│── src/
│   └── return_prediction.py
│
│── powerbi/
│   └── Return_Risk_Dashboard.pbix
│
│── reports/
│   └── summary_report.pdf
│
│── README.md
│── requirements.txt
```

---

## 📊 Power BI Dashboard
- Return % by **category, supplier, geography, channel**  
- **Drill-through filters** for deeper insights  
- Return risk **scoring visualization**

---

## 🤖 Logistic Regression Model
- Cleans order & return datasets  
- Merges data by `order_id / product_id`  
- Extracts features like category, geography, price, supplier  
- Predicts **probability of product return**  
- Outputs **high-risk products** to `high_risk_products.csv`

---

## 🚀 Deliverables
- ✅ Interactive Power BI Dashboard (`Return_Risk_Dashboard.pbix`)  
- ✅ Python codebase for return prediction (`src/return_prediction.py`)  
- ✅ CSV of high-risk products (`data/high_risk_products.csv`)  
- ✅ Documentation (`README.md`, `summary_report.pdf`)  

---

## 📌 How to Run
1. Clone the repo  
   ```bash
   git clone https://github.com/yourusername/Ecommerce-Return-Rate-Analysis.git
   cd Ecommerce-Return-Rate-Analysis
   ```
2. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```
3. Run logistic regression script  
   ```bash
   python src/return_prediction.py
   ```
4. Open **Power BI file** in `/powerbi/Return_Risk_Dashboard.pbix`

---

## 📈 Example Output (`high_risk_products.csv`)
| order_id | product_id | category   | supplier | geography | channel | price | return_probability | risk_level |
|----------|------------|-----------|----------|-----------|---------|-------|--------------------|------------|
| 101      | P001       | Clothing  | ABC Co.  | USA       | Online  | 49.99 | 0.82               | High       |
| 103      | P003       | Footwear  | StyleHub | USA       | Online  | 79.99 | 0.76               | High       |

---

 
