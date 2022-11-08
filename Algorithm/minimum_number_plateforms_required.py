def find_minimum_platforms_needed(arrival_time, departure_times):
    platforms = {}
    arrival_departure_map = {arr_time: departure_times[index] for index, arr_time in enumerate(arrival_time)}
    print(arrival_departure_map)
    for arr_time in arrival_time:
        if not platforms:
            platforms[1] = arrival_departure_map[arr_time]
        else:
            found_platform = False
            for platform in platforms:
                if platforms.get(platform) <= arr_time:
                    found_platform = True
                    platforms[platform] = arrival_departure_map[arr_time]
                    break
            if not found_platform:
                platforms[len(platforms) + 1] = arrival_departure_map[arr_time]
    print(len(platforms), platforms)
    return len(platforms)


find_minimum_platforms_needed([900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000])
find_minimum_platforms_needed([900, 940], [910, 1200])
