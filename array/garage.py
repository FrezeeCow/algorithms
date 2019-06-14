"""
There is a parking lot with only one empty spot. Given the initial state of the parking lot and the final state. 
Each step we are only allowed to move a car out of its place and move it into the empty spot.
The goal is to find out the least movement needed to rearrange the parking lot from the initial state to the final state.
"""

"""
有一个只有一个空位的停车场。 鉴于停车场的初始状态和最终状态。 每一步我们只允许将汽车移出其位置并将其移动到空位。目标是找出将停车场
从初始状态重新排列到最终状态所需的最少运动。
"""

# Say the initial state is an array:

# input initial: [1,2,3,0,4]  # where 1,2,3,4 are different cars, and 0 is the empty spot.
# input final: [0, 3, 2, 1, 4]

# output: 4


# We can swap 1 with 0 in the initial array to get [0,2,3,1,4] and so on.
# Each step swap with 0 only.

# 1 2 3 0 4 --> 0 3 2 1 4
# step1: 1 2 3 0 4 --> 0 2 3 1 4 
# step2：0 2 3 1 4 --> 3 2 0 1 4
# step3: 3 2 0 1 4 --> 3 0 2 1 4
# step4: 3 0 2 1 4 --> 0 3 2 1 4



def garage(initial, final):
    steps = 0
    while initial != final:
        zero = initial.index(0)
        if zero != final.index(0):
            car_to_move = final[zero]
            pos = initial.index(car_to_move)
            initial[zero], initial[pos] = initial[pos], initial[zero]
        else:
            for i in range(len(initial)):
                if initial[i] != final[i]:
                    initial[zero], initial[i] = initial[i], initial[zero]
                    break
        steps += 1
    return steps

if __name__ == "__main__":
    initial = [1, 2, 3, 0, 4]
    final = [0, 3, 2, 1, 4]
    print("initial:", initial)
    print("final:", final)
    print(garage(initial, final))
