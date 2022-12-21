# Issue 630: mhansen's big combinatorics update

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2007-09-09 19:18:16

Assignee: mhansen

CC:  sage-combinat

Includes C interface for symmetrica.


---

Attachment


---

Comment by mhansen created at 2007-09-20 20:48:32

Bundle attached.


---

Attachment

NOTE:

The old partitions function (copied below), was vastly faster than the new
Partitions(n).list() for n=30...

```
def partitions(n):
    r"""
    Generator of all the partitions of the integer $n$.

    INPUT:
        n -- int

    To compute the number of partitions of $n$ use
    \code{number_of_partitions(n)}.

    EXAMPLES:
        sage.: partitions(3)
        <generator object at 0xab3b3eac>
        sage: list(partitions(3))
        [(1, 1, 1), (1, 2), (3,)]


    AUTHOR: Adapted from David Eppstein, Jan Van lent, George Yoshida;
    Python Cookbook 2, Recipe 19.16.
    """
    n == ZZ(n)
    # base case of the recursion: zero is the sum of the empty tuple
    if n == 0:
        yield ( )
        return
    # modify the partitions of n-1 to form the partitions of n
    for p in partitions(n-1):
        yield (1,) + p
        if p and (len(p) < 2 or p[1] > p[0]):
            yield (p[0] + 1,) + p[1:]
sage: time v=list(partitions(30))
CPU times: user 0.03 s, sys: 0.00 s, total: 0.03 s


--
[15:59] <william_stein> mhansen -- interestingly the *old* partitions function is way faster than your new one...??
[15:59] <william_stein> old:
[15:59] <william_stein> sage: time v=list(partitions(30))
[15:59] <william_stein> CPU times: user 0.03 s, sys: 0.00 s, total: 0.03 s
[15:59] <millster> aha
[15:59] <william_stein> new:
[15:59] <william_stein> sage: time v=Partitions(30).list()
[15:59] <william_stein> CPU times: user 0.46 s, sys: 0.02 s, total: 0.48 s
```



---

Comment by was created at 2007-09-20 23:16:43

Resolution: fixed


---

Attachment


---

Attachment
