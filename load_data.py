with open("workout_log.csv") as f:
  exercise_dict = {}
  # found = set()
  for line in f:
    parts = line.strip().split(",")
    if parts[2] == "8th from top":
      parts[2] = "40"
    if parts[2] == "7th from top":
      parts[2] = "35"
    exercise = parts[1]
    try:
          weight = float(parts[2])
    except ValueError:
      continue
    if exercise not in exercise_dict:
      exercise_dict[exercise] = weight
    else:
      if exercise_dict[exercise] < weight:
        exercise_dict[exercise] = weight
        
for execise, weight in exercise_dict.items():
  print(f"{execise}: {weight}")

  # for line in f:
  #   if "top" in line:
  #     print(line)

  #   if "top" in line:
  #     found.add(line.strip().split(",")[2])
  # print(found)
