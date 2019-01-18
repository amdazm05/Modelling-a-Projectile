from visual import *
import math
from math import cos, sin
print "Enter 2 for 2D case and 3 for 3D case"
choice=input("Enter your choice of dimensions=")
###########################################################################################################################################################
#                                               START OF 2D
############################################################################################################################################################
if (choice==2):
        user_number = input ("Enter your Initial Height = ")
        initialHeight = int (user_number)

        user_number = input ("Enter your Initial Velocity = ")
        initialVelocity = int (user_number)

        user_number = input ("Enter Angle in degrees = ")
        Angle = int (user_number)

        #Set up the display window
        scene1 = display (      title="NEW", x=0, y=0, width=700,
                                    height = 600, range=10, background=color.black,
                                    center = (10, initialHeight, 0))

        #Create our objects:
        table = box (pos = (0, initialHeight-1, 0), size= (2,1,4), color=color.white)

        holder = box (pos = (-2, initialHeight/2 + 0.25, 0), size= (1,initialHeight,9), color=color.white)

        ball1 =  sphere (pos = (0, initialHeight, 0), radius= 1,
                            color=color.green, make_trail = true)

        ball2 =  sphere (pos = (0, initialHeight, 0), radius= 1,
                            color=color.red, make_trail = true)

        floor = box (pos = (0,0,0), size= (500,0.25,10), color=color.white)

        t=0
        dt = 0.001
        g = -32 #ft/s-2

        Fgrav = vector (0,g*dt,0)

        #velocity vector for ball
        ball1v = vector (  initialVelocity * cos(Angle*pi/180),
                             initialVelocity * sin(Angle*pi/180),
                              0)

        dummy=1;

        #Motion  
        while True and initialVelocity!=0: 
              rate (300) #speeds it up
              ball1v = ball1v + Fgrav
              ball1.pos += ball1v*dt
              
              ball2.pos = (initialVelocity*cos(Angle*pi/180)*t,
              initialHeight + initialVelocity*t*sin(Angle*pi/180)- 16*t**2)

              if (ball1v.y <= 0) and (dummy==1):
                 dummy=0
                 ball3 =  sphere (pos = ball1.pos, radius= 0.5,
                            color=color.white, make_trail = true)
                 print "\nMax height" , ball3.pos, "time for max height= " ,t
                 max_time_meas=t
            
              elif Angle == 90 and ball1.y <= initialHeight :
                  break
              elif ball1.y <= 0.25 and dummy==0:
                  print "ball1.pos = ", ball1.pos , "t= " ,t
                  print "ball2.pos = ", ball2.pos , "t= " ,t
                  break
              t += dt

#using fromulas 

        print "\nUsing formula to find and verify time (total and max height),range and maxheight\n"
        print "initialHeight = initialVelocity*sin (Angle) * t - g*t*t /2"
        cal_time = (- initialVelocity * sin(Angle*pi/180) - math.sqrt((initialVelocity * sin(Angle*pi/180))**2 - 4 * -16 * initialHeight))/(-2*16)
        print "Time by formula = ", cal_time
        print "Percentage error = ", (cal_time-t)/cal_time*100

        print "\nRange = initialVelocity*cos (Angle) * cal_time "
        cal_range = initialVelocity * cos(Angle*pi/180) * cal_time
        print "Range by formula = ", cal_range
        print "Percentage error = ", (cal_range-ball1.x)/cal_range*100

        print "\nMax height = (initialVelocity*sin (Angle))^2/(2g)\t wrt floor"
        max_height = (initialVelocity * sin(Angle*pi/180))**2 / (2*32) + initialHeight
        print "Max height = ",  max_height
        print "Percentage error = ", (max_height-ball3.y)/max_height*100

        print "\nTime for max height = (2*(max_height - initial_height)/g)^0.5 "
        time_maxheight_cal = math.sqrt(2*(max_height - initialHeight) / 32)
        print "time for max height = ",  time_maxheight_cal

        if Angle !=0:
              print "Percentage error = ", (time_maxheight_cal-max_time_meas)/time_maxheight_cal*100
        else:
              print "Percentage error = 0"

###########################################################################################################################################################
#                                               END OF 2D
#                                               START OF 3D
############################################################################################################################################################
if (choice==3):
        print"---------Initialising 3D projectile--------"
        H=input("Enter Initial height=")
        V=input("Enter Velocity=")
        theta=input("Enter Theta (x-z plane projection angle clockwise angle=")
        phi=input("Enter Phi (angle between y axis and projectile)=")

        scene1=display(title="projectile",x=0,y=0,width=1920,height=1080,
               range=400,background=color.black,
               center=(10,H,0))

        #Enviroment objects
        table1=box(pos=(0,(H-4.5)/2,0),size=(10,H-5,10),color=color.cyan)
        ball1=sphere(pos=(0,H,0),radius=5,color=color.blue,make_trail=true,trail_type="curve")
        ball2=sphere(pos=(0,H,0),radius=5,color=color.yellow,make_trail=true,trail_type="curve")
        floor=box(pos=(0,0,0),size=(1200,0.25,1200),color=color.white)
        table2=box(pos=(0,H-5,0),size=(15,0.5,15),color=color.cyan)


        Xpos_axis=box(pos=(225,0.25,0),size=(900/2,0.25,1),color=color.red)
        Xpos_axis_marker1=box(pos=(400,0.25,30),size=(10,0.25,30),color=color.red)
        Xpos_axis_marker1=box(pos=(400,0.25,30),size=(30,0.25,10),color=color.red)


        Xneg_axis=box(pos=(-225,0.25,0),size=(900/2,0.25,1),color=color.red)
        Xpos_axis_marker1=box(pos=(-400,0.25,30),size=(10,0.25,30),color=color.red)


        zpos_axis=box(pos=(0,0.25,225),size=(1,0.25,900/2),color=color.green)
        zneg_axis_marker1=box(pos=(-30,0.25,-400),size=(10,0.25,30),color=color.green)


        zneg_axis=box(pos=(0,0.25,-225),size=(1,0.25,900/2),color=color.green)
        zpos_axis_marker1=box(pos=(30,0.25,400),size=(30,0.25,10),color=color.green)
        zneg_axis_marker1=box(pos=(30,0.25,400),size=(10,0.25,30),color=color.green)


        #Constant Conditions &  Value of G
        t=0
        dt=0.001
        g=-32.2
        #ft/sec^2



        #Motion for 3D Projectile
        while true and V!=0:
                rate(600)
                fgrav=vector(0,g*t,0)
                ball2v=vector(V*cos(theta*pi/180)*sin(phi*pi/180),V*cos(phi*pi/180),V*sin(phi*pi/180)*sin(theta*pi/180))
                ball2v=ball2v+fgrav
                ball2.pos = ball2.pos+(ball2v*dt)
                # Equivalent to saying ball2.pos+=vector(V*dt*cos(45*pi/180)*sin(45*pi/180),(V*cos(45*pi/180)*dt)+(g*t*dt),V*dt*sin(45*pi/180)*sin(45*pi/180))
        
                ball1.pos=(V*t*cos(theta*pi/180)*sin(phi*pi/180),(H)+(V*cos(phi*pi/180)*t)-(16.1*t*t),V*t*sin(phi*pi/180)*sin(theta*pi/180))
                t+=dt
                if(ball2v.y<=0.1)and(ball2v.y>=0):
                    ballcheck=sphere(pos=ball2.pos,radius=4,color=color.white,make_trail=true)
                if (ball2.y<=0):
                    print "Coordinate of impact"
                    print ball2.x
                    print "0"
                    print ball2.z
                    break
                if (ball2.y<=H-4.5) and (phi==0):
                    print "Coordinate of impact (x,y,z)"
                    print ball2.x
                    print "0"
                    print ball2.z
                    break  
                    break

        #######################################################################################################################################################
        print "Time till impact"
        print t
    
        print "------------End of Program------------"
