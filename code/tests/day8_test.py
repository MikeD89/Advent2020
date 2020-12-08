from utils import utils
import day8


def test():
    a = day8.BootCode()
    assert a.accumulator == 0
    assert a.pointer == 0
    a.step("acc", 5)
    assert a.accumulator == 5
    assert a.pointer == 1
    a.undo()
    assert a.accumulator == 0
    assert a.pointer == 0
    a.step("acc", 5)
    a.step("jmp", -100)
    assert a.accumulator == 5
    assert a.pointer == -99
    a.undo()
    assert a.accumulator == 5
    assert a.pointer == 1
    a.step("nop", "uefhiuhsewifuhse")
    assert a.accumulator == 5
    assert a.pointer == 2
    a.undo()
    assert a.accumulator == 5
    assert a.pointer == 1

    return "Pass!"
