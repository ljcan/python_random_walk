import matplotlib.pyplot as plt
from Random_Walk import Random_Walk
while True:
  RW=Random_Walk()
  RW.walk()
  point_number=list(range(RW.number_point))
  #the parameter of 's' is set size of point
  plt.scatter(RW.x_values,RW.y_values,c=point_number,cmap=plt.cm.Blues,edgecolors='None',s=15)
  # the symbol of begin point and last point
  plt.scatter(0, 0, c='red', edgecolors='None', s=100)
  plt.scatter(RW.x_values[-1], RW.y_values[-1], c='red', edgecolors='None', s=100)
  #hidden x,y Coordinate axis
  plt.axes().get_xaxis().set_visible(False)
  plt.axes().get_yaxis().set_visible(False)
  plt.show()
  keep_running=raw_input('Make another walk?(Y/N):')
  if keep_running=='N':
      break
