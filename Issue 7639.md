# Issue 7639: notebook -- change "address" option to "interface" in notebook(...) command

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-12-09 14:46:48

Assignee: was

Address refers to a network interface. So perhaps we can change address to interface, but continue accepting address for backwards compatibility? Something like this in the docstring:

```
            - ``interface``       -- (default: 'localhost'), address of network
              interface to listen on; give '' to listen on all interfaces. You may 
              use ``address`` here for backwards compatibility, but this is deprecated
              and will be removed in the future.
```



---

Attachment


---

Comment by was created at 2009-12-09 15:12:51

Changing status from new to needs_review.


---

Comment by ddrake created at 2009-12-10 02:35:28

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2009-12-10 02:35:28

Works as advertised. Positive review here.


---

Comment by was created at 2010-01-04 06:53:41

Merged into sagenb-0.4.8.


---

Comment by was created at 2010-01-04 06:53:41

Resolution: fixed
