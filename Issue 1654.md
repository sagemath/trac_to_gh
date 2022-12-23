# Issue 1654: [easy -- no patch required] excise pysqlite

Issue created by migration from https://trac.sagemath.org/ticket/1654

Original creator: was

Original creation time: 2008-01-02 07:32:09

Assignee: mabshoff


```
Francois wrote:
> I was looking at the deps file and stumble across this:
> 
> $(INST)/$(PYSQLITE): $(INST)/$(PYTHON) $(INST)/$(SQLITE)
>         $(SAGE_SPKG) $(SQLITE) 2>&1
> 
> Given that there is a pysqlite spkg I assume that must be a mistake.

pysqlite is included in Python 2.5.1.  For a long time we shipped and built
pysqlite since it wasn't part of Python, but now that it is we don't need to.

The pysqlite package should be removed from sage-2.9.2 if it hasn't
already been removed, and we might as well delete the above line from deps.

 -- William
```



---

Comment by mabshoff created at 2008-01-03 07:22:29

Resolution: fixed


---

Comment by mabshoff created at 2008-01-03 07:22:29

Fixed in 2.9.2.alpha0
