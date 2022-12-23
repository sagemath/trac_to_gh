# Issue 3090: first maxima use after restart returns zero, or fails

Issue created by migration from https://trac.sagemath.org/ticket/3090

Original creator: gnprice

Original creation time: 2008-05-03 07:13:17

Assignee: was

If maxima crashes (at least if a keyboard interrupt kills it),
the next evaluation to require maxima restarts it but sometimes
returns zero instead of the right answer, or spits out a big traceback.


```
sage: version()
'SAGE Version 2.10.1, Release Date: 2008-02-02'
sage: factor(1
  - 16*ab^2*(ab^2*(ac^2*ad^2
- (-cd^2 + ad^2 + ac^2)^2/4) - (-bc^2 + ac^2 + ab^2)*(ad^2*(-bc^2 +
ac^2 + ab^2)/2 - (-bd^2 + ad^2 + ab^2)*(-cd^2 + ad^2 + ac^2)/4)/2 +
(-bd^2 + ad^2 + ab^2)*((-bc^2 + ac^2 + ab^2)*(-cd^2 + ad^2 + ac^2)/4 -
ac^2*(-bd^2 + ad^2 + ab^2)/2)/2)
   / ((-bc + ac + ab)*(bc - ac + ab)*(bc +
ac - ab)*(bc + ac + ab)*(-bd + ad + ab)*(bd - ad + ab)*(bd + ad -
ab)*(bd + ad + ab)) * (ab^2*(ac^2*ad^2 - (-cd^2 + ad^2 + ac^2)^2/4)
    - (-bc^2 + ac^2 + ab^2)
     * (ad^2*(-bc^2 + ac^2 + ab^2)/2 -
(-bd^2 + ad^2 + ab^2)*(-cd^2 + ad^2 + ac^2)/4)/2
    + (-bd^2 + ad^2 + ab^2)
     * ((-bc^2 + ac^2 + ab^2)*(-cd^2 + ad^2 + ac^2)/4 - ac^2*(-bd^2 +
ad^2 + ab^2)/2)/2)
   / ((-bc + ac + ab)*(bc - ac + ab)*(bc + ac - ab)*(bc
+ ac + ab)*(-bd + ad + ab)*(bd - ad + ab)*(bd + ad - ab)*(bd + ad + ab)))
<hit Ctrl-c>
Control-C pressed.  Interrupting Maxima. Please wait a few seconds...
[long traceback...]
sage: diff(1
  - 16*ab^2*(ab^2*(ac^2*ad^2
- (-cd^2 + ad^2 + ac^2)^2/4) - (-bc^2 + ac^2 + ab^2)*(ad^2*(-bc^2 +
ac^2 + ab^2)/2 - (-bd^2 + ad^2 + ab^2)*(-cd^2 + ad^2 + ac^2)/4)/2 +
(-bd^2 + ad^2 + ab^2)*((-bc^2 + ac^2 + ab^2)*(-cd^2 + ad^2 + ac^2)/4 -
ac^2*(-bd^2 + ad^2 + ab^2)/2)/2)
   / ((-bc + ac + ab)*(bc - ac + ab)*(bc +
ac - ab)*(bc + ac + ab)*(-bd + ad + ab)*(bd - ad + ab)*(bd + ad -
ab)*(bd + ad + ab)) * (ab^2*(ac^2*ad^2 - (-cd^2 + ad^2 + ac^2)^2/4)
    - (-bc^2 + ac^2 + ab^2)
     * (ad^2*(-bc^2 + ac^2 + ab^2)/2 -
(-bd^2 + ad^2 + ab^2)*(-cd^2 + ad^2 + ac^2)/4)/2
    + (-bd^2 + ad^2 + ab^2)
     * ((-bc^2 + ac^2 + ab^2)*(-cd^2 + ad^2 + ac^2)/4 - ac^2*(-bd^2 +
ad^2 + ab^2)/2)/2)
   / ((-bc + ac + ab)*(bc - ac + ab)*(bc + ac - ab)*(bc
+ ac + ab)*(-bd + ad + ab)*(bd - ad + ab)*(bd + ad - ab)*(bd + ad + ab)), ac)
Maxima crashed -- automatically restarting.
---------------------------------------------------------------------------
<class 'pexpect.EOF'>                     Traceback (most recent call last)

/afs/athena.mit.edu/user/p/r/price/<ipython console> in <module>()

/mit/sage/sage-2.10.1/local/lib/python2.5/site-packages/sage/calculus/functional.py in derivative(f, *args, **kwds)
     45     """
     46     try:
---> 47         return f.derivative(*args, **kwds)
     48     except AttributeError:
     49         pass

/mit/sage/sage-2.10.1/local/lib/python2.5/site-packages/sage/calculus/calculus.py in derivative(self, *args)
   1593         except IndexError:
   1594             pass
-> 1595         t = maxima('diff(%s, %s)'%(self._maxima_().name(), s))
   1596         f = self.parent()(t)
   1597         return f

/mit/sage/sage-2.10.1/local/lib/python2.5/site-packages/sage/calculus/calculus.py in _maxima_(self, session)
    767     def _maxima_(self, session=None):
    768         if session is None:
--> 769             return RingElement._maxima_(self, maxima)
    770         else:
    771             return RingElement._maxima_(self, session)

/afs/athena.mit.edu/user/p/r/price/sage_object.pyx in sage.structure.sage_object.SageObject._maxima_()

/afs/athena.mit.edu/user/p/r/price/sage_object.pyx in sage.structure.sage_object.SageObject._interface_()

/mit/sage/sage-2.10.1/local/lib/python2.5/site-packages/sage/interfaces/maxima.py in __call__(self, x)
    376     def __call__(self, x):
    377         import sage.rings.all
--> 378         return Expect.__call__(self, x)
    379         
    380     def __init__(self, script_subdirectory=None, logfile=None, server=None,

/mit/sage/sage-2.10.1/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __call__(self, x)
    736             return x
    737         if isinstance(x, basestring):
--> 738             return cls(self, x)
    739         try:
    740             return self._coerce_from_special_method(x)

/mit/sage/sage-2.10.1/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __init__(self, parent, value, is_name)
    984         else:
    985             try:
--> 986                 self._name = parent._create(value)
    987             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:
    988                 self._session_number = -1

/mit/sage/sage-2.10.1/local/lib/python2.5/site-packages/sage/interfaces/expect.py in _create(self, value)
    880         name = self._next_var_name()
    881         #self._last_name = name
--> 882         self.set(name, value)
    883         return name
    884 

/mit/sage/sage-2.10.1/local/lib/python2.5/site-packages/sage/interfaces/maxima.py in set(self, var, value)
    845         cmd = '%s : %s$'%(var, value.rstrip(';'))
    846         if len(cmd) > self.__eval_using_file_cutoff:
--> 847             self._batch(cmd, batchload=True)
    848         else:
    849             self._eval_line(cmd)

/mit/sage/sage-2.10.1/local/lib/python2.5/site-packages/sage/interfaces/maxima.py in _batch(self, s, batchload)
    522 
    523         self._sendline(cmd)
--> 524         self._expect_expr(s)
    525         out = self._before()
    526         self._error_check(str, out)

/mit/sage/sage-2.10.1/local/lib/python2.5/site-packages/sage/interfaces/maxima.py in _expect_expr(self, expr, timeout)
    453                 i = self._expect.expect(expr,timeout=timeout)
    454             else:
--> 455                 i = self._expect.expect(expr)
    456             if i > 0:
    457                 v = self._expect.before

/mit/sage/sage-2.10.1/local/lib/python2.5/site-packages/pexpect.py in expect(self, pattern, timeout, searchwindowsize)
    910         """
    911         compiled_pattern_list = self.compile_pattern_list(pattern)
--> 912         return self.expect_list(compiled_pattern_list, timeout, searchwindowsize)
    913 
    914     def expect_list(self, pattern_list, timeout = -1, searchwindowsize = -1):

/mit/sage/sage-2.10.1/local/lib/python2.5/site-packages/pexpect.py in expect_list(self, pattern_list, timeout, searchwindowsize)
    976                 self.match = None
    977                 self.match_index = None
--> 978                 raise EOF (str(e) + '\n' + str(self))
    979         except TIMEOUT, e:
    980             self.before = incoming

<class 'pexpect.EOF'>: End Of File (EOF) in read_nonblocking(). Exception style platform.
<pexpect.spawn instance at 0xf1a8a1ec>
version: 2.0 ($Revision: 1.151 $)
command: /usr/bin/maxima
args: ['/usr/bin/maxima', '-p', '/mit/sage/sage-2.10.1/local/bin/sage-maxima.lisp']
patterns:
    909034618
buffer (last 100 chars): 
before (last 100 chars): debugger-hook* to nil.
(%i22) 
out of memory allocating 8 bytes after a total of 98253624 bytes

after: <class 'pexpect.EOF'>
match: None
match_index: None
exitstatus: 1
flag_eof: 1
pid: 8338
child_fd: 3
timeout: None
delimiter: <class 'pexpect.EOF'>
logfile: None
maxread: 10000
searchwindowsize: None
delaybeforesend: 0
```



In fact in the first manifestation of this that I saw, the return value was 0, with no error message.  I've had less success trimming this test case down, so a short .sage file is attached.



```
sage: version()
'SAGE Version 2.10.1, Release Date: 2008-02-02'
sage: attach hessian.sage
sage: factor(1
  - 16*ab^2*(ab^2*(ac^2*ad^2
- (-cd^2 + ad^2 + ac^2)^2/4) - (-bc^2 + ac^2 + ab^2)*(ad^2*(-bc^2 +
ac^2 + ab^2)/2 - (-bd^2 + ad^2 + ab^2)*(-cd^2 + ad^2 + ac^2)/4)/2 +
(-bd^2 + ad^2 + ab^2)*((-bc^2 + ac^2 + ab^2)*(-cd^2 + ad^2 + ac^2)/4 -
ac^2*(-bd^2 + ad^2 + ab^2)/2)/2)
   / ((-bc + ac + ab)*(bc - ac + ab)*(bc +
ac - ab)*(bc + ac + ab)*(-bd + ad + ab)*(bd - ad + ab)*(bd + ad -
ab)*(bd + ad + ab)) * (ab^2*(ac^2*ad^2 - (-cd^2 + ad^2 + ac^2)^2/4)
    - (-bc^2 + ac^2 + ab^2)
     * (ad^2*(-bc^2 + ac^2 + ab^2)/2 -
(-bd^2 + ad^2 + ab^2)*(-cd^2 + ad^2 + ac^2)/4)/2
    + (-bd^2 + ad^2 + ab^2)
     * ((-bc^2 + ac^2 + ab^2)*(-cd^2 + ad^2 + ac^2)/4 - ac^2*(-bd^2 +
ad^2 + ab^2)/2)/2)
   / ((-bc + ac + ab)*(bc - ac + ab)*(bc + ac - ab)*(bc
+ ac + ab)*(-bd + ad + ab)*(bd - ad + ab)*(bd + ad - ab)*(bd + ad + ab)))
<hit Ctrl-c>
Control-C pressed.  Interrupting Maxima. Please wait a few seconds...
[long traceback...]
sage: attach hessian.sage
sage: diff(sinth, ac)
Maxima crashed -- automatically restarting.
0
sage: 
```



(I don't see a 'maxima' component, so I'm settling for 'calculus'.)



---

Comment by gnprice created at 2008-05-03 07:14:34

test-case setup for one of two variants of bug


---

Attachment

I guess I should add this:

$ uname -a
Linux vinegar-pot 2.6.24.5 #1 SMP Sun Apr 20 05:23:49 UTC 2008 i686 GNU/Linux


---

Comment by mabshoff created at 2008-05-03 12:53:41

Hi Gregory,

this is likely a valid bug report for 3.0, too, but it would be better if you tested with the current release before opening tickets because that is what we actually do fix. The only release we support is the last release and that changes on average every two weeks. :)

Cheers,

Michael


---

Comment by mhansen created at 2009-01-22 07:45:01

I'm having problems reproducing this on my Sage 3.2.3 install.


---

Comment by mhansen created at 2009-06-04 23:03:02

Resolution: invalid


---

Comment by mhansen created at 2009-06-04 23:03:02

I still cannot reproduce this in 4.0.1.rc1.  I'm going to mark this as invalid.
