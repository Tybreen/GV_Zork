from item import Item
from npc import NPC
from location import Location

#############
### Items ###
#############

test_food = Item("my_item_food", "This is a test food!", 10, 5)
test_item = Item("my_item_nonfood", "This is a test nonfood!", 0, 25)

############
### NPCs ###
############

mr_w = NPC("Mr. W", ("Mr. W is a professor at GVSU, he is very "
            "involved in computer science."))
mr_w.add_message("Hi there! If you need any coding help just ask!")

#################
### Locations ###
#################


mackinac = Location("Mackinac Hall", ("Mackinac Hall is one of "
            "GVSU’s academic buildings on the Allendale campus. It is "
            "commonly used for classrooms, offices, and student learning "
            "spaces."))
kirkhof = Location("Kirkhof Center", ("The Russel H. Kirkhof Center "
            "is a central student gathering space at GVSU. It includes areas "
            "for events, student organizations, meetings, and community "
            "activities."))
henry = Location("Henry Hall", ("Henry Hall is an academic building "
            "at GVSU connected to student learning and support services. It "
            "has housed resources such as the Tutoring and Reading Center, "
            "making it a useful place for academic help."))

mackinac.add_location("south", kirkhof)
mackinac.add_location("west", henry)
mackinac.add_item(test_item)
mackinac.add_npc(mr_w)

kirkhof.add_location("north", mackinac)
kirkhof.add_location("west", henry)
kirkhof.add_item(test_food)
kirkhof.add_item(test_item)

henry.add_location("south", kirkhof)
henry.add_location("north", mackinac)


##################
### World Data ###
##################

world_data = {
    "items": {
        "test_food": test_food,
        "test_item": test_item
    },
    "npcs": {
        "mr_w": mr_w
    },
    "locations": {
        "mackinac": mackinac,
        "kirkhof": kirkhof,
        "henry": henry
    }
}