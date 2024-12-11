# Sunset Views Problem

The `sunsetViews` function determines which buildings in a row can see the sunset based on their height and the direction of the sunset. The direction can either be `"EAST"` (sunset on the right) or `"WEST"` (sunset on the left).

---

## Approach

1. **Initialize Variables**:
   - Use a list `buildingsHaveSunset` to store the indices of buildings that can see the sunset.
   - Determine the starting index (`initiateIndex`) and step direction (`step`) based on the `direction`.

2. **Traverse the Buildings**:
   - Use a while loop to iterate through the buildings from the starting index to the end (or beginning, depending on the direction).
   - Track the tallest building encountered so far using `maxBuildingHeight`.
   - For each building:
     - Compare its height with `maxBuildingHeight`.
     - If the current building is taller, it has a sunset view. Append its index to `buildingsHaveSunset`.
     - Update `maxBuildingHeight` to reflect the height of the tallest building seen so far.

3. **Reverse the Indices (If Necessary)**:
   - If the direction is `"EAST"`, reverse the order of indices in `buildingsHaveSunset` since they were collected from right to left.

4. **Return the Result**:
   - Return the list of indices for buildings with a sunset view.

---

## Complexity Analysis

- **Time Complexity**: **O(n)**, where `n` is the number of buildings.
   - The function iterates over the buildings only once.
- **Space Complexity**: **O(n)** in the worst case, due to the storage of indices in `buildingsHaveSunset`.

---

## Code 

```python
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

buildings = [3, 5, 4, 4, 3, 1, 3, 2]
direction = "EAST"

result = sunsetViews(buildings, direction)
print("Buildings with a sunset view:", result)

