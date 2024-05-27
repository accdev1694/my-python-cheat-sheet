import cowsay
import sys

# modules are codes that you or others have written that you can have access to for use in your own code

# lets us ethe cowsay module

if len(sys.argv) == 2:
    cowsay.trex(sys.argv[1])
