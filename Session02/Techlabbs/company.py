class Talent:
    nextId=1000
    def __init__(self,name):
        self.name = name
        Talent.nextId+=1
        self.id = Talent.nextId
    def get_name(self):
        return self.name
    def get_id(self):
        return self.id


