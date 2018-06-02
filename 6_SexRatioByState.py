import pandas as pd
import matplotlib.pyplot as plt


# the data frame
df = pd.read_csv("all-census-data/india-districts-census-2011.csv", usecols = ['State Name', 'Male', 'Female'])

# Grouping the States data and then summing up the Male and Female Data
df_sum = df.groupby('State Name')['Male', 'Female'].sum()

# Putting in a  new column called ratio
# df_sum["Ratio"] = ""

# getting in the ratios
df_sum[['Ratio']] = df_sum[['Female']].div(df_sum.Male, axis=0)

#  New DF
final_df = df_sum.loc[:, ['Ratio']]

# One can see the df which is going to be plotted now
# print final_df

#  Plotting the above data now
ax = final_df.plot(kind='bar', color='g', title ="Sex Ratio per State: INDIA", figsize=(10, 6), fontsize=12)
ax.set_xlabel("States", fontsize=12)
ax.set_ylabel("Sex Ratio", fontsize=12)

# A Few more touch-ups
plt.legend(loc='center left', bbox_to_anchor=(1.0, 1.0))
plt.subplots_adjust(bottom=.5)
plt.show()

