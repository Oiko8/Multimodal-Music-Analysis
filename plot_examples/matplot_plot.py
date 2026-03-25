import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from data_interface import DataInterface

df = DataInterface()
df.create("Players_data.csv")
data = df.data
column = "Jump Height (Flight Time) [cm] "


""" -------------------------------------------------------- MATPLOT STRUCTURE ---------------------------------------------------- """
# players_max_jump = df.get_max_values(column)
# players = players_max_jump.index.tolist()
# values = players_max_jump.values.tolist()

# # same commands , all in one
# # fig = plt.figure(figsize=(10, 5))
# # ax = fig.add_subplot(1,1,1)
# fig, ax = plt.subplots(figsize=(12, 5))
# ax.bar(players[15:20], values[15:20])
# ax.set_title('Max jump of each player')
# ax.set_xlabel('Players')
# ax.set_ylabel('Jump Height[cm]')

# plt.show()



""" ---------------------------------------------------------- LINE PLOT ------------------------------------------------------------ """
# list_of_players = ["GIANNIS OIKONOMIDIS", "NIKOS ATHANASIOU"]
# df_player1 = data[data["Name"] == "GIANNIS OIKONOMIDIS"]
# df_player2 = data[data["Name"] == "NIKOS ATHANASIOU"]
# player1_values = df_player1[column].tolist()
# player2_values = df_player2[column].tolist()
# tries1 = np.arange(0, len(player1_values))
# tries2 = np.arange(0, len(player2_values))


# plt.figure(figsize=(12,6))
# plt.plot(tries1, player1_values, label = list_of_players[0], color = "blue", linestyle = "-", marker = "s") #if marker is s, it means square
# plt.plot(tries2, player2_values, label = list_of_players[1], color = "red", linestyle = "-", marker = "s") 
# plt.title("Jump Height [cm] throught time")
# plt.legend()

# # adding arrow
# plt.arrow( 5,max(player1_values), 0, -5, length_includes_head=True, head_width=0.3, head_length=1, color='red')

# plt.show()


#                       ######### comparing between 5 top leagues #############
# premier_league_goals = [975, 1026, 1064, 1018, 1072, 1074]
# la_liga_goals = [1043, 1002, 1118, 1024, 993, 983]
# serie_a_goals = [1033, 979, 1115, 1019, 1017, 1015]
# bundesliga_goals = [843, 866, 877, 855, 967, 973]
# ligue_1_goals = [947, 960, 991, 1033, 972, 973]

# years = np.arange(2014, 2020)

# plt.figure(figsize=(12, 6))
# plt.plot(
#     years,
#     premier_league_goals,
#     label="Premier League",
#     linestyle="-",
#     color="blue",
#     marker="o",
# )
# plt.plot(years, la_liga_goals, label="La Liga", linestyle="--", color="red", marker="s")
# plt.plot(
#     years, serie_a_goals, label="Serie A", linestyle="-.", color="green", marker="^"
# )
# plt.plot(
#     years,
#     bundesliga_goals,
#     label="Bundesliga",
#     linestyle=":",
#     color="purple",
#     marker="D",
# )
# plt.plot(
#     years, ligue_1_goals, label="Ligue 1", linestyle="-", color="orange", marker="x"
# )

# plt.xlabel("Year")
# plt.ylabel("Goals")
# plt.title("Goals Scored by Top 5 European Leagues (2014-2019)")
# plt.legend()

# plt.show()


""" -------------------------------------------------- SCATTER PLOT -----------------------------------------------------"""
# print(df.columns_name)
# columns = ['Eccentric Peak Power [W] ', 'Eccentric Peak Power / BM [W/kg] ']
# power = df.get_mean_values(columns[0])
# powerPerBm = df.get_mean_values(columns[1])
# players = power.index.tolist()[15:20]
# power = power.values.tolist()[15:20]
# powerPerBm = powerPerBm.values.tolist()[15:20]

# plt.figure(figsize=(12,6))
# plt.scatter(power, powerPerBm, s=20, edgecolors='black', linewidths=1)

# for i, player in enumerate(players):
#     plt.annotate(player, (power[i],powerPerBm[i]), textcoords="offset points", xytext=(-20, 5))

# plt.xlabel('Eccentric Power [W]')
# plt.ylabel('Eccentric Power / BM [W/kg]')
# plt.title('Average Eccentric Power and Average Eccentric Power/ BM')

# # plt.grid(True)
# plt.show()


""" ---------------------------------------------------- BAR PLOT -------------------------------------------------------- """

# column = "Peak Power [W] " 
# serie_peak_power = df.get_mean_values(column)
# player_names = serie_peak_power.index.tolist()[15:20]
# values = serie_peak_power.values.tolist()[15:20]

# # # normal bar
# plt.figure(figsize=(14,6))
# plt.bar(player_names, values)
# plt.xlabel("Players")
# plt.xticks(player_names, rotation = 45)
# plt.grid(False)
# plt.title("Average Peak Power [W]")

# # # orizontal
# # plt.figure(figsize=(12,6))
# # plt.barh(player_names, values)
# # plt.ylabel("Players")
# # plt.grid(False)
# # plt.title("Average Peak Power [W]")
# # plt.yticks(player_names, rotation = 45)

# plt.tight_layout() # USEFUL!!!! MAKE THE PLOT LAYOUT TO FIT THE SCREEN

# plt.show()


""" ----------------------------------------------------- STACKED BAR ------------------------------------------------- """
# column = "Jump Height (Flight Time) [cm] "
# players_max_jump = df.get_max_values(column)
# players = players_max_jump.index.tolist()[15:20]
# max_values = players_max_jump.values.tolist()[15:20]

# players_mean_jump = df.get_mean_values(column)
# mean_values = players_mean_jump.values.tolist()[15:20]

# plt.figure(figsize=(12,6))


# plt.bar(players, max_values, label = "Max", width=0.5, zorder = 1)
# plt.bar(players, mean_values, bottom = max_values, label="Average", width=0.5, zorder = 2)
# # # OVERLAPPING BAR
# # plt.bar(players, mean_values, label="Average", width=0.5, zorder = 2)

# plt.xlabel("Players")
# plt.title(column)

# plt.tight_layout()

# plt.show()



""" ----------------------------------------------------------- PIE CHART ------------------------------------------------- """

# column = "Concentric Peak Force [N] "
# serie_peak_force = df.get_max_values(column)
# player_names = serie_peak_force.index.tolist()[15:20]
# values = serie_peak_force.values.tolist()[15:20]

# explode = (0.01, 0.01, 0.01, 0.01, 0.01)  # separate each sector

# # Pie plot
# plt.figure(figsize=(12, 6))
# plt.pie(values, labels=player_names, autopct='%1.2f%%', startangle=90, explode= explode)
# plt.title('Peak force per player: Comparison')

# plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular


# # # Draw a white circle at the center : making it a donut
# # centre_circle = plt.Circle((0, 0), 0.70, fc='white')
# # fig = plt.gcf()
# # fig.gca().add_artist(centre_circle)

# plt.tight_layout()
# plt.show()


""" ---------------------------------------------------- HISTOGRAM --------------------------------------------------- """
# player_goals = [32, 36, 22, 28, 30, 24, 26, 34, 29, 31]
# bins = 5
# range = (20, 40)
# color = 'blue'
# alpha = 0.5

# plt.figure(figsize=(12, 6))
# plt.hist(player_goals, bins, range, color=color, alpha=alpha)
# plt.xlabel('Goals Scored')
# plt.ylabel('Frequency')
# plt.title('Histogram of Goals Scored by Famous Soccer Players')
# plt.show()


""" ------------------------------------------------------- BOX PLOTS ------------------------------------------------------ """

# player_goals = [32, 36, 22, 28, 30, 24, 26, 34, 29, 31]

# plt.figure(figsize=(12, 6))
# plt.boxplot(player_goals, vert=True, patch_artist=True,
#             boxprops=dict(facecolor='blue', color='blue'),
#             medianprops=dict(color='red'),
#             whiskerprops=dict(color='green', linestyle='--'),
#             capprops=dict(color='purple'),
#             flierprops=dict(marker='o', markerfacecolor='yellow', markersize=8))
# plt.ylabel('Goals Scored')
# plt.title('Box Plot of Goals Scored by Famous Soccer Players')
# plt.show()



""" ---------------------------------------------------------- HEATMAP ---------------------------------------------------- """
# # Sample data (positions of soccer players on the field)
# data = np.array([
#     [3, 2, 1, 0, 0],
#     [2, 3, 2, 1, 0],
#     [1, 2, 3, 2, 1],
#     [0, 1, 2, 3, 2],
#     [0, 0, 1, 2, 3]
# ])

# plt.figure(figsize=(12, 6))
# plt.imshow(data, cmap='coolwarm', interpolation='nearest')
# plt.colorbar()

# # Custom labels
# x_labels = ['Left', 'Mid-Left', 'Center', 'Mid-Right', 'Right']
# y_labels = ['Defense', 'Mid-Defense', 'Midfield', 'Mid-Attack', 'Attack']
# plt.xticks(np.arange(len(x_labels)), x_labels)
# plt.yticks(np.arange(len(y_labels)), y_labels)

# plt.show()


""" -------------------------------------------------- CONTOUR PLTO -------------------------------------------- """
# # Sample data (performance of soccer players)
# x = np.linspace(0, 5, 6)
# y = np.linspace(0, 5, 6)
# X, Y = np.meshgrid(x, y)
# Z = np.array([
#     [3, 2, 1, 0, 0, 0],
#     [2, 3, 2, 1, 0, 0],
#     [1, 2, 3, 2, 1, 0],
#     [0, 1, 2, 3, 2, 1],
#     [0, 0, 1, 2, 3, 2],
#     [0, 0, 0, 1, 2, 3]
# ])

# plt.figure(figsize=(12, 6))
# contour_plot = plt.contour(X, Y, Z, cmap='coolwarm')
# plt.clabel(contour_plot, inline=True, fontsize=8)
# plt.colorbar()

# # Custom labels
# x_labels = ['Messi', 'Ronaldo', 'Neymar', 'Mbappe', 'Salah', 'Lewandowski']
# y_labels = ['Goals', 'Assists', 'Passes', 'Dribbles', 'Tackles', 'Interceptions']
# plt.xticks(np.arange(len(x_labels)), x_labels, rotation=45)
# plt.yticks(np.arange(len(y_labels)), y_labels)
# plt.tight_layout()

# plt.show()


""" ---------------------------------------------------- 3D BOX PLOT --------------------------------------------- """


# # Sample data
# player_names = ['Lionel Messi', 'Cristiano Ronaldo', 'Neymar Jr', 'Kylian Mbappe', 'Mohamed Salah']
# goals = [68, 674, 366, 131, 186]
# assists = [305, 229, 216, 76, 74]
# appearances = [778, 895, 513, 216, 329]

# fig = plt.figure(figsize=(20, 8))
# ax = fig.add_subplot(111, projection='3d')

# xpos = np.arange(len(player_names))
# ypos = np.zeros(len(player_names))
# zpos = np.zeros(len(player_names))

# dx = np.ones(len(player_names))
# dy = np.array(assists)
# dz = np.array(goals)

# ax.bar3d(xpos, ypos, zpos, dx, dy, dz)

# ax.set_xticks(xpos)
# ax.set_xticklabels(player_names)
# ax.set_ylabel('Assists')
# ax.set_zlabel('Goals')

# plt.tight_layout()

# plt.show()


###########################################
# bar3d(x, y, z, dx, dy, dz)              #
# x: A list or array of x-coordinates.    #
# y: A list or array of y-coordinates.    #
# z: A list or array of z-coordinates.    #
# dx: A list or array of bar widths.      #
# dy: A list or array of bar depths.      #
# dz: A list or array of bar heights.     #
###########################################

#### my data with the 3d bar 
# columns = ['Eccentric Peak Power [W] ', 'Peak Power [W] ']
# eccentric_power = df.get_mean_values(columns[0])
# power = df.get_mean_values(columns[1])
# player_names = power.index.tolist()[15:20]
# eccentric_power = eccentric_power.values.tolist()[15:20]
# power = power.values.tolist()[15:20]

# # create the figure and add a 3d subplot
# fig = plt.figure(figsize=(12, 5))
# ax = fig.add_subplot(111, projection='3d')

# # setting the x,y,z coor and the dx,dy,dz
# xpos = np.arange(len(player_names))
# ypos = np.zeros(len(player_names))
# zpos = np.zeros(len(player_names))

# dx = np.full(len(player_names), 0.5)
# dy = np.array(eccentric_power) 
# dz = np.array(power) 

# # create the 3d plot
# ax.bar3d(xpos,ypos,zpos,dx,dy,dz, color = "lightblue", edgecolor='black', linewidth = 1.5)

# # setting the axis
# ax.set_xticks(xpos)
# ax.set_xticklabels(player_names)
# ax.set_ylabel('Eccentric Peak Power')
# ax.set_zlabel('Peak Power')
# plt.xticks(rotation = 45)


# plt.title("Average Peak power and Eccentric Peak power")

# plt.tight_layout()
# plt.show()



""" --------------------------------------------- COMBINING PLOTS IN THE SAME FIGURE --------------------------------------- """

# Define the sample data: players' names and their respective goals
players = ["Lionel Messi", "Cristiano Ronaldo", "Neymar Jr"]
goals = [672, 674, 366]

# Create a 1x2 subplot grid with a specified figure size
fig, ax = plt.subplots(1, 2, figsize=(18, 6))

# First subplot: Create a bar plot of goals scored by each player
ax[0].bar(players, goals)
# Set the title for the first subplot
ax[0].set_title("Goals Scored")

# Second subplot: Create a pie chart showing the distribution of goals among the players
ax[1].pie(goals, labels=players, autopct="%1.1f%%")
# Set the title for the second subplot
ax[1].set_title("Goals Distribution")

# space between plots
plt.subplots_adjust(wspace=0.1)

plt.tight_layout()
# Display the resulting plots
plt.show()

