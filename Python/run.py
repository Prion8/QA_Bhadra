# import modules
# modules.Hello()
# print(modules.name)
# print(modules.age)
# modules.print_name()
from modules import Hello,age
Hello()

#import from alias
import modules as md
md.Hello()

from modules import print_name as pn
pn()