
#--------------≤‚ ‘”√------------
import pstats, cProfile
mingw_setup_args={'options': {'build_ext': {'compiler': 'mingw32'}}}
import pyximport; pyximport.install(setup_args=mingw_setup_args)
from cython2 import  b

def intest():
    for i in xrange(3000000):
        b(2)

cProfile.runctx("intest()", globals(), locals(), "Profile.prof")

s = pstats.Stats("Profile.prof")
s.strip_dirs().sort_stats("time").print_stats()


