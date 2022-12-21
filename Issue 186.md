# Issue 186: ECM str concactenation error

Issue created by migration from Trac.

Original creator: yi

Original creation time: 2006-12-19 00:34:57

Assignee: was

CC:  wstein@gmail.com

Keywords: ecm

sage: ECM().factor(2^100-1)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/yi/<ipython console> in <module>()

/Users/yi/Software/sage-1.5.1.2/local/lib/python2.5/site-packages/sage/interfaces/ecm.py in factor(self, n, factor_digits, B1, **kwds)
    235             last_B1 = 10
    236         if not _primality[1]: 
--> 237             factors[1:2] = self.factor(factors[1], B1=last_B1, **kwds)
    238             _primality[1:2] = self.primality
    239         if not _primality[0]: 

/Users/yi/Software/sage-1.5.1.2/local/lib/python2.5/site-packages/sage/interfaces/ecm.py in factor(self, n, factor_digits, B1, **kwds)
    235             last_B1 = 10
    236         if not _primality[1]: 
--> 237             factors[1:2] = self.factor(factors[1], B1=last_B1, **kwds)
    238             _primality[1:2] = self.primality
    239         if not _primality[0]: 

/Users/yi/Software/sage-1.5.1.2/local/lib/python2.5/site-packages/sage/interfaces/ecm.py in factor(self, n, factor_digits, B1, **kwds)
    238             _primality[1:2] = self.primality
    239         if not _primality[0]: 
--> 240             factors[0:1] = self.factor(factors[0], B1=last_B1, **kwds)
    241             _primality[0:1] = self.primality
    242         self.primality = _primality

/Users/yi/Software/sage-1.5.1.2/local/lib/python2.5/site-packages/sage/interfaces/ecm.py in factor(self, n, factor_digits, B1, **kwds)
    223             [197002597249, 1348959352853811313, 251951573867253012259144010843]
    224         """
--> 225         factors = self.find_factor(n, factor_digits, B1, **kwds)
    226         factors.sort()
    227         if len(factors) != 2: 

/Users/yi/Software/sage-1.5.1.2/local/lib/python2.5/site-packages/sage/interfaces/ecm.py in find_factor(self, n, factor_digits, B1, **kwds)
    179                     if not child.match.groups()[0] is None: 
    180                         child.kill(0)
--> 181                         return self.find_factor(n, B1=4+floor(B1/2), **kwds)
    182                     else: 
    183                         # primality testing is cheap compared to factoring, but has already been done

<type 'exceptions.TypeError'>: unsupported operand type(s) for /: 'str' and 'int'



---

Comment by was created at 2007-01-09 18:13:59

Fixed for sage-1.6.

```
rank4:~/d/sage/sage/interfaces was$ hg export 2315
# HG changeset patch
# User William Stein <wstein`@`gmail.com>
# Date 1168366339 28800
# Node ID 5e2621f3400050664fc52f68097a68a679bc5033
# Parent  158dfcee989ef03bf0caa3b5fc26d54cd589f6e2
Fix trac #186.  Also, fixed the documentation for ecm.factor, which was very misleading.

diff -r 158dfcee989e -r 5e2621f34000 sage/interfaces/ecm.py
--- a/sage/interfaces/ecm.py    Tue Jan 09 08:33:17 2007 -0800
+++ b/sage/interfaces/ecm.py    Tue Jan 09 10:12:19 2007 -0800
`@``@` -11,7 +11,7 `@``@` import re
 import re
 from math import ceil, floor
 
-import sage.rings.integer
+from sage.rings.integer import Integer
 from sage.misc.misc import verbose, get_verbose, tmp_filename
 
 import sage.misc.package
`@``@` -94,7 +94,7 `@``@` class ECM:
         return s
 
     def __call__(self, n, watch=False):
-        n = sage.rings.integer.Integer(n)
+        n = Integer(n)
         cmd = 'echo "%s" | %s'%(n, self.__cmd)
         if watch:
             t = tmp_filename()
`@``@` -155,7 +155,7 `@``@` class ECM:
         if not 'c' in kwds: kwds['c'] = 1000000000
         if not 'I' in kwds: kwds['I'] = 1
         if not factor_digits is None: 
-            B1 = self.recommended_B1(factor_digits);
+            B1 = self.recommended_B1(factor_digits)
         kwds['one'] = ''
         kwds['cofdec'] = ''
         self.__cmd = self._ECM__startup_cmd(B1, None, kwds)
`@``@` -178,17 +178,17 `@``@` class ECM:
                     self.primality = [false]
                     return [n]
                 else:
-                    p = sage.rings.integer.Integer(info[6])
+                    p = Integer(info[6])
                     child.expect('(input number)|(prime factor)|(composite factor)')
                     if not child.match.groups()[0] is None: 
                         child.kill(0)
-                        return self.find_factor(n, B1=4+floor(B1/2), **kwds)
+                        return self.find_factor(n, B1=4+floor(float(B1)/2), **kwds)
                     else: 
                         # primality testing is cheap compared to factoring, but has already been done
                         # return [p, n/p]
                         self.primality = [not child.match.groups()[1] is None]
                         child.expect('((prime cofactor)|(Composite cofactor)) (\d+)\D')
-                        q = sage.rings.integer.Integer(child.match.groups()[3])
+                        q = Integer(child.match.groups()[3])
                         self.primality += [not child.match.groups()[1] is None]
                         child.kill(0)
                         return [p, q]
`@``@` -203,33 +203,43 `@``@` class ECM:
 
     def factor(self, n, factor_digits=None, B1=2000, **kwds):
         """
-        Returns a list of all probable prime factors of n, using gmp-ecm.
+        Returns a list of integers whose product is n, computed using
+        gmp-ecm, and PARI for small factors.
+
+        ** WARNING: There is no guarantee that the factors returned are
+        prime. **
         
         INPUT:
             n -- a positive integer
             factor_digits -- optional guess at how many digits are in the smallest factor. 
             B1 -- initial lower bound, defaults to 2000 (15 digit factors)
-            kwds -- arguments to pass to ecm-gmp. See help for ECM for more details. 
-            
+            kwds -- arguments to pass to ecm-gmp. See help for ECM for more details.
+
         OUTPUT: 
-            factorization of n
+            a list of integers whose product is n
             
         NOTE: 
-            Trial division should typically be performed before using this method. 
-            Also, if you suspect that n is the product of two similarly-sized primes, 
-            other methods (such as pari's quadratic sieve) will usually be faster. 
+            Trial division should typically be performed before using
+            this method.  Also, if you suspect that n is the product
+            of two similarly-sized primes, other methods (such as a
+            quadratic sieve -- use the qsieve command) will usually be
+            faster.
         
         EXAMPLES: 
-            sage: ECM().factor(602400691612422154516282778947806249229526581)
+            sage: ecm.factor(602400691612422154516282778947806249229526581)
             [45949729863572179, 13109994191499930367061460439]
             
-            sage: ECM().factor((2^197 + 1)/3)           # takes a long time
+            sage: ecm.factor((2^197 + 1)/3)           # takes a long time
             [197002597249, 1348959352853811313, 251951573867253012259144010843]
         """
+        if B1 < 2000 or len(str(n)) < 15:
+            return sum([[p]*e for p, e in Integer(n).factor()], [])
+        
         factors = self.find_factor(n, factor_digits, B1, **kwds)
         factors.sort()
-        if len(factors) != 2: 
+        if len(factors) == 1: 
             return factors
+        assert len(factors) == 2
         _primality = [self.primality[0], self.primality[1]]
         try:
             last_B1 = self.last_params['B1']
`@``@` -260,7 +270,7 `@``@` class ECM:
             The parameters for the most recent factorization.
             
         EXAMPLES: 
-            sage: ecm.factor((2^197 + 1)/3)
+            sage: ecm.factor((2^197 + 1)/3)             # long time
             [197002597249, 1348959352853811313, 251951573867253012259144010843]
             sage: ecm.get_last_params()                 # random output
             {'poly': 'x^1', 'sigma': '1785694449', 'B1': '8885', 'B2': '1002846'}
`@``@` -284,11 +294,11 `@``@` class ECM:
         
             sage: n = next_prime(11^23)*next_prime(11^37)
                                 
-            sage.: ECM().time(n, 20)               
+            sage.: ecm.time(n, 20)               
             Expected curves: 77     Expected time: 7.21s
-            sage.: ECM().time(n, 25)               
+            sage.: ecm.time(n, 25)               
             Expected curves: 206    Expected time: 1.56m
-            sage.: ECM().time(n, 30, verbose=1)    
+            sage.: ecm.time(n, 30, verbose=1)    
             GMP-ECM 6.0.1 [powered by GMP 4.2] [ECM]
 
             Input number is 304481639541418099574459496544854621998616257489887231115912293 (63 digits)
`@``@` -349,4 +359,4 `@``@` class ECM:
         print "Expected curves:", curve_count, "\tExpected time:", time
 
 # unique instance
-ecm = ECM()
\ No newline at end of file
+ecm = ECM()
```



---

Comment by was created at 2007-01-09 18:13:59

Resolution: fixed
