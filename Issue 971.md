# Issue 971: update the sympy package

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-10-23 01:36:18

Assignee: was


```
Hi,

I finally found time to write those _sage_ methods in SymPy we
discussed earlier.
The code is here:

http://dakol.hopto.org/sympy-sage/

(we are in the state of moving from Subversion to Mercurial in SymPy).
I created a new sympy spkg, by updating it's hg repository:

http://dakol.hopto.org/sympy-spkg/

(the change is trivial, because the src is not included). The spkg can
be downloaded from:

http://dakol.fsik.cvut.cz/~ondra/sympy-0.5.5.spkg

Install with:

./sage -i sympy-0.5.5.spkg

Now test it. Run this in sage:

---------------------------------------------

#!/usr/bin/env sage
#import sys
#sys.path.insert(0,"/home/ondra/ext/sympy-sage/")
from sympy import __version__
print __version__

print "SAGE:"

e = 1/cos(x)**3
print e
f = e.taylor(x, 0, 8)
print f

print "SymPy:"
from sympy import Symbol, cos, sympify, pprint
from sympy.abc import x

e = sympify(1)/cos(x)**3
print e
f = e.series(x, 10)
print f
print "\nSymPy pretty printer:"
pprint(e)
pprint(f)

print "\nSymPy -> SAGE:"
print e._sage_()
print f._sage_()

-------------------------------------------

it will produce the following output (I put the code above into example.sage):

ondra`@`fuji:~/ext/sage-2.8.7-debian32-i686-Linux$ ./sage example.sage
0.5.5-svn
SAGE:
                                      1
                                   -------
                                      3
                                   cos (x)
                           8        6       4      2
                     8651 x    241 x    11 x    3 x
                     ------- + ------ + ----- + ---- + 1
                      13440     240       8      2
SymPy:
cos(x)**(-3)
1 + (3/2)*x**2 + (11/8)*x**4 + (241/240)*x**6 + (8651/13440)*x**8 + O(x**10)

SymPy pretty printer:
  -3
cos  (x)
      2       4        6         8
   3*x    11*x    241*x    8651*x
1 + ---- + ----- + ------ + ------- + O(x**10)
    2       8      240      13440

SymPy -> SAGE:
                                      1
                                   -------
                                      3
                                   cos (x)
                           8        6       4      2
                     8651 x    241 x    11 x    3 x
                     ------- + ------ + ----- + ---- + 1
                      13440     240       8      2



Currently only the Add, Mul, Pow, Rational, Integer, sin, cos classes
have the _sage_ method, but that is enough for some basic playing.
Let's now implement the corresponding _sympy_ method in SAGE and maybe
a few more iterations to see if we like it. And if so, I'll implement
the _sage_() for more SymPy classes.

I'd like to achieve a state, where the same code in SAGE could be run
on both backends (Maxima and SymPy). That way we could easily see
where Maxima is better than SymPy and vice versa.

Could you William please create a trac login for me? I'd like to open
and discuss a new ticket for it. Also so that I can attach any bundles
in there.

Are you planning to make another SAGE release before SD 6? If so, it
would be good if we could make it before it, then we'll release SymPy,
create spkg, you'll release SAGE, include the spkg, so that it's
working out of the box for everyone at SD6 and we can discuss some new
more exciting things to do in Bristol.

I am sorry it has taken me so long, I was really busy.

Ondrej
```



---

Comment by malb created at 2007-10-23 21:17:54


```
Just a note that the spkg above is just a preliminary unreleased
version and contains some other minor bugs. But I want to settle on
some interface to SAGE now. And then we'll fix the bugs and make a
release and then you can include it in SAGE officially.
```

so I push it back to 2.9.


---

Comment by cwitty created at 2007-10-30 16:07:48

From Ondrej, via sage-devel:


```
We made a new  release of SymPy with those _sage_() methods so that it
can be integrated in SAGE more systematically. If some suggestions
arise now, we'll simply change it and release again. 
```

and

```
I don't have access to the tracker, but here is how you can generate
the sympy spkg:

hg clone http://hgsympy.hopto.org/sympy-spkg/
cd sympy-spkg
./get-orig-sources
cd ..
/path/to/sage -pkg sympy-spkg

This will generate sympy-spkg.spkg. So you may want to rename the
sympy-spkg dir to the version of sympy. Generally I think the name of
the package shouldn't be inferred from the name of the directory,
since the directory doesn't change, but the version of the package
does.
```



---

Attachment

There's a new sympy spkg, generated according to the above instructions, at http://sage.math.washington.edu/home/cwitty/sympy-0.5.6.hg

Also, I've added a patch that does some minor doctesting of the new sympy.


---

Comment by mabshoff created at 2007-11-01 09:37:20

Resolution: fixed


---

Comment by mabshoff created at 2007-11-01 09:37:20

spkg updated, patch applied to 2.8.11.alpha0
