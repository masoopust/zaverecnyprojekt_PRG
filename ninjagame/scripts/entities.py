import pygame

class PhysicsEntity:
    def __init__(self, platformer, e_type, pos, size):    #inicializace + zpřístupnění
        self.platformer = platformer
        self.type = e_type
        self.pos = list(pos)                            #aby každa spawnutá entita měla vlastní list pro pozice
        self.size = size
        self.velocity = [0, 0]           # velocity je o kolik se změnila poloha např. na ose x každý frame
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}  # definice jakým směrem padám


    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])    # udělá obdelník se kterým můžeme mít kolizi kolize = obdelník narazí na obdelník


    def update(self, tilemap, movement = (0, 0)):
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}

        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])       # o kolik se mi to actually posune sčítam např gravitaci(padá dolů) (velocity) + movement šipkama (doprava doleva)

        self.pos[0] += frame_movement[0]     #update pozice na ose X

        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0:               # pokud se pohybuju doprava
                    entity_rect.right = rect.left       # pravý obdelnik postavy narazí do  levého boku překážky
                    self.collisions['right'] = True
                if frame_movement[0] < 0:
                    entity_rect.left = rect.right
                    self.collisions['left'] = True
                self.pos[0] = entity_rect.x

        self.pos[1] += frame_movement[1]     #update pozice na ose Y
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[1] > 0:
                    entity_rect.bottom = rect.top
                    self.collisions['down'] = True
                if frame_movement[1] < 0:
                    entity_rect.top = rect.bottom
                    self.collisions['up'] = True
                self.pos[1] = entity_rect.y

        self.velocity[1] = min(5, self.velocity[1] + 0.1)  # max rychlost padání je 5, pokud je rychlost padání menší než 5, tak každý frame zrychlí o 0.1

        if self.collisions['down'] or self.collisions['up']:                        # když se pohybuji po ose X chci velocity po ose Y 0
            self.velocity[1] = 0

    def render(self, surf):
        surf.blit(self.platformer.assets["player"], self.pos)











