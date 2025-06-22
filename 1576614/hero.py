# I AM STEVE
key_switch_camera = 'c' #the camera stick to STEVE or stick to NONEXISTENT
key_forward = 'w' #STEVE GOES no
key_left = 'a' #STEVE GOES idk
key_back = 's' #STEVE GOES nah im outta here
key_right = 'd' #STEVE GOES THE CORRECT WAY
key_turn_left = 'q' #STEVE LOOKS LEFT, which he gets hit by a missile
key_turn_right = 'e' #STEVE LOOKS THE RIGHT WAY
key_switch_mode = 'v' #if it can pass a danger thing so SETVE doesente dieded
key_up = 'space' #JUNPEI
key_down = 'b' #DOWN TO THE JUNGLE
key_build = 'z' #SETVE MINES A BUILD
key_destroy = 'x' #SEZVE MINES THE>>>>>MINE\
key_savemap = 'k'
key_loadmap = 'l'

class Player():
    def __init__(self, pos, land):
        self.land = land
        self.mode = True
        self.player = loader.loadModel('smiley') # type: ignore
        self.player.setColor(1,1,1)
        self.player.setScale(0.3)
        self.player.setH(180) #move the palVE 180 SETCVE
        self.player.setPos(pos)
        self.player.reparentTo(render) # type: ignore
        self.cameraBind() #so the cam can stick to STEVE
        self.accept_events() #so steve acceopt his coding demise (JKJKJKJKJKJKJKJKJKJKJK)

    #metosde to connect camera to setve
    def cameraBind(self):
        #no use mouse to use keiys
        base.disableMouse() #disable control cam from moouse
        base.camera.setH(180) #H IS HEADING and it rotate 180 degrees celcius
        base.camera.reparentTo(self.player) #connect cam to SETEV
        base.camera.setPos(0,0,1.5) #(x,y,z) change the cordinate cam
        self.cameraOn = True#ITS VERY TRUE

    #metse to unconnect to sesve
    def cameraUp(self):
        pos = self.player.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2]-3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False # THIS INFORMATION IS HOAX AND FALSE

    #change the cam show
    def changeView(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()

    #metodeh spiiiiiiiiiiiiiiiiiiiiiin camera to lefty
    def turn_left(self):
        self.player.setH((self.player.getH() + 5) % 360)

    #metodeh spiiiiiiiiiiiiiiiiiiiiiin camera to -leftah
    def turn_right(self):
        self.player.setH((self.player.getH() - 5) % 360)

    def look_at(self, angle):
        x_from = round(self.player.getX())
        y_from = round(self.player.getY())
        z_from = round(self.player.getZ())
        dx, dy = self.check_dir(angle)
        x_to = x_from+ dx
        y_to = y_from + dy
        return x_to, y_to, z_from
    
    def just_move(self, angle):
        pos = self.look_at(angle)
        self.player.setPos(pos)

    def move_to(self, angle):
        if self.mode:
            self.just_move(angle)
        else:
            self.try_move(angle)

    def check_dir(self, angle): #WHAT IS TJIS!!!!!!!!!!!!!!!!!!!!!!!!!???????????????
        if angle >= 0 and angle <= 20:
            return(0, -1)
        elif angle <= 65:
            return(1, -1)
        elif angle <= 110:
            return(1, 0)
        elif angle <= 155:
            return(1, 1)
        elif angle <= 200:
            return(0, 1)
        elif angle <= 245:
            return(-1, 1)
        elif angle <= 290:
            return(-1, 0)
        elif angle <= 335:
            return(-1, -1)
        else:
            return(0, -1)
        
    def forward(self):
        angle = (self.player.getH()) % 360
        self.move_to(angle)

    def back(self):
        angle = (self.player.getH() + 180) % 360
        self.move_to(angle)

    def left(self):
        angle = (self.player.getH() + 90) % 360 
        self.move_to(angle)

    def right(self):
        angle = (self.player.getH() + 270) % 360 
        self.move_to(angle)

    def changeMode(self):
        if self.mode:
            self.mode = False
        else:
            self.mode = True

    def up(self):
        if self.mode:
            self.player.setZ(self.player.getZ() + 1)

    def down(self):
        if self.mode and self.player.getZ() > 1:
            self.player.setZ(self.player.getZ() - 1)

    def try_move(self, angle):
        pos = self.look_at(angle)
        if self.land.isEmpty(pos):
            pos = self.land.findHighestEmpty(pos)
            self.player.setPos(pos)
        else:
            pos = pos[0], pos[1], pos[2]+1
            if self.land.isEmpty(pos):
                self.player.setPos(pos)

    def build(self):
        angle = self.player.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.addBlock(pos)
        else:
            self.land.buildBlock(pos)

    def destroy(self):
        angle = self.player.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.delBlock(pos)
        else:
            self.land.delBlockFrom(pos)

    def accept_events(self):
        base.accept(key_turn_left, self.turn_left)
        base.accept(key_turn_left + '-repeat', self.turn_left)
        base.accept(key_turn_right, self.turn_right)
        base.accept(key_turn_right + '-repeat', self.turn_right)

        base.accept(key_forward, self.forward)
        base.accept(key_forward + '-repeat', self.forward)
        base.accept(key_back, self.back)
        base.accept(key_back + '-repeat', self.back)
        base.accept(key_left, self.left)
        base.accept(key_left + '-repeat', self.left)
        base.accept(key_right, self.right)
        base.accept(key_right + '-repeat', self.right)

        base.accept(key_switch_mode, self.changeMode)

        base.accept(key_up, self.up)
        base.accept(key_up + '-repeat', self.up)
        base.accept(key_down, self.down)
        base.accept(key_down + '-repeat', self.down)

        base.accept(key_build, self.build)
        base.accept(key_destroy, self.destroy)

        base.accept(key_switch_camera, self.changeView)

        base.accept(key_savemap, self.land.saveMap)
        base.accept(key_loadmap, self.land.loadMap)