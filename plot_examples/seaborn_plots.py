import seaborn as sns 
import pandas as pd  # Importing pandas library for data manipulation
import matplotlib.pyplot as plt  # Importing matplotlib library for creating plots
from data_interface import DataInterface
import numpy as np

df = DataInterface()
df.create("Players_data.csv")
data = df.data

columns = ['Jump Height (Flight Time) [cm] ', 'Peak Power [W] ', 'Peak Power / BM [W/kg] ', 'Eccentric Peak Power [W] ', 'Eccentric Peak Power / BM [W/kg] ']


""" -------------------------------------------------- HISTOGRAM ----------------------------------------------------------  """

# sns.set_palette("pastel")
# sns.set_style("darkgrid")
# sns.set_theme("talk")
# sns.set_color_codes("dark")
# sns.histplot(data= data , x = columns[0], bins = 5)
# plt.title("Distribution of players Jump Height")

# plt.tight_layout()
# plt.show()  # Displaying the plot


""" -------------------------------------------------- SCATTERPLOT --------------------------------------------------------- """
# # Sample soccer player data
# data = {
#     "Name": [
#         "Lionel Messi",
#         "Cristiano Ronaldo",
#         "Neymar",
#         "Kylian Mbappé",
#         "Mohamed Salah",
#     ],
#     "Age": [34, 36, 29, 22, 29],
#     "Market Value (M€)": [80, 45, 100, 160, 110],
# }

# df = pd.DataFrame(data)  # Creating a pandas DataFrame from the data dictionary

# # Plotting market value vs. age
# sns.scatterplot(
#     data=df, x="Age", y="Market Value (M€)", hue="Name", s=100
# )  # Creating a scatterplot with seaborn
# plt.title("Soccer Players Market Value vs. Age")  # Adding a title to the plot
# plt.show()  # Displaying the plot


""" ------------------------------------------------- JOIN PLOT -------------------------------------------------------------- """

# # Define a dictionary containing data
# data = pd.DataFrame({
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
#     'Books_Read': [34, 36, 29, 30, 29],
#     'Hours_TV_Watched': [10, 7, 12, 8, 9],
# })

# # Create a jointplot 
# sns.jointplot(x='Books_Read', y='Hours_TV_Watched', data=data)

# # Display the plot
# plt.show()

""" --------------------------------------------------- FACET GRID -------------------------------------------------------- """

# # Set seed for reproducibility
# np.random.seed(0)

# # Define categories
# categories = ['Category A', 'Category B', 'Category C', 'Category D']  
# groups = ['Group 1', 'Group 2', 'Group 3', 'Group 4']  

# # Generate some synthetic data
# values = np.concatenate([np.random.normal(loc=mu, scale=5, size=100).astype(int) for mu in [80, 60, 50, 30]])

# # Create a dataframe
# data = {
#     'Category': np.repeat(categories, 100),  
#     'Group': np.tile(np.repeat(groups, 25), 4),  
#     'Value': values  
# }
# df = pd.DataFrame(data)  

# # Create a FacetGrid to visualize the data
# g = sns.FacetGrid(df, col='Group', row='Category', hue='Category', palette='muted', margin_titles=True)

# # Map histogram plot to the FacetGrid for the 'Value' column
# g = g.map(plt.hist, 'Value')

# plt.tight_layout()
# plt.show()  


""" ---------------------------------------------- SCATTER PLOT MATRIX ----------------------------------------------- """
# # Set seed for reproducibility
# np.random.seed(0)

# # Generate some synthetic data
# players = ['Player' + str(i) for i in range(1, 101)]  # Create a list of player names
# ages = np.random.randint(18, 40, size=100)  # Generate random ages between 18 and 40 for 100 players
# goals = np.random.poisson(lam=10, size=100)  # Generate random goals scored using Poisson distribution for 100 players
# assists = np.random.poisson(lam=5, size=100)  # Generate random assists using Poisson distribution for 100 players
# values = np.random.normal(loc=50, scale=15, size=100).astype(int)  # Generate random market values using normal distribution for 100 players

# # Create a dataframe
# data = {
#     'Player': players,
#     'Age': ages,
#     'Goals Scored': goals,
#     'Assists': assists,
#     'Market Value (in M€)': values
# }
# df = pd.DataFrame(data)  # Create a pandas DataFrame from the generated data

# # Create a scatterplot matrix
# sns.pairplot(df.drop('Player', axis=1))  # Create a scatterplot matrix of the numerical columns in the DataFrame
# plt.show()  # Display the scatterplot matrix


############## scatter plot matrix using our data ############# 

# serie_jump = df.get_mean_values(columns[0])
# serie_power = df.get_mean_values(columns[1])
# serie_power_bm = df.get_mean_values(columns[2])
# data_subset = {
#     "Name" : serie_jump.index.tolist()[10:20],
#     columns[0] : serie_jump.values.tolist()[10:20],
#     columns[1] : serie_power.values.tolist()[10:20],
#     columns[2] : serie_power_bm.values.tolist()[10:20]
# }
# df_subset = pd.DataFrame(data_subset)
# # print(df_subset)
# # Create a scatterplot matrix
# # sns.pairplot(df_subset.drop('Name', axis=1),hue='Name')  # Create a scatterplot matrix of the numerical columns in the DataFrame
# sns.pairplot(df_subset, hue='Name')

# plt.show()  # Display the scatterplot matrix



""" ----------------------------------------- REGRESSION SCATTER PLOT ---------------------------------------------------- """
# reps = df.get_mean_values("Reps")
# serie_jump = df.get_mean_values(columns[0])

# data_subset = {
#     "Name" : serie_jump.index.tolist(),
#     columns[0] : [round(num,2) for num in serie_jump.values.tolist()],
#     "Reps" : [round(num) for num in reps.values.tolist()]
# }

# df_subset = pd.DataFrame(data_subset)


# sns.set_style("darkgrid")  
# plt.figure(figsize=(12, 6))  

# # Create a scatter plot with a regression line using seaborn
# sns.regplot(y="Reps", x=columns[0], data=df_subset, marker="o", scatter_kws={"s": 200, "alpha": 0.5})
# plt.title("Jump Height in comparison with the repetitions")  
# plt.ylabel("Repetitions")  
# plt.xlabel("Height (cm)")  

# plt.show()  

