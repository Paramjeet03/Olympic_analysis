import pandas as pb
import numpy as np
class Medal_t:
    def __init__(self):
        self.df=pb.read_csv(r"C:\Users\Paramjeet\OneDrive\Desktop\New folder (2)\athlete_events.csv\athlete_events.csv")
        self.noc_df=pb.read_csv(r"C:\Users\Paramjeet\OneDrive\Desktop\New folder (2)\athlete_events.csv\noc_regions.csv")
    
    def medal_tally(self):
        df = self.df[self.df["Season"] == "Summer"]
        self.M_DF = df.merge(self.noc_df, on="NOC", how="left")
        # Properly drop duplicates
        self.M_DF = self.M_DF.drop_duplicates()
        self.M_DF = self.M_DF.drop_duplicates(subset=["NOC", "Games", "Year", "City", "Sport", "Event", "Medal"])
        # Convert medals to one-hot encoded columns
        dummy = pb.get_dummies(self.M_DF["Medal"], dtype=np.int16)
        self.M_DF = pb.concat([self.M_DF, dummy], axis=1)
        # Group by region and aggregate medals
        M_df = self.M_DF.groupby("region").sum(numeric_only=True)[["Gold", "Silver", "Bronze"]]
        M_df = M_df.sort_values("Gold", ascending=False).reset_index()
        # Rename columns and add total
        M_df.rename(columns={"region": "Region(Country)"}, inplace=True)
        M_df.index = range(1, len(M_df) + 1)
        M_df["Total_medal"] = M_df["Gold"] + M_df["Silver"] + M_df["Bronze"]
        return M_df

    def Year(self):
        years = sorted(self.df["Year"].dropna().unique().tolist())
        return ["Overall"] + years
    
    def Country(self):
        self.M_DF=self.df.merge(self.noc_df,on="NOC",how="left")
        return ["Overall"] + sorted(self.M_DF["region"].dropna().drop_duplicates().to_list()) 
    
    def Filtered(self,Year_T,Country):
        T_DS=self.M_DF.drop_duplicates().drop(["ID","Age","notes","Medal","NOC","Games"],axis=1)
        if Year_T == "Overall":
            result= T_DS[T_DS["region"] == Country]
        elif Country=="Overall":    
            result= T_DS[T_DS["Year"] == Year_T]
        else:
            result= T_DS[(T_DS["Year"] == Year_T) & (T_DS["region"] == Country)].reset_index()
        return result