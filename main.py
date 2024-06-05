mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]
# Varialbles
missionTotal = len(mission_names)
successfulMissions = sum(mission_success)
successRate = (successfulMissions/missionTotal) * 100
missionsBefore2000 = []
for missions in range(len(mission_names)):
    if mission_years[missions] < 2000:
        missionsBefore2000.append(mission_names[missions])
# Print out to console
print("Total Number of Missions: ", missionTotal)
print("Number of Successful Missions: ", successfulMissions)
print(f"Success Rate: {successRate:.2f}%")
print("Missions Launched Before the Year 2000: ")
for missions in missionsBefore2000:
    print("-", missions)
