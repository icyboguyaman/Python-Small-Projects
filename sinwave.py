import matplotlib.pyplot as mlt
import numpy as np
x = np.arange(1, 10, 0.1)
y = np.sin(x)
mlt.plot(x, y, '--')
mlt.show()
