# Issue 7486: implement automatic definition of undefined variables in the Sage command line (ipython)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-11-18 09:30:43

Assignee: was

CC:  olazo

See #7482, which is about doing this in the notebook.  For the command line, see the remarks below by the author of IPython.


---

Comment by was created at 2009-11-18 09:31:01

From Fernando Perez:


```
Actually no, not that hard: ipython executes all  user  code inside a
dict created at initialization time.  One could replace this (today a
plain python dict) with another dict that would implement the
requested behavior.  This would spring variables into existence when a
KeyError was about to occur.

The command-line doesn't have the notion of a cell (yet, that will
hopefully change soon) but it could be toggled with a function call.

It's basically a matter of instantiating the initial ipython with a
custom user_ns dict that does the above, that should be all.  And
providing a magic (or even plain) function in the global namespace to
toggle this behavior on/off at runtime.

The attached file (run it as 'ipauto.py') shows how it could work, I
didn't implement the toggling and it's a quick hack, but the basic
idea is  there.  Here it is in action:

In [1]: %autocall 0
Automatic calling is: OFF

In [2]: x+y
Injecting x
Injecting y
Out[2]: x + y

In [3]: type(x)
Out[3]: <class 'sympy.core.symbol.Symbol'>

In [4]: x+3
Out[4]: 3 + x

In [5]: x**2+x*x
Out[5]: 2*x**2

In [6]: x+z**3
Injecting z
Out[6]: x + z**3


A couple of notes:

- It's key to disable autocalling for this to work, otherwise too many
false positives are triggered.  If this idea proves to have  wings, it
will be one more argument in favor of disabling autocalling (it just
has too many uncontrollable side effects).

- Unfortunately IPython as shipped needs a tiny patch for this to
work, due to a really silly omission.  The patch is a trivial 2-liner,
in case anyone wants to take this further for Sage:

(ipython-0.10)maqroll[0.10]> bzr diff
### modified file 'IPython/Shell.py'
--- IPython/Shell.py    2009-04-14 20:12:02 +0000
+++ IPython/Shell.py    2009-11-18 09:03:01 +0000
`@``@` -1230,7 +1230,7 `@``@`


 # This is the one which should be called by external code.
-def start(user_ns = None):
+def start(user_ns = None, user_global_ns = None):
    """Return a running shell instance, dealing with threading options.

    This is a factory function which will instantiate the proper IPython shell
`@``@` -1238,7 +1238,7 `@``@`
    different GUI toolkits require different thread handling details."""

    shell = _select_shell(sys.argv)
-    return shell(user_ns = user_ns)
+    return shell(user_ns = user_ns, user_global_ns = user_global_ns)

 # Some aliases for backwards compatibility
 IPythonShell = IPShell



Cheers,

f
```



---

Attachment


---

Comment by was created at 2012-03-20 20:05:27

Changing type from defect to enhancement.
