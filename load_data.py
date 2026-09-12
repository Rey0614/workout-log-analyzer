def clean_weight(value):
  if value == "8th from top":
    value = "40"
  elif value == "7th from top":
    value = "35"
  try:
    return float(value)
  except ValueError:
    return None

def get_max_weight(filename):
  with open(filename) as f:
    result = {}
    for line in f:
      parts = line.strip().split(",")
      weight = clean_weight(parts[2])
      exercise = parts[1]
      if weight is None:
        continue
      if exercise not in result:
        result[exercise] = weight
      else:
        if result[exercise] < weight:
          result[exercise] = weight
  return result

def print_results(result_dict):
  for exercise, weight in result_dict.items():
    print(f"{exercise}: {weight}")

max_weight = get_max_weight("workout_log.csv")
print_results(max_weight)

