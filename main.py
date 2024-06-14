from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3


class MyApp(ShowBase):

    def __init__(self):
            ShowBase.__init__(self)

            # Loading the environment model.
            self.scene = self.loader.loadModel("models/environment")
            # Reparent the model to render.
            self.scene.reparentTo(self.render)
            # Apply scale and position transforms on the model.
            self.scene.setScale(0.25, 0.25, 0.25)
            self.scene.setPos(-8, 42, 0)

            #Add the spinCameraTask procedure to the task manager
            self.tasskMgr.add(self.spinCameraTask, "SpinCameraTask")

            #Load and transform the panda actor...
            self.pandaActor = Actor("models/panda-model",
                                    {"walk": "models/panda-walk4"})
            self.pandaActor.setScale(0.005, 0.005, 0.005)
            self.pandaActor.reparentTo(self.render)
            #Loop animation.
            self.pandaActor.loop("walk")

            # Create the four lerp intervals needed for the panda to walk back and forth...
            posInterval1 = self.pandaActor.posInterval(13,
                                                   Point3(0, -10, 0),
                                                   startPos=Point3(0, 10, 0))
            posInterval2 = self.pandaActor.posInterval(13,
                                                   Point3(0, 10, 0),
                                                   startPos=Point3(0, -10, 0))
            hprInterval1 = self.pandaActor.hprInterval(3,
                                                   Point3(180, 0, 0),
                                                   startHpr=Point3(0, 0, 0))
            hprInterval2 = self.pandaActor.hprInterval(3,
                                                   Point3(0, 0, 0),
                                                   startHpr=Point3(180, 0, 0))
            
            #Create and run the sequence that coordinates the intervals...
            self.pandaPace = Sequence(posInterval1, hprInterval1,
                                      posInterval2, hprInterval2,
                                      name="pandaPace")
            self.pandaPace.loop()

        
    #Define a procedure to move camera...
    def spinCameraTask(self, task):
          #task.time measured in seconds... multiplying by 6 converts seconds to a spectrum of elapsed degrees.
          angleDegrees = task.time * 6.0

          #basic precalculus operation to convert degrees to radians; necessary for trig functions
          angleRadians = angleDegrees * (pi / 180.0)

          #camera position in 3d space; sin(theta) for x-coordinate, cos(theta) for y-coordinate, constant 3 for z-coordinate
          #"20" was the coefficient chosen by the Panda3D tutorial...
          self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
          self.camera.setHpr(angleDegrees, 0, 0)
          return Task.cont
    
    
app = MyApp()
app.run()
