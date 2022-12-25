# Issue 1042: reset() doesn't do what's claimed -- in particular the symbolic x is gone after doing reset() but shouldn't be

archive/issues_001042.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe reset command is supposed to reset all variables etc., back to their defaults.  This is currently slightly broken, since the symbolic x doesn't get reset:\n\n```\nsage: reset()\nsage: x\nTraceback (most recent call last):\n...\nNameError: name 'x' is not defined\nsage: factor(90823048)\n2^3 * 11352881\n```\n\n\nI seem to recall implementing the symbolic being imported slightly differently, which is surely responsible for this bug. \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1042\n\n",
    "created_at": "2007-10-31T20:52:56Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.12",
    "title": "reset() doesn't do what's claimed -- in particular the symbolic x is gone after doing reset() but shouldn't be",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1042",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

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



Issue created by migration from https://trac.sagemath.org/ticket/1042





---

archive/issue_comments_006328.json:
```json
{
    "body": "In reset.pyx, \n\n```\n    \"\"\"\n    G = globals()  # this is the reason the code must be in SageX.\n    if not G.has_key('sage_mode'):\n        import sage.all\n        D = sage.all.__dict__\n    else:\n        mode = G['sage_mode']\n        if mode == 'cmdline':\n            import sage.all_cmdline\n            D = sage.all_cmdline.__dict__            \n        elif mode == 'notebook':\n            import sage.all_notebook\n            D = sage.all_notebook.__dict__            \n        else:\n            import sage.all\n            D = sage.all.__dict__     \n```\n\nG never the key 'sage_mode' so none of the custom imports in all_cmdline and all_notebook will make it in after reset().  This is where 'x' is imported.  Here is what 'print G' gives:\n\n\n```\n{'__nonzero__': <function __nonzero__ at 0x2b4a6a257b90>, '_iii': '', \n'__': '', '_i': '',\n '_i1': u'reset()\\n',\n '__IP': <IPython.iplib.InteractiveShell object at 0x2b4a6aa0e790>,\n '_ii': '', '__builtins__': <module '__builtin__' (built-in)>,\n '___': '', \n'_ih': ['\\n', u'reset()\\n'], \n'__file__': '/opt/sage/local/lib/python2.5/site-packages/IPython/FakeModule.pyc', \n'_dh': ['/opt/sage/local/bin'], '__name__': '__main__', '_': None, '_oh': {}}\n```\n",
    "created_at": "2007-11-03T20:39:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1042",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1042#issuecomment-6328",
    "user": "https://github.com/mwhansen"
}
```

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
'__': '', '_i': '',
 '_i1': u'reset()\n',
 '__IP': <IPython.iplib.InteractiveShell object at 0x2b4a6aa0e790>,
 '_ii': '', '__builtins__': <module '__builtin__' (built-in)>,
 '___': '', 
'_ih': ['\n', u'reset()\n'], 
'__file__': '/opt/sage/local/lib/python2.5/site-packages/IPython/FakeModule.pyc', 
'_dh': ['/opt/sage/local/bin'], '__name__': '__main__', '_': None, '_oh': {}}
```




---

archive/issue_comments_006329.json:
```json
{
    "body": "Attachment [trac1042.patch](tarball://root/attachments/some-uuid/ticket1042/trac1042.patch) by @williamstein created at 2007-11-03 21:02:18\n\nfixed by Mike Hansen and I.",
    "created_at": "2007-11-03T21:02:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1042",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1042#issuecomment-6329",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac1042.patch](tarball://root/attachments/some-uuid/ticket1042/trac1042.patch) by @williamstein created at 2007-11-03 21:02:18

fixed by Mike Hansen and I.



---

archive/issue_comments_006330.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-03T21:07:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1042",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1042#issuecomment-6330",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_001167.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-11-03T21:07:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1042",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1042#event-1167"
}
```
