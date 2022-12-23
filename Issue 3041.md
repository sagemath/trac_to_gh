# Issue 3041: optimization setting in LinBox.spkg is broken

Issue created by migration from https://trac.sagemath.org/ticket/3041

Original creator: mabshoff

Original creation time: 2008-04-27 04:54:06

Assignee: mabshoff

Francois reports:

```
Just reviewing what options linbox is compiled with for sage,
well I was really looking at whether optimizations are enabled.
In theory they are, except on Sun:
if [ $UNAME = "SunOS" ]; then
   OPT="--enable-optimization=false"
   echo "Building on SunOS"
else
   OPT="--enable-optimization"
fi

Of course in practice they aren't because "$OPS" and not
"$OPT" is passed to the configuration. I must admit I didn't
check if it was corrected in 3.0.1.alpha0 but if so I missed
it in michael's log. 
```



---

Attachment

The spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.1/alpha1/linbox-1.1.5.p4.spkg

contains the fix in form of the above patch. It builds fine for me on sage.math and bsd.

Cheers,

Michael


---

Comment by jkantor created at 2008-04-27 05:27:30

Tested on OSX and Linux. Spkg builds, modular forms doctest all pass.


---

Comment by mabshoff created at 2008-04-27 05:33:45

Merged in Sage 3.0.1.alpha1


---

Comment by mabshoff created at 2008-04-27 05:33:45

Resolution: fixed


---

Comment by mabshoff created at 2008-04-27 05:36:12

Partial credit goes to Francois Bissey.

Cheers,

Michael
