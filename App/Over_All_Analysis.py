import pandas as pb
import numpy as np
from Filtered_M_df import M_df as df_m
import plotly.express as plty
import plotly.graph_objects as go

class oALA:
    def __init__(self):
        self.df = pb.read_csv(r"C:\Users\Paramjeet\OneDrive\Desktop\New folder (2)\athlete_events.csv\athlete_events.csv")
        self.noc_df = pb.read_csv(r"C:\Users\Paramjeet\OneDrive\Desktop\New folder (2)\athlete_events.csv\noc_regions.csv")
        obj = df_m()
        self.M_DF=obj.Filter_m_df()
        
        

    def Total(self):
        T_edition = len(self.df["Year"].unique())
        T_H = len(self.df["City"].unique())
        T_S = len(self.df["Sport"].unique())
        T_E = len(self.df["Event"].unique())
        T_NOC = len(self.df["NOC"].unique())
        T_P_N = len(self.df["Name"].unique())
        return T_edition, T_H, T_S, T_E, T_NOC, T_P_N

    def nation_VS_year(self):
        nation_participation = self.M_DF.groupby("Year")["region"].nunique().reset_index(name="Nations")
        fig = plty.line(nation_participation, x="Year", y="Nations", title="Nations Participating Over the Years")
        return fig

    def event_VS_year(self):
        event_per_year = self.M_DF.groupby("Year")["Event"].nunique().reset_index()
        event_per_year.rename(columns={"Event": "Number of Events"}, inplace=True)
        fig = plty.line(event_per_year, x="Year", y="Number of Events", title="Number of Events Over the Years")
        return fig

    def Athlete_vs_year(self):
        athletes_per_year = self.M_DF.groupby("Year")["Name"].nunique().reset_index(name="Athletes")
        fig = plty.line(athletes_per_year, x="Year", y="Athletes", title="Athletes Participation Over the Years")
        return fig
    
    def sport_Parti_vs_year(self):
        top_sports = self.M_DF.groupby("Sport")["Name"].nunique().sort_values(ascending=False).head(4).index
        sport_participation = self.M_DF.groupby(["Sport", "Year"])["Name"].nunique().reset_index(name="Participation")
        sport_participation = sport_participation[sport_participation["Sport"].isin(top_sports)]
        sport_participation["Year"] = sport_participation["Year"].astype(str)
        fig = plty.bar(sport_participation,
                     x="Year",
                     y="Participation",
                     color="Sport",
                     barmode="group",
                     title="Top 4 Sport Participation per Edition",
                     template="plotly_white",
                     width=1100,
                     height=600)

        fig.update_layout(
            xaxis_title="Olympic Year",
            yaxis_title="Number of Participants",
            bargap=0.15,
            font=dict(size=13),
            xaxis=dict(tickangle=-45)
        )
        return fig

    def F_S_A(self):
        S_A = self.M_DF.groupby("Name")[["Gold", "Silver", "Bronze"]].sum()
        S_A["Total Medal"] = S_A["Gold"] + S_A["Silver"] + S_A["Bronze"]
        S_A = S_A.sort_values("Total Medal", ascending=False).reset_index()
        F_S_A = S_A.head(10)
        F_S_A.index = range(1, len(F_S_A) + 1)
        F_S_A.index.name = "Rank"
        df_plot = F_S_A.melt(
            id_vars="Name",
            value_vars=["Gold", "Silver", "Bronze"],
            var_name="Medal",
            value_name="Count"
        )
        fig = plty.bar(df_plot,x="Name",
                     y="Count",
                     color="Medal",
                     barmode="group",
                     title="Top 10 Successful Athletes by Medals",
                     template="plotly_white",
                     width=1100,
                     height=600)
        fig.update_layout(
            xaxis_title="Athlete Name",
            yaxis_title="Medal Count",
            xaxis=dict(tickangle=-45)
        )
        return fig
