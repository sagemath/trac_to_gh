# Issue 8434: sage -g uses user's PYTHONPATH

Issue created by migration from https://trac.sagemath.org/ticket/8434

Original creator: PolyBoRi

Original creation time: 2010-03-04 09:32:46

Assignee: GeorgSWeber

CC:  alexanderdreyer

Hi alltogether,
I currently work with the sage-4.3.3-linux-64bit-opensuse_11.1_x86_64-x86_64-Linux.tar.gz binary from sagemath.org on SuSE 11.1/x86_64.

```
./sage
./sage -b
```

installs stuff the users PYTHONPATH, not in the corresponding path of sage.

For instance, see:

```
byte-compiling /u/d/dreyer/.local//lib/python2.6/site-packages/sage/ext/gen_interpreters.py to gen_interpreters.pyc
running install_egg_info
Writing /u/d/dreyer/.local//lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info
```


I think, sage should overwrite PYTHONPATH in its own environment, doesn't it?

Regards,
  Alexander Dreyer


---

Comment by AlexanderDreyer created at 2010-08-19 06:50:10

Hello, I think this is just the same as #9536. Its fix should cures this problem.

Regards,

    Alexander


---

Comment by aapitzsch created at 2014-03-05 23:17:54

`./sage -b` uses the right path here.


---

Comment by aapitzsch created at 2014-03-05 23:17:54

Changing status from new to needs_review.


---

Comment by rws created at 2014-03-24 16:46:17

* `src/bin/sage-env:371...` changes `PYTHONPATH` and `PYTHONHOME` if it has found its own python, so the original `PYTHONPATH` gets used if there is no Sage python, which seems reasonable
* `src/bin/sage-spkg:161...` does some sanitizing *after sourcing the env, if I'm not mistaken

No additional appearance of `PYTHONPATH` in `src/`. Let's assume that the env is always sourced, so the ticket seems invalid to me.


---

Comment by rws created at 2014-03-24 16:46:17

Changing status from needs_review to positive_review.


---

Comment by AlexanderDreyer created at 2014-03-25 11:16:56

This was long, long time ago (perhaps even in a galaxy far, far away ...). So I assume the issue was just fixed meanwhile by incidence the. So feel free to close this now.


---

Comment by vbraun created at 2014-03-31 12:30:25

Resolution: fixed
