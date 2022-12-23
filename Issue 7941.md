# Issue 7941: sage -tp N should store times when some files fail

Issue created by migration from https://trac.sagemath.org/ticket/7941

Original creator: rlm

Original creation time: 2010-01-16 03:21:55

Assignee: AlexGhitza

line 364 of `$SAGE_LOCAL/bin/sage-ptest` is where to start looking:

```
    if len(failed) == 0:
        if interrupt == False:
            print "All tests passed!"
        else:
            print "Keyboard Interrupt: All tests that ran passed."
        #Only update timings if we are doing something standard
        if opts=="-long" or len(opts)==0:
            with open(time_file_name,"w") as time_file:
                pickle.dump(time_dict, time_file)
                print "Timings have been updated."
    else:
        if interrupt:
            print "Keyboard Interrupt, not all tests ran"
        print "\nThe following tests failed:\n"
        for i in range(len(failed)):
               print "\t", failed[i]
        print "-"*int(70)
```


The reason I want this is that if you're making lots of changes and testing frequently, and you never get a completely clean run, all the good files still run in a random order, which is inefficient.


---

Comment by AlexGhitza created at 2010-01-17 22:23:52

Changing assignee from AlexGhitza to tbd.


---

Comment by AlexGhitza created at 2010-01-17 22:23:52

Changing component from algebra to doctest.


---

Comment by rlm created at 2010-01-18 18:39:52

Changing status from new to needs_review.


---

Attachment

apply to scripts repo


---

Comment by rbeezer created at 2010-01-19 04:15:15

Changing status from needs_review to positive_review.


---

Comment by rbeezer created at 2010-01-19 04:15:15

Works as expected.  Removed timings, introduced a doctest that would fail.

Ran `sage  -tp 2  -long devel/sage/sage/graphs/`

twice, and repeated experiment without -long argument.

In both cases, second run obviously employed timings.

Positive review.


---

Comment by rlm created at 2010-01-19 04:28:30

Resolution: fixed
