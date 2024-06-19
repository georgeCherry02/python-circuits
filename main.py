from circuits.wire import Wire
from circuits.transistor import Transistor, TRANSISTOR_SIZE
from circuits.connection_point import ConnectionPoint

import pygame
from pygame import Vector2
from pygame.locals import K_SPACE, K_m, K_w, KEYDOWN

pygame.init()

screen = pygame.display.set_mode([500, 500])

source_state = False
signal_state = False


def source_func() -> bool:
    global source_state
    return source_state


def signal_func() -> bool:
    global signal_state
    return signal_state


def get_render_coords(x: int, y: int) -> Vector2:
    return Vector2(x + 250, y + 250)

def simple_example():
    source = ConnectionPoint(get_render_coords(-20, 0), source_func)
    source_end = ConnectionPoint(get_render_coords(-TRANSISTOR_SIZE, 0), lambda: False)
    source_wire = Wire(source, source_end)

    signal = ConnectionPoint(get_render_coords(0, 20), signal_func)
    signal_end = ConnectionPoint(get_render_coords(0, TRANSISTOR_SIZE), lambda: False)
    signal_wire = Wire(signal, signal_end)

    transistor = Transistor(source_end, signal_end)

    output_end = ConnectionPoint(get_render_coords(20, 0), lambda: False)
    output_wire = Wire(transistor.output, output_end)
    return (source_wire, signal_wire, output_wire, transistor)



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
                source_state = not source_state
            if event.key == K_m:
                signal_state = not signal_state

    # Fill the background with white
    screen.fill((140, 140, 140))

    # Draw components
    components = simple_example()
    for component in components:
        component.draw(screen)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
