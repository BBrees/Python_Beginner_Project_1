contacts = {
    "number":3,
    "students":
        [
            {"name":"Sarah Holdernss", "email":"sarah.holderness@student.com"},
            {"name":"Harry Potter", "email":"harry.potter@student.com"},
            {"name":"Ron Weasly", "email":"ron.weasly@student.com"}
        ]
}


for students in contacts["students"]:
    print(students["email"])