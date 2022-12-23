# Issue 2019: problem with gap_packages-4.4.10_3

Issue created by migration from https://trac.sagemath.org/ticket/2019

Original creator: wdj

Original creation time: 2008-01-31 23:31:49

Assignee: mabshoff

There is a serious problem with gap_packages-4.4.10_3.

If this package is not installed then

sage: C = RandomLinearCode(10, 3,GF(2))
sage: Cd = C.dual_code()

works fine. Otherwise, you get the following error (which is not
fixed by gap_reset_workspace() and has been verified on 
an ubuntu machine and an intel macbook):

---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/wdj/sagefiles/sage-2.9/<ipython console> in <module>()

/Users/wdj/sagefiles/sage-2.9/local/lib/python2.5/site-packages/sage/coding/linear_code.py in dual_code(self)
    745         #return LinearCode(A)       ## This does not work when k = n-1 for a mysterious reason.
    746         ##  less pythonic way :
--> 747         C = gap("DualCode(GeneratorMatCode("+Gstr+",GF("+str(q)+")))")
    748         G = C.GeneratorMat()
    749         Gs = G._matrix_(F)

/Users/wdj/sagefiles/sage-2.9/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __call__(self, x)
    736             return x
    737         if isinstance(x, basestring):
--> 738             return cls(self, x)
    739         try:
    740             return self._coerce_from_special_method(x)

/Users/wdj/sagefiles/sage-2.9/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __init__(self, parent, value, is_name)
    987             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:
    988                 self._session_number = -1
--> 989                 raise TypeError, x
    990         self._session_number = parent._session_number
    991 

<type 'exceptions.TypeError'>: Gap produced error output
List Element: <list>[2] must have an assigned value

   executing Read("/Users/wdj/.sage//temp/david_joyners_computer.local/16049//interface//tmp");

My fault, since created the package, but I have no idea how to fix this.



---

Comment by wdj created at 2008-02-01 00:52:36

This is not a fix but a work-around:
If you create a clone then the problem goes away!


---

Comment by wdj created at 2008-02-01 04:28:06

Here seems to be the solution, which makes the above problem go away: 

(1) in SAGE, run gap_reset_workspace()
(2) quit SAGE
(3) restart SAGE.

I don't know how to add this to the spkg-install script or even if that is the 
type of command one wants added to that. Maybe it should be added to sage-spkg??

I tried (1)+(2) before reporting the problem to trac in the first place but 
forgot to add step (3).

Possibly this is a bug in the version of guava included in gap_packages* ??
In any case, I prepared a new gap_packages* tarball with a few updated packages,
including a new version of guava. It is at
http://sage.math.washington.edu/home/wdj/patches/gap_packages-4.4.10_4.spkg
Seems to work fine but I am running sage -testall now and will report any problems.
However, even with this new package, you must do (1)+(2)+(3) after installing.

This seems to emphasize in my mind the need to write the guava functions in native 
Python as much as possible.


---

Comment by was created at 2008-02-01 05:09:56

Fortunately there is now a simple solution to this problem.

From spkg-install do

```
touch "$SAGE_LOCAL"/bin/gap_stamp
```


Then any user who starts sage will automatically have their gap workspace reset.
Any time any spkg install gap stuff, it is supposed to touch the above file.

 -- William


---

Comment by wdj created at 2008-02-01 05:20:32

That did it- thanks!

I am uploading right now a new version of
http://sage.math.washington.edu/home/wdj/patches/gap_packages-4.4.10_4.spkg
which has this command added to spkg-install

Thanks again William.


---

Comment by mabshoff created at 2008-02-02 06:50:39

I have uploaded the new optional spkg the the sagemath.org repo. In the future we should add a proper hg repo in the base directory as well as update SPKG.txt on changes.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-02 06:51:35

Optional spkg uploaded to sagemath.org and mirrored out


---

Comment by mabshoff created at 2008-02-02 06:51:35

Resolution: fixed
