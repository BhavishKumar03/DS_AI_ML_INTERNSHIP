raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
unique_users = set(raw_logs)
check_id = "ID05" in unique_users
print("Is ID05 in unique_users?", check_id)
print("Original list length:", len(raw_logs))
print("Unique set length:", len(unique_users))
print("Unique Visitors:", unique_users)