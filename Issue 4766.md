# Issue 4766: parallel? is lame and incomplete

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-12-12 04:16:06

Assignee: cwitty

CC:  mvngu


```
20:11 < wstein> I just noticed that the doctesting for parallel? is very confusing.
20:11 < wstein> It has no examples, and doesn't even seem right.
20:12 < wstein> The examples are in the __init__ method.
20:12 < wstein> Moreover, the docstring doesn't document that one can give an integer
20:12 < wstein> as input, which defaults to pyprocessing with that many cores.
```



---

Comment by was created at 2008-12-12 04:17:49

Further comment.  On the command line, IPython outputs the docstring for the class *and* the __init__ method, but in the notebook the output is *only* the class docstring.  Thus maybe the problem is partly in how the notebook shows docstrings.

```
In IPython.
        Create paralleled functions.
    
        INPUT:
            p_iter -- parallel iterator function or string:
                      'multiprocessing' -- use multiprocessing (aka pyprocessing)
                      'reference'       -- use a fake serial reference
                                           implementation
                      DSage instance    -- use dsage
        

Constructor information:
Definition:     parallel(self, p_iter='multiprocessing')
Docstring:
    
            Create a parallel iterator decorator object.
    
            EXAMPLES:
                sage: `@`parallel()
                ... def f(N): return N^2
                sage: v = list(f([1,2,4])); v.sort(); v
                [(((1,), {}), 1), (((2,), {}), 4), (((4,), {}), 16)]
                sage: `@`parallel('reference')
                ... def f(N): return N^2
```



---

Comment by AlexGhitza created at 2009-01-23 02:47:57

Changing type from defect to enhancement.


---

Comment by mpatel created at 2010-02-01 08:48:31

I get the same, complete information from `parallel?` in the notebook and at the command-line.  I suggest closing this ticket as fixed.


---

Comment by mvngu created at 2010-02-01 09:00:04

Resolution: fixed


---

Comment by mvngu created at 2010-02-01 09:00:04

Using the command line interface or notebook of Sage 4.3.2.alpha1, "parallel?" returns the same docstring.
