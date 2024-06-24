from circuits.wire import Wire
from circuits.not_gate import NotGate
from circuits.source import Source
from circuits.transistor import Transistor, TRANSISTOR_SIZE

from pygame import Vector2


def get_render_coords(x: int, y: int) -> Vector2:
    return Vector2(x + 250, y + 250)


def get_dead_connection(x: int, y: int) -> Wire.ConnectionPoint:
    return Wire.ConnectionPoint(get_render_coords(x, y), lambda: False)


def simple_example(source: Source, signal: Source):
    source_start = Wire.ConnectionPoint(get_render_coords(-20, 0), source.high)
    source_end = get_dead_connection(-TRANSISTOR_SIZE, 0)
    source_wire = Wire("source", source_start)
    source_wire.add_connection(source_end)

    signal_start = Wire.ConnectionPoint(get_render_coords(0, 20), signal.high)
    signal_end = get_dead_connection(0, TRANSISTOR_SIZE)
    signal_wire = Wire("signal", signal_start)
    signal_wire.add_connection(signal_end)

    transistor = Transistor(source_end, signal_end)

    output_end = get_dead_connection(20, 0)
    output_wire = Wire("output", transistor.output)
    output_wire.add_connection(output_end)

    return (source_wire, signal_wire, output_wire, transistor)


def not_gate(source: Source):
    source_start = Wire.ConnectionPoint(get_render_coords(-20, 0), source.high)
    source_end = get_dead_connection(-5, 0)
    source_wire = Wire("source", source_start)
    source_wire.add_connection(source_end)

    not_gate = NotGate(source_end)

    ground = get_dead_connection(20, 0)
    output_wire = Wire("output", not_gate.output)
    output_wire.add_connection(ground)

    return [source_wire, output_wire, not_gate]


def complex_wiring_example(i1: Source, i2: Source):
    i1_cp = Wire.ConnectionPoint(get_render_coords(-20, 0), i1.high)
    i2_cp = Wire.ConnectionPoint(get_render_coords(0, 20), i2.high)

    wire = Wire("test_wire", i1_cp)
    wire.add_stretch(get_render_coords(0, 0))
    wire.add_stretch(get_render_coords(10, 0))
    wire.add_stretch(get_render_coords(5, 30))
    wire.add_connection(i2_cp)

    return [wire]


def not_gate_if_resistance_was_a_thing(source: Source):
    input = Wire.ConnectionPoint(get_render_coords(0, 20), source.high)
    input_wire = Wire("input", input)
    input_wire.add_stretch(get_render_coords(0, 10))
    input_wire.add_stretch(get_render_coords(-10, 10))
    input_wire.add_stretch(get_render_coords(10, 10))

    battery = Wire.ConnectionPoint(get_render_coords(-20, 0), lambda: True)
    ground = Wire.ConnectionPoint(get_render_coords(20, 0), lambda: False)

    left_transistor_input = get_dead_connection(-17, 0)
    left_transistor_signal = get_dead_connection(-10, 7)
    left_transistor = Transistor(left_transistor_input, left_transistor_signal)

    right_transistor_input = get_dead_connection(3, 0)
    right_transistor_signal = get_dead_connection(10, 7)
    right_transistor = Transistor(right_transistor_input, right_transistor_signal)

    input_wire.add_connection(left_transistor_signal)
    input_wire.add_connection(right_transistor_signal)

    supply_wire = Wire("supply", battery)
    supply_wire.add_connection(left_transistor_input)

    connector_wire = Wire("connector", left_transistor.output)
    connector_wire.add_connection(right_transistor_input)

    ground_wire = Wire("ground", ground)
    ground_wire.add_connection(right_transistor.output)

    output = get_dead_connection(0, -20)
    connector_wire.add_connection(output)

    return [
        input_wire,
        left_transistor,
        right_transistor,
        supply_wire,
        connector_wire,
        ground_wire,
    ]


def or_gate(i1: Source, i2: Source):
    i1_source = Wire.ConnectionPoint(get_render_coords(-10, 20), i1.high)
    i2_source = Wire.ConnectionPoint(get_render_coords(10, 20), i2.high)

    input_one = Wire("Input one", i1_source)
    input_two = Wire("Input two", i2_source)

    t1_signal = get_dead_connection(-10, TRANSISTOR_SIZE)
    t2_signal = get_dead_connection(10, TRANSISTOR_SIZE)

    input_one.add_connection(t1_signal)
    input_two.add_connection(t2_signal)

    t1_battery = Wire.ConnectionPoint(
        get_render_coords(-10 - TRANSISTOR_SIZE, 0), lambda: True
    )
    t2_battery = Wire.ConnectionPoint(
        get_render_coords(10 - TRANSISTOR_SIZE, 0), lambda: True
    )

    t1 = Transistor(t1_battery, t1_signal)
    t2 = Transistor(t2_battery, t2_signal)

    output = Wire("output", t1.output)
    output.add_stretch(get_render_coords(0, 0))
    output.add_stretch(get_render_coords(0, -20))
    output.add_stretch(get_render_coords(20, -10))
    output.add_stretch(get_render_coords(20, 0))
    output.add_connection(t2.output)

    return (input_one, input_two, t1, t2, output)
