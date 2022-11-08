url = input()  # input url
n = int(input())  # total number of params
params = input().split(" ")  # Space separated params
vals = [int(val) for val in input().split(" ")]  # Space separated params values
actual_url = url.split("?")[0]
print(actual_url)

params_raw = url.split("?")[-1].split(",")
param_val_map_in_url = {}
for param in params_raw:
    param_val = param.split("=")
    param_val_map_in_url[param_val[0]] = int(param_val[1])

param_val_map_input = {}
for index, val in enumerate(params):
    param_val_map_input[val] = vals[index]

total_found = 0
found = 404
found_list = []
for param in param_val_map_input:
    if param in param_val_map_in_url and param_val_map_in_url[param] <= param_val_map_input[param]:
        found = 200
        total_found += 1
        found_list.append(param)

found_list = sorted(found_list)
print(total_found)
for param in found_list:
    print(param, param_val_map_input.get(param))

print(found)

