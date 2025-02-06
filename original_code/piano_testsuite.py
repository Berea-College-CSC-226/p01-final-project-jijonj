from inspect import getframeinfo, stack
from piano import *

def unit_test(did_pass):
    caller = getframeinfo(stack()[1][0])
    linenum = caller.lineno

    if did_pass:
        msg = f"Test at line {linenum} ok."

    else:
        msg = f"Test at line {linenum} FAILED."

    print(msg)

def piano_test_suite():
    obj = Piano()
    unit_test(obj.get_right_audio("C#") == "python_grand_piano/Csharpgrand.wav")
    unit_test(obj.get_right_audio("Q") == None)

    unit_test(obj.get_note_color("W#") == "black")
    unit_test(obj.get_note_color("D#") == "black")
    unit_test(obj.get_note_color("S") == "white")

    unit_test(obj.get_text_color("D#") == "white")
    unit_test(obj.get_text_color("C#") == "white")
    unit_test(obj.get_text_color("C") == "black")

def main():
    piano_test_suite()

if __name__ == "__main__":
    main()
