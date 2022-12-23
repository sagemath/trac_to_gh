# Issue 2120: maple -- the interface is completely broken in Sage-2.10.1 with Maple 11.

Issue created by migration from https://trac.sagemath.org/ticket/2120

Original creator: was

Original creation time: 2008-02-09 00:01:19

Assignee: was

This is what we get for not running the optional doctests.  Maple 10 still works fine.  With Maple 11 the Sage interfaces is completely totally broken (!). 


```
dhcp46-76:interfaces was$ sage -t --optional maple.py 
sage -t --optional maple.py                                 **********************************************************************
File "maple.py", line 22:
    sage: maple('3 * 5')
Expected:
    15
Got:
    <BLANKLINE>
**********************************************************************
File "maple.py", line 24:
    sage: maple.eval('ifactor(2005)')
Expected:
    '``(5)*``(401)'
Got:
    'read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";\nread "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";\nsage0'
**********************************************************************
File "maple.py", line 26:
    sage: maple.ifactor(2005)
Expected:
    ``(5)*``(401)
Got:
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    ``(5)*``(401)
**********************************************************************
File "maple.py", line 28:
    sage: maple.fsolve('x^2=cos(x)+4', 'x=0..5')
Expected:
    1.914020619
Got:
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp
**********************************************************************
File "maple.py", line 30:
    sage: maple.factor('x^5 - y^5')
Expected:
    (x-y)*(x^4+x^3*y+x^2*y^2+x*y^3+y^4)
Got:
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp
**********************************************************************
File "maple.py", line 55:
    sage: maple('factor(x^5-1)')
Expected:
    (x-1)*(x^4+x^3+x^2+x+1)
Got:
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
**********************************************************************
File "maple.py", line 65:
    sage: maple('(x^5-1)').factor()
Expected:
    (x-1)*(x^4+x^3+x^2+x+1)
Got:
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
**********************************************************************
File "maple.py", line 72:
    sage: maple('(x^12-1)/(x-1)').simplify()
Expected:
    x^11+x^10+x^9+x^8+x^7+x^6+x^5+x^4+x^3+x^2+x+1
Got:
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
**********************************************************************
File "maple.py", line 82:
    sage: maple('(x^12-1)').factor( )
Expected:
    (x-1)*(x+1)*(x^2+x+1)*(x^2-x+1)*(x^2+1)*(x^4-x^2+1)
Got:
    x^5-1
**********************************************************************
File "maple.py", line 85:
    sage: maple('(x^28-1)').factor( )
Expected:
    (x-1)*(x^6+x^5+x^4+x^3+x^2+x+1)*(x+1)*(1-x+x^2-x^3+x^4-x^5+x^6)*(x^2+1)*(x^12-x^10+x^8-x^6+x^4-x^2+1)
Got:
    x^5-1
**********************************************************************
File "maple.py", line 115:
    sage: maple.fibonacci(10)
Expected:
    fibonacci(10)
Got:
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    (x^12-1)/(x-1)
**********************************************************************
File "maple.py", line 121:
    sage: maple('combinat[fibonacci]')(10)
Expected:
    55
Got:
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp
**********************************************************************
File "maple.py", line 137:
    sage: maple.fibonacci(10)
Expected:
    55
Got:
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    [Chi, bell, binomial, cartprod, character, choose, composition, conjpart, 
    decodepart, encodepart, fibonacci, firstpart, graycode, inttovec, lastpart, 
    multinomial, nextpart, numbcomb, numbcomp, numbpart, numbperm, partition, 
    permute, powerset, prevpart, randcomb, randpart, randperm, setpartition, 
    stirling1, stirling2, subsets, vectoint]
**********************************************************************
File "maple.py", line 144:
    sage: maple('seq(fibonacci(i),i=1..19)')
Expected:
    1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584,
    4181
Got:
    <BLANKLINE>
**********************************************************************
File "maple.py", line 150:
    sage: maple.isprime(maple.fibonacci(27))
Expected:
    false
Got:
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
**********************************************************************
File "maple.py", line 152:
    sage: maple.ifactor(maple.fibonacci(27))
Expected:
    ``(2)*``(17)*``(53)*``(109)
Got:
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp
**********************************************************************
File "maple.py", line 161:
    sage: f19  = alpha^19 - beta^19/maple('sqrt(5)')
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[20]>", line 1, in <module>
        f19  = alpha**Integer(19) - beta**Integer(19)/maple('sqrt(5)')###line 161:
    sage: f19  = alpha^19 - beta^19/maple('sqrt(5)')
      File "element.pyx", line 1480, in sage.structure.element.RingElement.__div__
      File "coerce.pxi", line 136, in sage.structure.element._div_c
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1210, in _div_
        raise TypeError, msg
    TypeError: An error occured running a Maple command:
    INPUT:
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    OUTPUT:
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    Error, "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp"
    is an empty file
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
**********************************************************************
File "maple.py", line 162:
    sage: f19
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[21]>", line 1, in <module>
        f19###line 162:
    sage: f19
    NameError: name 'f19' is not defined
**********************************************************************
File "maple.py", line 164:
    sage: _= f19.simplify()                # somewhat randomly ordered output...
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[22]>", line 1, in <module>
        _= f19.simplify()                # somewhat randomly ordered output...###line 164:
    sage: _= f19.simplify()                # somewhat randomly ordered output...
    NameError: name 'f19' is not defined
**********************************************************************
File "maple.py", line 181:
    age: mysqcu(5)
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[24]>", line 1, in <module>
        mysqcu(Integer(5))###line 181:
    age: mysqcu(5)
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1015, in __call__
        return getattr(P, self.name())(*args)
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 939, in __call__
        return self._parent.function_call(self._name, list(args))
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 901, in function_call
        return self.new("%s(%s)"%(function, ",".join([s.name() for s in args])))
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 803, in new
        return self(code)
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 738, in __call__
        return cls(self, x)
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 989, in __init__
        raise TypeError, x
    TypeError: An error occured running a Maple command:
    INPUT:
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    OUTPUT:
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    Error, "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp"
    is an empty file
**********************************************************************
File "maple.py", line 183:
    age: mysqcu(-5)
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[25]>", line 1, in <module>
        mysqcu(-Integer(5))###line 183:
    age: mysqcu(-5)
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/maple.py", line 732, in __repr__
        return self.parent().get(self._name)
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/maple.py", line 421, in get
        s = self.eval('printf("%%q",%s)'%var)
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 707, in eval
        return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/maple.py", line 385, in _eval_line
        wait_for_prompt=wait_for_prompt).replace('\\\n','').strip()
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 609, in _eval_line
        return self._eval_line_using_file(line)
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 594, in _eval_line_using_file
        s = self._eval_line(self._read_in_file_command(tmp_to_use), allow_use_file=False)
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/maple.py", line 399, in _eval_line
        raise RuntimeError, "An error occured running a Maple command:\nINPUT:\n%s\nOUTPUT:\n%s"%(line, z)
    RuntimeError: An error occured running a Maple command:
    INPUT:
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    OUTPUT:
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    Error, "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp"
    is an empty file
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
**********************************************************************
File "maple.py", line 514:
    sage: maple('partition(10)')              # optional
Expected:
    partition(10)
Got:
    <BLANKLINE>
**********************************************************************
File "maple.py", line 516:
    sage: maple('bell(10)')                   # optional
Expected:
    bell(10)
Got:
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp
**********************************************************************
File "maple.py", line 519:
    sage: maple('partition(10)')               # optional
Expected:
    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 2], [1, 1, 1, 1, 1, 1, 2, 2], [1, 1, 1, 1, 2, 2, 2], [1, 1, 2, 2, 2, 2], [2, 2, 2, 2, 2], [1, 1, 1, 1, 1, 1, 1, 3], [1, 1, 1, 1, 1, 2, 3], [1, 1, 1, 2, 2, 3], [1, 2, 2, 2, 3], [1, 1, 1, 1, 3, 3], [1, 1, 2, 3, 3], [2, 2, 3, 3], [1, 3, 3, 3], [1, 1, 1, 1, 1, 1, 4], [1, 1, 1, 1, 2, 4], [1, 1, 2, 2, 4], [2, 2, 2, 4], [1, 1, 1, 3, 4], [1, 2, 3, 4], [3, 3, 4], [1, 1, 4, 4], [2, 4, 4], [1, 1, 1, 1, 1, 5], [1, 1, 1, 2, 5], [1, 2, 2, 5], [1, 1, 3, 5], [2, 3, 5], [1, 4, 5], [5, 5], [1, 1, 1, 1, 6], [1, 1, 2, 6], [2, 2, 6], [1, 3, 6], [4, 6], [1, 1, 1, 7], [1, 2, 7], [3, 7], [1, 1, 8], [2, 8], [1, 9], [10]]
Got:
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp
**********************************************************************
File "maple.py", line 521:
    sage: maple('bell(10)')                   # optional
Expected:
    115975
Got:
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    sage2
**********************************************************************
File "maple.py", line 523:
    sage: maple('fibonacci(10)')              # optional
Expected:
    55
Got:
    <BLANKLINE>
**********************************************************************
File "maple.py", line 569:
    sage: g = maple('gcd')                   #optional requires maple
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_17[0]>", line 1, in <module>
        g = maple('gcd')                   #optional requires maple###line 569:
    sage: g = maple('gcd')                   #optional requires maple
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 738, in __call__
        return cls(self, x)
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 989, in __init__
        raise TypeError, x
    TypeError: An error occured running a Maple command:
    INPUT:
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    OUTPUT:
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";Error, "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp"
    is an empty file

    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
**********************************************************************
File "maple.py", line 570:
    sage: print g.curry._sage_src_().strip() #optional requires maple
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_17[1]>", line 1, in <module>
        print g.curry._sage_src_().strip() #optional requires maple###line 570:
    sage: print g.curry._sage_src_().strip() #optional requires maple
    NameError: name 'g' is not defined
**********************************************************************
File "maple.py", line 601:
    sage: m.__hash__()
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_18[1]>", line 1, in <module>
        m.__hash__()###line 601:
    sage: m.__hash__()
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/maple.py", line 611, in __hash__
        return int(maple.eval('StringTools:-Hash(convert(%s, string));'%self.name())[1:-1],16)
    ValueError: invalid literal for int() with base 16: ''
**********************************************************************
File "maple.py", line 603:
    sage: hash(m)
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_18[2]>", line 1, in <module>
        hash(m)###line 603:
    sage: hash(m)
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/maple.py", line 611, in __hash__
        return int(maple.eval('StringTools:-Hash(convert(%s, string));'%self.name())[1:-1],16)
    ValueError: invalid literal for int() with base 16: 'ead "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tm'
**********************************************************************
File "maple.py", line 606:
    sage: m.__hash__()
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_18[4]>", line 1, in <module>
        m.__hash__()###line 606:
    sage: m.__hash__()
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/maple.py", line 611, in __hash__
        return int(maple.eval('StringTools:-Hash(convert(%s, string));'%self.name())[1:-1],16)
    ValueError: invalid literal for int() with base 16: 'ead "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";\nread "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";\n"ce5b65cba4048e3ef10b852df09e25f4'
**********************************************************************
File "maple.py", line 608:
    sage: hash(m)
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_18[5]>", line 1, in <module>
        hash(m)###line 608:
    sage: hash(m)
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/maple.py", line 611, in __hash__
        return int(maple.eval('StringTools:-Hash(convert(%s, string));'%self.name())[1:-1],16)
    ValueError: invalid literal for int() with base 16: 'ead "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tm'
**********************************************************************
File "maple.py", line 622:
    sage: a == b
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_19[2]>", line 1, in <module>
        a == b###line 622:
    sage: a == b
      File "element.pyx", line 623, in sage.structure.element.Element.__richcmp__
      File "element.pyx", line 595, in sage.structure.element.Element._richcmp
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/maple.py", line 680, in __cmp__
        if (hash(self) < hash(other)):
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/maple.py", line 611, in __hash__
        return int(maple.eval('StringTools:-Hash(convert(%s, string));'%self.name())[1:-1],16)
    ValueError: invalid literal for int() with base 16: 'ead "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tm'
**********************************************************************
File "maple.py", line 624:
    sage: a == 5
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_19[3]>", line 1, in <module>
        a == Integer(5)###line 624:
    sage: a == 5
      File "element.pyx", line 623, in sage.structure.element.Element.__richcmp__
      File "element.pyx", line 568, in sage.structure.element.Element._richcmp
      File "element.pyx", line 554, in sage.structure.element.Element._richcmp_
      File "element.pyx", line 595, in sage.structure.element.Element._richcmp
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/maple.py", line 680, in __cmp__
        if (hash(self) < hash(other)):
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/maple.py", line 611, in __hash__
        return int(maple.eval('StringTools:-Hash(convert(%s, string));'%self.name())[1:-1],16)
    ValueError: invalid literal for int() with base 16: 'ead "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tm'
**********************************************************************
File "maple.py", line 628:
    sage: a == c
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_19[5]>", line 1, in <module>
        a == c###line 628:
    sage: a == c
      File "element.pyx", line 623, in sage.structure.element.Element.__richcmp__
      File "element.pyx", line 595, in sage.structure.element.Element._richcmp
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/maple.py", line 680, in __cmp__
        if (hash(self) < hash(other)):
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/maple.py", line 611, in __hash__
        return int(maple.eval('StringTools:-Hash(convert(%s, string));'%self.name())[1:-1],16)
    ValueError: invalid literal for int() with base 16: 'ead "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";\nread "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";\nread "/Users/was/.sage//temp/dhcp46_76.ipam.ucl'
**********************************************************************
File "maple.py", line 630:
    sage: a < c
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_19[6]>", line 1, in <module>
        a < c###line 630:
    sage: a < c
      File "element.pyx", line 623, in sage.structure.element.Element.__richcmp__
      File "element.pyx", line 595, in sage.structure.element.Element._richcmp
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/maple.py", line 680, in __cmp__
        if (hash(self) < hash(other)):
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/maple.py", line 611, in __hash__
        return int(maple.eval('StringTools:-Hash(convert(%s, string));'%self.name())[1:-1],16)
    ValueError: invalid literal for int() with base 16: 'ead "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tm'
**********************************************************************
File "maple.py", line 632:
    sage: a < 6
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_19[7]>", line 1, in <module>
        a < Integer(6)###line 632:
    sage: a < 6
      File "element.pyx", line 623, in sage.structure.element.Element.__richcmp__
      File "element.pyx", line 568, in sage.structure.element.Element._richcmp
      File "element.pyx", line 554, in sage.structure.element.Element._richcmp_
      File "element.pyx", line 595, in sage.structure.element.Element._richcmp
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/maple.py", line 680, in __cmp__
        if (hash(self) < hash(other)):
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/maple.py", line 611, in __hash__
        return int(maple.eval('StringTools:-Hash(convert(%s, string));'%self.name())[1:-1],16)
    ValueError: invalid literal for int() with base 16: 'ead "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tm'
**********************************************************************
File "maple.py", line 634:
    sage: c <= a
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_19[8]>", line 1, in <module>
        c <= a###line 634:
    sage: c <= a
      File "element.pyx", line 623, in sage.structure.element.Element.__richcmp__
      File "element.pyx", line 595, in sage.structure.element.Element._richcmp
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/maple.py", line 680, in __cmp__
        if (hash(self) < hash(other)):
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/maple.py", line 611, in __hash__
        return int(maple.eval('StringTools:-Hash(convert(%s, string));'%self.name())[1:-1],16)
    ValueError: invalid literal for int() with base 16: ''
**********************************************************************
File "maple.py", line 639:
    sage: Mm == Mm
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_19[11]>", line 1, in <module>
        Mm == Mm###line 639:
    sage: Mm == Mm
      File "element.pyx", line 623, in sage.structure.element.Element.__richcmp__
      File "element.pyx", line 595, in sage.structure.element.Element._richcmp
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/maple.py", line 680, in __cmp__
        if (hash(self) < hash(other)):
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/maple.py", line 611, in __hash__
        return int(maple.eval('StringTools:-Hash(convert(%s, string));'%self.name())[1:-1],16)
    ValueError: invalid literal for int() with base 16: 'ead "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tm'
**********************************************************************
File "maple.py", line 641:
    sage: Mm < 5
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_19[12]>", line 1, in <module>
        Mm < Integer(5)###line 641:
    sage: Mm < 5
      File "element.pyx", line 623, in sage.structure.element.Element.__richcmp__
      File "element.pyx", line 568, in sage.structure.element.Element._richcmp
      File "element.pyx", line 554, in sage.structure.element.Element._richcmp_
      File "element.pyx", line 595, in sage.structure.element.Element._richcmp
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/maple.py", line 680, in __cmp__
        if (hash(self) < hash(other)):
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/maple.py", line 611, in __hash__
        return int(maple.eval('StringTools:-Hash(convert(%s, string));'%self.name())[1:-1],16)
    ValueError: invalid literal for int() with base 16: 'ead "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tm'
**********************************************************************
File "maple.py", line 643:
    sage: (Mm < 5) == (M < 5)
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_19[13]>", line 1, in <module>
        (Mm < Integer(5)) == (M < Integer(5))###line 643:
    sage: (Mm < 5) == (M < 5)
      File "element.pyx", line 623, in sage.structure.element.Element.__richcmp__
      File "element.pyx", line 568, in sage.structure.element.Element._richcmp
      File "element.pyx", line 554, in sage.structure.element.Element._richcmp_
      File "element.pyx", line 595, in sage.structure.element.Element._richcmp
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/maple.py", line 680, in __cmp__
        if (hash(self) < hash(other)):
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/maple.py", line 611, in __hash__
        return int(maple.eval('StringTools:-Hash(convert(%s, string));'%self.name())[1:-1],16)
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 707, in eval
        return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/maple.py", line 385, in _eval_line
        wait_for_prompt=wait_for_prompt).replace('\\\n','').strip()
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 609, in _eval_line
        return self._eval_line_using_file(line)
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 594, in _eval_line_using_file
        s = self._eval_line(self._read_in_file_command(tmp_to_use), allow_use_file=False)
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/maple.py", line 399, in _eval_line
        raise RuntimeError, "An error occured running a Maple command:\nINPUT:\n%s\nOUTPUT:\n%s"%(line, z)
    RuntimeError: An error occured running a Maple command:
    INPUT:
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    OUTPUT:
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    Error, a Matrix is not valid rhs to < or <=
**********************************************************************
File "maple.py", line 645:
    sage: 5 < Mm
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_19[14]>", line 1, in <module>
        Integer(5) < Mm###line 645:
    sage: 5 < Mm
      File "integer.pyx", line 446, in sage.rings.integer.Integer.__richcmp__
      File "element.pyx", line 568, in sage.structure.element.Element._richcmp
      File "element.pyx", line 554, in sage.structure.element.Element._richcmp_
      File "element.pyx", line 595, in sage.structure.element.Element._richcmp
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/maple.py", line 675, in __cmp__
        raise RuntimeError, e
    RuntimeError: An error occured running a Maple command:
    INPUT:
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    OUTPUT:
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    Error, "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp"
    is an empty file
**********************************************************************
File "maple.py", line 654:
    sage: maple.eval('testeq(%s = %s)'%(t.name(),u.name()))
Expected:
    'true'
Got:
    ''
**********************************************************************
File "maple.py", line 691:
    sage: t*u
Expected:
    15
Got:
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp
**********************************************************************
File "maple.py", line 695:
    sage: Mm*Mm
Expected:
    Matrix(2, 2, [[2,3],[6,11]])
Got:
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp
**********************************************************************
File "maple.py", line 700:
    sage: vm*Mm
Expected:
    Vector[row](2, [6,11])
Got:
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp
**********************************************************************
File "maple.py", line 703:
    sage: t*Mm
Expected:
    Matrix(2, 2, [[0,5],[10,15]])
Got:
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    9
**********************************************************************
File "maple.py", line 723:
    sage: maple(x)
Expected:
    x
Got:
    <BLANKLINE>
**********************************************************************
File "maple.py", line 725:
    sage: maple(5)
Expected:
    5
Got:
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp
**********************************************************************
File "maple.py", line 728:
    sage: maple(M)
Expected:
    Matrix(2, 2, [[0,1],[2,3]])
Got:
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp";
    sage15
**********************************************************************
File "maple.py", line 739:
    sage: print latex(maple('(x^4 - y)/(y^2-3*x)'))      # optional
Expected:
    {\frac {{x}^{4}-y}{{y}^{2}-3\,x}}
Got:
    <BLANKLINE>
**********************************************************************
File "maple.py", line 741:
    sage: print latex(maple(pi - e^3))                   # optional
Expected:
    \pi - \left( {e^{1}} \right) ^{3}
Got:
    read "/Users/was/.sage//temp/dhcp46_76.ipam.ucla.edu/43017//interface//tmp
**********************************************************************
8 items had failures:
  21 of  26 in __main__.example_0
   5 of   7 in __main__.example_14
   2 of   4 in __main__.example_17
   4 of   6 in __main__.example_18
  11 of  19 in __main__.example_19
   4 of   9 in __main__.example_20
   3 of   5 in __main__.example_21
   2 of   2 in __main__.example_22
***Test Failed*** 52 failures.
For whitespace errors, see the file .doctest_maple.py
	 [14.3 s]
exit code: 256
 
----------------------------------------------------------------------
The following tests failed:


	sage -t --optional maple.py
Total time for all tests: 14.3 seconds
```



---

Comment by was created at 2008-02-09 00:02:21

Changing status from new to assigned.


---

Attachment

The attached patch trac-2120-maple_interface.patch completely fixes all these problems on Maple with OS X.   It may partly break things on Linux, maybe. (?)  I don't have a good net connection with access to Linux Maple right now for testing, but will someday and then post a followup patch that fixes any issues.

NOTE: This patch *vastly* improves the robustness of the Maple interface, to put it mildly.


---

Comment by craigcitro created at 2008-06-15 21:38:02

Changing keywords from "" to "editor_craigcitro".


---

Comment by mhansen created at 2008-06-15 21:38:33

I'll take care of this.


---

Comment by was created at 2009-01-21 11:55:12

With stock Maple 12 and stock sage-3.3.alpha0 on OS X, here's what happens (total disaster):

```
teragon-2:graphics wstein$ ~/build/sage-3.3.alpha0/sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: maple('2+2')
| Sage Version 3.3.alpha0, Release Date: 2009-01-19                  |
| Type notebook() for the GUI, and license() for information.        |
sage: maple('2+2')
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/wstein/.sage/temp/teragon_2.local/96783/_Users_wstein__sage_init_sage_0.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/Users/wstein/build/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in __call__(self, x, name)
    963             return x
    964         if isinstance(x, basestring):
--> 965             return cls(self, x, name=name)
    966         try:
    967             return self._coerce_from_special_method(x)

/Users/wstein/build/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in __init__(self, parent, value, is_name, name)
   1333             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:
   1334                 self._session_number = -1
-> 1335                 raise TypeError, x
   1336         self._session_number = parent._session_number
   1337 

TypeError: An error occured running a Maple command:
INPUT:
read "/Users/wstein/.sage//temp/teragon_2.local/96783//interface//tmp96783";
OUTPUT:
read "/Users/wstein/.sage//temp/teragon_2.local/96783//interface//tmp96783";
on line 2, syntax error, `)` unexpected:
age0);
    ^
Error, while reading
`/Users/wstein/.sage//temp/teragon_2.local/96783//interface//tmp96783`

```



---

Comment by was created at 2009-01-24 01:00:45

I tried today, and 
   * maple 12 works fine on OS X (for me).  Perfect in fact.
   * maple 12 on linux, fails totally:

```
wstein@sage:~$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: maple('2+3')
| Sage Version 3.2.3, Release Date: 2009-01-05                       |
| Type notebook() for the GUI, and license() for information.        |
sage: maple('2+3')
read "/scratch/wstein/sage//temp/sage.math.washington.edu/1285//interface/
```



---

Comment by was created at 2009-01-24 01:04:13

the poor attached patch:

```
Hunk #1 FAILED at 859
Hunk #2 succeeded at 1496 with fuzz 2 (offset 382 lines).
1 out of 2 hunks FAILED -- saving rejects to file sage/interfaces/expect.py.rej
patching file sage/interfaces/maple.py
Hunk #3 FAILED at 245
Hunk #4 FAILED at 390
Hunk #5 FAILED at 442
Hunk #6 FAILED at 606
4 out of 7 hunks FAILED -- saving rejects to file sage/interfaces/maple.py.rej
```



---

Attachment

The second patch rebases the *much* earlier patch.  It makes doctests and the command line work for me on sage.math, but not having maple I need testers on consumer linux distros and especially Mac OS X.


---

Comment by was created at 2009-04-01 13:01:15

It hangs forever on using it with Maple 12 on my Mac laptop:

```
sage: maple('2+3')
[hang forever]
```

I'll install Maple 12 on my beefy office desktop OS X box (bsd.math.washington.edu), and give you an account.


---

Comment by was created at 2009-04-01 13:32:18

By the way, the code *currently* in sage-3.4 works fine with Maple 12 on OS X on my laptop.  So the patch breaks things for OS X.


---

Comment by malb created at 2009-08-25 22:55:37

Here is what I currently get with Maple 11:


```
sage -t --optional "devel/sage-main/sage/interfaces/maple.py"            
**********************************************************************   
File "/usr/local/sage-4.1/devel/sage-main/sage/interfaces/maple.py", line 29:
    sage: maple.eval('ifactor(2005)')                    # optional - maple  
Expected:                                                                    
    '"(5)*"(401)'                                                            
Got:                                                                         
    '``(5)*``(401)'                                                          
**********************************************************************       
File "/usr/local/sage-4.1/devel/sage-main/sage/interfaces/maple.py", line 31:
    sage: maple.ifactor(2005)                            # optional - maple  
Expected:                                                                    
    "(5)*"(401)                                                              
Got:                                                                         
    ``(5)*``(401)                                                            
**********************************************************************       
File "/usr/local/sage-4.1/devel/sage-main/sage/interfaces/maple.py", line 188:
    sage: maple.ifactor(maple.fibonacci(27))     # optional - maple
Expected:
    "(2)*"(17)*"(53)*"(109)
Got:
    ``(2)*``(17)*``(53)*``(109)
**********************************************************************
File "/usr/local/sage-4.1/devel/sage-main/sage/interfaces/maple.py", line 1068:
    sage: print latex(maple(pi - e^3))                   # optional -- requires maple
Expected:
    \pi - \left( {e^{1}} \right) ^{3}
Got:
    \pi-{e^{3}}
**********************************************************************
2 items had failures:
   3 of  28 in __main__.example_0
   1 of   4 in __main__.example_40
***Test Failed*** 4 failures.
For whitespace errors, see the file /usr/local/sage-4.1/tmp/.doctest_maple.py
         [21.0 s]
```



---

Comment by abbot created at 2011-06-04 19:34:41

I have tested this patch on Linux/x86_64 (Fedora 14) with sage-4.4.1 and Maple 13, and also Maple 11. It does fix the problem. Test output with Maple 13:


```
sage -t --optional "devel/sage-main/sage/interfaces/maple.py"
**********************************************************************
File "/opt/sage-4.4.1/devel/sage-main/sage/interfaces/maple.py", line 1013:
    sage: u == t                                   # optional -- requires maple
Expected:
    True
Got:
    False
**********************************************************************
File "/opt/sage-4.4.1/devel/sage-main/sage/interfaces/maple.py", line 1118:
    sage: print latex(maple(pi - e^3))                   # optional -- requires maple
Expected:
    \pi - \left( {e^{1}} \right) ^{3}
Got:
    \pi-{{\rm e}^{3}}
**********************************************************************
2 items had failures:
   1 of  22 in __main__.example_36
   1 of   4 in __main__.example_40
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/shamardin/.sage//tmp/.doctest_maple.py
	 [39.6 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t --optional "devel/sage-main/sage/interfaces/maple.py"
Total time for all tests: 39.6 seconds
```



---

Comment by robertwb created at 2012-12-30 00:26:31

As of sage 5.5


```
	sage -t --only-optional=maple devel/sage/sage/symbolic/expression.pyx # 2 doctests failed
	sage -t --only-optional=maple devel/sage/sage/symbolic/integration/integral.py # 2 doctests failed
	sage -t --only-optional=maple devel/sage/sage/calculus/calculus.py # 1 doctests failed
	sage -t --only-optional=maple devel/sage/sage/misc/functional.py # 1 doctests failed
	sage -t --only-optional=maple devel/sage/sage/tests/benchmark.py # 5 doctests failed
	sage -t --only-optional=maple devel/sage/sage/interfaces/maple.py # 123 doctests failed
```


Related: #13540


---

Comment by jdemeyer created at 2013-01-01 13:35:26

Changing keywords from "editor_craigcitro" to "".


---

Comment by migeruhito created at 2013-02-16 17:30:52

See Ticket #12295


---

Comment by mmezzarobba created at 2014-03-15 18:38:00

close in favor of #12295, which is more up to date?


---

Comment by mmezzarobba created at 2014-03-15 18:38:00

Changing status from needs_work to needs_review.


---

Comment by rws created at 2014-03-24 15:41:16

Yes, since there is apparently a fix attached for sage-5.9, while the last comment here concerns 5.5.


---

Comment by rws created at 2014-03-24 15:41:16

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-03-31 12:27:12

Resolution: duplicate
