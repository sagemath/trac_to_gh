# Issue 2621: parallell doctest: concurrency problem when creating .doctest directories

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-03-20 23:36:40

Assignee: gfurnish

When parallel doctesting a clean, i.e. never before doctested, tree there are concurrency issues when creating the .doctest directory:

```
Traceback (most recent call last):
  File "/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/bin/sage-doctest", line 427, in <module>
    test_file(argv[1])
  File "/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/bin/sage-doctest", line 321, in test_file
    os.makedirs(".doctest")
  File "/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/os.py", line 172, in makedirs
    mkdir(name, mode)
OSError: [Errno 17] File exists: '.doctest'
```

The above is just a scary message and doesn't affect the operation of the doctests. Creating all the .doctest directories before starting to run the doctests would fix the problem.

Cheers,

Michael


---

Comment by gfurnish created at 2008-03-20 23:41:00

Changing status from new to assigned.


---

Attachment


---

Comment by mabshoff created at 2008-03-21 00:04:23

Patch looks good to me. Positive review ;)

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-21 00:05:18

Resolution: fixed


---

Comment by mabshoff created at 2008-03-21 00:05:18

Merged in Sage 2.11.alpha1
