import numpy as np
import matplotlib.pyplot as plt

stud_marks = np.array([69,60,50])
work_hours = np.array([9,6,5])

plt.bar(work_hours, stud_marks)
plt.show()