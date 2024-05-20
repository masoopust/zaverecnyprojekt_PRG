import pygame

class PhysicsEntity:
    def __init__(self, platformer, e_type, pos, size):    #inicializace + zpřístupnění
        self.platformer = platformer
        self.type = e_type
        self.pos = list(pos)                            #aby každa spawnutá entita měla vlastní list pro pozice
        self.size = size
        self.velocity = [0,0]           # velocity je o kolik se změnila poloha např. na ose x každý frame



    def update(self, movement = (0,0)):
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])       # o kolik se mi to actually posune sčítam např gravitaci(padá dolů) (velocity) + movement šipkama (doprava doleva)

        self.pos[0] += frame_movement[0]     #update pozice na ose X
        self.pos[1] += frame_movement[1]     #update pozice na ose Y

    def render(self, surf):
        surf.blit(self.platformer.assets["player"], self.pos)











