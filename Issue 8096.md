# Issue 8096: Coersion of square matrices is slow

archive/issues_008096.json:
```json
{
    "body": "Assignee: was\n\nCC:  robertwb malb\n\nMultiplication of small square matrices is ridiculously slow:\n\n```\nsage: for d in range(1, 100):\n...    print d\n...    A = random_matrix(GF(3), d)\n...    B = random_matrix(GF(3), d)\n...    timeit(\"C = A*B\")\n    \n\n1\n625 loops, best of 3: 93.8 \u00b5s per loop\n2\n625 loops, best of 3: 93.9 \u00b5s per loop\n3\n625 loops, best of 3: 94.2 \u00b5s per loop\n4\n625 loops, best of 3: 94.1 \u00b5s per loop\n5\n625 loops, best of 3: 94.7 \u00b5s per loop\n6\n625 loops, best of 3: 94.9 \u00b5s per loop\n7\n625 loops, best of 3: 95.2 \u00b5s per loop\n8\n625 loops, best of 3: 95.8 \u00b5s per loop\n9\n625 loops, best of 3: 96.8 \u00b5s per loop\n10\n625 loops, best of 3: 97.6 \u00b5s per loop\n11\n625 loops, best of 3: 98.1 \u00b5s per loop\n12\n625 loops, best of 3: 101 \u00b5s per loop\n13\n625 loops, best of 3: 101 \u00b5s per loop\n14\n625 loops, best of 3: 104 \u00b5s per loop\n15\n625 loops, best of 3: 104 \u00b5s per loop\n16\n625 loops, best of 3: 108 \u00b5s per loop\n17\n625 loops, best of 3: 108 \u00b5s per loop\n18\n625 loops, best of 3: 113 \u00b5s per loop\n19\n625 loops, best of 3: 112 \u00b5s per loop\n20\n625 loops, best of 3: 118 \u00b5s per loop\n21\n625 loops, best of 3: 117 \u00b5s per loop\n22\n625 loops, best of 3: 125 \u00b5s per loop\n23\n625 loops, best of 3: 123 \u00b5s per loop\n24\n625 loops, best of 3: 133 \u00b5s per loop\n25\n625 loops, best of 3: 129 \u00b5s per loop\n26\n625 loops, best of 3: 143 \u00b5s per loop\n27\n625 loops, best of 3: 137 \u00b5s per loop\n28\n625 loops, best of 3: 155 \u00b5s per loop\n29\n625 loops, best of 3: 147 \u00b5s per loop\n30\n625 loops, best of 3: 166 \u00b5s per loop\n31\n625 loops, best of 3: 157 \u00b5s per loop\n32\n625 loops, best of 3: 179 \u00b5s per loop\n33\n625 loops, best of 3: 168 \u00b5s per loop\n34\n625 loops, best of 3: 196 \u00b5s per loop\n35\n625 loops, best of 3: 182 \u00b5s per loop\n36\n625 loops, best of 3: 214 \u00b5s per loop\n37\n625 loops, best of 3: 198 \u00b5s per loop\n38\n625 loops, best of 3: 234 \u00b5s per loop\n39\n625 loops, best of 3: 213 \u00b5s per loop\n40\n625 loops, best of 3: 255 \u00b5s per loop\n41\n625 loops, best of 3: 231 \u00b5s per loop\n42\n625 loops, best of 3: 279 \u00b5s per loop\n43\n625 loops, best of 3: 251 \u00b5s per loop\n44\n625 loops, best of 3: 307 \u00b5s per loop\n45\n625 loops, best of 3: 271 \u00b5s per loop\n46\n625 loops, best of 3: 335 \u00b5s per loop\n47\n625 loops, best of 3: 298 \u00b5s per loop\n48\n625 loops, best of 3: 363 \u00b5s per loop\n49\n625 loops, best of 3: 319 \u00b5s per loop\n50\n625 loops, best of 3: 401 \u00b5s per loop\n51\n625 loops, best of 3: 346 \u00b5s per loop\n```\n\n\nHere's a profile of the 1x1 case:\n\n\n```\n625 loops, best of 3: 91.7 \u00b5s per loop\n         810004 function calls in 5.980 CPU seconds\n\n   Ordered by: standard name\n\n   ncalls  tottime  percall  cumtime  percall filename:lineno(function)\n    40000    0.100    0.000    0.100    0.000 :0(IntegerMod)\n    30000    0.080    0.000    0.080    0.000 :0(append)\n    10000    0.030    0.000    0.030    0.000 :0(base_ring)\n    10000    0.150    0.000    0.900    0.000 :0(category)\n    40000    0.250    0.000    0.290    0.000 :0(has_key)\n    10000    0.070    0.000    0.070    0.000 :0(hasattr)\n    10000    0.030    0.000    0.030    0.000 :0(is_Matrix)\n    80000    0.250    0.000    0.250    0.000 :0(isinstance)\n    30000    0.070    0.000    0.070    0.000 :0(keys)\n    30000    0.040    0.000    0.040    0.000 :0(len)\n    30001    0.080    0.000    0.080    0.000 :0(range)\n    10000    0.030    0.000    0.030    0.000 :0(setdefault)\n        1    0.000    0.000    0.000    0.000 :0(setprofile)\n    30000    0.140    0.000    0.140    0.000 :0(sorted)\n        1    0.380    0.380    5.980    5.980 <string>:1(<module>)\n    30000    0.250    0.000    1.750    0.000 cachefunc.py:155(get_key)\n    10000    0.060    0.000    0.850    0.000 cachefunc.py:220(__call__)\n    10000    0.060    0.000    0.090    0.000 cachefunc.py:254(get_cache)\n    10000    0.050    0.000    0.050    0.000 cachefunc.py:275(__get__)\n    20000    0.270    0.000    1.550    0.000 cachefunc.py:76(__call__)\n    20000    0.060    0.000    0.060    0.000 cachefunc.py:95(get_cache)\n    10000    0.070    0.000    2.520    0.000 category.py:459(__contains__)\n    10000    0.360    0.000    1.550    0.000 category.py:651(is_subcategory)\n    20000    0.120    0.000    1.670    0.000 classcall_metaclass.py:64(__call__)\n    20000    0.040    0.000    0.040    0.000 finite_field_prime_modn.py:121(characteristic)\n    20000    0.110    0.000    0.110    0.000 finite_field_prime_modn.py:187(order)\n    30000    1.010    0.000    1.500    0.000 function_mangling.py:205(fix_to_pos)\n    30000    0.080    0.000    0.080    0.000 function_mangling.py:261(<genexpr>)\n    40000    0.290    0.000    0.390    0.000 integer_mod_ring.py:733(__call__)\n    10000    0.050    0.000    0.070    0.000 matrix_group_element.py:68(is_MatrixGroupElement)\n    10000    0.450    0.000    0.710    0.000 matrix_space.py:1035(matrix)\n    10000    0.140    0.000    4.000    0.000 matrix_space.py:1089(matrix_space)\n    10000    0.200    0.000    3.830    0.000 matrix_space.py:110(MatrixSpace)\n    10000    0.000    0.000    0.000    0.000 matrix_space.py:1112(ncols)\n    10000    0.030    0.000    0.030    0.000 matrix_space.py:1124(nrows)\n    10000    0.310    0.000    1.270    0.000 matrix_space.py:271(__call__)\n    10000    0.000    0.000    0.000    0.000 misc.py:514(get_verbose)\n        1    0.000    0.000    5.980    5.980 profile:0(for i in range(10000): C = A*B)\n        0    0.000             0.000          profile:0(profiler)\n    90000    0.270    0.000    0.270    0.000 unique_representation.py:454(__eq__)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8096\n\n",
    "created_at": "2010-01-27T20:32:00Z",
    "labels": [
        "linear algebra",
        "minor",
        "bug"
    ],
    "title": "Coersion of square matrices is slow",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8096",
    "user": "boothby"
}
```
Assignee: was

CC:  robertwb malb

Multiplication of small square matrices is ridiculously slow:

```
sage: for d in range(1, 100):
...    print d
...    A = random_matrix(GF(3), d)
...    B = random_matrix(GF(3), d)
...    timeit("C = A*B")
    

1
625 loops, best of 3: 93.8 µs per loop
2
625 loops, best of 3: 93.9 µs per loop
3
625 loops, best of 3: 94.2 µs per loop
4
625 loops, best of 3: 94.1 µs per loop
5
625 loops, best of 3: 94.7 µs per loop
6
625 loops, best of 3: 94.9 µs per loop
7
625 loops, best of 3: 95.2 µs per loop
8
625 loops, best of 3: 95.8 µs per loop
9
625 loops, best of 3: 96.8 µs per loop
10
625 loops, best of 3: 97.6 µs per loop
11
625 loops, best of 3: 98.1 µs per loop
12
625 loops, best of 3: 101 µs per loop
13
625 loops, best of 3: 101 µs per loop
14
625 loops, best of 3: 104 µs per loop
15
625 loops, best of 3: 104 µs per loop
16
625 loops, best of 3: 108 µs per loop
17
625 loops, best of 3: 108 µs per loop
18
625 loops, best of 3: 113 µs per loop
19
625 loops, best of 3: 112 µs per loop
20
625 loops, best of 3: 118 µs per loop
21
625 loops, best of 3: 117 µs per loop
22
625 loops, best of 3: 125 µs per loop
23
625 loops, best of 3: 123 µs per loop
24
625 loops, best of 3: 133 µs per loop
25
625 loops, best of 3: 129 µs per loop
26
625 loops, best of 3: 143 µs per loop
27
625 loops, best of 3: 137 µs per loop
28
625 loops, best of 3: 155 µs per loop
29
625 loops, best of 3: 147 µs per loop
30
625 loops, best of 3: 166 µs per loop
31
625 loops, best of 3: 157 µs per loop
32
625 loops, best of 3: 179 µs per loop
33
625 loops, best of 3: 168 µs per loop
34
625 loops, best of 3: 196 µs per loop
35
625 loops, best of 3: 182 µs per loop
36
625 loops, best of 3: 214 µs per loop
37
625 loops, best of 3: 198 µs per loop
38
625 loops, best of 3: 234 µs per loop
39
625 loops, best of 3: 213 µs per loop
40
625 loops, best of 3: 255 µs per loop
41
625 loops, best of 3: 231 µs per loop
42
625 loops, best of 3: 279 µs per loop
43
625 loops, best of 3: 251 µs per loop
44
625 loops, best of 3: 307 µs per loop
45
625 loops, best of 3: 271 µs per loop
46
625 loops, best of 3: 335 µs per loop
47
625 loops, best of 3: 298 µs per loop
48
625 loops, best of 3: 363 µs per loop
49
625 loops, best of 3: 319 µs per loop
50
625 loops, best of 3: 401 µs per loop
51
625 loops, best of 3: 346 µs per loop
```


Here's a profile of the 1x1 case:


```
625 loops, best of 3: 91.7 µs per loop
         810004 function calls in 5.980 CPU seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    40000    0.100    0.000    0.100    0.000 :0(IntegerMod)
    30000    0.080    0.000    0.080    0.000 :0(append)
    10000    0.030    0.000    0.030    0.000 :0(base_ring)
    10000    0.150    0.000    0.900    0.000 :0(category)
    40000    0.250    0.000    0.290    0.000 :0(has_key)
    10000    0.070    0.000    0.070    0.000 :0(hasattr)
    10000    0.030    0.000    0.030    0.000 :0(is_Matrix)
    80000    0.250    0.000    0.250    0.000 :0(isinstance)
    30000    0.070    0.000    0.070    0.000 :0(keys)
    30000    0.040    0.000    0.040    0.000 :0(len)
    30001    0.080    0.000    0.080    0.000 :0(range)
    10000    0.030    0.000    0.030    0.000 :0(setdefault)
        1    0.000    0.000    0.000    0.000 :0(setprofile)
    30000    0.140    0.000    0.140    0.000 :0(sorted)
        1    0.380    0.380    5.980    5.980 <string>:1(<module>)
    30000    0.250    0.000    1.750    0.000 cachefunc.py:155(get_key)
    10000    0.060    0.000    0.850    0.000 cachefunc.py:220(__call__)
    10000    0.060    0.000    0.090    0.000 cachefunc.py:254(get_cache)
    10000    0.050    0.000    0.050    0.000 cachefunc.py:275(__get__)
    20000    0.270    0.000    1.550    0.000 cachefunc.py:76(__call__)
    20000    0.060    0.000    0.060    0.000 cachefunc.py:95(get_cache)
    10000    0.070    0.000    2.520    0.000 category.py:459(__contains__)
    10000    0.360    0.000    1.550    0.000 category.py:651(is_subcategory)
    20000    0.120    0.000    1.670    0.000 classcall_metaclass.py:64(__call__)
    20000    0.040    0.000    0.040    0.000 finite_field_prime_modn.py:121(characteristic)
    20000    0.110    0.000    0.110    0.000 finite_field_prime_modn.py:187(order)
    30000    1.010    0.000    1.500    0.000 function_mangling.py:205(fix_to_pos)
    30000    0.080    0.000    0.080    0.000 function_mangling.py:261(<genexpr>)
    40000    0.290    0.000    0.390    0.000 integer_mod_ring.py:733(__call__)
    10000    0.050    0.000    0.070    0.000 matrix_group_element.py:68(is_MatrixGroupElement)
    10000    0.450    0.000    0.710    0.000 matrix_space.py:1035(matrix)
    10000    0.140    0.000    4.000    0.000 matrix_space.py:1089(matrix_space)
    10000    0.200    0.000    3.830    0.000 matrix_space.py:110(MatrixSpace)
    10000    0.000    0.000    0.000    0.000 matrix_space.py:1112(ncols)
    10000    0.030    0.000    0.030    0.000 matrix_space.py:1124(nrows)
    10000    0.310    0.000    1.270    0.000 matrix_space.py:271(__call__)
    10000    0.000    0.000    0.000    0.000 misc.py:514(get_verbose)
        1    0.000    0.000    5.980    5.980 profile:0(for i in range(10000): C = A*B)
        0    0.000             0.000          profile:0(profiler)
    90000    0.270    0.000    0.270    0.000 unique_representation.py:454(__eq__)
```


Issue created by migration from https://trac.sagemath.org/ticket/8096





---

archive/issue_comments_070973.json:
```json
{
    "body": "Changing assignee from was to boothby.",
    "created_at": "2010-01-27T22:11:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-70973",
    "user": "boothby"
}
```

Changing assignee from was to boothby.



---

archive/issue_comments_070974.json:
```json
{
    "body": "Attachment [8096-new_matrix.patch](tarball://root/attachments/some-uuid/ticket8096/8096-new_matrix.patch) by boothby created at 2010-01-28 01:03:44",
    "created_at": "2010-01-28T01:03:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-70974",
    "user": "boothby"
}
```

Attachment [8096-new_matrix.patch](tarball://root/attachments/some-uuid/ticket8096/8096-new_matrix.patch) by boothby created at 2010-01-28 01:03:44



---

archive/issue_comments_070975.json:
```json
{
    "body": "I'm not sure that I did this in the right place, but it cuts the time to multiply two 1x1 matrices down to 1/3 of the previous time -- which is still dog slow, but significantly better.  As a reference,\n\n\n```\nsage: A = GF(3).random_element()\nsage: B = GF(3).random_element()\nsage: timeit(\"C = A*B\")\n625 loops, best of 3: 142 ns per loop\n```\n\n\nand with this patch, I'm getting:\n\n\n```\nsage: d = 1\nsage: A = random_matrix(GF(3), d)\nsage: B = random_matrix(GF(3), d)\nsage: timeit(\"C = A*B\")\n625 loops, best of 3: 32.5 \u00b5s per loop\n\nsage: import profile\nsage: profile.run(\"for i in range(10000): C = A*B\")\n         250004 function calls in 1.840 CPU seconds\n\n   Ordered by: standard name\n\n   ncalls  tottime  percall  cumtime  percall filename:lineno(function)\n    40000    0.120    0.000    0.120    0.000 :0(IntegerMod)\n    10000    0.070    0.000    0.070    0.000 :0(hasattr)\n    10000    0.060    0.000    0.060    0.000 :0(is_Matrix)\n    70000    0.190    0.000    0.190    0.000 :0(isinstance)\n        1    0.000    0.000    0.000    0.000 :0(range)\n        1    0.000    0.000    0.000    0.000 :0(setprofile)\n        1    0.400    0.400    1.840    1.840 <string>:1(<module>)\n    20000    0.060    0.000    0.060    0.000 finite_field_prime_modn.py:121(characteristic)\n    40000    0.230    0.000    0.350    0.000 integer_mod_ring.py:733(__call__)\n    10000    0.060    0.000    0.070    0.000 matrix_group_element.py:68(is_MatrixGroupElement)\n    10000    0.390    0.000    0.720    0.000 matrix_space.py:1035(matrix)\n    10000    0.030    0.000    0.030    0.000 matrix_space.py:1112(ncols)\n    10000    0.020    0.000    0.020    0.000 matrix_space.py:1124(nrows)\n    10000    0.160    0.000    1.100    0.000 matrix_space.py:271(__call__)\n    10000    0.050    0.000    0.050    0.000 misc.py:514(get_verbose)\n        1    0.000    0.000    1.840    1.840 profile:0(for i in range(10000): C = A*B)\n        0    0.000             0.000          profile:0(profiler)\n```\n",
    "created_at": "2010-01-28T01:11:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-70975",
    "user": "boothby"
}
```

I'm not sure that I did this in the right place, but it cuts the time to multiply two 1x1 matrices down to 1/3 of the previous time -- which is still dog slow, but significantly better.  As a reference,


```
sage: A = GF(3).random_element()
sage: B = GF(3).random_element()
sage: timeit("C = A*B")
625 loops, best of 3: 142 ns per loop
```


and with this patch, I'm getting:


```
sage: d = 1
sage: A = random_matrix(GF(3), d)
sage: B = random_matrix(GF(3), d)
sage: timeit("C = A*B")
625 loops, best of 3: 32.5 µs per loop

sage: import profile
sage: profile.run("for i in range(10000): C = A*B")
         250004 function calls in 1.840 CPU seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    40000    0.120    0.000    0.120    0.000 :0(IntegerMod)
    10000    0.070    0.000    0.070    0.000 :0(hasattr)
    10000    0.060    0.000    0.060    0.000 :0(is_Matrix)
    70000    0.190    0.000    0.190    0.000 :0(isinstance)
        1    0.000    0.000    0.000    0.000 :0(range)
        1    0.000    0.000    0.000    0.000 :0(setprofile)
        1    0.400    0.400    1.840    1.840 <string>:1(<module>)
    20000    0.060    0.000    0.060    0.000 finite_field_prime_modn.py:121(characteristic)
    40000    0.230    0.000    0.350    0.000 integer_mod_ring.py:733(__call__)
    10000    0.060    0.000    0.070    0.000 matrix_group_element.py:68(is_MatrixGroupElement)
    10000    0.390    0.000    0.720    0.000 matrix_space.py:1035(matrix)
    10000    0.030    0.000    0.030    0.000 matrix_space.py:1112(ncols)
    10000    0.020    0.000    0.020    0.000 matrix_space.py:1124(nrows)
    10000    0.160    0.000    1.100    0.000 matrix_space.py:271(__call__)
    10000    0.050    0.000    0.050    0.000 misc.py:514(get_verbose)
        1    0.000    0.000    1.840    1.840 profile:0(for i in range(10000): C = A*B)
        0    0.000             0.000          profile:0(profiler)
```




---

archive/issue_comments_070976.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-28T01:11:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-70976",
    "user": "boothby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070977.json:
```json
{
    "body": "Replying to [comment:2 boothby]:\n\n> ... As a reference, ` sage: A = GF(3).random_element() sage: B = GF(3).random_element() sage: timeit(\"C = A*B\") 625 loops, best of 3: ``142 ns`` per loop ` and with this patch, I'm getting: {{{ sage: d = 1 sage: A = random_matrix(GF(3), d) sage: B = random_matrix(GF(3), d) sage: timeit(\"C = A*B\") 625 loops, best of 3: 32.5 \u00b5s per loop\n\nBut 32.5 \u00b5s (with the patch) is much *slower *than `142 ns (without the patch)!`",
    "created_at": "2010-01-30T23:44:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-70977",
    "user": "SimonKing"
}
```

Replying to [comment:2 boothby]:

> ... As a reference, ` sage: A = GF(3).random_element() sage: B = GF(3).random_element() sage: timeit("C = A*B") 625 loops, best of 3: ``142 ns`` per loop ` and with this patch, I'm getting: {{{ sage: d = 1 sage: A = random_matrix(GF(3), d) sage: B = random_matrix(GF(3), d) sage: timeit("C = A*B") 625 loops, best of 3: 32.5 µs per loop

But 32.5 µs (with the patch) is much *slower *than `142 ns (without the patch)!`



---

archive/issue_comments_070978.json:
```json
{
    "body": "You'll note that the 32.5\u00b5s is matrix-by-matrix, whereas the 142ns is element-by-element.  Before my patch, the matrix-by-matrix time was 101\u00b5s.\n\nI'd like the 32.5\u00b5s to go away, but I don't know how much of that would be possible, at the moment.",
    "created_at": "2010-01-31T06:36:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-70978",
    "user": "boothby"
}
```

You'll note that the 32.5µs is matrix-by-matrix, whereas the 142ns is element-by-element.  Before my patch, the matrix-by-matrix time was 101µs.

I'd like the 32.5µs to go away, but I don't know how much of that would be possible, at the moment.



---

archive/issue_comments_070979.json:
```json
{
    "body": "Replying to [comment:4 boothby]:\n\n> You'll note that the 32.5\u00b5s is matrix-by-matrix, whereas the 142ns is element-by-element.  Before my patch, the matrix-by-matrix time was 101\u00b5s. I'd like the 32.5\u00b5s to go away, but I don't know how much of that would be possible, at the moment.\n\nOK, then it is an improvement. I hope to be able to do some refereeing later today or tomorrow.\n\nAnyway, I still wonder why basic matrix operations in Sage tend to be so slow. I mean, do any complicated operations with parents happen behind the scenes? By \"slow\", I mean \"compared with MeatAxe matrices as provided by my cohomology spkg\":\n\n\n```\nsage: from pGroupCohomology.mtx import MTX\nsage: F = GF(3)\nsage: A = random_matrix(F,3)\nsage: B = random_matrix(F,3)\nsage: a = MTX(3,[list(r) for r in A.rows()])\nsage: b = MTX(3,[list(r) for r in B.rows()])\nsage: timeit(\"C=A*B\")\n625 loops, best of 3: 99.6 \u00c2\u00b5s per loop\nsage: timeit(\"c=a*b\")\n625 loops, best of 3: 1.01 \u00c2\u00b5s per loop\nsage: a*b == MTX(3,[list(r) for r in C.rows()])\nTrue\nsage: A = random_matrix(F,100)\nsage: B = random_matrix(F,100)\nsage: a = MTX(3,[list(r) for r in A.rows()])\nsage: b = MTX(3,[list(r) for r in B.rows()])\nsage: timeit(\"C=A*B\")\n125 loops, best of 3: 2.43 ms per loop\nsage: timeit(\"c=a*b\")\n625 loops, best of 3: 376 \u00c2\u00b5s per loop\nsage: a*b == MTX(3,[list(r) for r in C.rows()])\nTrue\n```\n",
    "created_at": "2010-01-31T09:41:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-70979",
    "user": "SimonKing"
}
```

Replying to [comment:4 boothby]:

> You'll note that the 32.5µs is matrix-by-matrix, whereas the 142ns is element-by-element.  Before my patch, the matrix-by-matrix time was 101µs. I'd like the 32.5µs to go away, but I don't know how much of that would be possible, at the moment.

OK, then it is an improvement. I hope to be able to do some refereeing later today or tomorrow.

Anyway, I still wonder why basic matrix operations in Sage tend to be so slow. I mean, do any complicated operations with parents happen behind the scenes? By "slow", I mean "compared with MeatAxe matrices as provided by my cohomology spkg":


```
sage: from pGroupCohomology.mtx import MTX
sage: F = GF(3)
sage: A = random_matrix(F,3)
sage: B = random_matrix(F,3)
sage: a = MTX(3,[list(r) for r in A.rows()])
sage: b = MTX(3,[list(r) for r in B.rows()])
sage: timeit("C=A*B")
625 loops, best of 3: 99.6 Âµs per loop
sage: timeit("c=a*b")
625 loops, best of 3: 1.01 Âµs per loop
sage: a*b == MTX(3,[list(r) for r in C.rows()])
True
sage: A = random_matrix(F,100)
sage: B = random_matrix(F,100)
sage: a = MTX(3,[list(r) for r in A.rows()])
sage: b = MTX(3,[list(r) for r in B.rows()])
sage: timeit("C=A*B")
125 loops, best of 3: 2.43 ms per loop
sage: timeit("c=a*b")
625 loops, best of 3: 376 Âµs per loop
sage: a*b == MTX(3,[list(r) for r in C.rows()])
True
```




---

archive/issue_comments_070980.json:
```json
{
    "body": "Replying to [comment:5 SimonKing]:\n\n> Anyway, I still wonder why basic matrix operations in Sage tend to be so slow. I mean, do any complicated operations with parents happen behind the scenes? By \"slow\", I mean \"compared with MeatAxe matrices as provided by my cohomology spkg\":\n\nThis is because they have only been optimized for large dimension and word-sized p. I bet MeatAxe is slower for 1000 x 1000 matrices.",
    "created_at": "2010-01-31T10:18:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-70980",
    "user": "robertwb"
}
```

Replying to [comment:5 SimonKing]:

> Anyway, I still wonder why basic matrix operations in Sage tend to be so slow. I mean, do any complicated operations with parents happen behind the scenes? By "slow", I mean "compared with MeatAxe matrices as provided by my cohomology spkg":

This is because they have only been optimized for large dimension and word-sized p. I bet MeatAxe is slower for 1000 x 1000 matrices.



---

archive/issue_comments_070981.json:
```json
{
    "body": "Replying to [comment:6 robertwb]:\n\n> This is because they have only been optimized for large dimension and word-sized p. I bet MeatAxe is slower for 1000 x 1000 matrices.\n\nYou just lost the bet.\n\n\n```\nsage: from pGroupCohomology.mtx import MTX\nsage: F = GF(3)\nsage: A = random_matrix(F,2000)\nsage: B = random_matrix(F,2000)\nsage: a = MTX(3,[list(r) for r in A.rows()])\nsage: b = MTX(3,[list(r) for r in B.rows()])\nsage: timeit(\"C=A*B\")\n5 loops, best of 3: 12.6 s per loop\nsage: timeit(\"c=a*b\")\n5 loops, best of 3: 2.01 s per loop\nsage: C = A*B\nsage: a*b == MTX(3,[list(r) for r in C.rows()])\nTrue\n```\n\nWhen I did some benchmarks two years ago, I was often astonished how MeatAxe outperformed the usual matrices in Sage in basic operations such as computing hash, copying, getting the list of coefficients, changing a coefficient, etc: Hash and copying took *seconds* for size 10000x10000!\n\nI complained, and things did improve: hash and copy is alright. But with the above matrix, loads(dumps(A)) did not terminate after a minute, and ate 90% of my computer's memory.",
    "created_at": "2010-01-31T11:52:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-70981",
    "user": "SimonKing"
}
```

Replying to [comment:6 robertwb]:

> This is because they have only been optimized for large dimension and word-sized p. I bet MeatAxe is slower for 1000 x 1000 matrices.

You just lost the bet.


```
sage: from pGroupCohomology.mtx import MTX
sage: F = GF(3)
sage: A = random_matrix(F,2000)
sage: B = random_matrix(F,2000)
sage: a = MTX(3,[list(r) for r in A.rows()])
sage: b = MTX(3,[list(r) for r in B.rows()])
sage: timeit("C=A*B")
5 loops, best of 3: 12.6 s per loop
sage: timeit("c=a*b")
5 loops, best of 3: 2.01 s per loop
sage: C = A*B
sage: a*b == MTX(3,[list(r) for r in C.rows()])
True
```

When I did some benchmarks two years ago, I was often astonished how MeatAxe outperformed the usual matrices in Sage in basic operations such as computing hash, copying, getting the list of coefficients, changing a coefficient, etc: Hash and copying took *seconds* for size 10000x10000!

I complained, and things did improve: hash and copy is alright. But with the above matrix, loads(dumps(A)) did not terminate after a minute, and ate 90% of my computer's memory.



---

archive/issue_comments_070982.json:
```json
{
    "body": "Attachment [8096-zero-matrix.patch](tarball://root/attachments/some-uuid/ticket8096/8096-zero-matrix.patch) by robertwb created at 2010-01-31 13:05:19\n\napply on top of previous",
    "created_at": "2010-01-31T13:05:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-70982",
    "user": "robertwb"
}
```

Attachment [8096-zero-matrix.patch](tarball://root/attachments/some-uuid/ticket8096/8096-zero-matrix.patch) by robertwb created at 2010-01-31 13:05:19

apply on top of previous



---

archive/issue_comments_070983.json:
```json
{
    "body": "SimonKing: I'm impressed and depressed. Is MeatAxe's runtime a function of the characteristic? At least one can do\n\n\n```\nsage: A = random_matrix(GF(3), 2000)\nsage: B = random_matrix(GF(3), 2000)\nsage: %timeit A._multiply_linbox(B)\n5 loops, best of 3: 1.9 s per loop\n```\n\n\nbut I agree the current state of matrices are in quite a bit of a mess. Granted, most of this code was written *way* back before Sage had the quality control it has now, just to get something up and running, and hasn't been touched since. (They're pretty good over Z and Q, which is what I use...)\n\nTom: Your patch looks good, positive review to that. I've posted another patch which provides another 2x speedup. There's still a lot of cruft it goes through, and matrix_space could really stand to be cythonized (there are 3 mandatory Python calls on it every time a matrix is created), but I don't have time to dig through it now.",
    "created_at": "2010-01-31T13:18:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-70983",
    "user": "robertwb"
}
```

SimonKing: I'm impressed and depressed. Is MeatAxe's runtime a function of the characteristic? At least one can do


```
sage: A = random_matrix(GF(3), 2000)
sage: B = random_matrix(GF(3), 2000)
sage: %timeit A._multiply_linbox(B)
5 loops, best of 3: 1.9 s per loop
```


but I agree the current state of matrices are in quite a bit of a mess. Granted, most of this code was written *way* back before Sage had the quality control it has now, just to get something up and running, and hasn't been touched since. (They're pretty good over Z and Q, which is what I use...)

Tom: Your patch looks good, positive review to that. I've posted another patch which provides another 2x speedup. There's still a lot of cruft it goes through, and matrix_space could really stand to be cythonized (there are 3 mandatory Python calls on it every time a matrix is created), but I don't have time to dig through it now.



---

archive/issue_comments_070984.json:
```json
{
    "body": "Replying to [comment:8 robertwb]:\n\n> SimonKing: I'm impressed and depressed. Is MeatAxe's runtime a function of the characteristic?\n\nYes. Over a non-prime field:\n\n\n```\nsage: F = GF(8,'t')\nsage: A = random_matrix(F,2000)\nsage: B = random_matrix(F,2000)\nsage: from pGroupCohomology.mtx import MTX\nsage: a = MTX(8,[list(r) for r in A.rows()])\nsage: b = MTX(8,[list(r) for r in B.rows()])\nsage: %time c = a*b\nCPU times: user 5.19 s, sys: 0.00 s, total: 5.19 s\nWall time: 5.19 s\nsage: %time C = A*B\n```\n\nThe last line took several minutes, and it was not possible to interrupt with Ctrl-c. So, I had to kill the Python process.\n\nAnd with a bigger prime, comparing against linbox:\n\n\n```\nsage: F = GF(37)\nsage: A = random_matrix(F,2000)\nsage: B = random_matrix(F,2000)\nsage: a = MTX(37,[list(r) for r in A.rows()])\nsage: b = MTX(37,[list(r) for r in B.rows()])\nsage: %time c = a*b\nCPU times: user 11.83 s, sys: 0.00 s, total: 11.84 s\nWall time: 11.87 s\nsage: %time C = A._multiply_linbox(B)\nCPU times: user 1.82 s, sys: 0.00 s, total: 1.82 s\nWall time: 1.82 s\nsage: %time C = A*B\nCPU times: user 12.65 s, sys: 0.00 s, total: 12.65 s\nWall time: 12.70 s\n```\n\nIn other words, for bigger fields, linbox is clearly better than MeatAxe, but the overhead kills it.\n\n> At least one can do ` sage: A = random_matrix(GF(3), 2000) sage: B = random_matrix(GF(3), 2000) sage: %timeit A._multiply_linbox(B) 5 loops, best of 3: 1.9 s per loop`\n\nAgain, there is a huge overhead. But at what point? I mean, the parents of A and B are the same, so, it can't be in the coercion model. And if two matrices have the same parent, then I'd expect that `A*B` would simply call A._multiply_linbox(B).\n\n> Tom: Your patch looks good, positive review to that. I've posted another patch which provides another 2x speedup. There's still a lot of cruft it goes through, and matrix_space could really stand to be cythonized (there are 3 mandatory Python calls on it every time a matrix is created), but I don't have time to dig through it now.\n\nWhich means, a third person (e.g.) should review both Tom's and your patch, right?",
    "created_at": "2010-01-31T16:05:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-70984",
    "user": "SimonKing"
}
```

Replying to [comment:8 robertwb]:

> SimonKing: I'm impressed and depressed. Is MeatAxe's runtime a function of the characteristic?

Yes. Over a non-prime field:


```
sage: F = GF(8,'t')
sage: A = random_matrix(F,2000)
sage: B = random_matrix(F,2000)
sage: from pGroupCohomology.mtx import MTX
sage: a = MTX(8,[list(r) for r in A.rows()])
sage: b = MTX(8,[list(r) for r in B.rows()])
sage: %time c = a*b
CPU times: user 5.19 s, sys: 0.00 s, total: 5.19 s
Wall time: 5.19 s
sage: %time C = A*B
```

The last line took several minutes, and it was not possible to interrupt with Ctrl-c. So, I had to kill the Python process.

And with a bigger prime, comparing against linbox:


```
sage: F = GF(37)
sage: A = random_matrix(F,2000)
sage: B = random_matrix(F,2000)
sage: a = MTX(37,[list(r) for r in A.rows()])
sage: b = MTX(37,[list(r) for r in B.rows()])
sage: %time c = a*b
CPU times: user 11.83 s, sys: 0.00 s, total: 11.84 s
Wall time: 11.87 s
sage: %time C = A._multiply_linbox(B)
CPU times: user 1.82 s, sys: 0.00 s, total: 1.82 s
Wall time: 1.82 s
sage: %time C = A*B
CPU times: user 12.65 s, sys: 0.00 s, total: 12.65 s
Wall time: 12.70 s
```

In other words, for bigger fields, linbox is clearly better than MeatAxe, but the overhead kills it.

> At least one can do ` sage: A = random_matrix(GF(3), 2000) sage: B = random_matrix(GF(3), 2000) sage: %timeit A._multiply_linbox(B) 5 loops, best of 3: 1.9 s per loop`

Again, there is a huge overhead. But at what point? I mean, the parents of A and B are the same, so, it can't be in the coercion model. And if two matrices have the same parent, then I'd expect that `A*B` would simply call A._multiply_linbox(B).

> Tom: Your patch looks good, positive review to that. I've posted another patch which provides another 2x speedup. There's still a lot of cruft it goes through, and matrix_space could really stand to be cythonized (there are 3 mandatory Python calls on it every time a matrix is created), but I don't have time to dig through it now.

Which means, a third person (e.g.) should review both Tom's and your patch, right?



---

archive/issue_comments_070985.json:
```json
{
    "body": "With the patch, I get:\n\n\n```\nsage: F = GF(3)\nsage: A = random_matrix(F,3)\nsage: B = random_matrix(F,3)\nsage: %timeit C = A*B\n625 loops, best of 3: 14.9 \u00b5s per loop # was: 99.6 \u00c2\u00b5s\nsage: A = random_matrix(F,2000)\nsage: B = random_matrix(F,2000)\nsage: %timeit C = A*B\n5 loops, best of 3: 12.4 s per loop # was: 12.6 s\n```\n\nSo, there is only a small improvement. But it *is* an improvement.\n\nI currently do sage -testall. If it passes, I'll give it a positive review, and suggest to open two new tickets, one concerning the overhead in multiplying matrices, the other concerning the problem that loads(dumps()) fails on big matrices.",
    "created_at": "2010-01-31T16:31:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-70985",
    "user": "SimonKing"
}
```

With the patch, I get:


```
sage: F = GF(3)
sage: A = random_matrix(F,3)
sage: B = random_matrix(F,3)
sage: %timeit C = A*B
625 loops, best of 3: 14.9 µs per loop # was: 99.6 Âµs
sage: A = random_matrix(F,2000)
sage: B = random_matrix(F,2000)
sage: %timeit C = A*B
5 loops, best of 3: 12.4 s per loop # was: 12.6 s
```

So, there is only a small improvement. But it *is* an improvement.

I currently do sage -testall. If it passes, I'll give it a positive review, and suggest to open two new tickets, one concerning the overhead in multiplying matrices, the other concerning the problem that loads(dumps()) fails on big matrices.



---

archive/issue_comments_070986.json:
```json
{
    "body": "There are doctest failures after installing the patches. See http://sage.math.washington.edu/home/SimonKing/logs/8096test.log\n\nSome of these failures seem pretty severe. There are unexpected numerical values and recursion depth problems.\n\nDo you have an idea how such innocent-looking change can have such a big effect?",
    "created_at": "2010-01-31T17:47:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-70986",
    "user": "SimonKing"
}
```

There are doctest failures after installing the patches. See http://sage.math.washington.edu/home/SimonKing/logs/8096test.log

Some of these failures seem pretty severe. There are unexpected numerical values and recursion depth problems.

Do you have an idea how such innocent-looking change can have such a big effect?



---

archive/issue_comments_070987.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-31T17:47:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-70987",
    "user": "SimonKing"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_070988.json:
```json
{
    "body": "Looks to me like the second patch isn't compatible matrix_double_dense -- that's an easy fix.  I'm unsure of matrix_2x2, though.  I'll check these out after I get some homework done.",
    "created_at": "2010-02-01T00:17:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-70988",
    "user": "boothby"
}
```

Looks to me like the second patch isn't compatible matrix_double_dense -- that's an easy fix.  I'm unsure of matrix_2x2, though.  I'll check these out after I get some homework done.



---

archive/issue_comments_070989.json:
```json
{
    "body": "Hi Tom!\n\nHopefully your fix will work. This message is mainly to test whether it works with Firefox 3.0.6 on my desktop computer to commit a message starting in wysiwyg mode.",
    "created_at": "2010-02-01T08:24:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-70989",
    "user": "SimonKing"
}
```

Hi Tom!

Hopefully your fix will work. This message is mainly to test whether it works with Firefox 3.0.6 on my desktop computer to commit a message starting in wysiwyg mode.



---

archive/issue_comments_070990.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-03-17T06:01:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-70990",
    "user": "jason"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_070991.json:
```json
{
    "body": "I think it is worth while to revive that ticket!\n\nThere has been some work done in the past, e.g., on #10763 (already merged) and #11589. I therefore suggest to start with determining the status quo (performance wise). \n\nThe following is with sage-4.7.rc2 (which contains #10763) and #11589. I provide the timings with sage-4.6.2 in square brackets:\n\n```\nsage: F = GF(3)\nsage: A = random_matrix(F,3)\nsage: B = random_matrix(F,3)\nsage: %timeit C = A*B\n625 loops, best of 3: 36.6 \u00b5s per loop\n[625 loops, best of 3: 54.6 \u00b5s per loop]\nsage: A = random_matrix(F,2000)\nsage: B = random_matrix(F,2000)\nsage: %timeit C = A*B\n5 loops, best of 3: 8.36 s per loop\n[5 loops, best of 3: 8.27 s per loop]\n```\n\n\nSo, part of the issue with small matrices is resolved. The second patch [attachment:8096-new_matrix.patch] is actually obsoleted by #10763 and #11589, and the first patch needs to be rebased.\n\nHowever, large matrices are still not nice. We have seen that linbox provides a much faster multiplication. Wouldn't it be a valid approach to use linbox more often? Perhaps make it the default over finite fields?",
    "created_at": "2011-07-12T14:03:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-70991",
    "user": "SimonKing"
}
```

I think it is worth while to revive that ticket!

There has been some work done in the past, e.g., on #10763 (already merged) and #11589. I therefore suggest to start with determining the status quo (performance wise). 

The following is with sage-4.7.rc2 (which contains #10763) and #11589. I provide the timings with sage-4.6.2 in square brackets:

```
sage: F = GF(3)
sage: A = random_matrix(F,3)
sage: B = random_matrix(F,3)
sage: %timeit C = A*B
625 loops, best of 3: 36.6 µs per loop
[625 loops, best of 3: 54.6 µs per loop]
sage: A = random_matrix(F,2000)
sage: B = random_matrix(F,2000)
sage: %timeit C = A*B
5 loops, best of 3: 8.36 s per loop
[5 loops, best of 3: 8.27 s per loop]
```


So, part of the issue with small matrices is resolved. The second patch [attachment:8096-new_matrix.patch] is actually obsoleted by #10763 and #11589, and the first patch needs to be rebased.

However, large matrices are still not nice. We have seen that linbox provides a much faster multiplication. Wouldn't it be a valid approach to use linbox more often? Perhaps make it the default over finite fields?



---

archive/issue_comments_070992.json:
```json
{
    "body": "For the record: Today I slightly improved MeatAxe matrix initialisation (my MeatAxe wrapper relies on a modified/improved version of MeatAxe-2.2.4, and today I added memset). \n\nNow, multiplication of two random 2000x2000 matrices over GF(3) takes 1.72 seconds with MeatAxe (it used to be 11 seconds, without memset), compared to 1.65 seconds with _multiply_linbox and 8.34 seconds with plain Sage matrices.\n\nI really wonder why linbox isn't used by default.",
    "created_at": "2011-07-12T15:11:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-70992",
    "user": "SimonKing"
}
```

For the record: Today I slightly improved MeatAxe matrix initialisation (my MeatAxe wrapper relies on a modified/improved version of MeatAxe-2.2.4, and today I added memset). 

Now, multiplication of two random 2000x2000 matrices over GF(3) takes 1.72 seconds with MeatAxe (it used to be 11 seconds, without memset), compared to 1.65 seconds with _multiply_linbox and 8.34 seconds with plain Sage matrices.

I really wonder why linbox isn't used by default.



---

archive/issue_comments_070993.json:
```json
{
    "body": "I guess that the generic Strassen-Winograd implementation in sage.matrix.strassen is related with, but not really in the focus of, this ticket. Therefore I opened a new ticket for Strassen: #11610.",
    "created_at": "2011-07-18T21:32:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-70993",
    "user": "SimonKing"
}
```

I guess that the generic Strassen-Winograd implementation in sage.matrix.strassen is related with, but not really in the focus of, this ticket. Therefore I opened a new ticket for Strassen: #11610.



---

archive/issue_comments_070994.json:
```json
{
    "body": "Here is another data point concerning slowness - ridiculous slowness, actually - of matrix multiplication in Sage. The following is with sage-4.7.1.rc1 plus the patches from #11589:\n\n```\nsage: MS = MatrixSpace(GF(64,'a'),5000,5000)\n# I think the following is already WAY too slow!\nsage: %time A = MS.random_element()\nCPU times: user 38.42 s, sys: 0.13 s, total: 38.55 s\nWall time: 38.67 s\nsage: B = MS.random_element()\nsage: %time C = A*B\n^C^C^C^C^C^C^C^C^C^C^C^C^C^C\n```\n\n\nIn other words:\n\n1. The computation can not be interrupted, which is a bug.\n2. The computation takes more than 45 minutes!!!\n3. The computation takes more than 880 MB.\n\nAs much as I see, GF(2) is the *only* finite field such that multiplication of square matrices over that field is not blatantly slow in Sage.\n\nIt makes me wonder if we shouldn't use a different package for matrix multiplication over finite fields different from GF(2).\n\nAs much as I know, there already is an experimental version for matrices over `GF(2^n)`, isn't it, Martin? How fast is it?\n\nOver finite prime fields, we could use Linbox. There are tickets to do so.\n\nBut What about finite non-prime fields? Would it be a reasonable idea to use something based on `MeatAxe`?\n\nI will very likely be using a Sage wrapper for `MeatAxe` matrices in my current project. So, I'll do the work anyway. From my perspective, the only question is whether we can/should use it by default in Sage.\n\nHere are some relevant data:\n\n1. I work on top of `MeatAxe 2.2.4`. That version is identic with 2.2.3, with one important difference. While all other meataxe versions are `GPL 2`, version 2.2.4 is `GPL 2+`. In fact, that version was made after I wanted to use meataxe 2.2.3 in my group cohomology package and asked Michael Ringe whether he could provide it in `GPL 2+`. \n\n2. I am not just wrapping it, in fact I am branching meataxe. I improved the implementation of the \"school book\" multiplication in meataxe, and I implemented Strassen-Winograd multiplication, which had so far been missing in meataxe.\n\n3. It would provide a vastly better performance. The above 5000x5000 multiplication over GF(4) with the school book method needs 173.68 CPU seconds and about 200 MB. With Strassen-Winograd, it is  only 85.04 CPU seconds, using less than 280 MB.\n\n4. Concerning prime fields: A multiplication of two 5000x5000 matrices A, B over GF(5) using `A._multipliy_linbox(B)` needs 21.49 CPU seconds and 1.2 GB(!). Using school book multiplication in meataxe, it is 46.70 s and 140 MB, or 30.29 CPU seconds and 160 MB using Strassen-Winograd.\n\n__Conclusion__\n\n* The licence of `MeatAxe 2.2.4` would be fine.\n\n* The default matrix multiplication over finite fields that is currently provided in Sage is not competitive at all.\n\n* Over prime fields, Linbox is still faster, but my implementation of Strassen multiplication needs only one tenth of the memory.\n\n* As far as I know, Linbox does not officially support non-prime fields, in contrast to meataxe. And Meataxe is a lot faster than the current implementation in Sage, except for GF(2).\n\n* My meataxe wrapper could still be improved - I have no idea of how to optimize the use of L1 and L2 cache, and would need help to do so.\n\n* Big disadvantage of my current meataxe wrapper: It only supports field sizes less than 256. There is a \"big\" version of meataxe that can deal with field sizes of up to `2^16-1`, but I did not wrap it yet, and I don't know how difficult it would be.\n\nAs I said: I will work on that wrapper anyway, because it seems well suited for my current project. But would it make sense in Sage as a default implementation for matrices over small finite fields (or at least over the non-prime fields)?",
    "created_at": "2011-08-11T17:38:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-70994",
    "user": "SimonKing"
}
```

Here is another data point concerning slowness - ridiculous slowness, actually - of matrix multiplication in Sage. The following is with sage-4.7.1.rc1 plus the patches from #11589:

```
sage: MS = MatrixSpace(GF(64,'a'),5000,5000)
# I think the following is already WAY too slow!
sage: %time A = MS.random_element()
CPU times: user 38.42 s, sys: 0.13 s, total: 38.55 s
Wall time: 38.67 s
sage: B = MS.random_element()
sage: %time C = A*B
^C^C^C^C^C^C^C^C^C^C^C^C^C^C
```


In other words:

1. The computation can not be interrupted, which is a bug.
2. The computation takes more than 45 minutes!!!
3. The computation takes more than 880 MB.

As much as I see, GF(2) is the *only* finite field such that multiplication of square matrices over that field is not blatantly slow in Sage.

It makes me wonder if we shouldn't use a different package for matrix multiplication over finite fields different from GF(2).

As much as I know, there already is an experimental version for matrices over `GF(2^n)`, isn't it, Martin? How fast is it?

Over finite prime fields, we could use Linbox. There are tickets to do so.

But What about finite non-prime fields? Would it be a reasonable idea to use something based on `MeatAxe`?

I will very likely be using a Sage wrapper for `MeatAxe` matrices in my current project. So, I'll do the work anyway. From my perspective, the only question is whether we can/should use it by default in Sage.

Here are some relevant data:

1. I work on top of `MeatAxe 2.2.4`. That version is identic with 2.2.3, with one important difference. While all other meataxe versions are `GPL 2`, version 2.2.4 is `GPL 2+`. In fact, that version was made after I wanted to use meataxe 2.2.3 in my group cohomology package and asked Michael Ringe whether he could provide it in `GPL 2+`. 

2. I am not just wrapping it, in fact I am branching meataxe. I improved the implementation of the "school book" multiplication in meataxe, and I implemented Strassen-Winograd multiplication, which had so far been missing in meataxe.

3. It would provide a vastly better performance. The above 5000x5000 multiplication over GF(4) with the school book method needs 173.68 CPU seconds and about 200 MB. With Strassen-Winograd, it is  only 85.04 CPU seconds, using less than 280 MB.

4. Concerning prime fields: A multiplication of two 5000x5000 matrices A, B over GF(5) using `A._multipliy_linbox(B)` needs 21.49 CPU seconds and 1.2 GB(!). Using school book multiplication in meataxe, it is 46.70 s and 140 MB, or 30.29 CPU seconds and 160 MB using Strassen-Winograd.

__Conclusion__

* The licence of `MeatAxe 2.2.4` would be fine.

* The default matrix multiplication over finite fields that is currently provided in Sage is not competitive at all.

* Over prime fields, Linbox is still faster, but my implementation of Strassen multiplication needs only one tenth of the memory.

* As far as I know, Linbox does not officially support non-prime fields, in contrast to meataxe. And Meataxe is a lot faster than the current implementation in Sage, except for GF(2).

* My meataxe wrapper could still be improved - I have no idea of how to optimize the use of L1 and L2 cache, and would need help to do so.

* Big disadvantage of my current meataxe wrapper: It only supports field sizes less than 256. There is a "big" version of meataxe that can deal with field sizes of up to `2^16-1`, but I did not wrap it yet, and I don't know how difficult it would be.

As I said: I will work on that wrapper anyway, because it seems well suited for my current project. But would it make sense in Sage as a default implementation for matrices over small finite fields (or at least over the non-prime fields)?



---

archive/issue_comments_070995.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2011-08-11T17:38:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-70995",
    "user": "SimonKing"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_070996.json:
```json
{
    "body": "I'm curious: have you compared with the matrix multiplication routines in flint 2? http://www.flintlib.org/",
    "created_at": "2011-08-11T17:57:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-70996",
    "user": "jason"
}
```

I'm curious: have you compared with the matrix multiplication routines in flint 2? http://www.flintlib.org/



---

archive/issue_comments_070997.json:
```json
{
    "body": "Replying to [comment:19 jason]:\n> I'm curious: have you compared with the matrix multiplication routines in flint 2? http://www.flintlib.org/\n\nPerhaps I am confusing things; but the impression that I got from polynomials in Sage is that flint and ntl are over the rationals and the integers. Does flint also do finite fields? Is the relevant part of flint available in Sage, or do I need to install flint separately?",
    "created_at": "2011-08-11T18:09:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-70997",
    "user": "SimonKing"
}
```

Replying to [comment:19 jason]:
> I'm curious: have you compared with the matrix multiplication routines in flint 2? http://www.flintlib.org/

Perhaps I am confusing things; but the impression that I got from polynomials in Sage is that flint and ntl are over the rationals and the integers. Does flint also do finite fields? Is the relevant part of flint available in Sage, or do I need to install flint separately?



---

archive/issue_comments_070998.json:
```json
{
    "body": "Flint 2.20 (which is not in Sage yet, IIRC) apparently handles Z mod n matrices.  See section 19 of the manual: http://www.flintlib.org/flint-2.2.pdf.",
    "created_at": "2011-08-11T18:18:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-70998",
    "user": "jason"
}
```

Flint 2.20 (which is not in Sage yet, IIRC) apparently handles Z mod n matrices.  See section 19 of the manual: http://www.flintlib.org/flint-2.2.pdf.



---

archive/issue_comments_070999.json:
```json
{
    "body": "Replying to [comment:21 jason]:\n> Flint 2.20 (which is not in Sage yet, IIRC) apparently handles Z mod n matrices.  See section 19 of the manual: http://www.flintlib.org/flint-2.2.pdf.\n\nYep, I was just reading the documentation.\n\nThey have matrices over Z/nZ, but I don't see finite fields mentioned. Except prime fields, of course. They go up to `n=2^64-1`, which Meataxe can't manage, even in the big implementation (the field size must be less than `2^16`).\n\nConcerning comparison of matrix operations, one must not forget higher level operations. To compute the echelon form of a 5000x5000 matrix over GF(5), the default implementation in Sage needs 12.65 s and 1.2 GB on my machine. _echelonize_linbox needs the same.\n\nMeataxe needs much less memory, but 45 seconds. Admittedly I did not care about echelonization in meataxe, since I don't need it for my application. Hm. That could be a show stopper.",
    "created_at": "2011-08-11T18:27:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-70999",
    "user": "SimonKing"
}
```

Replying to [comment:21 jason]:
> Flint 2.20 (which is not in Sage yet, IIRC) apparently handles Z mod n matrices.  See section 19 of the manual: http://www.flintlib.org/flint-2.2.pdf.

Yep, I was just reading the documentation.

They have matrices over Z/nZ, but I don't see finite fields mentioned. Except prime fields, of course. They go up to `n=2^64-1`, which Meataxe can't manage, even in the big implementation (the field size must be less than `2^16`).

Concerning comparison of matrix operations, one must not forget higher level operations. To compute the echelon form of a 5000x5000 matrix over GF(5), the default implementation in Sage needs 12.65 s and 1.2 GB on my machine. _echelonize_linbox needs the same.

Meataxe needs much less memory, but 45 seconds. Admittedly I did not care about echelonization in meataxe, since I don't need it for my application. Hm. That could be a show stopper.



---

archive/issue_comments_071000.json:
```json
{
    "body": "The original implementation of school book multiplication was far from optimal, and thus I guess that the school book echelonization in meataxe isn't optimal as well. And meataxe does not use Strassen's algorithm for echelon computation.\n\nSo, there probably is a similar room for improvement of echelonization than it was for matrix multiplication.\n\nThe problem is that, so far, the echelonization does not seem to be a bottle neck for my application. So, my motivation to implement it is not exactly big. But who knows: At some point of my project, I *will* be needing echelonization - I just don't know, yet, how large the matrix sizes will eventually be.",
    "created_at": "2011-08-11T18:42:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-71000",
    "user": "SimonKing"
}
```

The original implementation of school book multiplication was far from optimal, and thus I guess that the school book echelonization in meataxe isn't optimal as well. And meataxe does not use Strassen's algorithm for echelon computation.

So, there probably is a similar room for improvement of echelonization than it was for matrix multiplication.

The problem is that, so far, the echelonization does not seem to be a bottle neck for my application. So, my motivation to implement it is not exactly big. But who knows: At some point of my project, I *will* be needing echelonization - I just don't know, yet, how large the matrix sizes will eventually be.



---

archive/issue_comments_071001.json:
```json
{
    "body": "Yes, I should have clarified that I meant that it would be potentially interesting to compare flint 2 speeds for Z/pZ (p prime) with the other code that you are comparing, given that flint has a reputation for being blazingly fast.  Of course, it's not a total solution or replacement for meataxe, since meataxe handles many more fields.",
    "created_at": "2011-08-11T19:28:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-71001",
    "user": "jason"
}
```

Yes, I should have clarified that I meant that it would be potentially interesting to compare flint 2 speeds for Z/pZ (p prime) with the other code that you are comparing, given that flint has a reputation for being blazingly fast.  Of course, it's not a total solution or replacement for meataxe, since meataxe handles many more fields.



---

archive/issue_comments_071002.json:
```json
{
    "body": "Just a heads-up: flint2 should hold up well for a 32-bit or 64-bit prime field, but it is not optimized for and probably slower than some other libraries (e.g. Linbox) over something like GF(5). And yes, only prime fields are supported.",
    "created_at": "2011-08-11T22:11:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-71002",
    "user": "fredrik.johansson"
}
```

Just a heads-up: flint2 should hold up well for a 32-bit or 64-bit prime field, but it is not optimized for and probably slower than some other libraries (e.g. Linbox) over something like GF(5). And yes, only prime fields are supported.



---

archive/issue_comments_071003.json:
```json
{
    "body": "> As much as I know, there already is an experimental version for matrices over \n> GF(2^n), isn't it, Martin? How fast is it?\n\nSorry, I completely missed this question. M4RIE, i.e. dense linear algebra over GF(2<sup>e</sup>) for 2 <= e <= 10, is either about as fast as Magma or much faster. Actually, it's not experimental but a fully working patch + library has been around for ages, it was agreed months ago it would go into Sage, there has just not been enough push to finish the review: #9562\n\nHere's a summary of the current approach & performance:\n\nhttp://martinralbrecht.files.wordpress.com/2011/03/20110330_-_m4ri_-_nancy.pdf\n\nTo compare with your results:\n\n**Karatsuba**\n\n\n```python\nsage: K.<a> = GF(4)\nsage: A = random_matrix(K,5000,5000)\nsage: B = random_matrix(K,5000,5000)\nsage: %time C=A*B\nCPU times: user 0.51 s, sys: 0.01 s, total: 0.52 s\nWall time: 0.52 s\n```\n\n\n**Travolta**\n\n\n```python\nsage: K.<a> = GF(4)\nsage: A = random_matrix(K,5000,5000)\nsage: B = random_matrix(K,5000,5000)\nsage: %time C=A._multiply_travolta(B)\nCPU times: user 1.19 s, sys: 0.00 s, total: 1.20 s\nWall time: 1.20 s\n```\n\n\nSo both algorithms in M4RIE are much faster than ~80 seconds. I didn't precisely measure memory consumption though. \n\n\n\n> The default matrix multiplication over finite fields that is currently provided in Sage is  not competitive at all.\n\nVery much agreed!\n\n> Over prime fields, Linbox is still faster, but my implementation of Strassen multiplication needs only one tenth of the memory.\n\nI hope to fix this next week at Sage Days, i.e. to wrap LinBox properly.\n\n> As far as I know, Linbox does not officially support non-prime fields, in contrast to meataxe. And Meataxe is a lot faster than the current implementation in Sage, except for GF(2).\n\nCl\u00e9ment told me that LinBox does support non-prime fields we just never wrapped them in Sage.\n\n> My meataxe wrapper could still be improved - I have no idea of how to optimize the use of L1 and L2 cache, and would need help to do so.\n\nLet's move that to e-mail.\n\n> Big disadvantage of my current meataxe wrapper: It only supports field sizes less than 256. \n\nI don't think it's that big of an issue, a lot of applications need small fields!",
    "created_at": "2011-08-15T15:27:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-71003",
    "user": "malb"
}
```

> As much as I know, there already is an experimental version for matrices over 
> GF(2^n), isn't it, Martin? How fast is it?

Sorry, I completely missed this question. M4RIE, i.e. dense linear algebra over GF(2<sup>e</sup>) for 2 <= e <= 10, is either about as fast as Magma or much faster. Actually, it's not experimental but a fully working patch + library has been around for ages, it was agreed months ago it would go into Sage, there has just not been enough push to finish the review: #9562

Here's a summary of the current approach & performance:

http://martinralbrecht.files.wordpress.com/2011/03/20110330_-_m4ri_-_nancy.pdf

To compare with your results:

**Karatsuba**


```python
sage: K.<a> = GF(4)
sage: A = random_matrix(K,5000,5000)
sage: B = random_matrix(K,5000,5000)
sage: %time C=A*B
CPU times: user 0.51 s, sys: 0.01 s, total: 0.52 s
Wall time: 0.52 s
```


**Travolta**


```python
sage: K.<a> = GF(4)
sage: A = random_matrix(K,5000,5000)
sage: B = random_matrix(K,5000,5000)
sage: %time C=A._multiply_travolta(B)
CPU times: user 1.19 s, sys: 0.00 s, total: 1.20 s
Wall time: 1.20 s
```


So both algorithms in M4RIE are much faster than ~80 seconds. I didn't precisely measure memory consumption though. 



> The default matrix multiplication over finite fields that is currently provided in Sage is  not competitive at all.

Very much agreed!

> Over prime fields, Linbox is still faster, but my implementation of Strassen multiplication needs only one tenth of the memory.

I hope to fix this next week at Sage Days, i.e. to wrap LinBox properly.

> As far as I know, Linbox does not officially support non-prime fields, in contrast to meataxe. And Meataxe is a lot faster than the current implementation in Sage, except for GF(2).

Clément told me that LinBox does support non-prime fields we just never wrapped them in Sage.

> My meataxe wrapper could still be improved - I have no idea of how to optimize the use of L1 and L2 cache, and would need help to do so.

Let's move that to e-mail.

> Big disadvantage of my current meataxe wrapper: It only supports field sizes less than 256. 

I don't think it's that big of an issue, a lot of applications need small fields!



---

archive/issue_comments_071004.json:
```json
{
    "body": "One more data point.\n\nAgain, this is with #9562:\n\n\n```python\nsage: MS = MatrixSpace(GF(64,'a'),5000,5000)\nsage: %time A = MS.random_element()\nCPU times: user 0.46 s, sys: 0.01 s, total: 0.46 s\nWall time: 0.47 s\nsage: B = MS.random_element()\nsage: %time C = A*B \nCPU times: user 22.69 s, sys: 0.06 s, total: 22.75 s\nWall time: 22.84 s\n```\n\n\nNote that we only implemented Travolta for GF(2<sup>6</sup>) so far. With Karatsuba we expect to get close to 4.5 seconds, because:\n\n\n```python\nsage: A = random_matrix(GF(2),5000,5000)\nsage: B = random_matrix(GF(2),5000,5000)\nsage: %timeit C=A*B\n5 loops, best of 3: 249 ms per loop\n```\n\n\nand the best known formula for degree 5 polynomials needs 17 such multiplications: \n\nhttp://www.csd.uwo.ca/~eschost/Exam/Montgomery--Five_six_and_seven_terms_Karatsuba-like_formulae.pdf",
    "created_at": "2011-08-15T15:40:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-71004",
    "user": "malb"
}
```

One more data point.

Again, this is with #9562:


```python
sage: MS = MatrixSpace(GF(64,'a'),5000,5000)
sage: %time A = MS.random_element()
CPU times: user 0.46 s, sys: 0.01 s, total: 0.46 s
Wall time: 0.47 s
sage: B = MS.random_element()
sage: %time C = A*B 
CPU times: user 22.69 s, sys: 0.06 s, total: 22.75 s
Wall time: 22.84 s
```


Note that we only implemented Travolta for GF(2<sup>6</sup>) so far. With Karatsuba we expect to get close to 4.5 seconds, because:


```python
sage: A = random_matrix(GF(2),5000,5000)
sage: B = random_matrix(GF(2),5000,5000)
sage: %timeit C=A*B
5 loops, best of 3: 249 ms per loop
```


and the best known formula for degree 5 polynomials needs 17 such multiplications: 

http://www.csd.uwo.ca/~eschost/Exam/Montgomery--Five_six_and_seven_terms_Karatsuba-like_formulae.pdf



---

archive/issue_comments_071005.json:
```json
{
    "body": "... and Magma for comparison:\n\nGF(2<sup>2</sup>):\n\n\n```\nMagma V2.15-10    Mon Aug 15 2011 16:41:46 on road     [Seed = 3840120025]\nType ? for help.  Type <Ctrl>-D to quit.\n> K<a> := GF(4);               \n> A:=RandomMatrix(K,5000,5000);\n> B:=RandomMatrix(K,5000,5000);\n> time C:=A*B;                 \nTime: 2.130\n```\n\n\nGF(2<sup>6</sup>):\n\n\n```\nMagma V2.15-10    Mon Aug 15 2011 16:41:46 on road     [Seed = 3840120025]\nType ? for help.  Type <Ctrl>-D to quit.\n> K<a> := GF(64);\n> A:=RandomMatrix(K,5000,5000);\n> B:=RandomMatrix(K,5000,5000); \n> time C:=A*B;\nTime: 273.310\n```\n\n\nIt seems your MeatAxe fork is faster than Magma for GF(2<sup>6</sup>)?",
    "created_at": "2011-08-15T15:48:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-71005",
    "user": "malb"
}
```

... and Magma for comparison:

GF(2<sup>2</sup>):


```
Magma V2.15-10    Mon Aug 15 2011 16:41:46 on road     [Seed = 3840120025]
Type ? for help.  Type <Ctrl>-D to quit.
> K<a> := GF(4);               
> A:=RandomMatrix(K,5000,5000);
> B:=RandomMatrix(K,5000,5000);
> time C:=A*B;                 
Time: 2.130
```


GF(2<sup>6</sup>):


```
Magma V2.15-10    Mon Aug 15 2011 16:41:46 on road     [Seed = 3840120025]
Type ? for help.  Type <Ctrl>-D to quit.
> K<a> := GF(64);
> A:=RandomMatrix(K,5000,5000);
> B:=RandomMatrix(K,5000,5000); 
> time C:=A*B;
Time: 273.310
```


It seems your MeatAxe fork is faster than Magma for GF(2<sup>6</sup>)?



---

archive/issue_comments_071006.json:
```json
{
    "body": "Hi Martin!\n\nYour data points are amazing! Good that you point us to #9562, it really seems that it should soon become part of Sage. The link http://martinralbrecht.files.wordpress.com/2011/03/20110330_-_m4ri_-_nancy.pdf seems to be broken, though. \n\nConcerning my application, it probably was a very wise decision that my programs for the computation of Ext algebras of basic algebras are designed to use *any* type of matrices. So, one can easily pick the fastest available implementation for each base ring. It could be that eventually I will use M4RI(E) for powers of two, Meataxe for non-prime fields and and a full-grown Linbox-wrapper for prime fields except GF(2).",
    "created_at": "2011-08-15T15:51:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-71006",
    "user": "SimonKing"
}
```

Hi Martin!

Your data points are amazing! Good that you point us to #9562, it really seems that it should soon become part of Sage. The link http://martinralbrecht.files.wordpress.com/2011/03/20110330_-_m4ri_-_nancy.pdf seems to be broken, though. 

Concerning my application, it probably was a very wise decision that my programs for the computation of Ext algebras of basic algebras are designed to use *any* type of matrices. So, one can easily pick the fastest available implementation for each base ring. It could be that eventually I will use M4RI(E) for powers of two, Meataxe for non-prime fields and and a full-grown Linbox-wrapper for prime fields except GF(2).



---

archive/issue_comments_071007.json:
```json
{
    "body": "Replying to [comment:28 malb]:\n> ... and Magma for comparison:\n> \n> GF(2<sup>2</sup>):\n> ...\n> Time: 2.130\n\nThat beats Meataxe by a factor of 12 :-(\n\n> GF(2<sup>6</sup>):\n> ...\n> Time: 273.310\n> It seems your MeatAxe fork is faster than Magma for GF(2<sup>6</sup>)?\n\nAmazing! The Meataxe approach is very simple: Row-first storage of data, as many field elements stored in one Byte as possible (hence, over `GF(2^6)` we have two marks per byte), and multiplication tables that allow to multiply a field element with a whole byte in one go. \nThe rest is school book or Strassen-Winograd multiplication.\n\nAnyway. M4RIE seems to be a lot faster, and I am looking forward to use it!",
    "created_at": "2011-08-15T16:01:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-71007",
    "user": "SimonKing"
}
```

Replying to [comment:28 malb]:
> ... and Magma for comparison:
> 
> GF(2<sup>2</sup>):
> ...
> Time: 2.130

That beats Meataxe by a factor of 12 :-(

> GF(2<sup>6</sup>):
> ...
> Time: 273.310
> It seems your MeatAxe fork is faster than Magma for GF(2<sup>6</sup>)?

Amazing! The Meataxe approach is very simple: Row-first storage of data, as many field elements stored in one Byte as possible (hence, over `GF(2^6)` we have two marks per byte), and multiplication tables that allow to multiply a field element with a whole byte in one go. 
The rest is school book or Strassen-Winograd multiplication.

Anyway. M4RIE seems to be a lot faster, and I am looking forward to use it!



---

archive/issue_comments_071008.json:
```json
{
    "body": "correct link:  http://martinralbrecht.files.wordpress.com/2011/03/20110330_-_m4ri_-_nancy1.pdf\n\nWhat does \"two marks per byte\" mean? Do you store [xxxxxx00][xxxxxx00] or [xxxxxx|xx][xxxx0000] i.e. do you fit one element into one byte or do you really use every bit? In M4RIE (`mzed_t` data type) we do the former. The other representation `mzd_slice_t` stores matrices in \"slices\": GF(2) matrices.",
    "created_at": "2011-08-15T16:04:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-71008",
    "user": "malb"
}
```

correct link:  http://martinralbrecht.files.wordpress.com/2011/03/20110330_-_m4ri_-_nancy1.pdf

What does "two marks per byte" mean? Do you store [xxxxxx00][xxxxxx00] or [xxxxxx|xx][xxxx0000] i.e. do you fit one element into one byte or do you really use every bit? In M4RIE (`mzed_t` data type) we do the former. The other representation `mzd_slice_t` stores matrices in "slices": GF(2) matrices.



---

archive/issue_comments_071009.json:
```json
{
    "body": "Btw. the Travolta algorithm is also very simple and just avoids any multiplications in the inner loop. It's complexity is O(n<sup>2</sup>*2<sup>e</sup>) multiplications and O(n<sup>3</sup>) additions.\n\n   cf. https://bitbucket.org/malb/m4rie-old/src/841a71d72e24/matrix.cc#cl-202\n\nBtw. it takes 80 seconds for you to do 5,000 x 5,000 over GF(2<sup>2</sup>) and GF(2<sup>6</sup>)? Can time MeatAxe again and post the two timings here?",
    "created_at": "2011-08-15T16:09:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-71009",
    "user": "malb"
}
```

Btw. the Travolta algorithm is also very simple and just avoids any multiplications in the inner loop. It's complexity is O(n<sup>2</sup>*2<sup>e</sup>) multiplications and O(n<sup>3</sup>) additions.

   cf. https://bitbucket.org/malb/m4rie-old/src/841a71d72e24/matrix.cc#cl-202

Btw. it takes 80 seconds for you to do 5,000 x 5,000 over GF(2<sup>2</sup>) and GF(2<sup>6</sup>)? Can time MeatAxe again and post the two timings here?



---

archive/issue_comments_071010.json:
```json
{
    "body": "Replying to [comment:31 malb]:\n> correct link:  http://martinralbrecht.files.wordpress.com/2011/03/20110330_-_m4ri_-_nancy1.pdf\n\nThank you!\n\n> What does \"two marks per byte\" mean? \n\nSorry, where's my head? For field size 64, only one mark per byte is used, and it is [xxxxxx00][xxxxxx00].\n\nMeataxe packs as many field elements into a single byte as possible. Hence, if you work over GF(5) then a triple of field elements will be packed into one byte. That is since 5<sup>3</sup> is smaller than 256, but 5<sup>4</sup> is bigger.\n\nSo, really quite simplistic. No bit slicing or anything fancy.",
    "created_at": "2011-08-15T16:23:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-71010",
    "user": "SimonKing"
}
```

Replying to [comment:31 malb]:
> correct link:  http://martinralbrecht.files.wordpress.com/2011/03/20110330_-_m4ri_-_nancy1.pdf

Thank you!

> What does "two marks per byte" mean? 

Sorry, where's my head? For field size 64, only one mark per byte is used, and it is [xxxxxx00][xxxxxx00].

Meataxe packs as many field elements into a single byte as possible. Hence, if you work over GF(5) then a triple of field elements will be packed into one byte. That is since 5<sup>3</sup> is smaller than 256, but 5<sup>4</sup> is bigger.

So, really quite simplistic. No bit slicing or anything fancy.



---

archive/issue_comments_071011.json:
```json
{
    "body": "Martin, I just found that M4RIE just needs 10.42 seconds resp. 8.78 seconds on my computer for multiplying two random 5000x5000 matrices over GF(64).\n\n\n```\nsage: MS = MatrixSpace(GF(64,'a'),5000,5000)\nsage: A = MS.random_element()\nsage: type(A)\n<type 'sage.matrix.matrix_mod2e_dense.Matrix_mod2e_dense'>\nsage: B = MS.random_element()\nsage: %time C = A*B\nCPU times: user 10.42 s, sys: 0.15 s, total: 10.56 s\nWall time: 10.60 s\nsage: %time C = A._mult\nA._multiply_classical  A._multiply_karatsuba  A._multiply_strassen   A._multiply_travolta\nsage: %time C = A._multiply_travolta(B)\nCPU times: user 8.73 s, sys: 0.02 s, total: 8.75 s\nWall time: 8.78 s\n```\n\n\nThat's awesome! For these particular matrices, the Meataxe fork needs 85.26 seconds. Hopefully I'll be able to review #9562 tomorrow.",
    "created_at": "2011-08-15T17:39:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-71011",
    "user": "SimonKing"
}
```

Martin, I just found that M4RIE just needs 10.42 seconds resp. 8.78 seconds on my computer for multiplying two random 5000x5000 matrices over GF(64).


```
sage: MS = MatrixSpace(GF(64,'a'),5000,5000)
sage: A = MS.random_element()
sage: type(A)
<type 'sage.matrix.matrix_mod2e_dense.Matrix_mod2e_dense'>
sage: B = MS.random_element()
sage: %time C = A*B
CPU times: user 10.42 s, sys: 0.15 s, total: 10.56 s
Wall time: 10.60 s
sage: %time C = A._mult
A._multiply_classical  A._multiply_karatsuba  A._multiply_strassen   A._multiply_travolta
sage: %time C = A._multiply_travolta(B)
CPU times: user 8.73 s, sys: 0.02 s, total: 8.75 s
Wall time: 8.78 s
```


That's awesome! For these particular matrices, the Meataxe fork needs 85.26 seconds. Hopefully I'll be able to review #9562 tomorrow.



---

archive/issue_comments_071012.json:
```json
{
    "body": "This ticket is \"needs info\". What info is actually needed?",
    "created_at": "2011-11-28T09:01:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-71012",
    "user": "SimonKing"
}
```

This ticket is "needs info". What info is actually needed?



---

archive/issue_comments_071013.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2012-03-02T10:06:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-71013",
    "user": "SimonKing"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_071014.json:
```json
{
    "body": "Again, what information is needed? I'm changing it into \"needs review\", since I don't see a question that needed to be addressed.",
    "created_at": "2012-03-02T10:06:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-71014",
    "user": "SimonKing"
}
```

Again, what information is needed? I'm changing it into "needs review", since I don't see a question that needed to be addressed.



---

archive/issue_comments_071015.json:
```json
{
    "body": "Agreed. This ticket is about the overhead of multiplying small matrices, not the runtime of large non-prime-finite-field matrices.",
    "created_at": "2012-03-02T10:49:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-71015",
    "user": "robertwb"
}
```

Agreed. This ticket is about the overhead of multiplying small matrices, not the runtime of large non-prime-finite-field matrices.



---

archive/issue_comments_071016.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-03-10T17:01:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-71016",
    "user": "davidloeffler"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_071017.json:
```json
{
    "body": "These patches do not apply correctly on either the current release or the current beta (see patchbot logs).",
    "created_at": "2012-03-10T17:01:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-71017",
    "user": "davidloeffler"
}
```

These patches do not apply correctly on either the current release or the current beta (see patchbot logs).



---

archive/issue_comments_071018.json:
```json
{
    "body": "Replying to [comment:38 davidloeffler]:\n> These patches do not apply correctly on either the current release or the current beta (see patchbot logs).\n\nNo surprise that two-year-old patches don't apply anymore. I am rebasing them now, producing a single patch replacing the two. I am not totally sure, but I think the ideas of the second patch are already in Sage - need to verify it, though.",
    "created_at": "2012-03-10T20:34:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-71018",
    "user": "SimonKing"
}
```

Replying to [comment:38 davidloeffler]:
> These patches do not apply correctly on either the current release or the current beta (see patchbot logs).

No surprise that two-year-old patches don't apply anymore. I am rebasing them now, producing a single patch replacing the two. I am not totally sure, but I think the ideas of the second patch are already in Sage - need to verify it, though.



---

archive/issue_comments_071019.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-03-10T20:53:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-71019",
    "user": "SimonKing"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071020.json:
```json
{
    "body": "I have rebased the patches, combining them into one patch. In fact, a part (but not all) of the second patch is not needed anymore, since the creation of the zero matrix has been improved in another ticket.\n\nHere is evidence that the patch still does improve the timings for the computation of small matrices - even after we have switched to linbox:\n\nWithout patch:\n\n```\nsage: d = 1\nsage: A = random_matrix(GF(3), d)\nsage: B = random_matrix(GF(3), d)\nsage: timeit(\"C = A*B\")\n625 loops, best of 3: 40.5 \u00b5s per loop\n```\n\n\nWith the patch:\n\n```\nsage: d = 1\nsage: A = random_matrix(GF(3), d)\nsage: B = random_matrix(GF(3), d)\nsage: timeit(\"C = A*B\")\n625 loops, best of 3: 18.5 \u00b5s per loop\n```\n\n\nI need to run the doctests, though. But needs review.\n\nApply trac8096_speedup_matrix_parent.patch",
    "created_at": "2012-03-10T20:53:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-71020",
    "user": "SimonKing"
}
```

I have rebased the patches, combining them into one patch. In fact, a part (but not all) of the second patch is not needed anymore, since the creation of the zero matrix has been improved in another ticket.

Here is evidence that the patch still does improve the timings for the computation of small matrices - even after we have switched to linbox:

Without patch:

```
sage: d = 1
sage: A = random_matrix(GF(3), d)
sage: B = random_matrix(GF(3), d)
sage: timeit("C = A*B")
625 loops, best of 3: 40.5 µs per loop
```


With the patch:

```
sage: d = 1
sage: A = random_matrix(GF(3), d)
sage: B = random_matrix(GF(3), d)
sage: timeit("C = A*B")
625 loops, best of 3: 18.5 µs per loop
```


I need to run the doctests, though. But needs review.

Apply trac8096_speedup_matrix_parent.patch



---

archive/issue_comments_071021.json:
```json
{
    "body": "Here is the example from the ticket description.\n\nWithout the patch:\n\n```\nsage: for d in range(1, 70):\n....:     print d,\n....:     A = random_matrix(GF(3), d)\n....:     B = random_matrix(GF(3), d)\n....:     timeit(\"C = A*B\")\n....:     \n1 625 loops, best of 3: 41 \u00b5s per loop\n2 625 loops, best of 3: 41.1 \u00b5s per loop\n3 625 loops, best of 3: 41 \u00b5s per loop\n4 625 loops, best of 3: 41.4 \u00b5s per loop\n5 625 loops, best of 3: 41.6 \u00b5s per loop\n6 625 loops, best of 3: 42.4 \u00b5s per loop\n7 625 loops, best of 3: 42.9 \u00b5s per loop\n8 625 loops, best of 3: 43.3 \u00b5s per loop\n9 625 loops, best of 3: 43.5 \u00b5s per loop\n10 625 loops, best of 3: 44.1 \u00b5s per loop\n11 625 loops, best of 3: 44.8 \u00b5s per loop\n12 625 loops, best of 3: 45.5 \u00b5s per loop\n13 625 loops, best of 3: 46.3 \u00b5s per loop\n14 625 loops, best of 3: 47.6 \u00b5s per loop\n15 625 loops, best of 3: 48.8 \u00b5s per loop\n16 625 loops, best of 3: 50.4 \u00b5s per loop\n17 625 loops, best of 3: 51.8 \u00b5s per loop\n18 625 loops, best of 3: 53.4 \u00b5s per loop\n19 625 loops, best of 3: 54.7 \u00b5s per loop\n20 625 loops, best of 3: 56.5 \u00b5s per loop\n21 625 loops, best of 3: 58.4 \u00b5s per loop\n22 625 loops, best of 3: 60.8 \u00b5s per loop\n23 625 loops, best of 3: 63.3 \u00b5s per loop\n24 625 loops, best of 3: 61.7 \u00b5s per loop\n25 625 loops, best of 3: 64.1 \u00b5s per loop\n26 625 loops, best of 3: 66.3 \u00b5s per loop\n27 625 loops, best of 3: 70.3 \u00b5s per loop\n28 625 loops, best of 3: 72.7 \u00b5s per loop\n29 625 loops, best of 3: 75.2 \u00b5s per loop\n30 625 loops, best of 3: 79.4 \u00b5s per loop\n31 625 loops, best of 3: 82 \u00b5s per loop\n32 625 loops, best of 3: 86.5 \u00b5s per loop\n33 625 loops, best of 3: 89.8 \u00b5s per loop\n34 625 loops, best of 3: 94.3 \u00b5s per loop\n35 625 loops, best of 3: 98.1 \u00b5s per loop\n36 625 loops, best of 3: 92.1 \u00b5s per loop\n37 625 loops, best of 3: 95.9 \u00b5s per loop\n38 625 loops, best of 3: 100 \u00b5s per loop\n39 625 loops, best of 3: 105 \u00b5s per loop\n40 625 loops, best of 3: 109 \u00b5s per loop\n41 625 loops, best of 3: 117 \u00b5s per loop\n42 625 loops, best of 3: 123 \u00b5s per loop\n43 625 loops, best of 3: 129 \u00b5s per loop\n44 625 loops, best of 3: 136 \u00b5s per loop\n45 625 loops, best of 3: 142 \u00b5s per loop\n46 625 loops, best of 3: 149 \u00b5s per loop\n47 625 loops, best of 3: 156 \u00b5s per loop\n48 625 loops, best of 3: 146 \u00b5s per loop\n49 625 loops, best of 3: 154 \u00b5s per loop\n50 625 loops, best of 3: 161 \u00b5s per loop\n51 625 loops, best of 3: 168 \u00b5s per loop\n52 625 loops, best of 3: 177 \u00b5s per loop\n53 625 loops, best of 3: 185 \u00b5s per loop\n54 625 loops, best of 3: 194 \u00b5s per loop\n55 625 loops, best of 3: 202 \u00b5s per loop\n56 625 loops, best of 3: 213 \u00b5s per loop\n57 625 loops, best of 3: 222 \u00b5s per loop\n58 625 loops, best of 3: 234 \u00b5s per loop\n59 625 loops, best of 3: 244 \u00b5s per loop\n60 625 loops, best of 3: 225 \u00b5s per loop\n61 625 loops, best of 3: 235 \u00b5s per loop\n62 625 loops, best of 3: 248 \u00b5s per loop\n63 625 loops, best of 3: 260 \u00b5s per loop\n64 625 loops, best of 3: 271 \u00b5s per loop\n65 625 loops, best of 3: 287 \u00b5s per loop\n66 625 loops, best of 3: 297 \u00b5s per loop\n67 625 loops, best of 3: 311 \u00b5s per loop\n68 625 loops, best of 3: 324 \u00b5s per loop\n69 625 loops, best of 3: 340 \u00b5s per loop\n```\n\n\nWith the patch:\n\n```\nsage: for d in range(1, 70):\n....:     print d,\n....:     A = random_matrix(GF(3), d)\n....:     B = random_matrix(GF(3), d)\n....:     timeit(\"C = A*B\")\n....:     \n1 625 loops, best of 3: 18.3 \u00b5s per loop\n2 625 loops, best of 3: 18.4 \u00b5s per loop\n3 625 loops, best of 3: 18.5 \u00b5s per loop\n4 625 loops, best of 3: 18.8 \u00b5s per loop\n5 625 loops, best of 3: 18.9 \u00b5s per loop\n6 625 loops, best of 3: 19.5 \u00b5s per loop\n7 625 loops, best of 3: 19.9 \u00b5s per loop\n8 625 loops, best of 3: 20.3 \u00b5s per loop\n9 625 loops, best of 3: 21 \u00b5s per loop\n10 625 loops, best of 3: 21.4 \u00b5s per loop\n11 625 loops, best of 3: 22 \u00b5s per loop\n12 625 loops, best of 3: 22.4 \u00b5s per loop\n13 625 loops, best of 3: 23.9 \u00b5s per loop\n14 625 loops, best of 3: 24.9 \u00b5s per loop\n15 625 loops, best of 3: 25.6 \u00b5s per loop\n16 625 loops, best of 3: 27.2 \u00b5s per loop\n17 625 loops, best of 3: 28.2 \u00b5s per loop\n18 625 loops, best of 3: 29.8 \u00b5s per loop\n19 625 loops, best of 3: 31.4 \u00b5s per loop\n20 625 loops, best of 3: 33.1 \u00b5s per loop\n21 625 loops, best of 3: 35 \u00b5s per loop\n22 625 loops, best of 3: 37.2 \u00b5s per loop\n23 625 loops, best of 3: 39.4 \u00b5s per loop\n24 625 loops, best of 3: 38.3 \u00b5s per loop\n25 625 loops, best of 3: 40.9 \u00b5s per loop\n26 625 loops, best of 3: 43.2 \u00b5s per loop\n27 625 loops, best of 3: 46 \u00b5s per loop\n28 625 loops, best of 3: 49 \u00b5s per loop\n29 625 loops, best of 3: 51.9 \u00b5s per loop\n30 625 loops, best of 3: 55.2 \u00b5s per loop\n31 625 loops, best of 3: 58.3 \u00b5s per loop\n32 625 loops, best of 3: 62.8 \u00b5s per loop\n33 625 loops, best of 3: 66.9 \u00b5s per loop\n34 625 loops, best of 3: 71.1 \u00b5s per loop\n35 625 loops, best of 3: 75.1 \u00b5s per loop\n36 625 loops, best of 3: 68.1 \u00b5s per loop\n37 625 loops, best of 3: 72.3 \u00b5s per loop\n38 625 loops, best of 3: 76.9 \u00b5s per loop\n39 625 loops, best of 3: 81.7 \u00b5s per loop\n40 625 loops, best of 3: 85.8 \u00b5s per loop\n41 625 loops, best of 3: 94.2 \u00b5s per loop\n42 625 loops, best of 3: 99.8 \u00b5s per loop\n43 625 loops, best of 3: 106 \u00b5s per loop\n44 625 loops, best of 3: 112 \u00b5s per loop\n45 625 loops, best of 3: 119 \u00b5s per loop\n46 625 loops, best of 3: 126 \u00b5s per loop\n47 625 loops, best of 3: 132 \u00b5s per loop\n48 625 loops, best of 3: 123 \u00b5s per loop\n49 625 loops, best of 3: 130 \u00b5s per loop\n50 625 loops, best of 3: 137 \u00b5s per loop\n51 625 loops, best of 3: 145 \u00b5s per loop\n52 625 loops, best of 3: 153 \u00b5s per loop\n53 625 loops, best of 3: 162 \u00b5s per loop\n54 625 loops, best of 3: 170 \u00b5s per loop\n55 625 loops, best of 3: 180 \u00b5s per loop\n56 625 loops, best of 3: 190 \u00b5s per loop\n57 625 loops, best of 3: 200 \u00b5s per loop\n58 625 loops, best of 3: 210 \u00b5s per loop\n59 625 loops, best of 3: 221 \u00b5s per loop\n60 625 loops, best of 3: 202 \u00b5s per loop\n61 625 loops, best of 3: 212 \u00b5s per loop\n62 625 loops, best of 3: 224 \u00b5s per loop\n63 625 loops, best of 3: 237 \u00b5s per loop\n64 625 loops, best of 3: 248 \u00b5s per loop\n65 625 loops, best of 3: 263 \u00b5s per loop\n66 625 loops, best of 3: 276 \u00b5s per loop\n67 625 loops, best of 3: 288 \u00b5s per loop\n68 625 loops, best of 3: 305 \u00b5s per loop\n69 625 loops, best of 3: 318 \u00b5s per loop\n```\n\n\nSo, there is an improvement for bigger matrices as well.",
    "created_at": "2012-03-10T21:01:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-71021",
    "user": "SimonKing"
}
```

Here is the example from the ticket description.

Without the patch:

```
sage: for d in range(1, 70):
....:     print d,
....:     A = random_matrix(GF(3), d)
....:     B = random_matrix(GF(3), d)
....:     timeit("C = A*B")
....:     
1 625 loops, best of 3: 41 µs per loop
2 625 loops, best of 3: 41.1 µs per loop
3 625 loops, best of 3: 41 µs per loop
4 625 loops, best of 3: 41.4 µs per loop
5 625 loops, best of 3: 41.6 µs per loop
6 625 loops, best of 3: 42.4 µs per loop
7 625 loops, best of 3: 42.9 µs per loop
8 625 loops, best of 3: 43.3 µs per loop
9 625 loops, best of 3: 43.5 µs per loop
10 625 loops, best of 3: 44.1 µs per loop
11 625 loops, best of 3: 44.8 µs per loop
12 625 loops, best of 3: 45.5 µs per loop
13 625 loops, best of 3: 46.3 µs per loop
14 625 loops, best of 3: 47.6 µs per loop
15 625 loops, best of 3: 48.8 µs per loop
16 625 loops, best of 3: 50.4 µs per loop
17 625 loops, best of 3: 51.8 µs per loop
18 625 loops, best of 3: 53.4 µs per loop
19 625 loops, best of 3: 54.7 µs per loop
20 625 loops, best of 3: 56.5 µs per loop
21 625 loops, best of 3: 58.4 µs per loop
22 625 loops, best of 3: 60.8 µs per loop
23 625 loops, best of 3: 63.3 µs per loop
24 625 loops, best of 3: 61.7 µs per loop
25 625 loops, best of 3: 64.1 µs per loop
26 625 loops, best of 3: 66.3 µs per loop
27 625 loops, best of 3: 70.3 µs per loop
28 625 loops, best of 3: 72.7 µs per loop
29 625 loops, best of 3: 75.2 µs per loop
30 625 loops, best of 3: 79.4 µs per loop
31 625 loops, best of 3: 82 µs per loop
32 625 loops, best of 3: 86.5 µs per loop
33 625 loops, best of 3: 89.8 µs per loop
34 625 loops, best of 3: 94.3 µs per loop
35 625 loops, best of 3: 98.1 µs per loop
36 625 loops, best of 3: 92.1 µs per loop
37 625 loops, best of 3: 95.9 µs per loop
38 625 loops, best of 3: 100 µs per loop
39 625 loops, best of 3: 105 µs per loop
40 625 loops, best of 3: 109 µs per loop
41 625 loops, best of 3: 117 µs per loop
42 625 loops, best of 3: 123 µs per loop
43 625 loops, best of 3: 129 µs per loop
44 625 loops, best of 3: 136 µs per loop
45 625 loops, best of 3: 142 µs per loop
46 625 loops, best of 3: 149 µs per loop
47 625 loops, best of 3: 156 µs per loop
48 625 loops, best of 3: 146 µs per loop
49 625 loops, best of 3: 154 µs per loop
50 625 loops, best of 3: 161 µs per loop
51 625 loops, best of 3: 168 µs per loop
52 625 loops, best of 3: 177 µs per loop
53 625 loops, best of 3: 185 µs per loop
54 625 loops, best of 3: 194 µs per loop
55 625 loops, best of 3: 202 µs per loop
56 625 loops, best of 3: 213 µs per loop
57 625 loops, best of 3: 222 µs per loop
58 625 loops, best of 3: 234 µs per loop
59 625 loops, best of 3: 244 µs per loop
60 625 loops, best of 3: 225 µs per loop
61 625 loops, best of 3: 235 µs per loop
62 625 loops, best of 3: 248 µs per loop
63 625 loops, best of 3: 260 µs per loop
64 625 loops, best of 3: 271 µs per loop
65 625 loops, best of 3: 287 µs per loop
66 625 loops, best of 3: 297 µs per loop
67 625 loops, best of 3: 311 µs per loop
68 625 loops, best of 3: 324 µs per loop
69 625 loops, best of 3: 340 µs per loop
```


With the patch:

```
sage: for d in range(1, 70):
....:     print d,
....:     A = random_matrix(GF(3), d)
....:     B = random_matrix(GF(3), d)
....:     timeit("C = A*B")
....:     
1 625 loops, best of 3: 18.3 µs per loop
2 625 loops, best of 3: 18.4 µs per loop
3 625 loops, best of 3: 18.5 µs per loop
4 625 loops, best of 3: 18.8 µs per loop
5 625 loops, best of 3: 18.9 µs per loop
6 625 loops, best of 3: 19.5 µs per loop
7 625 loops, best of 3: 19.9 µs per loop
8 625 loops, best of 3: 20.3 µs per loop
9 625 loops, best of 3: 21 µs per loop
10 625 loops, best of 3: 21.4 µs per loop
11 625 loops, best of 3: 22 µs per loop
12 625 loops, best of 3: 22.4 µs per loop
13 625 loops, best of 3: 23.9 µs per loop
14 625 loops, best of 3: 24.9 µs per loop
15 625 loops, best of 3: 25.6 µs per loop
16 625 loops, best of 3: 27.2 µs per loop
17 625 loops, best of 3: 28.2 µs per loop
18 625 loops, best of 3: 29.8 µs per loop
19 625 loops, best of 3: 31.4 µs per loop
20 625 loops, best of 3: 33.1 µs per loop
21 625 loops, best of 3: 35 µs per loop
22 625 loops, best of 3: 37.2 µs per loop
23 625 loops, best of 3: 39.4 µs per loop
24 625 loops, best of 3: 38.3 µs per loop
25 625 loops, best of 3: 40.9 µs per loop
26 625 loops, best of 3: 43.2 µs per loop
27 625 loops, best of 3: 46 µs per loop
28 625 loops, best of 3: 49 µs per loop
29 625 loops, best of 3: 51.9 µs per loop
30 625 loops, best of 3: 55.2 µs per loop
31 625 loops, best of 3: 58.3 µs per loop
32 625 loops, best of 3: 62.8 µs per loop
33 625 loops, best of 3: 66.9 µs per loop
34 625 loops, best of 3: 71.1 µs per loop
35 625 loops, best of 3: 75.1 µs per loop
36 625 loops, best of 3: 68.1 µs per loop
37 625 loops, best of 3: 72.3 µs per loop
38 625 loops, best of 3: 76.9 µs per loop
39 625 loops, best of 3: 81.7 µs per loop
40 625 loops, best of 3: 85.8 µs per loop
41 625 loops, best of 3: 94.2 µs per loop
42 625 loops, best of 3: 99.8 µs per loop
43 625 loops, best of 3: 106 µs per loop
44 625 loops, best of 3: 112 µs per loop
45 625 loops, best of 3: 119 µs per loop
46 625 loops, best of 3: 126 µs per loop
47 625 loops, best of 3: 132 µs per loop
48 625 loops, best of 3: 123 µs per loop
49 625 loops, best of 3: 130 µs per loop
50 625 loops, best of 3: 137 µs per loop
51 625 loops, best of 3: 145 µs per loop
52 625 loops, best of 3: 153 µs per loop
53 625 loops, best of 3: 162 µs per loop
54 625 loops, best of 3: 170 µs per loop
55 625 loops, best of 3: 180 µs per loop
56 625 loops, best of 3: 190 µs per loop
57 625 loops, best of 3: 200 µs per loop
58 625 loops, best of 3: 210 µs per loop
59 625 loops, best of 3: 221 µs per loop
60 625 loops, best of 3: 202 µs per loop
61 625 loops, best of 3: 212 µs per loop
62 625 loops, best of 3: 224 µs per loop
63 625 loops, best of 3: 237 µs per loop
64 625 loops, best of 3: 248 µs per loop
65 625 loops, best of 3: 263 µs per loop
66 625 loops, best of 3: 276 µs per loop
67 625 loops, best of 3: 288 µs per loop
68 625 loops, best of 3: 305 µs per loop
69 625 loops, best of 3: 318 µs per loop
```


So, there is an improvement for bigger matrices as well.



---

archive/issue_comments_071022.json:
```json
{
    "body": "The patchbot found no doctest errors, but complains that the old patch has introduced white space.\n\nHence, I have updated the patch and hope that it will be fine now.\n\nApply trac8096_speedup_matrix_parent.patch",
    "created_at": "2012-03-11T08:53:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-71022",
    "user": "SimonKing"
}
```

The patchbot found no doctest errors, but complains that the old patch has introduced white space.

Hence, I have updated the patch and hope that it will be fine now.

Apply trac8096_speedup_matrix_parent.patch



---

archive/issue_comments_071023.json:
```json
{
    "body": "Curiously the latest version doesn't seem to build on 5.0.beta7: the patch applies, but the modified cython file `matrix_window.pyx` won't build. (See patchbot logs; I also reproduced this separately by hand.)",
    "created_at": "2012-03-11T09:24:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-71023",
    "user": "davidloeffler"
}
```

Curiously the latest version doesn't seem to build on 5.0.beta7: the patch applies, but the modified cython file `matrix_window.pyx` won't build. (See patchbot logs; I also reproduced this separately by hand.)



---

archive/issue_comments_071024.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-03-11T09:24:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-71024",
    "user": "davidloeffler"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_071025.json:
```json
{
    "body": "Replying to [comment:44 davidloeffler]:\n> Curiously the latest version doesn't seem to build on 5.0.beta7: the patch applies, but the modified cython file `matrix_window.pyx` won't build. (See patchbot logs; I also reproduced this separately by hand.)\n\nOops. Apparently, while removing white space, I have also removed something else. Sorry, I'll update it in a minute.",
    "created_at": "2012-03-11T12:14:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-71025",
    "user": "SimonKing"
}
```

Replying to [comment:44 davidloeffler]:
> Curiously the latest version doesn't seem to build on 5.0.beta7: the patch applies, but the modified cython file `matrix_window.pyx` won't build. (See patchbot logs; I also reproduced this separately by hand.)

Oops. Apparently, while removing white space, I have also removed something else. Sorry, I'll update it in a minute.



---

archive/issue_comments_071026.json:
```json
{
    "body": "Sorry that I did not try to build Sage again after manually editing the patch.\n\nI have updated the patch, and now it does build. I leave tests to the patchbot...\n\nApply trac8096_speedup_matrix_parent.patch",
    "created_at": "2012-03-11T12:18:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-71026",
    "user": "SimonKing"
}
```

Sorry that I did not try to build Sage again after manually editing the patch.

I have updated the patch, and now it does build. I leave tests to the patchbot...

Apply trac8096_speedup_matrix_parent.patch



---

archive/issue_comments_071027.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-03-11T12:18:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-71027",
    "user": "SimonKing"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071028.json:
```json
{
    "body": "Replaces the previous patches, rebased rel sage-5.0.beta7",
    "created_at": "2012-03-11T14:27:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-71028",
    "user": "SimonKing"
}
```

Replaces the previous patches, rebased rel sage-5.0.beta7



---

archive/issue_comments_071029.json:
```json
{
    "body": "Attachment [trac8096_speedup_matrix_parent.patch](tarball://root/attachments/some-uuid/ticket8096/trac8096_speedup_matrix_parent.patch) by SimonKing created at 2012-03-11 14:30:17\n\nArrgh! There was another trailing whitespace in the patch!\n\nIt should now be fixed.\n\nBy the way: Am I entitled to review the patch, even though rebasing the two original patches has not been totally mechanic? I still think that Tom and Robert are the authors, so that I could be reviewer. Agreed?",
    "created_at": "2012-03-11T14:30:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-71029",
    "user": "SimonKing"
}
```

Attachment [trac8096_speedup_matrix_parent.patch](tarball://root/attachments/some-uuid/ticket8096/trac8096_speedup_matrix_parent.patch) by SimonKing created at 2012-03-11 14:30:17

Arrgh! There was another trailing whitespace in the patch!

It should now be fixed.

By the way: Am I entitled to review the patch, even though rebasing the two original patches has not been totally mechanic? I still think that Tom and Robert are the authors, so that I could be reviewer. Agreed?



---

archive/issue_comments_071030.json:
```json
{
    "body": "Patchbot...\n\nApply trac8096_speedup_matrix_parent.patch",
    "created_at": "2012-03-11T14:30:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-71030",
    "user": "SimonKing"
}
```

Patchbot...

Apply trac8096_speedup_matrix_parent.patch



---

archive/issue_comments_071031.json:
```json
{
    "body": "I think reviewing patches you have rebased is allowed, as long as there's no change in functionality.",
    "created_at": "2012-03-11T14:40:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-71031",
    "user": "davidloeffler"
}
```

I think reviewing patches you have rebased is allowed, as long as there's no change in functionality.



---

archive/issue_comments_071032.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-03-13T01:48:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-71032",
    "user": "davidloeffler"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071033.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-03-21T22:04:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8096#issuecomment-71033",
    "user": "jdemeyer"
}
```

Resolution: fixed
