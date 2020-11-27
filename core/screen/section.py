class Section(): # Type de sauvegarde de donné pour structuré le menu

    def __init__(self,text,action,description="",color=(100,100,100),hold_color=(200,200,200)):
        self.text = text
        self.action = action
        self.color = color
        self.description = description
        self.hold_color = hold_color
        self.parent = None