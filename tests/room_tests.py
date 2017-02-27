import unittest

from app.dojo import Dojo
from app.person import Fellow, Staff
from app.room import Room


class TestDojo(unittest.TestCase):
    longStr = "RED\n" + "------------" \
        "------------------\n" \
        "bolaji olajide\n"

    longStr2 = "UNALLOCATED LIST\n" + "---------------" \
        "---------------\nbolaji olajide: Living Space\n" \
        "ladi adeniran: Living Space\n"

    def setUp(self):
        self.my_dojo = Dojo()

    def tearDown(self):
        Dojo.rooms_in_dojo = {}
        Dojo.all_office = []
        Dojo.all_living_space = []
        Dojo.unallocated_persons = {}

    def test_create_office(self):
        initial_room_count = len(self.my_dojo.rooms_in_dojo)
        self.assertEqual(initial_room_count, 0)
        self.my_dojo.create_room('office', ['meeting'])
        self.assertTrue('meeting' in self.my_dojo.rooms_in_dojo)
        new_room_count = len(self.my_dojo.rooms_in_dojo)
        self.assertEqual(new_room_count - initial_room_count, 1)
        same_meeting_office = self.my_dojo.create_room('office', ['meeting'])
        self.assertEqual(same_meeting_office, 'Room already exist.\n')
        double_red_offices = self.my_dojo.create_room('office', ['red', 'red'])
        self.assertEqual(double_red_offices,
                         'An office called red has been created.'
                         '\nRoom already exist.\n')
        self.assertTrue('red' in self.my_dojo.rooms_in_dojo)

    def test_create_ls(self):
        initial_room_count = len(self.my_dojo.rooms_in_dojo)
        self.assertEqual(initial_room_count, 0)
        self.my_dojo.create_room('living', ['blue'])
        self.assertTrue('blue' in self.my_dojo.rooms_in_dojo)
        new_room_count = len(self.my_dojo.rooms_in_dojo)
        self.assertEqual(new_room_count, 1)
        same_blue_ls = self.my_dojo.create_room('living', ['blue'])
        self.assertEqual(same_blue_ls, 'Room already exist.\n')
        double_red_ls = self.my_dojo.create_room('living', ['red', 'red'])
        self.assertEqual(double_red_ls,
                         'A living space called red has been created.'
                         '\nRoom already exist.\n')
        self.assertTrue('red' in self.my_dojo.rooms_in_dojo)

    def test_add_staff(self):
        self.my_dojo.create_room('office', ['blue'])
        self.my_dojo.create_room('living', ['red'])
        office_one = self.my_dojo.all_office[0]
        living_one = self.my_dojo.all_living_space[0]
        initial_person_count = len(office_one.room_members)
        self.assertEqual(initial_person_count, 0)
        self.my_dojo.add_person('ladi', 'adeniran', 'staff')
        second_person_count = len(office_one.room_members)
        self.assertEqual(second_person_count, 1)
        self.my_dojo.add_person('bolaji', 'olajide', 'staff', 'y')
        third_person_count = len(office_one.room_members)
        persons_in_living_count = len(living_one.room_members)
        self.assertEqual(third_person_count, 2)
        self.assertEqual(persons_in_living_count, 0)

    def test_add_more_than_six_person_in_office(self):
        self.my_dojo.create_room('office', ['blue'])
        office_one = self.my_dojo.all_office[0]
        initial_person_count = len(office_one.room_members)
        self.assertEqual(initial_person_count, 0)
        self.my_dojo.add_person('ladi', 'adeniran', 'staff')
        second_person_count = len(office_one.room_members)
        self.assertEqual(second_person_count, 1)
        self.my_dojo.add_person('bolaji', 'olajide', 'staff', 'y')
        self.my_dojo.add_person('oluwadamilola', 'durodola', 'staff')
        self.my_dojo.add_person('mumeen', 'olasode', 'staff')
        self.my_dojo.add_person('ichiato', 'ikikin', 'staff')
        self.my_dojo.add_person('falz', 'thabadguy', 'staff')
        self.my_dojo.add_person('valentine', 'mbonu', 'staff')
        third_person_count = len(office_one.room_members)
        self.assertNotEqual(third_person_count, 7)
        self.assertEqual(third_person_count, 6)

    def test_add_fellow(self):
        self.my_dojo.create_room('living', ['blue'])
        living_one = self.my_dojo.all_living_space[0]
        initial_person_count = len(living_one.room_members)
        self.assertEqual(initial_person_count, 0)
        self.my_dojo.add_person('bolaji', 'olajide', 'fellow', 'y')
        second_person_count = len(living_one.room_members)
        self.assertEqual(second_person_count, 1)
        self.my_dojo.add_person('ladi', 'adeniran', 'fellow', 'y')
        third_person_count = len(living_one.room_members)
        self.assertEqual(third_person_count, 2)

    def test_test_add_more_than_four_person_in_living(self):
        self.my_dojo.create_room('living', ['blue'])
        living_one = self.my_dojo.all_living_space[0]
        self.my_dojo.add_person('oluwadamilola', 'durodola', 'fellow', 'y')
        self.my_dojo.add_person('bolaji', 'olajide', 'fellow', 'y')
        self.my_dojo.add_person('mumeen', 'olasode', 'fellow', 'y')
        self.my_dojo.add_person('ichiato', 'ikikin', 'fellow', 'y')
        initial_person_count = len(living_one.room_members)
        self.assertEqual(initial_person_count, 4)
        self.my_dojo.add_person('falz', 'thabadguy', 'fellow', 'y')
        second_person_count = len(living_one.room_members)
        self.assertNotEqual(initial_person_count, 5)
        self.assertEqual(initial_person_count, 4)

    def test_print_room(self):
        self.my_dojo.create_room('office', ['red'])
        self.my_dojo.create_room('living', ['blue'])
        self.my_dojo.add_person('bolaji', 'olajide', 'staff', 'y')
        answer = self.my_dojo.print_room('red')
        self.assertEqual(
            answer, 'bolaji olajide --> staff\n')
        answer = self.my_dojo.print_room('blue')
        self.assertEqual(
            answer, 'There are no occupants in blue at the moment.')
        self.my_dojo.add_person('ladi', 'adeniran', 'fellow', 'y')
        output = self.my_dojo.print_room('red')
        self.assertEqual(output, 'bolaji olajide --> staff\n'
                         'ladi adeniran --> fellow\n')
        answer = self.my_dojo.print_room('blue')
        self.assertEqual(
            answer, 'ladi adeniran --> fellow\n')

    def test_print_allocations(self):
        self.my_dojo.create_room('office', ['red'])
        self.my_dojo.add_person('bolaji', 'olajide', 'fellow')
        content = self.my_dojo.print_allocations()
        self.assertEqual(content, self.longStr)

    def test_file_print_allocations(self):
        self.my_dojo.create_room('office', ['red'])
        self.my_dojo.add_person('bolaji', 'olajide', 'fellow', 'y')
        self.my_dojo.print_allocations('output')
        my_file = open('data/output.txt', 'r')
        content = my_file.read()
        my_file.close()
        self.assertEqual(content, self.longStr)

    def test_file_print_unallocated(self):
        self.my_dojo.create_room('office', ['red'])
        self.my_dojo.add_person('bolaji', 'olajide', 'fellow', 'y')
        self.my_dojo.add_person('ladi', 'adeniran', 'fellow', 'y')
        self.my_dojo.print_unallocated('test_output')
        my_file = open('data/test_output.txt', 'r')
        content = my_file.read()
        my_file.close()
        self.assertEqual(content, self.longStr2)

    def test_print_unallocated(self):
        self.my_dojo.create_room('office', ['red'])
        self.my_dojo.add_person('bolaji', 'olajide', 'fellow', 'y')
        self.my_dojo.add_person('ladi', 'adeniran', 'fellow', 'y')
        content = self.my_dojo.print_unallocated()
        self.assertEqual(content, self.longStr2)
