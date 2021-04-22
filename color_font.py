STD_INPUT_HANDLE   = -10
STD_OUTPUT_HANDLE  = -11
STD_ERROR_HANDLE   = -12

bule_font = 0x01 # text color contains blue.
green_font = 0x02 # text color contains green.
red_font = 0x04 # text color contains red.

import ctypes

std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

def set_color(color, handle=std_out_handle):
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool

