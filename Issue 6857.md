# Issue 6857: [with patch, needs review] in automorphism_group, orbits=True does not translate vertices back

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2009-09-02 01:00:23

Assignee: rlm

Reported by Chris Godsil


---

Attachment


---

Comment by ncohen created at 2009-09-06 14:23:50

Applies fines, does its job. Positive review !

Not related to this patch, I found out testing things some *really unimportant* error :


```
sage: g.automorphism_group(return_group=False)
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)

/user/ncohen/home/.sage/temp/rebelote.inria.fr/22721/_user_ncohen_home__sage_init_sage_0.py in <module>()

/usr/local/sage/local/lib/python2.6/site-packages/sage/graphs/graph.pyc in automorphism_group(self, partition, translation, verbosity, edge_labels, order, return_group, orbits)
   8462         # A Python switch statement!
   8463         return { 0: None,
-> 8464                  1: output[0],
   8465                  2: tuple(output),
   8466                  3: tuple(output),

IndexError: list index out of range 
```


This comes from the fact that in this configuration of arguments, the function is expected to ... do nothing ;-)

At the end of the function, the code already expects this eventuality and reads :


```
        # A Python switch statement!
        return { 0: None,
                 1: output[0],
                 2: tuple(output),
                 3: tuple(output),
                 4: tuple(output)
               }[len(output)]
```

I knew nothing about such things in Python and I am glad I read it. But the key 0: None does not behave as expected : it behaves as if there was NO key "0" in the dictionary and when len(output) equals 0 there is an error because of that... It can be fixed pretty easily this way :


```
        # A Python switch statement!
        return { 1: output[0],
                 2: tuple(output),
                 3: tuple(output),
                 4: tuple(output)
               }[len(output)] if len(output)>0 else None
```


Could it be possible to include discreetely it in your patch ? It does not seem necessary to create a ticket just for this ;-)

Nathann


---

Comment by mvngu created at 2009-09-07 18:42:48

Resolution: fixed
