# Issue 5999: faster recognise if there is no discrete log

Issue created by migration from https://trac.sagemath.org/ticket/5999

Original creator: gerrob

Original creation time: 2009-05-06 18:57:37

Assignee: was

Keywords: discrete log, factor

Just one example:
sage: n=15*(factorial(54)+1);a=Mod(8,n);b=Mod(7,n);discrete_log(a,b)

And this takes lots of time, because sage first factorize n, and this takes about 4 minutes on my pc. However after finding 3 and 5 as primefactors of n you can immediately observe that `7^x==8 mod 15` is unsolvable so the original problem also.

So the idea is that: get "small" prime(power) divisors of n by trial division/another method, and when you find a primepower divisor then check if the problem is still solvable or not.
