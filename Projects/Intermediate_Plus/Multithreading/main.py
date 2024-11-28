import threading
import time

def activity_1(activity_name):
    time.sleep(8)
    print(f"Finished Activity 1 ; {activity_name}")

def activity_2():
    time.sleep(2)
    print("Finished Activity 2")

def activity_3(param_1, param_2):
    time.sleep(10)
    print(f"Finished Activity 3 : {param_1} {param_2}")

def activity_4():
    time.sleep(5)
    print("Finished Activity 4")    

activity1 = threading.Thread(target=activity_1, args=("First_activity",))
activity1.start()

activity2 = threading.Thread(target=activity_2)
activity2.start()

activity3 = threading.Thread(target=activity_3, args=("First_Parameter", "Second_Parameter"))
activity3.start()

activity4 = threading.Thread(target=activity_4)
activity4.start()

# Wait for async tasks to complete
activity1.join()
activity2.join()
activity3.join()
activity4.join()

print("All tasks complete!")