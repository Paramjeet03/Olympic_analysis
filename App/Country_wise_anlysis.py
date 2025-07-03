from medal_tally import Medal_t as mt 
from Filtered_M_df import M_df as m_df_class
obj=mt()
class C_W_A:
    def Top_5_Func(self):
        df=obj.medal_tally()
        df=df.head(6).drop(["Gold","Silver","Bronze"],axis=1)
        return df
    
    def countryMedal_tally(self,region):
        df_obj=m_df_class()
        M_df=df_obj.Filter_m_df()
        C_M_T=M_df.groupby(["Year","Name","region","Sport"]).sum()[["Gold","Silver","Bronze"]].sort_values("Gold",ascending=False).reset_index() 
        C_M_T_region = C_M_T[
        (C_M_T["region"] == region) &
        ~((C_M_T["Gold"] == 0) & (C_M_T["Silver"] == 0) & (C_M_T["Bronze"] == 0))
        ].sort_values("Year").reset_index(drop=True)
        C_M_T_region.index = C_M_T_region.index + 1

        return C_M_T_region

    def region(self):
        df_obj=m_df_class()
        M_DF=df_obj.Filter_m_df()
        return list(M_DF["region"].drop_duplicates().reset_index(drop=True))
    
    def Top_10_athletes(self,region_df):
        region_df["Total Medal"]=region_df["Gold"]+region_df["Silver"]+region_df["Bronze"]
        F_U=F_U=region_df.sort_values("Total Medal",ascending=False).reset_index(drop=True)
        F_U.index+=1
        return F_U.head(10)