# Issue 3633: [witch patch, needs review] use commands.getoutput in hostinfo

Issue created by migration from Trac.

Original creator: yi

Original creation time: 2008-07-10 16:55:53

Assignee: rlm

For some reason twisted trial is not too happy with using os.popen. Switching to commands.getouput to fetch system information on the mac seems to work better.




---

Attachment

Robert: commands.getoutput gets the output of a command. This is a little bit better than doing os.popen (what I was doing before) since it actually correctly opens/closes the pipes. 


```
Definition:	commands.getstatusoutput(cmd)
Source:
def getstatusoutput(cmd):
    """Return (status, output) of executing cmd in a shell."""
    import os
    pipe = os.popen('{ ' + cmd + '; } 2>&1', 'r')
    text = pipe.read()
    sts = pipe.close()
    if sts is None: sts = 0
    if text[-1:] == '\n': text = text[:-1]
    return sts, text
```



---

Comment by rlm created at 2008-07-10 17:07:19

+1


---

Comment by rlm created at 2008-08-10 03:44:27

Changing assignee from rlm to yi.


---

Comment by mabshoff created at 2008-08-10 04:57:17

This is doctested indirectly, so I am not concerned here about the doctest. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-10 05:13:20

Merged in Sage 3.1.alpha1


---

Comment by mabshoff created at 2008-08-10 05:13:20

Resolution: fixed
