from random import choice
class Random_Walk:
    def __init__(self,number_point=5000):
        self.number_point=number_point
        self.x_values=[0]
        self.y_values=[0]
    def walk(self):
        while len(self.x_values)<self.number_point:
           # choice the direction of left or right:'1' express right#
           x_direction=choice([1,-1])
           x_distance=choice([1,2,3,4])
           x_step=x_direction*x_distance

           y_direction=choice([1,-1])
           y_distance=choice([1,2,3,4])
           y_step=y_direction*y_distance
           # if stay put into next circulation
           if x_step==0 and y_step==0:
               continue
           # calculate next point if x and y
           # the next of x by the last of x_values plus x_step,the same as y
           next_x=self.x_values[-1]+x_step
           next_y=self.y_values[-1]+y_step

           self.x_values.append(next_x)
           self.y_values.append(next_y)
