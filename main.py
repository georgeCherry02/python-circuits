from circuits.examples import or_gate
from circuits.new_wire import Wire
from circuits.connection_point import ConnectionPoint
from circuits.source import Source

import pygame
from pygame.locals import K_SPACE, K_m, K_w, KEYDOWN

pygame.init()

screen = pygame.display.set_mode([500, 500])

i1 = Source()
i2 = Source()

# drawables = or_gate(i1.high, i2.high)

def get_render_coords(x: int, y: int) -> pygame.Vector2:
    return pygame.Vector2(x + 250, y + 250)

i1_cp = ConnectionPoint(get_render_coords(-20, 0), i1.high)
i2_cp = ConnectionPoint(get_render_coords(0, 20), i2.high)

wire = Wire(i1_cp, "test_wire")
wire.add_stretch(get_render_coords(0, 0))
wire.add_stretch(get_render_coords(10, 0))
wire.add_stretch(get_render_coords(5, 30))
wire.add_connection(i2_cp)

drawables = [wire]

# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_w:
                running = False
            if event.key == K_SPACE:
                i1.inverse()
            if event.key == K_m:
                i2.inverse()

    # Fill the background with white
    screen.fill((140, 140, 140))

    # Draw components
    for drawable in drawables:
        drawable.draw(screen)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
