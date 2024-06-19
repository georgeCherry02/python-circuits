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

def get_dead_connection(x: int, y: int) -> ConnectionPoint:
    return ConnectionPoint(get_render_coords(x, y), lambda: False)


def simple_example():
    source = ConnectionPoint(get_render_coords(-20, 0), source_func)
    source_end = get_dead_connection(-TRANSISTOR_SIZE, 0)
    source_wire = Wire(source, source_end)

    signal = ConnectionPoint(get_render_coords(0, 20), signal_func)
    signal_end = get_dead_connection(0, TRANSISTOR_SIZE)
    signal_wire = Wire(signal, signal_end)

    transistor = Transistor(source_end, signal_end)

    output_end = get_dead_connection(20, 0)
    output_wire = Wire(transistor.output, output_end)
    return (source_wire, signal_wire, output_wire, transistor)

def not_gate():
    input = ConnectionPoint(get_render_coords(0, 20), source_func)
    input_mid = get_dead_connection(0, 10)

    input_wire = Wire(input, input_mid)
    left_input_end = get_dead_connection(-10, 10)
    right_input_end = get_dead_connection(10, 10)
    left_input_wire = input_wire.extend(left_input_end)
    right_input_wire = input_wire.extend(right_input_end)

    battery = ConnectionPoint(get_render_coords(-20, 0), lambda: True)
    ground = ConnectionPoint(get_render_coords(20, 0), lambda: False)

    left_transistor_input = get_dead_connection(-17, 0)
    left_transistor_signal = get_dead_connection(-10, 7)
    left_transistor = Transistor(left_transistor_input, left_transistor_signal)

    right_transistor_input = get_dead_connection(3, 0)
    right_transistor_signal = get_dead_connection(10, 7)
    right_transistor = Transistor(right_transistor_input, right_transistor_signal)

    input_to_left_transistor = left_input_wire.extend(left_transistor_signal)
    input_to_right_transistor = right_input_wire.extend(right_transistor_signal)
    battery_to_transistor = Wire(battery, left_transistor_input)
    inter_transistor_connection = Wire(left_transistor.output, right_transistor_input)
    transistor_to_ground = Wire(right_transistor.output, ground)
    

    return [input_wire, left_input_wire, right_input_wire, battery_to_transistor, inter_transistor_connection, transistor_to_ground, left_transistor, right_transistor, input_to_left_transistor, input_to_right_transistor]


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
    components = not_gate()
    for component in components:
        component.draw(screen)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
