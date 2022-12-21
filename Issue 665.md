# Issue 665: notebook() failure under VMware Player

Issue created by migration from Trac.

Original creator: jvoight

Original creation time: 2007-09-16 04:32:43

Assignee: boothby

Can't get notebook() to run on my Windows XP machine under VMware Player.  I downloaded SAGE and VMware Player; at the sage prompt did an upgrade() (to 2.8.4.2, everything seemed to go swimmingly); then tried notebook() and it hangs at:

Generating SSL certificate for server...
Using certtool to generate key
certtool --generate-privkey --outfile /home/sage/.sage/dsage/cacert.pem
Generating a private key...
Generating a 1024 bit RSA private key...

When I Ctrl-C twice, it streams by and the only part of the scrollback I can read is:

    record = _fixed_getinnerframes(etb, context,self.tb_offset)
  File "/usr/local/sage/local/lib/python2.5/site-packages/IPython/ultraTB.py", l
ine 124, in _fixed_getinnerframes
    records  = inspect.getinnerframes(etb, context)
  File "/usr/local/sage/local/lib/python2.5/inspect.py", line 877, in getinnerfr
ames
    framelist.append((tb.tb_frame,) + getframinfo(tb, context))
  File "/usr/local/sage/local/lib/python2.5/inspect.py", line 837, in getframin
fo
    filename = getsourcefile(frame) or getfile(frame)
  File "/usr/local/sage/local/lib/python2.5/inspect.py", line 393, in getsourcef
ile
    if hasattr(getmodule(object, filename), '__loader__'):
  File "/usr/local/sage/local/lib/python2.5/inspect.py", line 436, in getmodule
    os.path.realpath(f)] = module.__name__
  File "/usr/local/sage/local/lib/python2.5/posixpath.py", line 421, in realpath
    if islink(component);
  File "/usr/local/sage/local/lib/python2.5/posixpath.py", line 159, in islink
    st = os.lstat(path)
  File "/usr/local/sage/local/lib/python2.5/site-packages/sage/interfaces/get_si
gs.py", line 8, in my_sigint
    raise KeyboardInterrupt
KeyboardInterrupt

Unfortunately, your original traceback can not be constructed.




---

Comment by was created at 2007-09-21 00:18:18

Changing assignee from boothby to was.


---

Comment by was created at 2007-09-21 00:19:10

Resolution: fixed


---

Comment by was created at 2007-09-21 00:19:10

Start the SAGE console and type

```
  sage: notebook.setup()
```

