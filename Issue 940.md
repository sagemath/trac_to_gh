# Issue 940: read large output from octave (and probably matlab) takes *forever*

archive/issues_000940.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\n    sage: t = '\"%s\"'%10^10000   # ten thousand character string.\n    sage: a = octave(t)\n```\n\nIf you now try to print a, it take forever.\n\nIssue created by migration from https://trac.sagemath.org/ticket/940\n\n",
    "created_at": "2007-10-20T08:27:01Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.5",
    "title": "read large output from octave (and probably matlab) takes *forever*",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/940",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
    sage: t = '"%s"'%10^10000   # ten thousand character string.
    sage: a = octave(t)
```

If you now try to print a, it take forever.

Issue created by migration from https://trac.sagemath.org/ticket/940





---

archive/issue_comments_005731.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2008-08-31T06:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/940#issuecomment-5731",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_005732.json:
```json
{
    "body": "I started with\n\n```\nsage: t = '\"%s\"'%10^10000   # ten thousand character string.\nsage: a = octave(t)\n```\n\nwhich took little time.\n\nThen, I did\n\n```\nsage: s = repr(a)\n```\n\nwhich I had to interrupt.\n\nPressing Ctrl-c made the message \n\n```\n^CInterrupting Octave...\n```\n\nappear on screen, but nothing more happened. Then, I pressed Ctrl-c again, and finally the traceback was shown:\n\n```\n^CERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (80, 0))\n\n---------------------------------------------------------------------------\nKeyboardInterrupt                         Traceback (most recent call last)\n\n/home/king/<ipython console> in <module>()\n\n/mnt/local/king/SAGE/broken/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __repr__(self)\n   1738         try:\n   1739             if self._get_using_file:\n-> 1740                 s = self.parent().get_using_file(self._name)\n   1741         except AttributeError:\n   1742             s = self.parent().get(self._name)\n\n/mnt/local/king/SAGE/broken/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in get_using_file(self, var)\n   1262            if you're reading it through introspection and seeing this.\n   1263         \"\"\"\n-> 1264         return self.get(var)\n   1265\n   1266     def clear(self, var):\n\n/mnt/local/king/SAGE/broken/local/lib/python2.6/site-packages/sage/interfaces/octave.pyc in get(self, var)\n    311             ' 2'\n    312         \"\"\"\n--> 313         s = self.eval('%s'%var)\n    314         i = s.find('=')\n    315         return s[i+1:]\n\n/mnt/local/king/SAGE/broken/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in eval(self, code, strip, synchronize, locals, **kwds)\n   1048         try:\n   1049             with gc_disabled():\n-> 1050                 return '\\n'.join([self._eval_line(L, **kwds) for L in code.split('\\n') if L != ''])\n   1051         except KeyboardInterrupt:\n   1052             # DO NOT CATCH KeyboardInterrupt, as it is being caught\n\n/mnt/local/king/SAGE/broken/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in _eval_line(self, line, allow_use_file, wait_for_prompt)\n    733                 out = '\\n\\r'\n    734         except KeyboardInterrupt:\n--> 735             self._keyboard_interrupt()\n    736             raise KeyboardInterrupt, \"Ctrl-c pressed while running %s\"%self\n    737         i = out.find(\"\\n\")\n\n/mnt/local/king/SAGE/broken/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in _keyboard_interrupt(self)\n    750         else:\n    751             self._expect.sendline(chr(3))  # send ctrl-c\n--> 752             self._expect.expect(self._prompt)\n    753             self._expect.expect(self._prompt)\n    754             raise KeyboardInterrupt, \"Ctrl-c pressed while running %s\"%self\n\n/mnt/local/king/SAGE/broken/local/lib/python2.6/site-packages/pexpect.pyc in expect(self, pattern, timeout, searchwindowsize)\n    910         \"\"\"\n    911         compiled_pattern_list = self.compile_pattern_list(pattern)\n--> 912         return self.expect_list(compiled_pattern_list, timeout, searchwindowsize)\n    913\n    914     def expect_list(self, pattern_list, timeout = -1, searchwindowsize = -1):\n\n/mnt/local/king/SAGE/broken/local/lib/python2.6/site-packages/pexpect.pyc in expect_list(self, pattern_list, timeout, searchwindowsize)\n    961                     raise TIMEOUT ('Timeout exceeded in expect_list().')\n    962                 # Still have time left, so read more data\n--> 963                 c = self.read_nonblocking (self.maxread, timeout)\n    964                 incoming = incoming + c\n    965                 if timeout is not None:\n\n/mnt/local/king/SAGE/broken/local/lib/python2.6/site-packages/pexpect.pyc in read_nonblocking(self, size, timeout)\n    542                 raise EOF ('End Of File (EOF) in read_nonblocking(). Pokey platform.')\n    543\n--> 544         r, w, e = select.select([self.child_fd], [], [], timeout)\n    545         if not r:\n    546             if not self.isalive():\n\n/mnt/local/king/SAGE/broken/local/lib/python2.6/site-packages/sage/interfaces/get_sigs.pyc in my_sigint(x, n)\n      7\n      8 def my_sigint(x, n):\n----> 9     raise KeyboardInterrupt\n     10\n     11 def my_sigfpe(x, n):\n\nKeyboardInterrupt:\n```\n\n\nAnd then, I tried to repeat\n\n```\nsage: a = octave(t)\n```\n\nNow, it took forever, even though the first execution of the line only took a second or so.\n\nHence, apparently, more is broken than just the output. Perhaps the two problems have a common root?",
    "created_at": "2011-08-14T13:21:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/940#issuecomment-5732",
    "user": "https://github.com/simon-king-jena"
}
```

I started with

```
sage: t = '"%s"'%10^10000   # ten thousand character string.
sage: a = octave(t)
```

which took little time.

Then, I did

```
sage: s = repr(a)
```

which I had to interrupt.

Pressing Ctrl-c made the message 

```
^CInterrupting Octave...
```

appear on screen, but nothing more happened. Then, I pressed Ctrl-c again, and finally the traceback was shown:

```
^CERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (80, 0))

---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)

/home/king/<ipython console> in <module>()

/mnt/local/king/SAGE/broken/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __repr__(self)
   1738         try:
   1739             if self._get_using_file:
-> 1740                 s = self.parent().get_using_file(self._name)
   1741         except AttributeError:
   1742             s = self.parent().get(self._name)

/mnt/local/king/SAGE/broken/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in get_using_file(self, var)
   1262            if you're reading it through introspection and seeing this.
   1263         """
-> 1264         return self.get(var)
   1265
   1266     def clear(self, var):

/mnt/local/king/SAGE/broken/local/lib/python2.6/site-packages/sage/interfaces/octave.pyc in get(self, var)
    311             ' 2'
    312         """
--> 313         s = self.eval('%s'%var)
    314         i = s.find('=')
    315         return s[i+1:]

/mnt/local/king/SAGE/broken/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in eval(self, code, strip, synchronize, locals, **kwds)
   1048         try:
   1049             with gc_disabled():
-> 1050                 return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
   1051         except KeyboardInterrupt:
   1052             # DO NOT CATCH KeyboardInterrupt, as it is being caught

/mnt/local/king/SAGE/broken/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in _eval_line(self, line, allow_use_file, wait_for_prompt)
    733                 out = '\n\r'
    734         except KeyboardInterrupt:
--> 735             self._keyboard_interrupt()
    736             raise KeyboardInterrupt, "Ctrl-c pressed while running %s"%self
    737         i = out.find("\n")

/mnt/local/king/SAGE/broken/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in _keyboard_interrupt(self)
    750         else:
    751             self._expect.sendline(chr(3))  # send ctrl-c
--> 752             self._expect.expect(self._prompt)
    753             self._expect.expect(self._prompt)
    754             raise KeyboardInterrupt, "Ctrl-c pressed while running %s"%self

/mnt/local/king/SAGE/broken/local/lib/python2.6/site-packages/pexpect.pyc in expect(self, pattern, timeout, searchwindowsize)
    910         """
    911         compiled_pattern_list = self.compile_pattern_list(pattern)
--> 912         return self.expect_list(compiled_pattern_list, timeout, searchwindowsize)
    913
    914     def expect_list(self, pattern_list, timeout = -1, searchwindowsize = -1):

/mnt/local/king/SAGE/broken/local/lib/python2.6/site-packages/pexpect.pyc in expect_list(self, pattern_list, timeout, searchwindowsize)
    961                     raise TIMEOUT ('Timeout exceeded in expect_list().')
    962                 # Still have time left, so read more data
--> 963                 c = self.read_nonblocking (self.maxread, timeout)
    964                 incoming = incoming + c
    965                 if timeout is not None:

/mnt/local/king/SAGE/broken/local/lib/python2.6/site-packages/pexpect.pyc in read_nonblocking(self, size, timeout)
    542                 raise EOF ('End Of File (EOF) in read_nonblocking(). Pokey platform.')
    543
--> 544         r, w, e = select.select([self.child_fd], [], [], timeout)
    545         if not r:
    546             if not self.isalive():

/mnt/local/king/SAGE/broken/local/lib/python2.6/site-packages/sage/interfaces/get_sigs.pyc in my_sigint(x, n)
      7
      8 def my_sigint(x, n):
----> 9     raise KeyboardInterrupt
     10
     11 def my_sigfpe(x, n):

KeyboardInterrupt:
```


And then, I tried to repeat

```
sage: a = octave(t)
```

Now, it took forever, even though the first execution of the line only took a second or so.

Hence, apparently, more is broken than just the output. Perhaps the two problems have a common root?



---

archive/issue_comments_005733.json:
```json
{
    "body": "Changing component from interfaces to packages: optional.",
    "created_at": "2015-06-23T13:45:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/940#issuecomment-5733",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from interfaces to packages: optional.



---

archive/issue_comments_005734.json:
```json
{
    "body": "Changing component from packages: optional to interfaces: optional.",
    "created_at": "2015-06-23T13:49:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/940#issuecomment-5734",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from packages: optional to interfaces: optional.



---

archive/issue_comments_005735.json:
```json
{
    "body": "Changing keywords from \"\" to \"octave\".",
    "created_at": "2015-09-16T13:44:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/940#issuecomment-5735",
    "user": "https://github.com/fchapoton"
}
```

Changing keywords from "" to "octave".



---

archive/issue_comments_005736.json:
```json
{
    "body": "This issue was solved with the time, let us add a doctest to prevent its comeback.\n----\nNew commits:",
    "created_at": "2018-10-27T14:05:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/940#issuecomment-5736",
    "user": "https://trac.sagemath.org/admin/accounts/users/tmonteil"
}
```

This issue was solved with the time, let us add a doctest to prevent its comeback.
----
New commits:



---

archive/issue_comments_005737.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2018-10-27T14:05:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/940#issuecomment-5737",
    "user": "https://trac.sagemath.org/admin/accounts/users/tmonteil"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_005738.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2018-10-27T14:11:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/940#issuecomment-5738",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_005739.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2018-10-29T18:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/940#issuecomment-5739",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_005740.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2018-10-30T22:37:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/940#issuecomment-5740",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
