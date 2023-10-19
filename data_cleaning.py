import pandas as pd
import matplotlib.pyplot as plt

# Assuming nfl_data is your DataFrame
nfl_data = pd.read_csv('nfl_data.csv')

# 1. Player improvement over time
# Assuming 'FantPt' as a measure of performance

players = nfl_data['Player'].unique()

for player in players:
    player_data = nfl_data[nfl_data['Player'] == player]
    plt.plot(player_data['Year'], player_data['FantPt'], label=player)

plt.xlabel('Year')
plt.ylabel('Performance (FantPt)')
plt.title('Player Improvement Over Time')
plt.legend()
plt.show()

# 2. Colleges producing the best players over time
# Assuming 'FantPt' as a measure of performance

colleges = nfl_data['College'].unique()
college_avg_performance = {}

for college in colleges:
    college_data = nfl_data[nfl_data['College'] == college]
    college_avg_performance[college] = college_data['FantPt'].mean()

# Plotting bar chart
plt.bar(college_avg_performance.keys(), college_avg_performance.values())
plt.xlabel('College')
plt.ylabel('Average Performance (FantPt)')
plt.title('Colleges producing the best players over time')
plt.xticks(rotation=90)  # Rotates X-Axis Ticks by 90-degrees
plt.show()
