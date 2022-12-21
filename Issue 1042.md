# Issue 1042: reset() doesn't do what's claimed -- in particular the symbolic x is gone after doing reset() but shouldn't be

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-10-31 20:52:56

Assignee: was

The reset command is supposed to reset all variables etc., back to their defaults.  This is currently slightly broken, since the symbolic x doesn't get reset:

```
sage: reset()
sage: x
Traceback (most recent call last):
...
NameError: name 'x' is not defined
sage: factor(90823048)
2^3 * 11352881
```


I seem to recall implementing the symbolic being imported slightly differently, which is surely responsible for this bug. 




---

Comment by mhansen created at 2007-11-03 20:39:55

In reset.pyx, 

```
    """
    G = globals()  # this is the reason the code must be in SageX.
    if not G.has_key('sage_mode'):
        import sage.all
        D = sage.all.__dict__
    else:
        mode = G['sage_mode']
        if mode == 'cmdline':
            import sage.all_cmdline
            D = sage.all_cmdline.__dict__            
        elif mode == 'notebook':
            import sage.all_notebook
            D = sage.all_notebook.__dict__            
        else:
            import sage.all
            D = sage.all.__dict__     
```

G never the key 'sage_mode' so none of the custom imports in all_cmdline and all_notebook will make it in after reset().  This is where 'x' is imported.  Here is what 'print G' gives:


```
{'__nonzero__': <function __nonzero__ at 0x2b4a6a257b90>, '_iii': '', 
'__': _, '_i': _,
 '_i1': u'reset()\n',
 '__IP': <IPython.iplib.InteractiveShell object at 0x2b4a6aa0e790>,
 '_ii': '', '__builtins__': <module '__builtin__' (built-in)>,
 '___': '', 
'_ih': ['\n', u'reset()\n'], 
'__file__': '/opt/sage/local/lib/python2.5/site-packages/IPython/FakeModule.pyc', 
'_dh': ['/opt/sage/local/bin'], '__name__': '__main__', '_': None, '_oh': {}}
```



---

Attachment

fixed by Mike Hansen and I.


---

Comment by was created at 2007-11-03 21:07:26

Resolution: fixed
