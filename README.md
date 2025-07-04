# 🏅 Olympic Data Analysis Dashboard

An interactive and optimized Streamlit dashboard to explore Olympic Games data — covering medal tallies, athlete stats, country-wise trends, and participation history from 1896 onwards.

---

## 🔍 Key Features

### 1. **Over_All_Analysis**
- Animated counters for:
  - Olympic editions
  - Host cities
  - Sports, events, countries, athletes
- Visual trends for:
  - Participating nations
  - Events growth
  - Athlete count
  - Sport-wise popularity
  - Top 10 athletes by total medals

### 2. **Medal Tally**
- View total medal counts
- Filter by **year** and/or **country**
- See ranked table of gold, silver, bronze, and total medals

### 3. **Country-wise Analysis**
- Animated display of top 6 countries
- Drill into a country's yearly medal performance
- View its top 10 medal-winning athletes

---

## 🗂️ Project Structure

```
olympic-dashboard/
├── App.py                         # Main Streamlit app
├── Over_All_Analysis.py          # Overall Olympic stats and graphs
├── medal_tally.py                # Medal tally logic
├── Country_wise_anlysis.py       # Country-level analysis logic
├── Filtered_M_df.py              # Data loading, filtering, and preprocessing
├── athlete_events.csv            # Main dataset (Olympic history)
├── noc_regions.csv               # NOC (region) mapping
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

---

## 📁 Datasets

- **athlete_events.csv**: Olympic athlete records from 1896–2016  
- **noc_regions.csv**: Maps NOC codes to countries/regions

---

## 🚀 How to Run the App Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/olympic-dashboard.git
cd olympic-dashboard
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Launch the Dashboard

```bash
streamlit run App.py
```

---

## ⚙️ Technologies Used

- **Python**
- **Streamlit** – web app framework
- **Pandas & NumPy** – data manipulation
- **Plotly** – interactive charts
- **Caching** – improves performance with `@st.cache_data`

---

## 📌 Notes

- The dashboard uses caching for speed and responsiveness.
- Data is filtered for Summer Olympics only.
- Visuals are interactive and optimized using Plotly.

---

## 📄 License & Acknowledgment

- Dataset: [Kaggle Olympic History Dataset](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results)
- This project is for educational and data storytelling purposes.

---

Made with ❤️ using Python & Streamlit
