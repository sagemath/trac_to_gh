# Issue 5625: group cohomology -- bad error messages; should indicate an optional package is needed

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-03-29 00:36:43

Assignee: joyner

The following fails because I don't have the optional  gap_packages-* package installed:


```
sage: G = PermutationGroup([[(1,2,3),(4,5)],[(3,4)]])
sage: G.cohomology(1,3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/wstein/.sage/sage_notebook/worksheets/admin/59/code/369.py", line 8, in <module>
    G.cohomology(_sage_const_1 ,_sage_const_3 )
  File "/Users/wstein/build/sage-3.4/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/", line 1, in <module>
    
  File "/Users/wstein/build/sage-3.4/local/lib/python2.5/site-packages/sage/groups/perm_gps/permgroup.py", line 1132, in cohomology
    L = eval(gap.eval("GroupCohomology(%s,%s,%s)"%(GG,n,p)))
  File "/Users/wstein/build/sage-3.4/local/lib/python2.5/site-packages/sage/interfaces/gap.py", line 479, in eval
    result = Expect.eval(self, input_line, **kwds)
  File "/Users/wstein/build/sage-3.4/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 974, in eval
    return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
  File "/Users/wstein/build/sage-3.4/local/lib/python2.5/site-packages/sage/interfaces/gap.py", line 723, in _eval_line
    raise RuntimeError, message
RuntimeError: Gap produced error output
Variable: 'GroupCohomology' must have a value


   executing GroupCohomology(Group([(3,4), (1,2,3)(4,5)]),1,3);
```


The error message should say that I have to install that package.

Incidentally, installing the package doesn't work right now since Sage ships gap-4.12 (though I guess we're downgrading to 4.10 soon):


```
$ sage -i gap_packages-4.4.10_6
...
boom
mkdir: /Users/wstein/build/sage-3.4/local/lib/gap-4.4.10: No such file or directory
cp: directory /Users/wstein/build/sage-3.4/local/lib/gap-4.4.10/pkg does not exist
Error copying SPKG.txt

real	0m0.078s
user	0m0.007s
sys	0m0.019s
}}} 


---

Comment by jhpalmieri created at 2009-07-22 03:17:06

Here's a patch.  Skimming through the Sage source code, it seems that in other cases we usually raise a RuntimeError when an optional package is needed but not installed, so that's what I've done here.


---

Attachment


---

Comment by wdj created at 2009-07-25 19:08:11

Applies fine and passes sage -testall. A simple patch which does what it claims.


---

Comment by mvngu created at 2009-07-25 20:06:55

reviewer patch; fix typos


---

Attachment

The patch `trac_5625-typo-fixes.patch` fixes a number of typos found in John's patch.


---

Comment by mvngu created at 2009-07-25 20:42:53

Resolution: fixed


---

Comment by mvngu created at 2009-07-25 20:42:53

Merged both patches.
