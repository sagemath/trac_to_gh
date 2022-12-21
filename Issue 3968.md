# Issue 3968: Magma interface sometimes fails on long inputs

Issue created by migration from Trac.

Original creator: kedlaya

Original creation time: 2008-08-27 17:27:14

Assignee: was

This fails:

```
%magma
Qt<t> := RationalFunctionField(Rationals());
R<w,x,y,z> := PolynomialRing(Qt, 4);
P0 := w^3 + x^3 + y^3 + z^3;
P := P0 + (w+x)*(w+2*y)*(w+3*z) + x*y*z;
Pt := P0 + t*P;
Pt_gradient := [Derivative(Pt, w), Derivative(Pt, x), Derivative(Pt, y), Derivative(Pt, z)];
Pt_jac := IdealWithFixedBasis(Pt_gradient);
Pt_gradient_long := Append(Pt_gradient, (1+t)*w*x*y*z);
Pt_jac_long := IdealWithFixedBasis(Pt_gradient_long);
b := (1+t)*w*x*y*z;
diffbasis := [2*w*P, 2*x*P, 2*y*P, 2*z*P, 3*b*P];
temp := Coordinates(Pt_jac, diffbasis[5]);
diffbasis[5] := (Derivative(temp[1],w) + Derivative(temp[2],x) + \
    Derivative(temp[3],y) + Derivative(temp[4],z)) / (-3);
```

with the error: 

```
   File "<ipython console>", line 1
     logstr(r"""Loading "/home/r1/kedlaya/.sage//temp/DWORK.MIT.EDU/22570//interface//tmp"""")
                                                                                             ^
SyntaxError: EOL while scanning single-quoted string
```

but if you replace the last two lines by

```
diffbasis[5] := (Derivative(temp[1],w) + Derivative(temp[2],x) + Derivative(temp[3],y))/(-3);
```

then nothing breaks.



---

Comment by jason created at 2008-08-27 17:31:47

From IRC

```
[12:20] <jason_> my error has:
[12:20] <jason_>    File "<ipython console>", line 1
[12:20] <jason_>      logstr(r"""Loading "/home/jason/.sage//temp/sage/4426//interface//tmp4426"""")
[12:20] <kedlaya> yeah, I see something similar
[12:20] <jason_> I think that last """" is the problem
[12:20] <jason_> is it being parsed as " """
[12:20] <jason_> or as """ "
[12:21] <wjp> funny that that error message has a "# TODO: this is a very lazy temporary bug fix" above the line in the sources
[12:21] <kedlaya> too lazy, i guess
[12:21] <wjp> (sage/misc/preparser_ipython.py, search for logstr)
[12:21] <kedlaya> i wonder if I can find the ticket for it
[12:21] <jason_> wjp: if you have the sources, can you put a space in between the " and the """ ?
[12:22] <wjp> the line is return 'logstr(r"""%s""")'%t, but I'll add a space after the %s
[12:23] <wjp> works now
[12:23] <jason_> okay, now time for the ticket :)
[12:23] <kedlaya> I'm working on it now
[12:23] <jason_> from http://docs.python.org/ref/strings.html
[12:23] <jason_> In triple-quoted strings, unescaped newlines and quotes are allowed (and are retained), except that three unescaped quotes in a row terminate the string. (A ``quote'' is the character used to open the string, i.e. either ' or ".) 
[12:23] <jason_> so apparently the first three """ terminated the string
[12:24] <wjp> yes
[12:24] <kedlaya> ticket #3968 created. Now go fix it. :)
```



---

Comment by jason created at 2008-08-27 19:22:51

Updated patch to escape strings rather than hoping they don't contain triple quotes.


---

Attachment


---

Comment by jason created at 2008-08-27 19:28:12

Okay, again updated to use the much simpler solution: %r instead of %s.


---

Comment by mabshoff created at 2008-08-27 20:45:29

Shouldn't we add a doctest that tests for the case that Kiran discovered?

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-27 21:05:02

For the record: doctests pass with the patch applied.

Cheers,

Michael


---

Comment by wjp created at 2008-08-27 21:15:02

For a potential doctest, this is easy to trigger with the singular interface too:


```
sage: %singular

  --> Switching to Singular <-- 

''
singular: print("\"test\"")
------------------------------------------------------------
   File "<ipython console>", line 1
     logstr(r""""test"""")
                         ^
SyntaxError: EOL while scanning single-quoted string
```



---

Comment by mabshoff created at 2008-08-28 20:40:00

Resolution: fixed


---

Comment by mabshoff created at 2008-08-28 20:40:00

Merged in Sage 3.1.2.alpha2
