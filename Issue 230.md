# Issue 230: Notebook "load" or "attach" does not work

Issue created by migration from https://trac.sagemath.org/ticket/230

Original creator: nbruin

Original creation time: 2007-01-29 19:12:08

Assignee: boothby

If in a notebook I use:

```
%sh
cat > hello.spyx << EOF
def hello(name):
    """
    Print hello with the given name.
    """
    print("Hello %s"%name)
EOF
```

and then

```
load "hello.spyx"
```

the notebook hangs. In the server log I get:

```
  ...
  File "/usr/local/sage/default/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py", line 957, in _load_file
    t = self.do_sage_extensions_preparsing(t,
UnboundLocalError: local variable 't' referenced before assignment
```

This is not due to the file not being found: If I try to load or attach a non-existent file, I get an appropriate error message.


---

Comment by was created at 2007-08-16 05:19:38

Now, instead of an error, one gets a not implemented error.  I've changed this from
defect to feature request. 

Note the correct input should be:


```
%sh
cd
cat > hello.spyx << EOF
def hello(name):
    """
    Print hello with the given name.
    """
    print("Hello %s"%name)
EOF
```


```
load "hello.spyx"
```



---

Comment by was created at 2007-08-16 05:19:38

Changing type from defect to enhancement.


---

Comment by mabshoff created at 2007-08-21 12:04:11

I can reproduce the problem, but the error message has changed:

```
load "hello.spyx"
Error loading /tmp/Work2/sage-2.8.1/sage-2.8.1/hello.spyx -- file not
found
```


The spyx file can actually be found in $SAGE_ROOT/data/extcode/sage/hello.spyx

This bug also seems to be duplicate of #236.

Cheers,

Michael


---

Comment by was created at 2007-09-06 22:56:51

Resolution: wontfix
