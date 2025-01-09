import random 
import matplotlib.pyplot as plt
import pandas as pd



def display_coordinates(coordinates):
    walkers = len(coordinates)
    dims = len(coordinates[0])
    steps = len(coordinates[0][0])

    for walker in range(walkers):
        match dims:
            case 1: 
                plt.plot([step for step in range(steps)], coordinates[walker][0])
            case 2:
                plt.plot(coordinates[walker][0], coordinates[walker][1])
            case 3:
                if walker == 0:
                    ax = plt.axes(projection ='3d')
                ax.plot(coordinates[walker][0], coordinates[walker][1], coordinates[walker][2])
            case _:
                data = {f" dim {i+1}": coordinates[walker][i] for i in range(dims)}
                data_frame = pd.DataFrame(data, index=[i for i in range(steps)])
                print()
                print(f'<- walker {walker+1} table steps ->')
                print('step', end="")
                print(data_frame)
                
    if dims < 4:
        plt.show() 


def make_random_steps(coordinates, walker):
    dims = len(coordinates[0])
    steps = len(coordinates[0][0])

    for step in range(1, steps):
        for dim in range(dims): # initial all dims state for current step
            coordinates[walker][dim][step] = coordinates[walker][dim][step-1]
        rnd_dim = random.randint(0, dims-1)
        rnd_move = random.choice([-1, 1])

        coordinates[walker][rnd_dim][step] += rnd_move
        

def random_walk(walkers, dims, steps):
    coordinates = [[[0] * (steps+1) for _ in range(dims)] for _ in range(walkers)]

    for walker in range(walkers):
        make_random_steps(coordinates, walker)
    
    display_coordinates(coordinates)


if __name__ == '__main__':
    walkers = int(input("Please enter number of walkers: "))
    assert walkers > 0, "Number of walkers must be positive."

    dims = int(input("Please enter number of dims: "))
    assert dims > 0, "Number of dims must be positive."

    steps = int(input("Please enter number of steps: "))
    assert steps > 0, "Number of steps must be positive."

    random_walk(walkers, dims, steps)
    
   
    
