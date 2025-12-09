from crud import insert_user, get_users
# , update_user, delete_user

# INSERT
insert_user("Charlie", "charlie@example.com")

insert_user("John", "john@example.com")

# GET
users = get_users()
for u in users:
    print(u)

# # UPDATE
# update_user(1, "John Updated", "john.updated@example.com")

# # DELETE
# delete_user(2)
