# Issue 7193: os x 10.6 -- print warning about Sage being broken, so we can release

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-10-12 05:10:01

Assignee: tbd

CC:  jason

Since *everybody* is totally stumped about how to fix Sage on OS X 10.6, let's release but print a big warning message about the one remaining bug. 


---

Attachment


---

Comment by jason created at 2009-10-12 23:09:40

I'd love to referee this, but I don't have access to a 10.6 machine, so I can't verify that it works.


---

Comment by jason created at 2009-10-12 23:09:49

Changing status from new to needs_review.


---

Comment by jason created at 2009-10-13 03:45:34

Changing status from needs_review to needs_work.


---

Comment by jason created at 2009-10-13 03:45:34

Shouldn't this use the python platform module, rather than os.uname?

http://docs.python.org/library/platform.html


---

Comment by jason created at 2009-10-13 03:46:41

Changing status from needs_work to needs_info.


---

Comment by jason created at 2009-10-13 03:46:41

if you use the python platform module, you can check specifically for 10.6:


```
>>> platform.mac_ver()
('10.6.1', (_, _, ''), 'i386')
```


However, it might be nice to warn people on 10.5 that 10.6 will not work to prevent people from upgrading.  What do you think?


---

Comment by jhpalmieri created at 2009-10-13 04:49:52

Replying to [comment:5 jason]:
> if you use the python platform module, you can check specifically for 10.6:

I think the test `if os.uname()[2] == "10.0.0"` does check specifically for 10.6.  If you're running OS X 10.5, then os.uname()[2] returns "9.8.0" (at least on my machine.  (On the other hand, `platform.mac_ver()` doesn't return anything with 10.5: I get `(_, (_, _, _), '')` as output.)

As for the warning, in addition or instead, should we put a notice up on sagemath.org, on the Mac download page?


---

Comment by was created at 2009-10-13 05:49:34

I'm changing this back to needs review, in light of John's comments.


---

Comment by was created at 2009-10-13 05:49:34

Changing status from needs_info to needs_review.


---

Comment by AlexGhitza created at 2009-10-19 04:12:31

Changing component from algebra to distribution.


---

Comment by kcrisman created at 2009-10-20 05:39:38

In light of the recent message [here](http://groups.google.com/group/sage-support/browse_thread/thread/eaf6f141dab9ae54/90f42dab4f2884ac?show_docid=90f42dab4f2884ac), has enough testing been done to close this?


---

Comment by was created at 2009-11-11 19:03:47

>  In light of the recent message  here, has enough testing been done to close this?

No, that is orthogonal.


---

Comment by was created at 2009-11-11 19:04:52

Changing status from needs_review to needs_work.


---

Comment by was created at 2009-11-11 19:04:52

The line
`if os.uname()[2] == "10.0.0"`
must be changed, since in new versions of 10.6 we have

```
sage: os.uname()[2]
'10.2.0'
```



---

Attachment


---

Comment by was created at 2009-11-11 19:09:02

Changing status from needs_work to needs_review.


---

Comment by GeorgSWeber created at 2009-11-11 20:52:36

Changing status from needs_review to positive_review.


---

Comment by GeorgSWeber created at 2009-11-11 20:52:36

In verifying this, I cheated a bit.

(I've only got OS X 10.4, so I had to replace one "10" with an "8", just for the sake of the test of course.)


---

Comment by GeorgSWeber created at 2009-11-11 20:53:44

BTW: One has to apply both patches, first the original one, then the "part2" one.


---

Comment by jhpalmieri created at 2009-11-11 20:58:04

(For what it's worth, I checked on the machines I have easy access to: on 10.5, `os.uname()[2]` returns "9.8.0", on 10.6, it returns "10.0.0", and on 10.6.2, it returns "10.2.0".)


---

Comment by mhansen created at 2009-11-12 06:05:57

Resolution: fixed
