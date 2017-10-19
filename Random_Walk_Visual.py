import matplotlib.pyplot as plt
from Random_Walk import Random_Walk
while True:
  RW=Random_Walk()
  RW.walk()
  plt.scatter(RW.x_values,RW.y_values)
  plt.show()
  keep_running=raw_input('Make another walk?(Y/N):')
  if keep_running=='N':
      break
