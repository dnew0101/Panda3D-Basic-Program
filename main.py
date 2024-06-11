from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task

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
