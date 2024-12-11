def sunsetViews(buildings, direction):
    # Not using Stack
    buildingsHaveSunset = []

    if direction == "WEST":
        initiateIndex = 0    
    else:
        initiateIndex = len(buildings) - 1
    
    if direction == "WEST":
        step = 1
    else:
        step = -1
    
    index = initiateIndex
    maxBuildingHeight = 0
    while index >= 0 and index < len(buildings):
        HeightCurrBuilding = buildings[index]

        if HeightCurrBuilding > maxBuildingHeight:
            buildingsHaveSunset.append(index)

        maxBuildingHeight = max(maxBuildingHeight, HeightCurrBuilding)
        index += step

    if direction == "EAST":
        return buildingsHaveSunset[::-1]
    
    return buildingsHaveSunset

# Example input
buildings = [3, 5, 4, 4, 3, 1, 3, 2]
direction = "EAST"

# Run the function with the example input
result = sunsetViews(buildings, direction)
print("Buildings with a sunset view:", result)