import pygame


class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):  # inicializace + zpřístupnění
        self.game = game
        self.type = e_type
        self.pos = list(pos)  # aby každa spawnutá entita měla vlastní list pro pozice
        self.size = size
        self.velocity = [0, 0]  # velocity je o kolik se změnila poloha např. na ose x každý frame
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}  # definice jakým směrem padám

        self.action = ''
        self.anim_offset = (-3, -3)  # "rezervuji" si 3 pixely na každou stranu pro např. animaci běhu, kdee panáček má nohy před sebou/za sebou
        self.flip = False                   # mám animace jen na 1 stranu, případně se zrcadlí "True"
        self.set_action('idle')      # nese informaci, která animace zrovna běží

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])  # udělá obdelník se kterým můžeme mít kolizi kolize = obdelník narazí na obdelník

    def set_action(self, action):          # když se nová animace nerovná animaci právě běžící, tak ji přepíše a bude se provádět nová
        if action != self.action:
            self.action = action
            self.animation = self.game.assets[self.type + '/' + self.action].copy()

    def update(self, tilemap, movement=(0, 0)):
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}

        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])  # o kolik se mi to actually posune sčítam např gravitaci(padá dolů) (velocity) + movement šipkama (doprava doleva)

        self.pos[0] += frame_movement[0]  # update pozice na ose X
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0:  # pokud se pohybuju doprava
                    entity_rect.right = rect.left  # pravý obdelnik postavy narazí do  levého boku překážky
                    self.collisions['right'] = True
                if frame_movement[0] < 0:
                    entity_rect.left = rect.right
                    self.collisions['left'] = True
                self.pos[0] = entity_rect.x

        self.pos[1] += frame_movement[1]  # update pozice na ose Y
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

        if movement[0] > 0:             # určuje jestli jdeme doleva, či doprava a podle toho flipuje animaci
            self.flip = False
        if movement[0] < 0:
            self.flip = True

        self.velocity[1] = min(5, self.velocity[1] + 0.1)  # max rychlost padání je 5, pokud je rychlost padání menší než 5, tak každý frame zrychlí o 0.1

        if self.collisions['down'] or self.collisions['up']:  # když se pohybuji po ose X chci velocity po ose Y 0
            self.velocity[1] = 0

        self.animation.update()

    def render(self, surf, offset=(0, 0)):
        surf.blit(pygame.transform.flip(self.animation.img(), self.flip, False), (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1]))
        #                              bere zrovna probíhajíc animaci, flipuje nám animaci dle pohybu

class Player(PhysicsEntity):
    def __init__(self, game, pos, size):
        super().__init__(game, 'player', pos, size)    #super().init bere init z před
        self.air_time = 0

    def update(self, tilemap, movement=(0, 0)):
        super().update(tilemap, movement=movement)

        self.air_time += 1
        if self.collisions['down']:
            self.air_time = 0

        if self.air_time > 4:  # když je ninja ve vzduchu déle než 4 framy udělá se animace skoku
            self.set_action('jump')
        elif movement[0] != 0:          # když movement není 0 (tj. hábe se po ose X) provádí se animace běhu
            self.set_action('run')
        else:
            self.set_action('idle')










