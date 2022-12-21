# Issue 9037: pynac fails to build on 64-bit OpenSolaris x64.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-05-24 17:04:56

Assignee: drkirkby

CC:  jsp

The spkg-install of 'pynac' has:


```
if [ `uname` = "Darwin" -a "$SAGE64" = "yes" ]; then
    echo "64 bit MacIntel"
    CXXFLAGS="-m64 -O2 -g"; export CXXFLAGS
    LDFLAGS="-m64"; export LDFLAGS
fi
```


so obviously does not attempt to build 64-bit when SAGE64="yes", unless the operating systems is OS X. 

The build actually fails on a 64-bit OpenSolaris system, as pynac tries to link to 64-bit objects, which obviously fails. 


```
sage: An error occurred while installing pynac-0.1.12
```



---

Comment by drkirkby created at 2010-05-24 18:19:39

For other OpenSolaris issues, see #9026


---

Comment by mhansen created at 2010-05-25 19:01:25

This should be coordinated with #8903.  I can make a new spkg for this issue.


---

Comment by mhansen created at 2010-05-25 22:21:48

There is a new spkg at #8903 which fixes this issue.


---

Comment by drkirkby created at 2010-05-30 12:01:37

#8903 does *not* fix the issue, as it still has:


```
if [ `uname` = "Darwin" -a "$SAGE64" = "yes" ]; then
    echo "64 bit MacIntel"
    CXXFLAGS="-m64 -O2 -g"; export CXXFLAGS
    LDFLAGS="-m64"; export LDFLAGS
fi
```


I'll have to create a new package based on that at #8031. 

Dave


---

Comment by drkirkby created at 2010-05-30 12:03:03

Oops, I mean I'll have to create a new package based on that at #8903.


---

Comment by mhansen created at 2010-06-03 04:18:27

Changing status from new to needs_review.


---

Comment by mhansen created at 2010-06-03 04:18:27

This change looks good to me and is what is done in lots of other spkgs.


---

Comment by mhansen created at 2010-06-03 04:18:35

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-06-03 15:34:36

Resolution: fixed
