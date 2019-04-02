min_sleep_time = int(input())
max_sleep_time = int(input())
actual_sleep_time = int(input())

if actual_sleep_time < min_sleep_time:
  print("Недосып")
elif actual_sleep_time > max_sleep_time:
  print("Пересып")
else:
  print("Это нормально")