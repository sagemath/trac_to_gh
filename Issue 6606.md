# Issue 6606: [with patch; needs review] Add a more efficient implementation of index for Gamma(N).

Issue created by migration from Trac.

Original creator: simon

Original creation time: 2009-07-23 21:13:12

Assignee: craigcitro

CC:  roed

Gamma(N).index used the default implementation which was slow. Attached is a new implementation which works for the specific subgroup.


---

Attachment


---

Comment by cremona created at 2009-07-24 20:59:15

The code loooked (though I would have written p**(3*e-2)*(p*p-1) ) but after applying to 4.1:

```
sage: Gamma(19).index()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/home/john/.sage/temp/ubuntu/25083/_home_john__sage_init_sage_0.py in <module>()

/home/john/sage-4.1/local/lib/python2.6/site-packages/sage/modular/arithgroup/congroup_gamma.pyc in index(self)
    105             32893086819240
    106         """
--> 107         return prod([p**(3*e) - p**(3*e-2) for (p,e) in self.level().factor()])
    108 
```


Looks like someone forgot to run sage -t before submitting the patch...


---

Attachment


---

Comment by roed created at 2009-07-24 21:22:01

I ran sage -t after applying the patch, and all tests pass.  Looks good to me.


---

Comment by cremona created at 2009-07-24 21:52:07

That's better!


---

Comment by mvngu created at 2009-07-24 22:54:07

Simon: The patch `gamma.2.patch` doesn't contain your username. I've committed it in your name.


---

Comment by mvngu created at 2009-07-24 22:54:07

Resolution: fixed
