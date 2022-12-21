# Issue 9574: Ignore zope-testrunner in the scripts repository

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-07-22 05:10:00

Assignee: jason

In the forthcoming 4.5.2.alpha0, I get

```sh
$ cd sage-4.5.2.alpha0/local/bin
$ hg stat
? zope-testrunner
```

in the scripts repository.

Should we add `zope-testrunner` to `.hgignore`?


---

Comment by ddrake created at 2010-07-22 06:34:45

On OS X, I also see:

```
drake`@`bsd:~/sage-4.5.2.alpha0/local/bin$ hg stat
? gfortran
? gfortran-4.0
? gfortran-4.2
? gfortran-64
? gfortran-uninstall
? i686-apple-darwin8-gfortran-4.2
? powerpc-apple-darwin8-gfortran-4.2
? zope-testrunner
```



---

Comment by ddrake created at 2010-07-23 03:13:23

add files to .hgignore for scripts repo


---

Comment by ddrake created at 2010-07-23 03:13:55

Changing status from new to needs_review.


---

Attachment

I've attached a patch that adds all the above files to the .hgignore file.


---

Comment by mpatel created at 2010-07-23 07:31:36

This works for me on {bsd,sage}.math.


---

Comment by mpatel created at 2010-07-23 07:31:36

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2010-07-26 01:18:22

Resolution: fixed
