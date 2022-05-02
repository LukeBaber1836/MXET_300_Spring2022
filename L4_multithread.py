# This will be a minimal example of demonstrating multithreading for SCUTTLE.

# IMPORT EXTERNAL ITEMS
import time
import threading # only used for threading functionsdddd

# IMPORT INTERNAL ITEMS
import L3_OAM as obsAv
import L1_Luna_Lidar as luna
import L1_servo as servo
import L1_facial_tracking as f_track

# CREATE A THREAD FOR DRIVING
def loop_obs_avoid( ID ):
    obsAv.go()  # command the full program to run

# CREATE A THREAD FOR DISTANCE CONTROL
def loop_face_track( ID ):
    f_track.go() # command the full program to run


# ALL THREADS ARE CALLED TO RUN IN THE MAIN FUNCTION
def main():

        print("starting the main fcn")
        threads = []  # create an object for threads
        
        t1 = threading.Thread( target=loop_face_track, args=(1,) ) # make 1st thread object
        threads.append(t1) # add this function to the thread object
        t1.start() # start executing
        print("started thread1, for obstacle avoidance")

        t2 = threading.Thread( target=loop_obs_avoid, args=(2,) ) # make 2nd thread object
        threads.append(t2) # add this function to the thread object
        t2.start() # start executing
        print("started thread2, for gimbal")
        

        # the join commands manipulate the way the program concludes multithreading.
        t1.join()
        t2.join()

# EXECUTE THE MAIN FUNCTION
main()