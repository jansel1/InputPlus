import keyboard
import colorama

class Color:
    def fromrgb_fore(r, g, b): return f'\033[38;2;{r};{g};{b}m'
    def fromrgb_back(r, g, b): return f'\033[48;2;{r};{g};{b}m'

    def reset_fore(): return colorama.Fore.RESET
    def reset_back(): return colorama.Back.RESET

    def reset(): return colorama.Fore.RESET + colorama.Back.RESET

def Await(escapekey="esc"):
     while True: 
            k=keyboard.read_event().name; 

            if k == escapekey: break; return 0

def Print(*args, end="\n", flush=False):
    out = ""

    for v in args:
        if v:
            out += v 

    print(out, end=end, flush=flush)
    
def Input(prompt: str="", newline_after: bool=True, _await: bool=False, escapekey="esc"):
    print(prompt, end="", flush=True)

    _input = ""
    _text = ""

    _can_run = True

    if (_await): 
        while True: 
            k=keyboard.read_event().name; 

            if k == escapekey: break; return 0
    try:
        while _can_run:
            event = keyboard.read_event()
            
            if event.event_type == keyboard.KEY_DOWN and not keyboard.is_pressed("ctrl"):
                key = event.name

                if key == 'esc': break; return 0

                if key == 'enter':
                    if newline_after:
                        print()

                    break
                elif key == 'space':
                    _text += ' '
                    print(' ', end="", flush=True)
                elif key == 'backspace':
                    if _text:
                        _text = _text[:-1]
                        print('\b \b', end="", flush=True)
                elif key == 'tab':
                    _text += "\t"
                    print('\t', end="", flush=True)
                elif len(key) == 1:
                    _text += key
                    print(key, end="", flush=True)
    except KeyboardInterrupt: _can_run = False

    return _text

Print(Color.fromrgb_fore(55, 56, 7), "Hello world!", Color.reset())
Print("Life is like rizz")