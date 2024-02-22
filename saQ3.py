
def student(id, fname, lname, courses):
    return{
    'id' : id,
    'name' :[fname, lname],
    'courses' : courses
    }

print (student(1, "Clyde", "Joseph",["Agriculture","A"]))


def get(student):
    return student

