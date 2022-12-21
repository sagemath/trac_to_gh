# Issue 6333: optional doctest failure -- scilab interface is really really broken

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-06-16 15:12:21

Assignee: tbd


```
sage -t -long --optional devel/sage/sage/interfaces/scilab.py
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/scilab.py", line 19:
    sage: a**10                              # optional - scilab
Expected:
       1.000E+10
Got:
    <BLANKLINE>
    <BLANKLINE>
        1.000D+10
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/scilab.py", line 27:
    sage: print "ignore this";  scilab('date')                     # optional - scilab; random output
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[7]>", line 1, in <module>
        print "ignore this";  scilab('date')                     # optional - scilab; random output###line 27:
    sage: print "ignore this";  scilab('date')                     # optional - scilab; random output
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1584, in __repr__
        s = self.parent().get(self._name)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/scilab.py", line 321, in get
        s = self.eval('%s'%var)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/scilab.py", line 274, in eval
        s = Expect.eval(self, command, **kwds).replace("\x1b[?1l\x1b>","").strip()
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 975, in eval
        return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 668, in _eval_line
        raise RuntimeError, "%s\n%s crashed executing %s"%(msg,self, line)
    RuntimeError: End Of File (EOF) in read_nonblocking(). Exception style platform.
    <pexpect.spawn instance at 0x3669a70>
    version: 2.0 ($Revision: 1.151 $)
    command: /usr/bin/scilab
    args: ['/usr/bin/scilab', '-nogui']
    patterns:
        -->
    buffer (last 100 chars): 
    before (last 100 chars): sage0
    �[?1l�>
    after: <class 'pexpect.EOF'>
    match: None
    match_index: None
    exitstatus: None
    flag_eof: 1
    pid: 24781
    child_fd: 7
    timeout: None
    delimiter: <class 'pexpect.EOF'>
    logfile: None
    maxread: 100
    searchwindowsize: None
    delaybeforesend: 0
    Scilab crashed executing sage0
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/scilab.py", line 29:
    sage: scilab('5*10 + 6')                 # optional - scilab
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[8]>", line 1, in <module>
        scilab('5*10 + 6')                 # optional - scilab###line 29:
    sage: scilab('5*10 + 6')                 # optional - scilab
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1024, in __call__
        return cls(self, x, name=name)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1428, in __init__
        raise TypeError, x
    TypeError: End Of File (EOF) in read_nonblocking(). Exception style platform.
    <pexpect.spawn instance at 0x3669a70>
    version: 2.0 ($Revision: 1.151 $)
    command: /usr/bin/scilab
    args: ['/usr/bin/scilab', '-nogui']
    patterns:
        -->
    buffer (last 100 chars): 
    before (last 100 chars): sage3=5*10 + 6;

    after: <class 'pexpect.EOF'>
    match: None
    match_index: None
    exitstatus: 0
    flag_eof: 1
    pid: 24781
    child_fd: 7
    timeout: None
    delimiter: <class 'pexpect.EOF'>
    logfile: None
    maxread: 100
    searchwindowsize: None
    delaybeforesend: 0
    Scilab crashed executing sage3=5*10 + 6;
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/scilab.py", line 31:
    sage: scilab('(6+6)/3')                  # optional - scilab
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[9]>", line 1, in <module>
        scilab('(6+6)/3')                  # optional - scilab###line 31:
    sage: scilab('(6+6)/3')                  # optional - scilab
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1024, in __call__
        return cls(self, x, name=name)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1428, in __init__
        raise TypeError, x
    TypeError: End Of File (EOF) in read_nonblocking(). Exception style platform.
    <pexpect.spawn instance at 0x3669a70>
    version: 2.0 ($Revision: 1.151 $)
    command: /usr/bin/scilab
    args: ['/usr/bin/scilab', '-nogui']
    patterns:
        -->
    buffer (last 100 chars): 
    before (last 100 chars): sage2=(6+6)/3;

    after: <class 'pexpect.EOF'>
    match: None
    match_index: None
    exitstatus: 0
    flag_eof: 1
    pid: 24781
    child_fd: 7
    timeout: None
    delimiter: <class 'pexpect.EOF'>
    logfile: None
    maxread: 100
    searchwindowsize: None
    delaybeforesend: 0
    Scilab crashed executing sage2=(6+6)/3;
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/scilab.py", line 33:
    sage: scilab('9')^2                      # optional - scilab
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[10]>", line 1, in <module>
        scilab('9')**Integer(2)                      # optional - scilab###line 33:
    sage: scilab('9')^2                      # optional - scilab
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1024, in __call__
        return cls(self, x, name=name)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1428, in __init__
        raise TypeError, x
    TypeError: End Of File (EOF) in read_nonblocking(). Exception style platform.
    <pexpect.spawn instance at 0x3669a70>
    version: 2.0 ($Revision: 1.151 $)
    command: /usr/bin/scilab
    args: ['/usr/bin/scilab', '-nogui']
    patterns:
        -->
    buffer (last 100 chars): 
    before (last 100 chars): sage0=9;

    after: <class 'pexpect.EOF'>
    match: None
    match_index: None
    exitstatus: 0
    flag_eof: 1
    pid: 24781
    child_fd: 7
    timeout: None
    delimiter: <class 'pexpect.EOF'>
    logfile: None
    maxread: 100
    searchwindowsize: None
    delaybeforesend: 0
    Scilab crashed executing sage0=9;
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/scilab.py", line 35:
    sage: a = scilab(10); b = scilab(20); c = scilab(30)    # optional - scilab
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[11]>", line 1, in <module>
        a = scilab(Integer(10)); b = scilab(Integer(20)); c = scilab(Integer(30))    # optional - scilab###line 35:
    sage: a = scilab(10); b = scilab(20); c = scilab(30)    # optional - scilab
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1026, in __call__
        return self._coerce_from_special_method(x)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1052, in _coerce_from_special_method
        return self(x._interface_init_())
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1024, in __call__
        return cls(self, x, name=name)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1428, in __init__
        raise TypeError, x
    TypeError: End Of File (EOF) in read_nonblocking(). Exception style platform.
    <pexpect.spawn instance at 0x3669a70>
    version: 2.0 ($Revision: 1.151 $)
    command: /usr/bin/scilab
    args: ['/usr/bin/scilab', '-nogui']
    patterns:
        -->
    buffer (last 100 chars): 
    before (last 100 chars): sage4=10;

    after: <class 'pexpect.EOF'>
    match: None
    match_index: None
    exitstatus: 0
    flag_eof: 1
    pid: 24781
    child_fd: 7
    timeout: None
    delimiter: <class 'pexpect.EOF'>
    logfile: None
    maxread: 100
    searchwindowsize: None
    delaybeforesend: 0
    Scilab crashed executing sage4=10;
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/scilab.py", line 36:
    sage: avg = (a+b+c)/3                    # optional - scilab
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[12]>", line 1, in <module>
        avg = (a+b+c)/Integer(3)                    # optional - scilab###line 36:
    sage: avg = (a+b+c)/3                    # optional - scilab
    NameError: name 'b' is not defined
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/scilab.py", line 37:
    sage: avg                                # optional - scilab
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[13]>", line 1, in <module>
        avg                                # optional - scilab###line 37:
    sage: avg                                # optional - scilab
    NameError: name 'avg' is not defined
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/scilab.py", line 39:
    sage: parent(avg)                        # optional - scilab
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[14]>", line 1, in <module>
        parent(avg)                        # optional - scilab###line 39:
    sage: parent(avg)                        # optional - scilab
    NameError: name 'avg' is not defined
...
```

and it goes on for *hundreds* of pages.
And I do have scilab installed

```
wstein`@`sage:~/build/sage-4.0.2.alpha3$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: scilab.version()
'scilab-4.1.2'
```

