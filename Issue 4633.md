# Issue 4633: fix additional "Fortran-style" names and a coercion

Issue created by migration from Trac.

Original creator: bpage

Original creation time: 2008-11-27 01:42:53

Assignee: was

Keywords: axiom

In order to run the the comparison of integration results between FriCAS and Maxima, it is also necessary to make some simple additions to the 'axiom.py' interface:


```
wspage`@`debian:~/sage-3.1.4/devel/sage-main/sage/interfaces$ hg diff
diff -r ed3f78f99d2a sage/interfaces/axiom.py
--- a/sage/interfaces/axiom.py  Tue Nov 25 23:45:43 2008 -0500
+++ b/sage/interfaces/axiom.py  Wed Nov 26 19:43:59 2008 -0500
`@``@` -729,7 +729,10 `@``@`
        s = P.eval('unparse(%s::InputForm)'%self._name)
        if 'translation error' in s or 'Cannot convert' in s:
            raise NotImplementedError
-        s = multiple_replace({'\r\n':'', # fix stupid Fortran-ish
+        s = multiple_replace({'\r\n':'', # fix stupid Fortran-ish
+                              'DLOG(':'log(',
+                              'DEXP(':'exp(',
+                              '::(':_, ',Symbol)':_,
                              'DSIN(':'sin(',
                              'DCOS(':'cos(',
                              'DTAN(':'tan(',

```


----

Integration produce some additional "Fortran-style" names and a
coercion that have to be translated before the input form can be
processed by Sage.

With this change we can do:


```
  test_int = integrand.integrate(x)
  fricas_int = axiom.integrate(integrand,x).sage()
  fricas_cmp = (test_int.simplify_full()-fricas_int.simplify_full()).simplify_full()
  if (fricas_cmp == 0):
      print "FriCAS agrees with Maxima."

```




---

Comment by mabshoff created at 2008-11-27 01:44:05

Hi Bill,

please attach a proper hg patch. 

Cheers,

Michael


---

Attachment

patch file


---

Comment by bpage created at 2008-11-27 01:48:00

Sorry. What is a "hg patch"?


---

Comment by mabshoff created at 2008-11-27 01:49:25

Replying to [comment:2 bpage]:
> Sorry. What is a "hg patch"?

A mercurial patch. hg is the chemical symbol for mercurial, so that is why the mercurial binary is called hg. 

Cheers,

Michael


---

Comment by bpage created at 2008-11-27 01:50:28

Further note: The new release of FriCAS-1.0.4 which is not yet available as a Sage spkg no longer produces this "Fortranish" functions names.


---

Comment by bpage created at 2008-11-27 01:52:58

> A mercurial patch. hg is the chemical symbol for mercurial, so that is why the mercurial binary is called hg. 

:~) I meant, how do I create a "hg patch" if not by "hg diff"?


---

Comment by mabshoff created at 2008-11-27 02:01:53

Hi Bill,

 * Check in your changes: hg commit
 * export the last commit: hg export tip > trac_4633.patch
 * attach patch to this ticket
 * prepend "[with patch, needs review] to summary line
 * wait for review 

Cheers,

Michael


---

Attachment

[with patch, needs review] Better?


---

Comment by tjlahey created at 2008-11-30 21:42:53

Is there a specific procedure for installing (and testing) these kinds of patches? That is, how do I get Sage to know that the code has been updated? This kind of thing would be nice on a wiki page for new developers. Or have I just missed it?


---

Comment by bpage created at 2008-12-01 03:54:05

Replying to [comment:7 tjlahey]:
> Is there a specific procedure for installing (and testing) these kinds of patches? That is, how do I get Sage to know that the code has been updated? This kind of thing would be nice on a wiki page for new developers. Or have I just missed it?

This is what I do:

 0. Pretest, e.g. try: axiom(1/log(x)).sage()

```
    NotImplementedError
```

 1. Click on the link to that patch: "trac_4633.patch"
 2. Click on the link to "original format"
 3. Save the patch file somewhere, e.g. ~/trac_4633.patch
 4. cd sage*/devel/sage-main
 5. apply the patch: patch -p1 < ~/trac_4633.patch
 6. re-build sage: sage -br
 7. test, e.g. try: axiom(1/log(x)).sage()

```
    1/log(x)
```


I guess that in a more complete patch I should have added some tests like this to the doc tests. This just seemed too simple.


---

Comment by tjlahey created at 2008-12-02 23:23:04

Replying to [comment:8 bpage]:

It doesn't want to apply. In my version of sage/interfaces/axiom.py, I don't have:

```
         s = P.eval('unparse(%s::InputForm)'%self._name) 
         if 'translation error' in s or 'Cannot convert' in s: 
             raise NotImplementedError
```

so I get a rejection when I attempt to apply the patch. I'm using Sage 3.2.


---

Comment by mabshoff created at 2008-12-02 23:24:44

This is probably on top of #4036, which itself needs to be slightly rebased.

Cheers,

Michael


---

Comment by bpage created at 2008-12-03 00:20:09

Replying to [comment:10 mabshoff]:
> This is probably on top of #4036, which itself needs to be slightly rebased.

Correct. What is the proper procedure to follow in this case?


---

Comment by mabshoff created at 2008-12-03 00:23:15

Hi Bill,

Just mention it on the ticket and/or change the summary line like I just did.

Cheers,

Michael


---

Comment by was created at 2008-12-06 22:15:03

Please add a doctest that illustrates what you're fixing and mark it "#optional - fricas".    The doctest could also include your integration example.

Thanks!!


---

Comment by chapoton created at 2014-07-19 12:31:28

According to http://trac.sagemath.org/ticket/4633#comment:4, this is no longer needed in recent versions of FriCAS. Sage is now using FriCAS 1.0.9 (#9354).

So maybe this can be closed ?


---

Comment by chapoton created at 2014-07-19 12:31:28

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2014-10-16 11:23:11

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-10-27 16:26:00

Resolution: fixed
