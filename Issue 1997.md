# Issue 1997: magma interface -- interrupting restarts magma way way too aggressively

archive/issues_001997.json:
```json
{
    "body": "Assignee: @williamstein\n\nFrom the command line\n\n```\nteragon:~ was$ magma\nMagma V2.13-10    Wed Jan 30 2008 23:54:17 on teragon  [Seed = 166664802]\nType ? for help.  Type <Ctrl>-D to quit.\n> j:= 2; for i in [1..10^7] do j +:= i; end for;\n\n[Interrupted]\n> 2+2;\n4\n> \n```\n\n\nHowever, exactly the same always results in a complete restart of Magma:\n\n```\nsage: magma.eval('j:= 2; for i in [1..10^7] do j +:= i; end for;')\n^CInterrupting Magma...\n---------------------------------------------------------------------------\n<type 'exceptions.KeyboardInterrupt'>     Traceback (most recent call last)\n\n/Users/was/<ipython console> in <module>()\n\n/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/magma.py in eval(self, x, strip)\n    276         if len(x) == 0 or x[len(x) - 1] != ';':\n    277             x += ';'\n--> 278         ans = Expect.eval(self, x).replace('\\\\\\n','')\n    279         if 'Runtime error' in ans or 'User error' in ans:\n    280             raise RuntimeError, \"Error evaluation Magma code.\\nIN:%s\\nOUT:%s\"%(x, ans)\n\n/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py in eval(self, code, strip, **kwds)\n    705         try:\n    706             with gc_disabled():\n--> 707                 return '\\n'.join([self._eval_line(L, **kwds) for L in code.split('\\n') if L != ''])\n    708         except KeyboardInterrupt:\n    709             # DO NOT CATCH KeyboardInterrupt, as it is being caught\n\n/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py in _eval_line(self, line, allow_use_file, wait_for_prompt)\n    646                 out = '\\n\\r'\n    647         except KeyboardInterrupt:\n--> 648             self._keyboard_interrupt()\n    649             raise KeyboardInterrupt, \"Ctrl-c pressed while running %s\"%self\n    650         i = out.find(\"\\n\")\n\n/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py in _keyboard_interrupt(self)\n    660                 raise pexcept.ExceptionPexpect( \"THIS IS A BUG -- PLEASE REPORT. This should never happen.\\n\" + msg)\n    661             self._start()\n--> 662             raise KeyboardInterrupt, \"Restarting %s (WARNING: all variables defined in previous session are now invalid)\"%self\n    663         else:\n    664             self._expect.sendline(chr(3))  # send ctrl-c\n\n<type 'exceptions.KeyboardInterrupt'>: Restarting Magma (WARNING: all variables defined in previous session are now invalid)\nsage: magma.eval('j')\n---------------------------------------------------------------------------\n<type 'exceptions.RuntimeError'>          Traceback (most recent call last)\n\n/Users/was/<ipython console> in <module>()\n\n/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/magma.py in eval(self, x, strip)\n    278         ans = Expect.eval(self, x).replace('\\\\\\n','')\n    279         if 'Runtime error' in ans or 'User error' in ans:\n--> 280             raise RuntimeError, \"Error evaluation Magma code.\\nIN:%s\\nOUT:%s\"%(x, ans)\n    281         return ans\n    282 \n\n<type 'exceptions.RuntimeError'>: Error evaluation Magma code.\nIN:j;\nOUT:\n>> j;\n   ^\nUser error: Identifier 'j' has not been declared or assigned\n```\n\n\nThis is ridiculous.  It causes huge trouble for normal users.   Often people spend minutes or hours setting up a magma interface session -- to have it just die any time they hit control-c is ludicrous. \n\n\n```\nsage: m = magma('Factorial(10^7)')\n^CInterrupting Magma...\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/Users/was/<ipython console> in <module>()\n\n/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/magma.py in __call__(self, x, gens)\n    332             if isinstance(x, bool):\n    333                 return Expect.__call__(self, str(x).lower())\n--> 334             return Expect.__call__(self, x)\n    335         return self.objgens(x, gens)\n    336         \n\n/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __call__(self, x)\n    736             return x\n    737         if isinstance(x, basestring):\n--> 738             return cls(self, x)\n    739         try:\n    740             return self._coerce_from_special_method(x)\n\n/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __init__(self, parent, value, is_name)\n    987             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:\n    988                 self._session_number = -1\n--> 989                 raise TypeError, x\n    990         self._session_number = parent._session_number\n    991 \n\n<type 'exceptions.TypeError'>: Restarting Magma (WARNING: all variables defined in previous session are now invalid)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1997\n\n",
    "created_at": "2008-01-31T05:00:02Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "magma interface -- interrupting restarts magma way way too aggressively",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1997",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

From the command line

```
teragon:~ was$ magma
Magma V2.13-10    Wed Jan 30 2008 23:54:17 on teragon  [Seed = 166664802]
Type ? for help.  Type <Ctrl>-D to quit.
> j:= 2; for i in [1..10^7] do j +:= i; end for;

[Interrupted]
> 2+2;
4
> 
```


However, exactly the same always results in a complete restart of Magma:

```
sage: magma.eval('j:= 2; for i in [1..10^7] do j +:= i; end for;')
^CInterrupting Magma...
---------------------------------------------------------------------------
<type 'exceptions.KeyboardInterrupt'>     Traceback (most recent call last)

/Users/was/<ipython console> in <module>()

/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/magma.py in eval(self, x, strip)
    276         if len(x) == 0 or x[len(x) - 1] != ';':
    277             x += ';'
--> 278         ans = Expect.eval(self, x).replace('\\\n','')
    279         if 'Runtime error' in ans or 'User error' in ans:
    280             raise RuntimeError, "Error evaluation Magma code.\nIN:%s\nOUT:%s"%(x, ans)

/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py in eval(self, code, strip, **kwds)
    705         try:
    706             with gc_disabled():
--> 707                 return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
    708         except KeyboardInterrupt:
    709             # DO NOT CATCH KeyboardInterrupt, as it is being caught

/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py in _eval_line(self, line, allow_use_file, wait_for_prompt)
    646                 out = '\n\r'
    647         except KeyboardInterrupt:
--> 648             self._keyboard_interrupt()
    649             raise KeyboardInterrupt, "Ctrl-c pressed while running %s"%self
    650         i = out.find("\n")

/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py in _keyboard_interrupt(self)
    660                 raise pexcept.ExceptionPexpect( "THIS IS A BUG -- PLEASE REPORT. This should never happen.\n" + msg)
    661             self._start()
--> 662             raise KeyboardInterrupt, "Restarting %s (WARNING: all variables defined in previous session are now invalid)"%self
    663         else:
    664             self._expect.sendline(chr(3))  # send ctrl-c

<type 'exceptions.KeyboardInterrupt'>: Restarting Magma (WARNING: all variables defined in previous session are now invalid)
sage: magma.eval('j')
---------------------------------------------------------------------------
<type 'exceptions.RuntimeError'>          Traceback (most recent call last)

/Users/was/<ipython console> in <module>()

/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/magma.py in eval(self, x, strip)
    278         ans = Expect.eval(self, x).replace('\\\n','')
    279         if 'Runtime error' in ans or 'User error' in ans:
--> 280             raise RuntimeError, "Error evaluation Magma code.\nIN:%s\nOUT:%s"%(x, ans)
    281         return ans
    282 

<type 'exceptions.RuntimeError'>: Error evaluation Magma code.
IN:j;
OUT:
>> j;
   ^
User error: Identifier 'j' has not been declared or assigned
```


This is ridiculous.  It causes huge trouble for normal users.   Often people spend minutes or hours setting up a magma interface session -- to have it just die any time they hit control-c is ludicrous. 


```
sage: m = magma('Factorial(10^7)')
^CInterrupting Magma...
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/was/<ipython console> in <module>()

/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/magma.py in __call__(self, x, gens)
    332             if isinstance(x, bool):
    333                 return Expect.__call__(self, str(x).lower())
--> 334             return Expect.__call__(self, x)
    335         return self.objgens(x, gens)
    336         

/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __call__(self, x)
    736             return x
    737         if isinstance(x, basestring):
--> 738             return cls(self, x)
    739         try:
    740             return self._coerce_from_special_method(x)

/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __init__(self, parent, value, is_name)
    987             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:
    988                 self._session_number = -1
--> 989                 raise TypeError, x
    990         self._session_number = parent._session_number
    991 

<type 'exceptions.TypeError'>: Restarting Magma (WARNING: all variables defined in previous session are now invalid)
```


Issue created by migration from https://trac.sagemath.org/ticket/1997





---

archive/issue_comments_012883.json:
```json
{
    "body": "This is completely fixed by changing the restart_on_ctrlc option. see attached 1-line patch.  \n\nIt's not possible to doctest this, but easy to test by hand.",
    "created_at": "2008-10-24T03:40:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1997#issuecomment-12883",
    "user": "https://github.com/williamstein"
}
```

This is completely fixed by changing the restart_on_ctrlc option. see attached 1-line patch.  

It's not possible to doctest this, but easy to test by hand.



---

archive/issue_comments_012884.json:
```json
{
    "body": "Attachment [sage-1997.patch](tarball://root/attachments/some-uuid/ticket1997/sage-1997.patch) by @williamstein created at 2008-10-24 03:57:07\n\nWhen you apply this to 3.2.alpha0 it may complain\n\n```\nHunk #2 FAILED at 951\n1 out of 2 hunks FAILED -- saving rejects to file sage/interfaces/magma.py.rej\n```\n\n\nThis hunk #2 is a blank line, and is totally safe to ignore this failure.",
    "created_at": "2008-10-24T03:57:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1997#issuecomment-12884",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-1997.patch](tarball://root/attachments/some-uuid/ticket1997/sage-1997.patch) by @williamstein created at 2008-10-24 03:57:07

When you apply this to 3.2.alpha0 it may complain

```
Hunk #2 FAILED at 951
1 out of 2 hunks FAILED -- saving rejects to file sage/interfaces/magma.py.rej
```


This hunk #2 is a blank line, and is totally safe to ignore this failure.



---

archive/issue_comments_012885.json:
```json
{
    "body": "Looks good to me. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-24T11:18:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1997#issuecomment-12885",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Looks good to me. Positive review.

Cheers,

Michael



---

archive/issue_comments_012886.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-26T00:08:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1997#issuecomment-12886",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012887.json:
```json
{
    "body": "Merged in Sage 3.2.alpha1",
    "created_at": "2008-10-26T00:08:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1997#issuecomment-12887",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.alpha1



---

archive/issue_events_004825.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-26T00:08:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1997",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1997#event-4825"
}
```
