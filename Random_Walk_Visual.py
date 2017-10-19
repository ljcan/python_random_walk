import matplotlib.pyplot as plt
from Random_Walk import Random_Walk
while True:
  RW=Random_Walk()
  RW.walk()
  #使颜色渐变
  point_number=list(range(RW.number_point))
  plt.scatter(RW.x_values,RW.y_values,c=point_number,cmap=plt.cm.Blues,edgecolors='None',s=15)
  plt.show()
  keep_running=raw_input('Make another walk?(Y/N):')
  if keep_running=='N':
      break
