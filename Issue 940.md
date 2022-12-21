# Issue 940: read large output from octave (and probably matlab) takes *forever*

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-10-20 08:27:01

Assignee: was


```
    sage: t = '"%s"'%10^10000   # ten thousand character string.
    sage: a = octave(t)
```

If you now try to print a, it take forever.


---

Comment by mabshoff created at 2008-08-31 06:10:22

Changing assignee from was to mhansen.


---

Comment by SimonKing created at 2011-08-14 13:21:07

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

Comment by jdemeyer created at 2015-06-23 13:45:27

Changing component from interfaces to packages: optional.


---

Comment by jdemeyer created at 2015-06-23 13:49:26

Changing component from packages: optional to interfaces: optional.


---

Comment by chapoton created at 2015-09-16 13:44:58

Changing keywords from "" to "octave".


---

Comment by tmonteil created at 2018-10-27 14:05:07

This issue was solved with the time, let us add a doctest to prevent its comeback.
----
New commits:


---

Comment by tmonteil created at 2018-10-27 14:05:07

Changing status from new to needs_review.


---

Comment by git created at 2018-10-27 14:11:27

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by vdelecroix created at 2018-10-29 18:13:52

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2018-10-30 22:37:40

Resolution: fixed
