# F-String trick in Python
# 1 - quick debugging
var: int = 100
print(f'{var=}')
print(f'{isinstance(var, int)=}')
print(f'{1+1=}')

# 2 - rounding
decimal: float = 1234.5678
percent: float = .5678
print(f'{decimal:.2f}')
print(f'{percent: .2%}')

# 3 - separator on big number
big_number: float = 1_000000000.456
print(f'{big_number:_}')
print(f'{big_number:,}')
print(f'{big_number:,.1f}')

# 4 - datetime objects
from datetime import datetime
now: datetime = datetime.now()
print(f'{now:%x}')
print(f'{now:%c}')
print(f'{now:%H:%M:%S}')

# 5 - frenchstrings (fr/rf) - not really recommend to use for path sequence because \ kinda buggy
user: str = 'lucidasan'
path: str = fr'\User\{user}\Documents'
# path: str = fr'\User\{user}\Documents\' # not working(?)
print(path)

# 6 - nested string (f string inside of f string)
print(f'{1+1=} {f'{2+2=} {f'{3+3=}'}'}')

# 7 - Alignment (filling space) (:<) is actually default
text: str = 'LUCIDMOON IS HERE'
print(f'{text:_>30}')
print(f'{text:_^30}')
print(f'{text:_<30}')

print(f'{text:>30}')
print(f'{text:^30}')
print(f'{text:<30}')

# 8 - Custom format specifier
class Teks:
    def __init__(self, teks: str) -> None:
        self.teks = teks

    def __format__(self, format_spec: str) -> str:
        match format_spec:
            case 'upper':
                return self.teks.upper()
            case 'lower':
                return self.teks.lower()
            case 'count':
                return str(len(self.teks))
            case _:
                raise ValueError(f'Format specifier "{format_spec}" does not exist!')

my_teks: Teks = Teks('lucidmoon in uppercase')
my_teks2: Teks = Teks('LuCidmoon in LowerCASE')
print(f'{my_teks:upper}')
print(f'{my_teks2:lower}')
print(f'{my_teks:count}')