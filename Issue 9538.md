# Issue 9538: internal side effect in roots?

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2010-07-18 15:42:05

Assignee: burcin

CC:  nbruin

Keywords: roots, side effect

Consider the following with Sage 4.4.4:

```
sage: var('a6,a5,a4,x')
(a6, a5, a4, x)
sage: e=15*a6*x^2 + 5*a5*x + a4
sage: e.roots(x)
[(-1/30*(sqrt(-12*a4*a6 + 5*a5^2)*sqrt(5) + 5*a5)/a6, 1), (1/30*(sqrt(-12*a4*a6 + 5*a5^2)*sqrt(5) - 5*a5)/a6, 1)]
```

This is fine. However:

```
sage: var('f6,f5,f4,x')
(f6, f5, f4, x)
sage: e=15*f6*x^2 + 5*f5*x + f4
sage: e.roots(x)
[(1/30*(-I*sqrt(35) - 5)/binomial(n, k), 1), (1/30*(I*sqrt(35) - 5)/binomial(n, k), 1)]
```

WTF???


---

Comment by mhansen created at 2010-07-18 17:11:12

I'm pretty sure this is just #8734.


---

Comment by zimmerma created at 2010-07-18 17:55:19

Replying to [comment:1 mhansen]:
> I'm pretty sure this is just #8734.

I tried the patch coming with #8734, but this does not resolve this issue.

Paul


---

Comment by mpatel created at 2010-08-12 22:43:58

Replying to [comment:2 zimmerma]:
> Replying to [comment:1 mhansen]:
> > I'm pretty sure this is just #8734.
> 
> I tried the patch coming with #8734, but this does not resolve this issue.

Could you try this again?  After applying #8734 to 4.5.3.alpha0 (and ignoring the patch rejects), I get

```python
sage: var('f6,f5,f4,x')
(f6, f5, f4, x)
sage: e=15*f6*x^2 + 5*f5*x + f4
sage: e.roots(x)
[(-1/30*(sqrt(-12*f4*f6 + 5*f5^2)*sqrt(5) + 5*f5)/f6, 1), (1/30*(sqrt(-12*f4*f6 + 5*f5^2)*sqrt(5) - 5*f5)/f6, 1)]
```



---

Comment by burcin created at 2010-09-26 00:07:30

The patch attached to #8734 indeed fixes this problem. However there are simpler solutions, and I'm not convinced that #8734 is necessary, given that #7377 could solve this in a much cleaner way. Also see the discussion linked from comment:3:ticket:8734:

http://groups.google.com/group/sage-devel/browse_thread/thread/67f0a63d00b8d835/06557a921a582f87

In particular, Robert Dodier's suggestion to apply this patch to maxima:


```
--- share/contrib/Zeilberger/testZeilberger.mac 9 Feb 2007 22:32:34
-0000       1.4
+++ share/contrib/Zeilberger/testZeilberger.mac 15 Jan 2010 19:10:53
-0000
`@``@` -110,3 +110,8 `@``@`

 FULL_TEST : append(GOSPER_TEST,EASY_TEST,
                    HARD_TEST,EXTREME_TEST);
+
+kill (g1, g2, g3, g4, g5, g6, g7,
+    f1, f2, f3, f4, f5, f6, f7, f8, f9, f10,
+    h1, h2, h3, h4, h5, h6, h6b, h7, h8, h9, h10, h11, h12, h13,
+    d1, d2); 
```


I can confirm that adding these lines to `$SAGE_LOCAL/share/maxima/5.20.1/share/contrib/Zeilberger/testZeilberger.mac` solves this issue.

Perhaps this patch is already in a more recent version of maxima?


---

Comment by zimmerma created at 2010-09-26 08:05:26

I confirm that with the #8734 patch applied to 4.5.3 (and ignoring the patch reject) it works
fine.

However I'm convinced by Burcin's argument. I am ready to review a patch based on this patch
applied to Maxima.

Paul


---

Attachment


---

Comment by burcin created at 2010-09-26 16:00:29

Here is a maxima package that patches the file `share/contrib/Zeilberger/testZeilberger.mac` as suggested by Robert Dodier:

http://sage.math.washington.edu/home/burcin/maxima-5.20.1.p1.spkg

attachment:trac_9538-maxima_kill.patch adds a doctest to check the example given in the description.


---

Comment by burcin created at 2010-09-26 16:00:29

Changing status from new to needs_review.


---

Comment by zimmerma created at 2010-09-26 16:39:36

I tried `sage -i /tmp/maxima-5.20.1.p1.spkg` but got:

```
...
;;; OPTIMIZE levels: Safety=2, Space=0, Speed=3, Debug=2
;;; End of Pass 1.
;;; Note: Creating tag: "_eclFGkv5HJdeKquW_9rDWPWz" for #P"binary-ecl/maxima-package.o"
;;; Internal error: Unable to find include directory
;      - Binary file binary-ecl/maxima-package.fas is old or does not exist. 
;        Compile (and load) source file /usr/local/sage-4.5.3/sage/spkg/build/maxima-5.20.1.p1/src/src/maxima-package.lisp instead? y

;      - Should I bother you if this happens again? y

;      - Compiling source file
;        "/usr/local/sage-4.5.3/sage/spkg/build/maxima-5.20.1.p1/src/src/maxima-package.lisp"
;;; Compiling /usr/local/sage-4.5.3/sage/spkg/build/maxima-5.20.1.p1/src/src/maxima-package.lisp.
;;; OPTIMIZE levels: Safety=2, Space=0, Speed=3, Debug=2
;;; End of Pass 1.
;;; Note: Creating tag: "_eclFGkv5HJdeKquW_IVMWPWz" for #P"binary-ecl/maxima-package.o"
;;; Internal error: Unable to find include directory
;      - Loading binary file "binary-ecl/maxima-package.fas" An error occurred during initialization:
Filesystem error with pathname #P"/usr/local/sage-4.5.3/sage/spkg/build/maxima-5.20.1.p1/src/src/binary-ecl/maxima-package.fas".
Either
 1) the file does not exist, or
 2) we are not allow to access the file, or
 3) the pathname points to a broken symbolic link..
make[1]: *** [binary-ecl/maxima] Error 1
make[1]: Leaving directory `/usr/local/sage-4.5.3/sage/spkg/build/maxima-5.20.1.p1/src/src'
make: *** [all-recursive] Error 1
***********************************************************
Failed to make Maxima.
***********************************************************
```

Did I something wrong? How to install the patched spkg?

Paul


---

Comment by zimmerma created at 2010-09-26 16:39:36

Changing status from needs_review to needs_info.


---

Comment by burcin created at 2010-09-26 20:20:35

patch for maxima spkg


---

Attachment

Replying to [comment:7 zimmerma]:
> Did I something wrong? How to install the patched spkg?

I don't have any experience with the maxima spkg. I just applied the patch in attachment:maxima_package.patch. It works here, but just complains about not being able to build `maxima.fasb`:


```
cp: cannot stat `maxima.fasb': No such file or directory
```


Perhaps someone more knowledgeable can help out. Building maxima as a library is #8645.


---

Comment by zimmerma created at 2010-09-27 09:06:54

maybe we should wait that #8645 is fixed and merged within Sage to review that ticket.

Paul


---

Comment by mpatel created at 2010-09-30 23:18:10

Adding

```
kill (g1, g2, g3, g4, g5, g6, g7,
    f1, f2, f3, f4, f5, f6, f7, f8, f9, f10,
    h1, h2, h3, h4, h5, h6, h6b, h7, h8, h9, h10, h11, h12, h13,
    d1, d2);
```

directly to the bottom of 

 `SAGE_ROOT/local/share/maxima/5.20.1/share/contrib/Zeilberger/testZeilberger.mac`

without installing http://sage.math.washington.edu/home/burcin/maxima-5.20.1.p1.spkg fixes the problem in the description.


---

Comment by mpatel created at 2010-09-30 23:26:03

Replying to [comment:7 zimmerma]:
> I tried `sage -i /tmp/maxima-5.20.1.p1.spkg` but got: 

> [...]

> Did I something wrong? How to install the patched spkg?

I have the same problem with the forthcoming 4.6.alpha2, *if* I've renamed `SAGE_ROOT` since that copy of Sage was first compiled (and another installation with the previous name does not exist).  In this case, even reinstalling the included Maxima, with

 `./sage -f spkg/standard/maxima-5.20.1.p0.spkg`

triggers the behavior.  Paul, did you happen to move or rename your Sage root directory?  Does  Burcin's p1 package install successfully and fix the roots problem with a Sage that has not been moved?


---

Comment by mpatel created at 2010-09-30 23:32:50

Nils, do you have any thoughts about the problem in [comment:7 comment 7ff]?


---

Comment by zimmerma created at 2010-10-01 06:53:17

> Paul, did you happen to move or rename your Sage root directory?

no, I did all my experiments in /tmp/sage-4.6.alpha1, where I built sage-4.6.alpha1 from source.
I have no `SAGE_ROOT` environment variable.

Paul


---

Comment by zimmerma created at 2010-10-01 06:58:21

Burcin, do you agree that we try Mitesh's solution from comment 10, which avoids installing a new
Maxima spkg? If so, if someone can provide a patch, I will review it.

Paul


---

Comment by mpatel created at 2010-10-01 07:24:03

Replying to [comment:14 zimmerma]:
> Burcin, do you agree that we try Mitesh's solution from comment 10, which avoids installing a new
> Maxima spkg? If so, if someone can provide a patch, I will review it.

Except for `SAGE_LOCAL/bin`, the files under `SAGE_LOCAL` are not under version control.  I was mainly trying to check whether Robert's fix works with an already installed Maxima in Sage.

So far, it seems the build problem is orthogonal to the problem in the description.


---

Comment by zimmerma created at 2010-10-01 07:46:00

> So far, it seems the build problem is orthogonal to the problem in the description. 

agreed, but how can we proceed in practice so that I can review this ticket?

Paul


---

Comment by burcin created at 2010-10-01 15:59:58

apply only this patch -- forget about the package :)


---

Comment by burcin created at 2010-10-01 16:04:37

Changing status from needs_info to needs_review.


---

Attachment

I uploaded an alternate patch, attachment:trac_9538-maxima_kill.take2.patch. This issues the `kill` command Robert Dodier recommended when initializing maxima. There is no need for any changes to the maxima package.


---

Comment by zimmerma created at 2010-10-03 10:31:07

Changing status from needs_review to positive_review.


---

Comment by zimmerma created at 2010-10-03 10:31:07

ok for the last patch, which fixes the problem, and all tests pass (tested with Sage 4.4.4).

Paul

PS: a minor remark, is there a mechanism to update the calculus.py patch once the problem is
fixed upstream?


---

Comment by burcin created at 2010-10-03 10:58:41

Thank you for the review.

Replying to [comment:18 zimmerma]:
> PS: a minor remark, is there a mechanism to update the calculus.py patch once the problem is
> fixed upstream?

If it is fixed upstream, this doctest should fail:


```
sage: maxima = Maxima(init_code = ['load(simplify_sum)']) 
sage: maxima('f1') 
binomial(n,k) 
```


Then we can remove the line with the `kill` command.


---

Comment by zimmerma created at 2010-10-03 11:42:10

> If it is fixed upstream, this doctest should fail: [...]

excellent!

Paul


---

Comment by mpatel created at 2010-10-04 02:48:22

Resolution: fixed


---

Comment by vbraun created at 2010-10-29 15:08:32

For the record, this fails with maxima-5.22.1:

```
File "/home/vbraun/opt/sage-4.6.rc0/devel/sage-main/sage/calculus/calculus.py", line 368:
    sage: maxima('f1')
Expected:
    binomial(n,k)
Got:
    f1
```

None of the patches from `maxima_package.patch` are in the updated maxima-5.22.1 package. See #10187 for the updated spgk. I take it that this is the expected behaviour and no further patches to maxima are necessary.
