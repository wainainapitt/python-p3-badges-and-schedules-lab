
def badge_maker(name):
    return "Hello, my name is {}.".format(name)

def batch_badge_creator(speakers):
    return ["Hello, my name is {}.".format(name) for name in speakers]

def assign_rooms(speakers):
    return ["Hello, {}! You'll be assigned to room {}!".format(name, index + 1) for index, name in enumerate(speakers)]

def printer(speakers):
    badges = batch_badge_creator(speakers)
    rooms = assign_rooms(speakers)

    for badge in badges:
        print(badge)

    for room_assignment in rooms:
        print(room_assignment)
