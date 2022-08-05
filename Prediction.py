from codrone_edu.drone import *
import time
drone = Drone()
drone.pair()
drone.load_classifier("color_data")
for i in range(500):
    color_data = drone.get_color_data()
    color = drone.predict_colors(color_data)
    print(color)
    time.sleep(0.5)
drone.close()