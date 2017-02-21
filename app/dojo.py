from app.person import Fellow, Person, Staff
from app.room import LivingSpace, Office, Room


class Dojo(object):
    rooms_in_dojo = {}
    persons_in_dojo = {}
    all_office = []
    all_living_space = []
    unallocated_persons = {}

    def create_room(self, room_type, room_name):
        output = ""
        for room in room_name:
            if room in Dojo.rooms_in_dojo:
                output = output + ('Room already exist.\n')
            elif not room.isalnum():
                output = output + ('Invalid room naming convention!\n')
            elif room_type == 'office':
                new_room = Office(room)
                self.all_office.append(new_room)
                self.rooms_in_dojo[new_room.room_name] = new_room.room_type
                output = output + \
                    ('An office called %s has been created.\n' % room)
            elif room_type == 'living':
                new_room = LivingSpace(room)
                self.all_living_space.append(new_room)
                self.rooms_in_dojo[new_room.room_name] = new_room.room_type
                output = output + \
                    ('A living space called %s has been created.\n' % room)
            elif room_type != 'living' and room_type != 'office':
                output = output + ('Invalid command.\nFirst argument must be either'
                                   ' office or living.\n')
        return output
