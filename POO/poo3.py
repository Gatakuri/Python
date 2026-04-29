class camera:
    def __init__(self, name, filming=False):
        self.name = name
        self.filming = filming

    def film(self):
        if self.filming:
            print(f'{self.name} is already filming...')
            return
        
        print(f'{self.name} filming...')
        self.filming = True

    def stop_filming(self):
        if not self.filming:
            print(f'{self.name} isn\'t filming yet...')
            return
        
        print(f'{self.name} stopping filming...')
        self.filming = False

    def photograph(self):
        if self.filming:
            print(f'{self.name} can\'t take photo while filming.')
            return
        
        print(f'{self.name} photographed...')

cam1 = camera(name="WebCam")
cam1.film()
cam1.film()
cam1.photograph()
cam1.stop_filming()
cam1.stop_filming()
cam1.photograph()
print(cam1.filming)