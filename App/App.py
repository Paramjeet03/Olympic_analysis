import streamlit as st 
from medal_tally import Medal_t
from Over_All_Analysis import oALA
from Country_wise_anlysis import C_W_A
import time

# Page config
st.set_page_config(page_title="Olympic Dashboard", layout="wide")

# Initialize classes
O_A_A = oALA()
Cl_M = Medal_t()

# Light background and white text styling with animation
st.markdown("""
    <style>
    body {
        background-color: #0a0a0a;
        color: white;
    }

    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(-10px);}
        to {opacity: 1; transform: translateY(0);}
    }

    .fade-text {
        animation: fadeIn 1.2s ease-in-out;
        color: white;
    }

    h1, h2, h3, p, .stTextInput label, .stSelectbox label, .stSidebar, .stRadio label {
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar menu (default to home: Overall Analysis)
user_menu = st.sidebar.radio("Select One Option", ["Over_All_Analysis", "Medal Tally", "Country_wise_Analysis"])

# Home Page Header & Description — only for "Over_All_Analysis"
if user_menu == "Over_All_Analysis":
    st.markdown(
        """
        <div class="fade-text" style='text-align: center; margin-bottom: 25px;'>
            <h1 style='text-decoration: underline; font-size: 38px;'>Olympic Analysis Dashboard</h1>
            <p style='font-size: 18px;'>Explore the history of the Olympics with insightful stats, medal tallies,<br> and participation trends across nations and sports events.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Animate metric counters
def animate_metric(label, value):
    placeholder = st.empty()
    for i in range(0, value + 1, max(1, value // 100)):
        placeholder.metric(label, i)
        time.sleep(0.005)

# ===== HOME PAGE =====
if user_menu == "Over_All_Analysis":
    st.markdown("<h2 class='fade-text' style='text-align: center; text-decoration: underline;'>Overall Olympic Analysis</h2>", unsafe_allow_html=True)

    year_count, city_count, sport_count, event_count, country_count, athlete_count = O_A_A.Total()

    c1, c2, c3 = st.columns(3)
    c4, c5, c6 = st.columns(3)

    with c1:
        animate_metric("Editions (Years)", year_count)
    with c2:
        animate_metric("Host Cities", city_count)
    with c3:
        animate_metric("Sports", sport_count)
    with c4:
        animate_metric("Events", event_count)
    with c5:
        animate_metric("Countries", country_count)
    with c6:
        animate_metric("Athletes", athlete_count)

    st.subheader("Nations Participating Over the Years")
    st.plotly_chart(O_A_A.nation_VS_year(), use_container_width=True)

    st.subheader("Events Over the Years")
    st.plotly_chart(O_A_A.event_VS_year(), use_container_width=True)

    st.subheader("Athlete Participation Over the Years")
    st.plotly_chart(O_A_A.Athlete_vs_year(), use_container_width=True)

    st.subheader("Top 4 Sport Participation per Edition")
    st.plotly_chart(O_A_A.sport_Parti_vs_year(), use_container_width=True)
    
    st.subheader("Top 10 Successful Athletes by Medals")
    st.plotly_chart(O_A_A.F_S_A(), use_container_width=True)

# ===== MEDAL TALLY =====
elif user_menu == "Medal Tally":
    year = st.sidebar.selectbox("Year", options=Cl_M.Year(), index=None, placeholder="Search on Year")
    Country = st.sidebar.selectbox("Region", options=Cl_M.Country(), index=None, placeholder="Search on Region")

    st.header("Medal Tally")
    st.dataframe(Cl_M.medal_tally())

    st.header("Medal Tally On Custom Year and Region")
    if year == "Overall" and Country == "Overall":
        st.dataframe(Cl_M.medal_tally())
    else:
        st.dataframe(Cl_M.Filtered(year, Country))

# ===== COUNTRY-WISE ANALYSIS =====
elif user_menu == "Country_wise_Analysis":
    ob=C_W_A()
    st.markdown("<h2 class='fade-text' style='text-align: center; text-decoration: underline;'>Top 6 Nation </h2>", unsafe_allow_html=True)
    df=ob.Top_5_Func()
    df = df.reset_index(drop=True)
    c1, c2, c3 = st.columns(3)
    c4, c5 ,c6= st.columns(3)

    with c1:
        animate_metric(df["Region(Country)"][0],df["Total_medal"][0])
    with c2:
        animate_metric(df["Region(Country)"][1],df["Total_medal"][1])
    with c3:
        animate_metric(df["Region(Country)"][2],df["Total_medal"][2])
    with c4:
        animate_metric(df["Region(Country)"][3],df["Total_medal"][3])
    with c5:
        animate_metric(df["Region(Country)"][4],df["Total_medal"][4])
    with c6:
        animate_metric(df["Region(Country)"][5],df["Total_medal"][5])

    st.header("COUNTRY-WISE ANALYSIS")
    country = st.selectbox("Choose your country:",ob.region())
    if country:
        df_top_10=ob.countryMedal_tally(country)
        st.dataframe(df_top_10)
    
    st.header("Top 10 Players of Country")
    st.dataframe(ob.Top_10_athletes(df_top_10))
    

