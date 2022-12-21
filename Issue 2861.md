# Issue 2861: scripts do not exit with correct exit code when sys.exit() is used

Issue created by migration from Trac.

Original creator: ddrake

Original creation time: 2008-04-09 06:42:30

Assignee: was

If I call `sys.exit()` from a Sage script, the script exits but not with the correct exit code. For example, the script

```
import sys

print 'exiting!'
sys.exit(1)
```

exits with exit code 0 when run from Sage:

```
$ sage exitcode.sage 
exiting!
1
$ echo $?
0
```

(the 1 gets printed because the preparser turns it into a Sage integer, and Python prints out anything except Python integers.) But the same script works properly when run from Python:

```
$ python exitcode.sage
exiting!
$ echo $?
1
```

I don't know if this is Sage or IPython behavior, but having this work would be really useful.



---

Attachment


---

Comment by rlm created at 2009-01-24 15:21:11

+1

was showed me this patch working in all the permutations of inputs... Looks good to me.


---

Comment by mabshoff created at 2009-01-24 22:47:59

Resolution: fixed


---

Comment by mabshoff created at 2009-01-24 22:47:59

Merged in Sage 3.3.alpha2


---

Comment by ddrake created at 2009-04-21 01:48:15

I was going to reopen this ticket, but instead I'll leave this comment as warning to anyone else trying to use this:

If you do `sys.exit(0)` in a Sage script, because of preparsing, you effectively get `sys.exit(Integer(0))`, which results in the script exiting with code 1! This is not what anyone would expect! This is because of [how sys.exit works](http://docs.python.org/library/sys.html#sys.exit) when given non-Python-integer arguments. To make sure that you get the desired behavior, use `int` inside the call to get a Python integer: `sys.exit(int(2))` or whatever.
