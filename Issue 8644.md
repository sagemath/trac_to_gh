# Issue 8644: update pynac to 0.1.12

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2010-04-02 14:47:11

Assignee: tbd

I released a new pynac version after applying a few upstream patches from `GiNaC`, the most important being a fix for #8565.

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.12.spkg

Since these are minor changes, I don't expect any build problems. I've tested the package on 
 * an up-to-date 64-bit Gentoo system (my laptop) with 

```
gcc (Gentoo 4.3.4 p1.0, pie-10.1.5) 4.3.4
```

 * 32-bit Debian GNU/Linux 5.0.4 (lenny)

```
gcc (Debian 4.3.2-1.1) 4.3.2
```



---

Comment by burcin created at 2010-04-02 14:47:22

Changing status from new to needs_review.


---

Comment by robert.marik created at 2010-04-09 11:10:37

Installs fine, all tests passed, works ad advertised, solves #8565. Positive review and thanks for fixing.


---

Comment by robert.marik created at 2010-04-09 11:10:37

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-04-27 06:53:41

Looks good to me too.  There is a new spkg at 

http://sage.math.washington.edu/home/mhansen/pynac-0.1.12.spkg

which incorporates the fixes at #8753.


---

Comment by was created at 2010-04-28 18:57:26

Resolution: fixed
