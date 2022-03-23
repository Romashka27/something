from copy import deepcopy

class Config:
    def __init__(self, loader):
        self.loader = self.cop(loader)

    def cop(self ,loader):
        return deepcopy(loader)

    def refresh(self, new_d):
        self.loader = self.cop(new_d)



