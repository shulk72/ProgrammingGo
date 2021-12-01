from lex import LexAnalyzer
from parser import NParser
from colorama import init
from termcolor import colored
import math
import sys
import os
# os
if __name__ == "__main__":

    print("\n---------- RUNNING TESTS -----------\n\n")

    failed = 0

    init() # Colorama stuff
    lexer = LexAnalyzer()
    parser = NParser()

    tests = [
        ("a[1+1]", ['+', 1.0, 1.0]),
        ("-4+5^2*10/2-2* 2+2", -4+5**2*10/2-2* 2+2),
        ("x=10; -2x^3", -2000),
        ("x=10; (-2x)^3", (-20)**3),
        ("4+5", 9),
        ("a=10; ----------a", 10),
        ("x=10; f(x,y)=x+y; f(2,3)", 5),
        ("x=10; f(x,y)=y then 's x+s'; f(2,3)", 5),
        ("x=10; f(x,y)=y+c with c=0 then 's s+x'; f(2,3)", 5),
        ("x=10; f(x,y)=y+c with c=x; f(2,3)", 5),
        ("a=b=2; d=-2a^2+5b; ans", 0),
        ("a=b=2; d=-2a^2+5b; d; 10ans; ans", 10*(-2*4+10)),
        ("f(x,y)=x+y; f(2,3)", 5),
        ("""   sum(x,y)=x+y
            sub(x,y) = x - y
            diff(x,y)=sum(x,y) * sub ( x ,y)
            diff(14,27)""", 14**2 - 27**2),




        ("f(x,y) = x + 2^x; f(2, -135)", 2+2**2),

        ("sum(x,y)=x+y; sum=15; sum(sum,sum(sum,sum))", 15+(15+15)), # what??

        ("f(x,y)=x+y; f(15)", 0),
        ("f(x,y^2)=x+y", None),


        ("f(x) = sin(x)+1; int f(x) from -2pi to 0.5pi", 1+(5*math.pi)/2),
        ("f(x)=2x; int f(x) from f(1) to f(f(f(2)))", 16*16 - 2*2),


        ("f(x) = |x|; int f(x) from -10 to 10", 100),
        ("f(x) = x; int f(x) from -10 to 10", 0),
        ("wtf(x,y) = 2y + int e^x from x to 3; wtf(1,2)", 21.367255094728623),

        ("1+2*3", 7),
        ("1+2 $ *3", 9),
        ("1+1+1+1+1+1 $ * 5", 30),
        ("int x from 0 to 1 + 14", 112.50000000000001),
        ("int x from 0 to 1 $+ 14", 14.5),
        ("5j(2)", 10j),
        ("j2=6; 5j2", 30),
        ("j(x)=2x; 5j(2)", 20),
        ("j(x)=x^2+1; 5 j(2)", 25),

        ("e0 = 15; 8e0", 15*8),


    ]

    for (expr, val) in tests:
        # Parsing wrapped with a stdout redirect to prevent prints unless --echo flag
        if (len(sys.argv)>1 and sys.argv[1]=='--echo'):
            tree = parser.parse(lexer.tokenize("new;"+expr))
            comp = parser.eval_tree(tree) if tree else None
            # print(tree)
        else:
            old_stdout = sys.stdout
            sys.stdout = open(os.devnull, "w")
            tree = parser.parse(lexer.tokenize("new;"+expr))
            comp = parser.eval_tree(tree) if tree else None
            sys.stdout = old_stdout

        if comp == val:
            print(  f"{colored('PASSED','green')} [ {expr} ] == {colored(f'({val})','cyan')}\n")
        else:
            print(  f"{colored('FAILED','red')} [ {expr} ], {colored(f'EXPECTED ({val})','yellow')}"+
                    f", {colored(f'GOT ({comp})','red')}\n")
            failed += 1

    print("------------------------------------")
    if failed>0:
        print(f"{colored(f'FAILED: {failed}','red')} (out of {len(tests)})\n")
    else:
        print(colored(f"All {len(tests)} tests were successful.\n",'green'))