import pandas as pb
import numpy as np
class M_df:
    def __init__(self):
        self.df=pb.read_csv(r"C:\Users\Paramjeet\OneDrive\Desktop\New folder (2)\athlete_events.csv\athlete_events.csv")
        self.noc_df=pb.read_csv(r"C:\Users\Paramjeet\OneDrive\Desktop\New folder (2)\athlete_events.csv\noc_regions.csv")
    
    def Filter_m_df(self):
        self.df = self.df[self.df["Season"] == "Summer"]
        self.M_DF = self.df.merge(self.noc_df, on="NOC", how="left")
        # Properly drop duplicates
        self.M_DF = self.M_DF.drop_duplicates()
        self.M_DF = self.M_DF.drop_duplicates(subset=["NOC", "Games", "Year", "City", "Sport", "Event", "Medal"])
        # Convert medals to one-hot encoded columns
        dummy = pb.get_dummies(self.M_DF["Medal"], dtype=np.int16)
        self.M_DF = pb.concat([self.M_DF, dummy], axis=1)
        return self.M_DF