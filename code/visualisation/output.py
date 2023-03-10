import json

def output(grid):
    """

    Args:
        batteries (_type_): _description_
        houses (_type_): _description_
    """
    grid_json = [{"district":int(grid.district),
    f"costs-{grid.price_type}":grid.total_price}]
    
    for battery in grid.batteries:
        houses = []
        for house in battery.houses:
            cables = []
            for cable in house.cables:
                cables.append(f"{cable[0]},{cable[1]}")
            houses.append({
            "location": f"{house.pos_x},{house.pos_y}",
            "output": house.max_output,
            "cables": cables})
        grid_json.append({
            "location":f"{battery.pos_x},{battery.pos_y}",
            "capacity": battery.capacity,
            "houses": houses
        })
    
    grid_json = json.dumps(grid_json, indent=2)
    with open("output.json", "w") as outfile:
        outfile.write(grid_json)
    