from prob_dist import *
import pandas as pd

#rooms in house 1
PANTRY = 'pantry'
KITCHEN = 'kitchen'
SCHOOL_ROOM = 'school room'
DEN = 'den'
OFFICE_HALL = 'office hall'
OFFICE = 'office'
HALL = 'hall'
HALL_BATHROOM = 'hall bathroom'
BOY_BEDROOM = 'boy bedroom'
GIRL_BEDROOM = 'girl bedroom'
MASTER_BEDROOM = 'master bedroom'
MASTER_BATHROOM = 'master bathroom'



#Do it a couple of different ways.
#1 a bunch of probability distributions, specifying the probability of each room given where you are now
#1 a matrix of transition probabilities


#way 1
kitchen_probs = ProbDist({SCHOOL_ROOM: 1, PANTRY: 3, DEN: 6}, id=KITCHEN)
pantry_probs = ProbDist({KITCHEN: 1}, id=PANTRY)
school_room_probs = ProbDist({KITCHEN: 2, OFFICE: 1}, id=SCHOOL_ROOM)
office_probs = ProbDist({SCHOOL_ROOM: 2, OFFICE_HALL: 3}, id=OFFICE)
office_hall_probs = ProbDist({OFFICE: 1, DEN: 1}, id=OFFICE_HALL)
den_probs = ProbDist({KITCHEN: 4, OFFICE_HALL: 2, HALL: 4}, id=DEN)
hall_probs = ProbDist({MASTER_BEDROOM: 5, DEN: 5}, id=HALL)
master_bedroom_probs = ProbDist({HALL: 6, MASTER_BATHROOM: 4}, id=MASTER_BEDROOM)
master_batrhoom_probs = ProbDist({MASTER_BEDROOM: 1}, id=MASTER_BATHROOM)

dist_map = {
    KITCHEN: kitchen_probs,
    PANTRY: pantry_probs,
    SCHOOL_ROOM: school_room_probs,
    OFFICE: office_probs,
    OFFICE_HALL: office_hall_probs,
    DEN: den_probs,
    HALL: hall_probs,
    MASTER_BEDROOM: master_bedroom_probs,
    MASTER_BATHROOM: master_batrhoom_probs
}

def do_rooms_transitions():
    #start in kitchen, get next room
    current_room = KITCHEN
    num_transitions = 1000000
    chain = [current_room]
    for i in range(num_transitions):
        current_room = dist_map[current_room].get_random_value()[0]
        #print(current_room)
        chain.append(current_room)

    return chain


chain = do_rooms_transitions()
print(pd.Series(chain).value_counts())