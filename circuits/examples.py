from .connection_point import ConnectionPoint
from .not_gate import NotGate
from .source import Source
from .transistor import Transistor, TRANSISTOR_SIZE
from .wire import Wire

from pygame import Vector2

source = Source()
signal = Source()


def get_render_coords(x: int, y: int) -> Vector2:
    return Vector2(x + 250, y + 250)


def get_dead_connection(x: int, y: int) -> ConnectionPoint:
    return ConnectionPoint(get_render_coords(x, y), lambda: False)


def simple_example():
    source_start = ConnectionPoint(get_render_coords(-20, 0), source.high)
    source_end = get_dead_connection(-TRANSISTOR_SIZE, 0)
    source_wire = Wire(source_start, source_end)

    signal_start = ConnectionPoint(get_render_coords(0, 20), signal.high)
    signal_end = get_dead_connection(0, TRANSISTOR_SIZE)
    signal_wire = Wire(signal_start, signal_end)

    transistor = Transistor(source_end, signal_end)

    output_end = get_dead_connection(20, 0)
    output_wire = Wire(transistor.output, output_end)
    return (source_wire, signal_wire, output_wire, transistor)


def not_gate():
    source_start = ConnectionPoint(get_render_coords(-20, 0), source.high)
    source_end = get_dead_connection(-5, 0)
    source_wire = Wire(source_start, source_end)

    not_gate = NotGate(source_end)

    ground = get_dead_connection(20, 0)
    output_wire = Wire(not_gate.output, ground)
    return [source_wire, output_wire, not_gate]


def not_gate_if_resistance_was_a_thing():
    input = ConnectionPoint(get_render_coords(0, 20), source.high)
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

    return [
        input_wire,
        left_input_wire,
        right_input_wire,
        battery_to_transistor,
        inter_transistor_connection,
        transistor_to_ground,
        left_transistor,
        right_transistor,
        input_to_left_transistor,
        input_to_right_transistor,
    ]


def or_gate():
    i1_start = ConnectionPoint(get_render_coords(-10, 20), source.high)
    i1_end = get_dead_connection(-10, TRANSISTOR_SIZE)
    i1_wire = Wire(i1_start, i1_end, "i1")

    i2_start = ConnectionPoint(get_render_coords(10, 20), signal.high)
    i2_end = get_dead_connection(10, TRANSISTOR_SIZE)
    i2_wire = Wire(i2_start, i2_end, "i2")

    t1_battery = ConnectionPoint(
        get_render_coords(-10 - TRANSISTOR_SIZE, 0), lambda: True
    )
    t2_battery = ConnectionPoint(
        get_render_coords(10 - TRANSISTOR_SIZE, 0), lambda: True
    )

    t1 = Transistor(t1_battery, i1_wire.end)
    t2 = Transistor(t2_battery, i2_wire.end)

    t1_out = Wire(t1.output, get_dead_connection(0, 0), "t1")
    t1_out1 = t1_out.extend(get_dead_connection(0, -20))
    t2_out = Wire(t2.output, get_dead_connection(20, 0), "t2")
    t2_out1 = t2_out.extend(get_dead_connection(20, -10))
    t1_t2_meet = t1_out1.connect_wire(t2_out1, "End")

    # output_end = get_dead_connection(20, 0)
    # output_wire = Wire(transistor.output, output_end)
    return (i1_wire, i2_wire, t1, t2, t1_out, t1_out1, t2_out, t2_out1, t1_t2_meet)
