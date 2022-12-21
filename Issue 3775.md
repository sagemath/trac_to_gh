# Issue 3775: sage -maxima broken on OSX

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-08-05 17:29:39

Assignee: mabshoff


```
However, this is what happens when I invoke maxima, from the sage
directory:

$ /Applications/sage/local/bin/maxima
dyld: Library not loaded: /Users/was/build/sage-3.0.5/local/lib/
libreadline.5.2.dylib
  Referenced from: /Applications/sage/local/lib/maxima/5.13.0/binary-
clisp/lisp.run
  Reason: image not found
Trace/BPT trap 
```

The solution is to source local/bin/sage-env before starting Maxima.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-05 17:35:24

Arrg, invalid. The above happened when invoking Maxima directly, so this is not a bug on our end.


---

Comment by mabshoff created at 2008-08-05 17:35:24

Resolution: invalid
