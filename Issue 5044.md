# Issue 5044: on some systems mwrank dumps core and crashes on exit when run under pexpect

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-01-21 05:59:52

Assignee: cwitty

A workaround is to add


```
def quit(self, verbose=False):
    if self._expect is None: return
    os.kill(self._expect.pid, 9)
    self._expect = None
```

as the last method to interfaces/mwrank.py to override the builtin quit method.


---

Attachment


---

Comment by mabshoff created at 2009-01-28 13:07:52

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-28 13:07:52

Changing priority from major to critical.


---

Comment by mabshoff created at 2009-01-28 13:48:52

Merged in Sage 3.3.alpha3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-28 13:48:52

Resolution: fixed
