from item import Item
from npc import NPC
from location import Location

#############
### Items ###
#############

pizza = Item("Pizza",
             "A large slice of pepperoni pizza from Kirkhof.",
             220, 12)

burger = Item("Burger",
              "A leftover burger from the dining hall.",
              240, 14)

shake = Item("Shake",
                     "A thick protein shake from the Fieldhouse.",
                     180, 10)

donuts = Item("Donuts",
                 "A box of donuts left after a club meeting.",
                 260, 16)

snack = Item("Snack",
                 "A large bag of trail mix.",
                 140, 8)

textbook = Item("Textbook",
                "A heavy cybersecurity textbook filled with networking concepts.",
                0, 12)

laptop = Item("Laptop",
              "A powerful gaming laptop running far too many tabs.",
              0, 8)

id = Item("ID",
                  "A student identification card.",
                  0, 1)

ticket = Item("Ticket",
                      "An expensive reminder to follow parking rules.",
                      0, 1)

keyboard = Item("Keyboard",
                       "Several keys are missing.",
                       0, 5)

############
### NPCs ###
############

mr_w = NPC("Mr. W", ("Mr. W is a professor at GVSU, he is very "
            "involved in computer science."))
mr_w.add_message("Hi there! If you need any coding help just ask!")
troy = NPC("Troy", ("Troy is a cybersecurity student who seems "
            "determined to save the campus from the troll's spell."))
troy.add_message("I found some food here earlier. The elf might want it.")
troy.add_message("The Little Mac Bridge leads toward the ravines.")

william = NPC("William", ("William is a computer science student "
               "who appears oddly calm despite the frozen campus."))
william.add_message("The elf will only save campus if it gets enough calories.")
william.add_message("Be careful not to give it anything inedible.")

tyler = NPC("Tyler", ("Tyler is a computer science student studying in the library. "
             "He looks like he was interrupted in the middle of finals week."))
tyler.add_message("I saw some snacks around campus before everything froze.")
tyler.add_message("The bridge leads to the ravines where the elf lives.")

coach = NPC("Coach", ("The Fieldhouse coach watches over the athletic "
             "facilities and encourages students to stay active."))
coach.add_message("Athletes always keep snacks nearby.")
coach.add_message("You might find something useful around the Fieldhouse.")

elf = NPC("Elf", ("A magical elf who lives in the ravines beneath "
           "the Little Mac Bridge."))
elf.add_message("Bring me food and I may save your campus.")
elf.add_message("I need at least 500 calories before I can break the spell.")
elf.add_message("Do not try to feed me junk!")

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
library = Location("Mary Idema Pew Library", ("The Mary Idema Pew "
            "Library serves as GVSU's main library. Students come here "
            "to study, research, and work on assignments."))
padnos = Location("Padnos Hall of Science", ("Padnos Hall houses "
            "many of GVSU's science programs. Laboratories and classrooms "
            "for biology, chemistry, and related fields are located here."))
fieldhouse = Location("Fieldhouse", ("The Fieldhouse is one of "
            "GVSU's athletic facilities. It hosts sporting events, "
            "recreation activities, and fitness opportunities."))
bridge = Location("Little Mac Bridge", ("The Little Mac Bridge is "
            "one of GVSU's most recognizable landmarks. It spans the "
            "ravines of the Allendale campus and connects different areas "
            "of the university. Students cross it every day on their way "
            "to classes."))
forest = Location("Campus Ravines", ("Below the Little Mac Bridge lies "
            "a wooded area of trails and ravines. The forest is quiet and "
            "shaded, making it feel separated from the busy campus above."))

mackinac.add_location("north", henry)
mackinac.add_location("south", kirkhof)
mackinac.add_location("east", library)
mackinac.add_item(textbook)
mackinac.add_npc(mr_w)

kirkhof.add_location("north", mackinac)
kirkhof.add_location("west", fieldhouse)
kirkhof.add_location("south", bridge)
kirkhof.add_item(pizza)
kirkhof.add_item(ticket)
kirkhof.add_npc(troy)

henry.add_location("south", mackinac)
henry.add_npc(william)
henry.add_item(id)

library.add_location("west", mackinac)
library.add_location("south", padnos)
library.add_npc(tyler)
library.add_item(laptop)
library.add_item(donuts)

padnos.add_location("north", library)
padnos.add_location("west", bridge)
padnos.add_item(keyboard)
padnos.add_item(burger)

fieldhouse.add_location("east", kirkhof)
fieldhouse.add_location("south", bridge)
fieldhouse.add_npc(coach)
fieldhouse.add_item(shake)
fieldhouse.add_item(snack)

bridge.add_location("north", kirkhof)
bridge.add_location("east", padnos)
bridge.add_location("west", fieldhouse)
bridge.add_location("south", forest)

forest.add_location("north", bridge)
forest.add_npc(elf)

##################
### World Data ###
##################

world_data = {
    "items": {
        "textbook": textbook,
        "pizza": pizza,
        "ticket": ticket,
        "id": id,
        "laptop": laptop,
        "donuts": donuts,
        "keyboard": keyboard,
        "burger": burger,
        "shake": shake,
        "snack": snack,
    },
    "npcs": {
        "mr w": mr_w,
        "troy": troy,
        "william": william,
        "tyler": tyler,
        "coach": coach,
        "elf": elf
    },
    "locations": {
        "mackinac": mackinac,
        "kirkhof": kirkhof,
        "henry": henry,
        "library": library,
        "padnos": padnos,
        "fieldhouse": fieldhouse,
        "bridge": bridge,
        "forest": forest
    }
}