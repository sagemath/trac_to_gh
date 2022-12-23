# Issue 8903: update pynac to 0.2.0

Issue created by migration from https://trac.sagemath.org/ticket/8903

Original creator: burcin

Original creation time: 2010-05-06 04:08:57

Assignee: tbd

CC:  mhansen

Keywords: pynac

A new pynac package with several critical fixes is available here:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.2.0.spkg

It contains fixes for:

 * #8542: function table for Cygwin
 * #8651: binomial(n, 0) -> 1
 * #8688: extra parenthesis when typesetting fractions
 * #8775: auto evaluation of conjugates

Note that patches from the above tickets need to be applied to test this ticket. Without #8542, you'll get a segfault. The others fix doctests.


---

Comment by burcin created at 2010-05-06 04:32:29

Changing status from new to needs_review.


---

Comment by burcin created at 2010-05-06 18:04:32

This package depends on the Python package at #8907.


---

Comment by burcin created at 2010-05-23 15:10:17

Changing status from needs_review to needs_work.


---

Comment by burcin created at 2010-05-23 15:10:17

The last patch for conjugates and power simplification included in this pynac version breaks doctests in `sage/rings/qqbar.py` and a bunch of other places.

I suppose the fix will involve looking into the `power_helper` in detail, hopefully fixing #8959 on the way. I won't have time for this at least for a week though.

If anybody is interested in working on the cygwin port, I can prepare a package which includes only the patches relevant for that in the mean time.


---

Comment by mhansen created at 2010-05-25 22:19:09

I've put a new spkg up at http://sage.math.washington.edu/home/burcin/pynac/pynac-0.2.0.spkg .  This just has a simple fix for #9307.


---

Comment by mhansen created at 2010-05-25 22:19:34

err, #8907


---

Comment by mhansen created at 2010-05-25 22:20:47

Third time is the charm: #9037


---

Comment by mhansen created at 2010-05-26 02:19:35

I've made a new spkg at  http://sage.math.washington.edu/home/burcin/pynac/pynac-0.2.0.spkg which just backs out the commit which adds "auto evaluation of conjugates".  All tests in qqbar pass.  We can add the auto evaluation of conjugates in 0.2.1.


---

Comment by was created at 2010-05-28 19:32:12

I merged in   http://sage.math.washington.edu/home/burcin/pynac/pynac-0.2.0.spkg


---

Comment by was created at 2010-05-28 19:32:12

Resolution: fixed


---

Comment by drkirkby created at 2010-05-30 12:06:56

Despite Mike's comments on #9037, this does not resolve the issue there, as it still has:


```
if [ `uname` = "Darwin" -a "$SAGE64" = "yes" ]; then
    echo "64 bit MacIntel"
    CXXFLAGS="-m64 -O2 -g"; export CXXFLAGS
    LDFLAGS="-m64"; export LDFLAGS
fi
```


I'll have to create a new package based on this one and apply the fix again. 

Dave


---

Comment by burcin created at 2010-05-30 12:12:25

Hi Dave,

Which package are you looking at. Unfortunately, there are several packages named pynac-0.2.0.spkg floating around. My version at

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.2.0.spkg

doesn't have the said fix, but Mike's version at 

http://sage.math.washington.edu/home/mhansen/pynac-0.2.0.spkg

might do. I believe the version included in the release is the latter.


---

Comment by drkirkby created at 2010-05-30 12:53:44

Replying to [comment:12 burcin]:
> Hi Dave,
> 
> Which package are you looking at. Unfortunately, there are several packages named pynac-0.2.0.spkg floating around. My version at
> 
> http://sage.math.washington.edu/home/burcin/pynac/pynac-0.2.0.spkg
> 
> doesn't have the said fix, but Mike's version at 
> 
> http://sage.math.washington.edu/home/mhansen/pynac-0.2.0.spkg
> 
> might do. I believe the version included in the release is the latter.

I often wish there was a central repository, as having different versions and constant rebasing does get a bit annoying. 

Mike's version at http://sage.math.washington.edu/home/mhansen/pynac-0.2.0.spkg does have the fix, but the only version mentioned on this trac ticket was yours at http://sage.math.washington.edu/home/burcin/pynac/pynac-0.2.0.spkg which does not have the fix. The comment from William was 

"I merged in  http://sage.math.washington.edu/home/burcin/pynac/pynac-0.2.0.spkg"

so I can only assume your version, and not Mikes is merged. 

Actually, it appears changing

```
if [ `uname` = "Darwin" -a "$SAGE64" = "yes" ]; then
```

to 

```
if [ "$SAGE64" = "yes" ]; then
```


(as in Mike's version), does not fully solve the 64-bit build issue on OpenSolaris. However, it is certainly a desirable change, so if you make any more changes to pynac, can you change that one line. 

In the mean time, I'll work on trying to resolve why that is not a complete fix for the 64-bit OpenSolaris issue, but it is certainly a necessary change. 

Dave


---

Comment by mhansen created at 2010-05-30 18:16:08

I'll make sure that mine is the one in 4.4.3.alpha1.


---

Comment by drkirkby created at 2010-05-30 18:48:06

Replying to [comment:14 mhansen]:
> I'll make sure that mine is the one in 4.4.3.alpha1.

The ticket says Burchin's package has already been merged in sage-4.4.3.alpha1 - whether it is possible to reverse that easily I don't know. 

Dave
