# Issue 2943: bug with power series and/or p-adics

Issue created by migration from Trac.

Original creator: jen

Original creation time: 2008-04-16 19:37:15

Assignee: was

CC:  roed

Keywords: power series, p-adic extensions

Can't manipulate certain elements of a power series ring:

```
sage: R.<x> = QQ[]
sage: p =11
sage: K = Qp(p,10)
sage: J.<a> = K.extension(x^2-p)
sage: C.<t> = LaurentSeriesRing(J)
sage: D.<s> = PowerSeriesRing(C)
sage: x = (10 + 10*a^2 + 10*a^4 + 10*a^6 + 10*a^8 + 10*a^10 + 10*a^12 + 10*a^14 + 10*a^16 + 10*a^18 + O(a^20)) + (2 + 2*a^4 + 2*a^8 + 2*a^12 + 2*a^16 + O(a^20))*t^2 + (10*a^2 + 5*a^4 + 7*a^6 + 6*a^8 + 3*a^10 + 2*a^12 + 9*a^14 + 3*a^16 + 2*a^18 + O(a^22))*t^4 + (10 + 7*a^2 + 9*a^4 + 8*a^6 + 5*a^8 + 10*a^12 + 3*a^14 + 6*a^16 + 8*a^18 + O(a^20))*t^6 + (6 + 2*a^4 + 8*a^6 + 6*a^8 + 2*a^10 + 6*a^12 + 6*a^14 + 4*a^16 + 5*a^18 + O(a^20))*t^8 + (9 + a^2 + 4*a^4 + 7*a^6 + a^8 + 2*a^10 + 4*a^12 + a^16 + 5*a^18 + O(a^20))*t^10 + (1 + 4*a^2 + 7*a^4 + 7*a^6 + 4*a^8 + 7*a^12 + 4*a^14 + 7*a^16 + 6*a^18 + O(a^20))*t^12 + ((7 + 4*a + 10*a^2 + 6*a^4 + 4*a^5 + 10*a^6 + 6*a^8 + 4*a^9 + 10*a^10 + 6*a^12 + 4*a^13 + 10*a^14 + 6*a^16 + 4*a^17 + 10*a^18 + O(a^20))*t^2 + O(a^20)*t^3 + (2*a + 4*a^2 + 4*a^3 + 9*a^4 + a^5 + 2*a^6 + 6*a^7 + 6*a^8 + 9*a^9 + 7*a^10 + 5*a^11 + a^12 + 4*a^13 + 7*a^14 + 3*a^15 + 6*a^16 + 8*a^17 + a^18 + 9*a^19 + O(a^20))*t^4 + O(a^20)*t^5 + (6 + 8*a + 7*a^2 + 8*a^3 + 7*a^4 + 7*a^5 + a^6 + 7*a^7 + 9*a^8 + 4*a^9 + 7*a^10 + 5*a^11 + 5*a^12 + 5*a^13 + 9*a^14 + 4*a^15 + 5*a^16 + 7*a^17 + 3*a^18 + a^19 + O(a^20))*t^6 + O(a^20)*t^7 + (7 + 2*a + 6*a^2 + 7*a^3 + 5*a^4 + 6*a^5 + 3*a^7 + a^8 + 3*a^9 + a^10 + 5*a^12 + 5*a^13 + 2*a^14 + 7*a^15 + 7*a^16 + 2*a^17 + 8*a^19 + O(a^20))*t^8 + O(a^20)*t^9 + (9 + 10*a + 3*a^2 + 8*a^3 + 2*a^4 + 2*a^5 + 3*a^6 + 5*a^7 + 5*a^8 + a^9 + 3*a^11 + 2*a^12 + 7*a^14 + a^15 + 8*a^17 + 4*a^18 + 5*a^19 + O(a^20))*t^10 + O(a^20)*t^11 + (10 + 7*a + 5*a^2 + 10*a^3 + 10*a^4 + a^5 + 6*a^6 + 3*a^7 + 9*a^8 + 9*a^9 + 5*a^10 + 7*a^11 + 3*a^12 + 7*a^13 + 10*a^14 + 3*a^15 + 9*a^16 + 9*a^17 + 7*a^18 + 4*a^19 + O(a^20))*t^12 + O(a^20)*t^13 + O(t^14))*s + ((2 + 7*a + 2*a^2 + 10*a^3 + 2*a^4 + 6*a^5 + 2*a^6 + 10*a^7 + 2*a^8 + 6*a^9 + 2*a^10 + 10*a^11 + 2*a^12 + 6*a^13 + 2*a^14 + 10*a^15 + 2*a^16 + 6*a^17 + 2*a^18 + 10*a^19 + O(a^20))*t^2 + O(a^20)*t^3 + (9*a + 7*a^2 + 3*a^3 + 4*a^4 + 6*a^5 + 3*a^6 + 10*a^7 + 6*a^8 + 2*a^9 + 9*a^11 + 5*a^12 + 9*a^13 + 9*a^14 + 10*a^15 + 4*a^17 + 8*a^18 + 4*a^19 + O(a^20))*t^4 + O(a^20)*t^5 + (7 + 5*a + 2*a^2 + 3*a^3 + 4*a^5 + 7*a^6 + 7*a^8 + 10*a^9 + a^10 + 2*a^11 + 9*a^12 + a^13 + a^15 + 3*a^16 + a^17 + 7*a^19 + O(a^20))*t^6 + O(a^20)*t^7 + (3 + 8*a + 2*a^3 + 9*a^4 + 8*a^5 + 10*a^6 + a^7 + 2*a^8 + 8*a^10 + 3*a^11 + 6*a^12 + 5*a^13 + 3*a^14 + 8*a^15 + 6*a^16 + 3*a^18 + 7*a^19 + O(a^20))*t^8 + O(a^20)*t^9 + (9 + 2*a + 6*a^2 + 5*a^3 + 10*a^4 + 10*a^5 + a^6 + a^7 + 10*a^8 + 10*a^10 + a^11 + 3*a^12 + 10*a^13 + 3*a^14 + a^15 + 6*a^16 + a^17 + 2*a^18 + 9*a^19 + O(a^20))*t^10 + O(a^20)*t^11 + (7*a + 6*a^3 + 5*a^4 + 3*a^5 + 9*a^6 + 9*a^7 + 4*a^9 + 7*a^10 + 5*a^11 + 4*a^12 + 9*a^13 + a^14 + 3*a^16 + 5*a^18 + 10*a^19 + O(a^20))*t^12 + O(a^20)*t^13 + O(t^14))*s^2 + ((4*a^2 + 10*a^3 + 10*a^4 + 8*a^6 + 4*a^7 + 3*a^8 + 4*a^10 + 4*a^11 + 2*a^12 + 9*a^13 + a^14 + 9*a^15 + 6*a^16 + 5*a^17 + 10*a^18 + 10*a^19 + 3*a^20 + O(a^22))*t^4 + O(a^22)*t^5 + (9 + 6*a + 8*a^3 + 3*a^4 + 9*a^5 + 8*a^6 + 10*a^7 + 3*a^8 + 6*a^9 + 4*a^10 + 6*a^12 + a^13 + 7*a^14 + 8*a^15 + 2*a^16 + 2*a^17 + 7*a^18 + a^19 + O(a^20))*t^6 + O(a^20)*t^7 + (5 + 10*a + 10*a^3 + 9*a^4 + 4*a^5 + 10*a^6 + 5*a^7 + 6*a^8 + a^10 + 7*a^11 + 6*a^12 + 4*a^13 + 8*a^14 + a^15 + 7*a^16 + 6*a^17 + 8*a^18 + 6*a^19 + O(a^20))*t^8 + O(a^20)*t^9 + (9 + 3*a + 5*a^2 + 9*a^5 + 4*a^6 + 9*a^7 + 6*a^9 + 6*a^10 + 7*a^11 + 9*a^13 + 4*a^14 + 8*a^15 + 6*a^16 + a^17 + 5*a^18 + 5*a^19 + O(a^20))*t^10 + O(a^20)*t^11 + (7*a + a^2 + 2*a^3 + 9*a^4 + 10*a^6 + 8*a^7 + a^8 + 9*a^9 + 4*a^10 + 4*a^11 + 10*a^12 + 8*a^13 + 7*a^14 + a^15 + 7*a^16 + 10*a^17 + 5*a^18 + 6*a^19 + O(a^20))*t^12 + O(a^20)*t^13 + (9*a^2 + 7*a^3 + 2*a^4 + 2*a^5 + 10*a^6 + 10*a^7 + 5*a^8 + 4*a^9 + 2*a^11 + 2*a^12 + 6*a^13 + 6*a^14 + 4*a^15 + a^16 + 6*a^17 + 7*a^18 + 2*a^19 + O(a^20))*t^14 + O(a^20)*t^15 + O(t^16))*s^3 + ((10*a^2 + 4*a^3 + 10*a^4 + 2*a^5 + 8*a^6 + a^7 + 2*a^8 + 9*a^9 + 7*a^10 + 2*a^11 + 8*a^12 + 9*a^13 + 4*a^14 + 8*a^15 + 6*a^16 + 2*a^17 + a^18 + 8*a^19 + 7*a^20 + O(a^22))*t^4 + O(a^22)*t^5 + (7 + 5*a + 6*a^2 + 5*a^3 + 3*a^6 + 6*a^7 + 3*a^10 + 10*a^11 + 6*a^12 + 4*a^13 + 5*a^14 + 7*a^15 + 9*a^17 + 6*a^18 + 2*a^19 + O(a^20))*t^6 + O(a^20)*t^7 + (2 + 4*a^2 + 2*a^3 + 9*a^4 + 2*a^5 + 3*a^6 + 9*a^7 + 7*a^8 + 10*a^9 + 2*a^10 + 7*a^11 + 10*a^12 + 5*a^13 + 6*a^14 + 10*a^15 + 2*a^16 + 10*a^17 + 9*a^18 + 9*a^19 + O(a^20))*t^8 + O(a^20)*t^9 + (9 + 5*a + 9*a^2 + 8*a^5 + 10*a^6 + 4*a^7 + 5*a^8 + 8*a^9 + 8*a^10 + 3*a^11 + 5*a^12 + 3*a^13 + 2*a^14 + 5*a^15 + 3*a^16 + a^17 + 6*a^18 + 6*a^19 + O(a^20))*t^10 + O(a^20)*t^11 + (2*a + 2*a^2 + 10*a^3 + 3*a^4 + 7*a^5 + 7*a^6 + 2*a^7 + 2*a^8 + 5*a^9 + a^10 + 5*a^11 + a^12 + 8*a^14 + 7*a^16 + 4*a^17 + 5*a^18 + 10*a^19 + O(a^20))*t^12 + O(a^20)*t^13 + (2*a + 8*a^2 + 2*a^3 + 8*a^4 + 7*a^5 + 6*a^6 + 3*a^7 + 6*a^9 + 10*a^10 + 4*a^11 + 2*a^12 + 6*a^13 + 7*a^14 + 5*a^15 + 8*a^16 + 2*a^17 + 3*a^18 + 10*a^19 + O(a^20))*t^14 + O(a^20)*t^15 + O(t^16))*s^4 + ((6 + 3*a + a^2 + a^3 + 3*a^4 + a^5 + 6*a^6 + 6*a^7 + 9*a^8 + 6*a^9 + 8*a^10 + 10*a^11 + 8*a^12 + 4*a^13 + 6*a^14 + 8*a^15 + 8*a^16 + a^17 + 10*a^18 + 2*a^19 + O(a^20))*t^6 + O(a^20)*t^7 + (5 + 4*a + 2*a^2 + 5*a^3 + 2*a^4 + 8*a^7 + 10*a^8 + 9*a^9 + 10*a^10 + 2*a^11 + 2*a^12 + 10*a^13 + 5*a^15 + 4*a^16 + 6*a^18 + 7*a^19 + O(a^20))*t^8 + O(a^20)*t^9 + (9 + 8*a + 6*a^2 + 7*a^3 + 9*a^4 + 7*a^5 + 9*a^6 + 7*a^7 + 10*a^8 + 9*a^9 + 5*a^10 + 3*a^12 + 4*a^13 + 5*a^15 + 6*a^16 + 4*a^17 + 6*a^18 + 3*a^19 + O(a^20))*t^10 + O(a^20)*t^11 + (9*a + 10*a^2 + 9*a^3 + 2*a^4 + 8*a^5 + 10*a^6 + 9*a^7 + 10*a^8 + 8*a^9 + 4*a^11 + 6*a^13 + 5*a^14 + 5*a^15 + 5*a^16 + 7*a^17 + 10*a^18 + 2*a^19 + O(a^20))*t^12 + O(a^20)*t^13 + (5*a + 9*a^2 + 7*a^3 + 7*a^4 + 7*a^5 + 3*a^6 + 9*a^7 + 3*a^8 + 7*a^9 + 10*a^10 + a^11 + 4*a^12 + 10*a^13 + 8*a^14 + 3*a^15 + 2*a^16 + 3*a^17 + 8*a^18 + 10*a^19 + O(a^20))*t^14 + O(a^20)*t^15 + (9*a^2 + 10*a^5 + 9*a^6 + 8*a^7 + 10*a^8 + 10*a^9 + 5*a^10 + 9*a^11 + 3*a^12 + 4*a^13 + 9*a^14 + 10*a^15 + 6*a^16 + 8*a^17 + 3*a^18 + 6*a^19 + O(a^20))*t^16 + O(a^20)*t^17 + O(t^18))*s^5 + ((10 + 6*a + 3*a^2 + 5*a^3 + 3*a^4 + 9*a^5 + 8*a^6 + a^7 + 6*a^8 + 4*a^9 + 10*a^10 + 3*a^11 + 3*a^12 + 4*a^13 + 3*a^14 + 3*a^15 + 7*a^16 + 10*a^17 + 7*a^18 + 6*a^19 + O(a^20))*t^6 + O(a^20)*t^7 + (3 + 7*a + a^2 + 9*a^3 + 8*a^4 + 8*a^5 + 5*a^6 + 4*a^7 + 6*a^8 + 8*a^9 + a^10 + 10*a^11 + 2*a^12 + 5*a^14 + 7*a^15 + 6*a^16 + 8*a^17 + 3*a^19 + O(a^20))*t^8 + O(a^20)*t^9 + (9 + 2*a + 4*a^2 + 10*a^3 + 3*a^4 + 10*a^5 + 8*a^6 + 6*a^7 + 8*a^8 + 4*a^9 + 3*a^10 + 7*a^11 + 10*a^12 + 10*a^13 + 5*a^14 + 6*a^15 + 6*a^17 + 10*a^18 + 2*a^19 + O(a^20))*t^10 + O(a^20)*t^11 + (5*a + 4*a^2 + 5*a^3 + 9*a^4 + 4*a^5 + 10*a^6 + 7*a^7 + 4*a^8 + 9*a^9 + 8*a^10 + 3*a^11 + 10*a^12 + 9*a^13 + 6*a^14 + a^15 + 3*a^16 + 8*a^17 + 8*a^18 + 9*a^19 + O(a^20))*t^12 + O(a^20)*t^13 + (a + 7*a^2 + 10*a^3 + 9*a^4 + 3*a^5 + 2*a^6 + 5*a^7 + 6*a^10 + 10*a^11 + 7*a^13 + 5*a^14 + 5*a^15 + 8*a^16 + 6*a^17 + 2*a^18 + 5*a^19 + O(a^20))*t^14 + O(a^20)*t^15 + (5*a + 8*a^2 + 4*a^4 + 2*a^5 + 7*a^6 + 4*a^7 + 8*a^8 + 8*a^9 + 6*a^10 + 10*a^11 + 8*a^12 + 2*a^13 + 6*a^15 + 10*a^16 + 9*a^17 + a^19 + O(a^20))*t^16 + O(a^20)*t^17 + O(t^18))*s^6 + ((7 + 6*a + 10*a^2 + 5*a^3 + 4*a^4 + 10*a^5 + 3*a^6 + 5*a^7 + a^8 + 4*a^9 + 3*a^10 + 5*a^11 + 2*a^12 + 2*a^13 + a^14 + 3*a^16 + 8*a^17 + 10*a^18 + 4*a^19 + O(a^20))*t^8 + O(a^20)*t^9 + (9 + 6*a + 7*a^2 + 8*a^3 + 3*a^4 + 2*a^5 + 4*a^6 + 2*a^7 + 5*a^8 + 9*a^9 + 6*a^10 + 8*a^12 + 6*a^14 + 5*a^15 + 9*a^16 + 2*a^17 + 2*a^18 + a^19 + O(a^20))*t^10 + O(a^20)*t^11 + (6*a + 3*a^2 + 4*a^4 + 2*a^5 + 3*a^6 + a^7 + 3*a^8 + 3*a^9 + 9*a^10 + 5*a^11 + 7*a^13 + 9*a^14 + 5*a^15 + 10*a^17 + 7*a^18 + 4*a^19 + O(a^20))*t^12 + O(a^20)*t^13 + (a + 3*a^2 + 9*a^4 + 10*a^5 + 4*a^6 + 6*a^7 + 10*a^8 + 4*a^9 + 7*a^10 + 7*a^11 + 7*a^12 + 5*a^13 + 5*a^14 + 5*a^15 + 3*a^18 + 6*a^19 + O(a^20))*t^14 + O(a^20)*t^15 + (2*a^2 + 2*a^3 + 8*a^4 + 8*a^5 + 7*a^6 + 10*a^7 + 4*a^8 + 9*a^9 + 10*a^10 + 7*a^11 + 4*a^12 + 4*a^13 + 4*a^14 + 10*a^15 + 10*a^16 + a^17 + 7*a^18 + O(a^20))*t^16 + O(a^20)*t^17 + (9*a + 5*a^2 + 7*a^3 + 5*a^4 + 3*a^5 + 5*a^6 + 6*a^7 + 6*a^8 + 8*a^9 + 8*a^10 + a^11 + 9*a^12 + 3*a^13 + 3*a^14 + 4*a^15 + 9*a^16 + a^17 + 3*a^18 + 9*a^19 + O(a^20))*t^18 + O(a^20)*t^19 + O(t^20))*s^7 + ((6 + 7*a + 3*a^2 + 8*a^4 + 2*a^5 + 7*a^6 + 5*a^7 + 4*a^8 + 6*a^9 + 8*a^10 + 6*a^11 + a^12 + 9*a^13 + 2*a^15 + a^16 + 6*a^17 + a^18 + 7*a^19 + O(a^20))*t^8 + O(a^20)*t^9 + (9 + 3*a + 6*a^2 + 10*a^3 + 4*a^4 + 2*a^5 + 10*a^6 + 2*a^7 + 9*a^9 + a^10 + 7*a^11 + 10*a^12 + 4*a^14 + 9*a^15 + 8*a^16 + 7*a^17 + 10*a^18 + 7*a^19 + O(a^20))*t^10 + O(a^20)*t^11 + (5*a + 8*a^2 + a^3 + 10*a^4 + a^5 + 7*a^6 + 2*a^7 + 8*a^8 + 5*a^9 + 10*a^10 + 4*a^11 + 3*a^12 + 7*a^13 + 4*a^14 + 4*a^15 + 10*a^16 + 2*a^17 + 3*a^18 + 7*a^19 + O(a^20))*t^12 + O(a^20)*t^13 + (2*a^2 + a^3 + 3*a^4 + 7*a^5 + 7*a^6 + 3*a^7 + 4*a^8 + 10*a^9 + 7*a^10 + 5*a^11 + 2*a^12 + a^13 + 9*a^14 + 7*a^15 + 10*a^16 + 7*a^17 + 3*a^18 + 3*a^19 + O(a^20))*t^14 + O(a^20)*t^15 + (10*a + 8*a^2 + 5*a^3 + a^4 + 5*a^5 + 10*a^6 + 2*a^7 + 7*a^8 + 3*a^9 + 2*a^10 + 7*a^11 + 8*a^12 + 9*a^13 + 2*a^14 + 4*a^15 + 4*a^16 + 10*a^17 + 7*a^18 + O(a^20))*t^16 + O(a^20)*t^17 + (2*a^2 + 9*a^3 + 8*a^5 + 8*a^6 + 10*a^7 + 2*a^8 + 9*a^9 + a^10 + 2*a^12 + 5*a^13 + 3*a^14 + 6*a^15 + 8*a^16 + 4*a^17 + 5*a^18 + 4*a^19 + O(a^20))*t^18 + O(a^20)*t^19 + O(t^20))*s^8 + ((9 + 7*a + 8*a^2 + a^3 + 8*a^4 + 9*a^5 + 4*a^6 + 2*a^7 + 4*a^8 + 10*a^9 + 2*a^10 + 3*a^11 + 9*a^12 + 3*a^13 + 9*a^14 + 4*a^15 + 10*a^16 + a^17 + 8*a^18 + 7*a^19 + O(a^20))*t^10 + O(a^20)*t^11 + (9*a + 7*a^2 + 10*a^3 + 6*a^4 + 9*a^5 + 6*a^6 + 9*a^8 + 3*a^9 + 4*a^10 + a^12 + 4*a^13 + 2*a^14 + 4*a^15 + 10*a^16 + 10*a^17 + 5*a^18 + 4*a^19 + O(a^20))*t^12 + O(a^20)*t^13 + (8*a + 6*a^2 + 5*a^3 + 3*a^4 + 7*a^5 + 5*a^6 + 10*a^7 + 7*a^8 + 5*a^9 + a^10 + 5*a^11 + 3*a^12 + 3*a^13 + 3*a^14 + 7*a^15 + 7*a^16 + a^17 + 7*a^18 + 6*a^19 + O(a^20))*t^14 + O(a^20)*t^15 + (10*a + 9*a^2 + 2*a^3 + a^4 + a^5 + 3*a^6 + a^8 + 8*a^10 + 7*a^11 + 5*a^12 + 3*a^14 + 9*a^16 + 3*a^17 + 7*a^18 + 8*a^19 + O(a^20))*t^16 + O(a^20)*t^17 + (6*a + 9*a^2 + 8*a^3 + 7*a^4 + 2*a^5 + 5*a^6 + 3*a^7 + 6*a^8 + 2*a^9 + a^10 + 4*a^12 + 8*a^13 + 10*a^14 + 5*a^15 + 4*a^16 + 3*a^17 + 9*a^18 + 7*a^19 + O(a^20))*t^18 + O(a^20)*t^19 + (2*a + 10*a^2 + a^3 + 2*a^4 + 8*a^5 + 3*a^6 + 4*a^7 + a^8 + 6*a^9 + a^10 + a^11 + a^12 + 10*a^13 + 8*a^14 + 3*a^15 + 2*a^16 + 7*a^19 + O(a^20))*t^20 + O(a^20)*t^21 + O(t^22))*s^9 + ((9 + 9*a + 10*a^2 + a^3 + 6*a^4 + 2*a^5 + 2*a^6 + 4*a^8 + 6*a^9 + 7*a^10 + 7*a^11 + a^12 + a^13 + 8*a^14 + 7*a^15 + 3*a^16 + 8*a^17 + 6*a^19 + O(a^20))*t^10 + O(a^20)*t^11 + (10*a + 4*a^2 + a^4 + 4*a^5 + 5*a^6 + 5*a^7 + 9*a^8 + 3*a^9 + 7*a^11 + 4*a^12 + 2*a^13 + 2*a^14 + 5*a^15 + 3*a^16 + 3*a^17 + 8*a^18 + 4*a^19 + O(a^20))*t^12 + O(a^20)*t^13 + (4*a + 2*a^2 + 7*a^3 + 8*a^4 + 10*a^5 + 3*a^6 + 10*a^7 + 5*a^8 + 6*a^9 + a^10 + 9*a^11 + 6*a^12 + 2*a^13 + 10*a^14 + 8*a^15 + a^16 + 5*a^17 + 6*a^18 + 9*a^19 + O(a^20))*t^14 + O(a^20)*t^15 + (5*a + 3*a^2 + 10*a^3 + 9*a^4 + 7*a^6 + 3*a^7 + 9*a^8 + 5*a^9 + 8*a^10 + 10*a^11 + 10*a^12 + 10*a^13 + 10*a^14 + 3*a^15 + 2*a^16 + 8*a^17 + a^18 + 10*a^19 + O(a^20))*t^16 + O(a^20)*t^17 + (3*a + 3*a^2 + 9*a^3 + 9*a^4 + a^5 + 2*a^6 + 7*a^7 + 7*a^9 + 3*a^10 + 7*a^11 + 2*a^12 + a^13 + 8*a^14 + 3*a^15 + 8*a^16 + 10*a^17 + 9*a^19 + O(a^20))*t^18 + O(a^20)*t^19 + (a + 7*a^2 + 10*a^3 + 2*a^4 + 6*a^5 + 7*a^6 + 5*a^7 + 4*a^8 + 8*a^9 + 10*a^10 + 5*a^14 + a^15 + 2*a^16 + 9*a^17 + 8*a^18 + O(a^20))*t^20 + O(a^20)*t^21 + O(t^22))*s^10 + ((10 + 5*a^2 + a^3 + 5*a^4 + 9*a^5 + 6*a^6 + 8*a^7 + 10*a^8 + a^9 + 6*a^10 + 9*a^11 + 9*a^12 + 8*a^13 + 3*a^14 + a^15 + 8*a^16 + 8*a^17 + 2*a^18 + 2*a^19 + O(a^20))*t^12 + O(a^20)*t^13 + (6*a^3 + 6*a^4 + 10*a^5 + 4*a^6 + 2*a^7 + 7*a^8 + 3*a^9 + 8*a^11 + 10*a^12 + a^13 + 4*a^14 + 10*a^15 + 4*a^16 + 2*a^17 + 3*a^18 + 7*a^19 + O(a^20))*t^14 + O(a^20)*t^15 + (9*a^3 + 5*a^4 + 3*a^5 + 7*a^6 + 3*a^7 + 10*a^9 + 2*a^10 + a^11 + 8*a^12 + a^14 + 3*a^15 + 3*a^16 + 2*a^17 + 7*a^18 + 7*a^19 + O(a^20))*t^16 + O(a^20)*t^17 + (3*a^3 + 2*a^4 + a^5 + 2*a^6 + 2*a^8 + 4*a^9 + 10*a^10 + 10*a^11 + 3*a^12 + 7*a^13 + 7*a^14 + 3*a^15 + 8*a^16 + a^17 + 3*a^18 + 5*a^19 + O(a^20))*t^18 + O(a^20)*t^19 + (4*a^3 + 2*a^4 + 4*a^6 + 5*a^7 + 3*a^8 + 7*a^10 + 7*a^12 + a^13 + 4*a^15 + 7*a^17 + 8*a^18 + 7*a^19 + O(a^20))*t^20 + O(a^20)*t^21 + (5*a^3 + a^4 + 9*a^5 + 8*a^6 + 3*a^7 + 2*a^8 + 2*a^9 + 3*a^10 + 10*a^11 + 2*a^12 + 3*a^13 + 8*a^14 + 3*a^15 + 8*a^16 + 2*a^17 + 3*a^18 + 5*a^19 + O(a^20))*t^22 + O(a^20)*t^23 + O(t^24))*s^11 + ((1 + 10*a + 4*a^2 + 5*a^3 + 2*a^4 + a^5 + 7*a^7 + 9*a^8 + a^9 + 7*a^10 + 7*a^11 + 2*a^12 + 4*a^13 + 2*a^14 + 8*a^15 + 2*a^16 + 2*a^17 + 3*a^18 + 8*a^19 + O(a^20))*t^12 + O(a^20)*t^13 + (5*a + 6*a^3 + 6*a^4 + a^5 + 6*a^6 + 4*a^7 + 2*a^8 + 3*a^9 + 9*a^10 + 8*a^11 + 7*a^12 + 5*a^13 + 5*a^14 + a^15 + 10*a^16 + 7*a^17 + 4*a^18 + 3*a^19 + O(a^20))*t^14 + O(a^20)*t^15 + (2*a + 8*a^3 + 5*a^4 + 5*a^5 + 3*a^6 + 5*a^7 + 3*a^8 + 9*a^9 + 5*a^11 + 9*a^12 + 5*a^13 + 3*a^14 + 9*a^15 + 3*a^16 + 5*a^17 + a^18 + 8*a^19 + O(a^20))*t^16 + O(a^20)*t^17 + (8*a + 5*a^3 + 2*a^4 + 8*a^5 + 3*a^6 + 9*a^7 + 7*a^8 + 8*a^9 + 6*a^10 + 8*a^11 + 9*a^12 + 9*a^13 + 8*a^14 + 8*a^15 + 7*a^16 + 8*a^17 + 7*a^19 + O(a^20))*t^18 + O(a^20)*t^19 + (7*a + 4*a^3 + 2*a^4 + 5*a^5 + 5*a^6 + 8*a^7 + 9*a^8 + 2*a^9 + 6*a^10 + 10*a^11 + 10*a^12 + 6*a^13 + 10*a^14 + 5*a^15 + 7*a^16 + 7*a^17 + 9*a^18 + O(a^20))*t^20 + O(a^20)*t^21 + (6*a + 9*a^3 + a^4 + 8*a^5 + a^6 + a^7 + 2*a^8 + a^10 + 4*a^11 + 3*a^12 + 7*a^13 + 5*a^14 + 8*a^15 + 4*a^17 + 9*a^18 + 5*a^19 + O(a^20))*t^22 + O(a^20)*t^23 + O(t^24))*s^12
sage: y = (1 + O(a^20))*t + ((10 + a + 10*a^2 + 10*a^4 + 10*a^6 + 10*a^8 + 10*a^10 + 10*a^12 + 10*a^14 + 10*a^16 + 10*a^18 + O(a^20))*t + O(a^21)*t^2 + (6*a + 7*a^3 + 7*a^5 + 5*a^7 + 9*a^9 + 3*a^11 + 2*a^15 + 2*a^17 + O(a^21))*t^3 + O(a^21)*t^4 + (9*a + a^3 + 2*a^5 + 6*a^7 + 2*a^11 + 4*a^13 + 2*a^17 + a^19 + O(a^21))*t^5 + O(a^21)*t^6 + (3*a + a^3 + 5*a^5 + a^11 + 4*a^13 + 9*a^15 + 4*a^17 + 9*a^19 + O(a^21))*t^7 + O(a^21)*t^8 + (4*a + 8*a^3 + 4*a^5 + a^11 + 10*a^13 + 7*a^15 + 2*a^17 + 3*a^19 + O(a^21))*t^9 + O(a^21)*t^10 + (5*a + 9*a^3 + 2*a^5 + 5*a^9 + 8*a^11 + 5*a^13 + 3*a^15 + 5*a^17 + 8*a^19 + O(a^21))*t^11 + O(t^13))*s
sage: f = x/y                 #ok
sage: g = x*derivative(x)     #ok
sage: h = x*derivative(x)/y  
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/jen/<ipython console> in <module>()

/home/jen/element.pyx in sage.structure.element.RingElement.__div__()

/home/jen/coerce.pxi in sage.structure.element._div_c()

/home/jen/power_series_ring_element.pyx in sage.rings.power_series_ring_element.PowerSeries._div_c_impl()

/home/jen/element.pyx in sage.structure.element.RingElement.__mul__()

/home/jen/coerce.pxi in sage.structure.element._mul_c()

/home/jen/power_series_poly.pyx in sage.rings.power_series_poly.PowerSeries_poly._mul_c_impl()

/home/jen/element.pyx in sage.structure.element.RingElement.__mul__()

/home/jen/coerce.pxi in sage.structure.element._mul_c()

/home/jen/element.pyx in sage.structure.element.RingElement._mul_()

/home/jen/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.Polynomial._mul_c_impl()

/home/jen/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.Polynomial._mul_karatsuba()

/home/jen/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.do_karatsuba()

/home/jen/polynomial_element.pyx in sage.rings.polynomial.polynomial_element._karatsuba_sum()

/home/jen/element.pyx in sage.structure.element.ModuleElement.__add__()

/home/jen/coerce.pxi in sage.structure.element._add_c()

/home/jen/laurent_series_ring_element.pyx in sage.rings.laurent_series_ring_element.LaurentSeries._add_c_impl()

/home/jen/laurent_series_ring_element.pyx in sage.rings.laurent_series_ring_element.LaurentSeries.__init__()

/home/jen/power_series_poly.pyx in sage.rings.power_series_poly.PowerSeries_poly.valuation()

/home/jen/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.Polynomial.valuation()

<type 'exceptions.TypeError'>: The polynomial, p, must have the same parent as self.
```



---

Comment by jen created at 2008-04-18 14:43:01

This is strange:

```
sage: (derivative(x)).parent()
Power Series Ring in s over Laurent Series Ring in t over Eisenstein Extension of 11-adic Field with capped relative precision 10 in a defined by (1 + O(11^10))*x^2 + (10*11 + 10*11^2 + 10*11^3 + 10*11^4 + 10*11^5 + 10*11^6 + 10*11^7 + 10*11^8 + 10*11^9 + 10*11^10 + O(11^11))
sage: y.parent()
Power Series Ring in s over Laurent Series Ring in t over Eisenstein Extension of 11-adic Field with capped relative precision 10 in a defined by (1 + O(11^10))*x^2 + (10*11 + 10*11^2 + 10*11^3 + 10*11^4 + 10*11^5 + 10*11^6 + 10*11^7 + 10*11^8 + 10*11^9 + 10*11^10 + O(11^11))
sage: (derivative(x)).parent == y.parent()
False
```



---

Comment by jen created at 2008-04-18 14:43:01

Changing priority from major to critical.


---

Comment by dmharvey created at 2008-04-29 19:28:47

Here is a much smaller example that triggers the bug:


```
sage: R.<u> = QQ[]
sage: p = 11
sage: K = Qp(p,10)
sage: J.<a> = K.extension(u^2-p)
sage: C.<t> = LaurentSeriesRing(J)
sage: D.<s> = PowerSeriesRing(C)

sage: y = t + (t^2 + O(t^3))*s
sage: h = y / y
[boom]
```


Interestingly, if we use the vanilla p-adics instead of a ramified extension, we get a different traceback, which seems to indicate a different (possibly related?) bug:


```
sage: R.<u> = QQ[]
sage: p = 11
sage: K = Qp(p,10)
sage: C.<t> = LaurentSeriesRing(K)
sage: D.<s> = PowerSeriesRing(C)

sage: y = t + (t^2 + O(t^3))*s

sage: h = y / y
Traceback (most recent call last):
...
File "/Users/david/sage-2.11/local/lib/python2.5/site-packages/sage/rings/polynomial/padics/polynomial_padic_capped_relative_dense.py", line 379, in __getslice__
    raise IndexError, "list index out of range"
IndexError: list index out of range
```



---

Comment by dmharvey created at 2008-04-29 20:32:57

Even series inversion gives the list index breakage:


```
sage: p = 11
sage: K = Qp(p,10)
sage: C.<t> = LaurentSeriesRing(K)
sage: D.<s> = PowerSeriesRing(C)
sage: z = 1 + (t^3 + O(t^13))*s
sage: 1/z
```



---

Comment by dmharvey created at 2008-04-29 20:48:39

Actually even just squaring something really simple can break:


```
sage: K = Qp(p,10)
sage: C.<t> = LaurentSeriesRing(K)
sage: D.<s> = PowerSeriesRing(C)
sage: z = (1 + O(t)) + t*s^2
sage: z * z
[boom]
```



---

Comment by dmharvey created at 2008-04-29 20:55:57

ok, the bug is in the polynomial mult instead of the power series mult:


```
sage: K = Qp(p,10)
sage: C.<t> = LaurentSeriesRing(K)
sage: D.<s> = PolynomialRing(C)
sage: z = (1 + O(t)) + t*s^2
sage: z * z
[boom]
```



---

Comment by dmharvey created at 2008-04-29 21:29:31

At least part of this bug is caused by some broken code in p-adic polynomial getslice. Here is the example from the docstring:


```
sage: K = Qp(13,7)
sage: R.<t> = K[]       
sage: a = 13^7*t^3 + K(169,4)*t - 13^4
sage: a[1:2]
(13^2 + O(13^4))*t
```


but this one dies:

```
sage: t[0:1]
[boom]
```



---

Comment by dmharvey created at 2008-04-30 18:02:40

A smaller example of the original bug (this example involves only multiplication, no division):


```
sage: R.<u> = QQ[]
sage: p = 11
sage: K = Qp(p,10)
sage: J.<a> = K.extension(u^2-p)
sage: C.<t> = LaurentSeriesRing(J)
sage: D.<s> = PowerSeriesRing(C)
sage: x = t + (t^2 + O(t^3))*s
sage: y = t^(-1) + (-1 + O(t))*s + O(s^2)
sage: x * y
[boom]
```



---

Comment by dmharvey created at 2008-04-30 18:09:55

Even simpler (doesn't need the outer PowerSeries ring):


```
R.<u> = QQ[]
p = 11
K = Qp(p,10)
J.<a> = K.extension(u^2-p)
C.<t> = LaurentSeriesRing(J)
D.<s> = PolynomialRing(C)
x = t + (t^2 + O(t^3))*s
y = t^(-1) + (-1 + O(t))*s
h = x * y
[boom]
```



---

Comment by dmharvey created at 2008-04-30 20:43:02

I just did some more debugging with David Roe and I'm just going to write down our discoveries since I'm exhausted now.

The problem is, at some point a Laurent series object is coming into existence whose unit part is a power series whose coefficients are all indistinguishable from zero (but not actually zero). Then when calling valuation on that laurent series, something blows up. It only happens when the base ring is unramified extensions of Qp, since something in the underlying polynomial class hasn't been implemented properly. (Maybe.)

The actual exception generated is a bit misleading. It comes up in the last line of this code in `polynomial_element.pyx`:


```
        if p is None:
            for k from 0 <= k <= self.degree():
                if self[k]:
                    return ZZ(k)
                
        if not isinstance(p, Polynomial) or not p.parent() is self.parent():
            raise TypeError, "The polynomial, p, must have the same parent as self."
```


It's entering the loop with p == None, but it should never drop out of the bottom of the loop (it expects to find a nonzero-coefficient).


---

Comment by dmharvey created at 2008-05-10 19:02:11

Getting closer now.

Set up some polynomial rings over Qp and an unramified extension of Qp. Notice that the polynomial ring over Qp itself uses a specialised type, whereas over the ramified extension uses the generic polynomial ring:

```
sage: R.<u> = QQ[]
sage: p = 7
sage: K = Qp(p, 10)
sage: J.<a> = K.extension(u^2 - p)
sage: 
sage: S.<x> = PolynomialRing(K)
sage: T.<y> = PolynomialRing(J)
sage: 
sage: type(S)
<class 'sage.rings.polynomial.polynomial_ring.PolynomialRing_dense_padic_field_capped_relative'>
sage: type(T)
<class 'sage.rings.polynomial.polynomial_ring.PolynomialRing_field'>
```


The specialised type lets you have polynomials whose coefficients are indistinguishable from zero, but it still knows that the whole polynomial is "zero":


```
sage: f = S([O(p^5), O(p^5)])
sage: f
(O(7^5))*x + (O(7^5))
sage: f.__nonzero__()
False
```


But the generic polynomial type just strips them off, since it thinks they are zero:


```
sage: g = T([O(a^5), O(a^5)])
sage: g
0
sage: g.coeffs()
[]
sage: g.__nonzero__()
False
```


Now we can try forcing the generic code to let us have coefficients indistinguishable from zero:

```
sage: g = T([O(a^5), O(a^5)], check=False)
sage: g
0
sage: g.coeffs()
[O(a^5), O(a^5)]
sage: g.__nonzero__()
True
```


And that's basically the problem. The generic polynomial code thinks that the polynomial is nonzero because its coefficient list is non-empty.


---

Comment by dmharvey created at 2008-05-10 20:45:31

After discussion with broune and cwitty on IRC, the proposed solution is as follows:

 * in the long run, implement the specialised class for polynomials over ramified extension rings; but we don't have time to do this right now.
 * change the generic polynomial's `__nonzero__` method to first check the base ring's `is_exact` method. If the base ring is not exact, we need to check whether each coefficient of the polynomial is zero.
 * for performance reasons, change `is_exact` to a cpdef method (also, probably move it up the hierarchy from rings to parents).


---

Attachment

Attached patch should fix this bug.

(Note: this does not fix the "list index" exception issue, which also came up in the above discussion. That is now a separate ticket: #3184)


---

Comment by dmharvey created at 2008-05-19 00:16:25

After this patch, there is still a bug (thanks Kiran Kedlaya for pointing this out). Here is an example:


```
sage: R.<u> = QQ[]
sage: p = 11
sage: K = Qp(p,10)
sage: J.<a> = K.extension(u^2-p)
sage: C.<t> = LaurentSeriesRing(J)
sage: D.<s> = PowerSeriesRing(C)
sage: y = 1 - (t + O(t^2))*s + O(s^5)
sage: 1/y
(1 + O(a^20)) + ((1 + O(a^20))*t + O(t^2))*s + O(s^5)
```


The output is wrong; there should be s<sup>2</sup>, s<sup>3</sup>, s<sup>4</sup> terms.

Kiran's example was:


```
sage: R.<u> = QQ[]
sage: p = 11
sage: K = Qp(p,10)
sage: J.<a> = K.extension(u^2-p)
sage: C.<t> = LaurentSeriesRing(J)
sage: D.<s> = PowerSeriesRing(C)

sage: y = t + (t^2 + O(t^3))*s
sage: h = y / y
sage: h
(1 + O(a^20)) + O(t^2)*s + O(t^2)*s^2 + O(t^3)*s^3 + O(t^4)*s^4 +
O(t^5)*s^5 + ((7 + 10*a^2 + 10*a^4 + 10*a^6 + 10*a^8 + 10*a^10 + 10*a^12
+ 10*a^14 + 10*a^16 + 10*a^18 + O(a^20))*t^6 + O(t^7))*s^6 + O(s^20)
```

which is distinguishable from 1.


---

Comment by dmharvey created at 2008-07-17 15:35:12

Someone else seems to have hit a related bug, see the following thread:

http://groups.google.com/group/sage-devel/browse_thread/thread/56a73f331e6b2977


---

Comment by mabshoff created at 2008-11-23 10:17:39

Any movement here? This ticket seems to have gone stale.

Cheers,

Michael


---

Comment by kedlaya created at 2009-01-22 03:00:09

I can simplify dmharvey's bad example even further. No need to work over the p-adics at all! (This execution is from 3.2.3.)

```
sage: C.<t> = PowerSeriesRing(Integers())                                       
sage: D.<s> = PowerSeriesRing(C)                                               
sage: y = 1 - (t + O(t^2))*s + O(s^5)                                          
sage: 1/y                                                                      
1 + (t + O(t^2))*s + (2*t^2 + O(t^3))*s^2 + O(s^5)
```

So I dare say this is really a bug in power series, specifically in precision management.


---

Comment by kedlaya created at 2009-01-22 05:15:32

I traced through the computation of 1/y in my previous example by hand, and this turned up the following perhaps more telling example.

```
sage: C.<t> = PowerSeriesRing(Integers())
sage: D.<s> = PolynomialRing(C)
sage: z = 1 + (t + O(t^2))*s + (t^2 + O(t^3))*s^2
sage: z*z
(t^4 + O(t^5))*s^4 + (2*t + O(t^2))*s + 1
```

By contrast, this is correct:

```
sage: z = 1 + (t + O(t^3))*s + (t^2 + O(t^3))*s^2
sage: z*z
(t^4 + O(t^5))*s^4 + (2*t^3 + O(t^4))*s^3 + (3*t^2 + O(t^3))*s^2 + (2*t + O(t^3))*s + 1
```

I think multiplication here uses z._mul_karatsuba, so maybe dmharvey needs to look at this again. Karatsuba may cause problems when working over an inexact coefficient ring.


---

Comment by dmharvey created at 2009-01-22 13:08:10

Replying to [comment:17 kedlaya]:
> I think multiplication here uses z._mul_karatsuba, so maybe dmharvey needs to look at this again. Karatsuba may cause problems when working over an inexact coefficient ring.

I don't know who wrote the karatsuba code. I think it was there long before I started working on sage. Sure, I agree karatsuba should give inaccurate answers over an inexact coefficient ring, but it shouldn't give *wrong* answers. I guess the easiest solution is just to disable or remove karatsuba altogether, or first check whether the coefficient ring is exact.

david


---

Comment by dmharvey created at 2009-01-22 13:16:31

Replying to [comment:17 kedlaya]:

Actually, there's nothing incorrect in your first example, except perhaps the printing:

```
sage: C.<t> = PowerSeriesRing(Integers())
sage: D.<s> = PolynomialRing(C)
sage: z = 1 + (t + O(t^2))*s + (t^2 + O(t^3))*s^2
sage: z * z
(t^4 + O(t^5))*s^4 + (2*t + O(t^2))*s + 1
sage: (z*z).list()
[1, 2*t + O(t^2), O(t^2), O(t^3), t^4 + O(t^5)]
# let's do it "by hand"
sage: [sum([z[i] * z[n-i] for i in range(n+1)]) for n in range(5)]
[1, 2*t + O(t^2), 3*t^2 + O(t^3), 2*t^3 + O(t^4), t^4 + O(t^5)]
```

So it's not printing the "zero" coefficients, and it's losing precision, but the result is correct up to the known precision.


---

Comment by kedlaya created at 2009-01-22 15:23:09

Replying to [comment:18 dmharvey]:
> Replying to [comment:17 kedlaya]:
> > I think multiplication here uses z._mul_karatsuba, so maybe dmharvey needs to look at this again. Karatsuba may cause problems when working over an inexact coefficient ring.
> 
> I don't know who wrote the karatsuba code. I think it was there long before I started working on sage. Sure, I agree karatsuba should give inaccurate answers over an inexact coefficient ring, but it shouldn't give *wrong* answers. I guess the easiest solution is just to disable or remove karatsuba altogether, or first check whether the coefficient ring is exact.
> 
> david

Fair enough, but the behavior of `__invert__` (in sage/sage/rings/power_series_ring_element.pyx; I believe you wrote this) seems to depend on Karatsuba giving better answers than this. Here's what happens when I go through `__invert__` by hand:


```
sage: sage: y = 1 - (t + O(t^2))*s + O(s^5)
sage: C.<t> = PowerSeriesRing(Integers())
sage: D.<s> = PowerSeriesRing(C)
sage: y = 1 - (t + O(t^2))*s + O(s^5)
sage: sage.misc.misc.newton_method_sizes(5)
[1, 2, 3, 5]
sage: A = y.truncate()
sage: current = A.parent()(1)
sage: current
1
sage: z = current.square() * A.truncate(1)
sage: current = 2*current - z.truncate(1)
sage: current
1
sage: z = current.square() * A.truncate(2)
sage: current = 2*current - z.truncate(2)
sage: current
(t + O(t^2))*s + 1
sage: z = current.square() * A.truncate(3)
sage: current = 2*current - z.truncate(3)
sage: current
(t^2 + O(t^3))*s^2 + (t + O(t^2))*s + 1
sage: z = current.square() * A.truncate(5)
sage: z.list()
[1, t + O(t^2), O(t^2), O(t^3), O(t^4), -t^5 + O(t^6)]
sage: current = 2*current - z.truncate(5)
sage: current
(2*t^2 + O(t^3))*s^2 + (t + O(t^2))*s + 1
```


My previous example is the `last current.square()` in this sequence, which gives an answer with too little precision. This would be consistent, if undesirable, except for the fact that here:

```
sage: z.list()
[1, t + O(t^2), O(t^2), O(t^3), O(t^4), -t^5 + O(t^6)]
sage: z.truncate(5).list()
[1, t + O(t^2)]
```

I lose the extra `O(t^*)` terms at the end. This causes current not to get properly degraded in its `s^2` and higher coefficients, hence the wrong answer.

So now as I see it, there are actually two different issues.

1. Karatsuba doesn't give best possible answers over inexact rings. This could be fixed by explicitly calling `_mul_generic` instead of implicitly calling `_mul_karatsuba`, but that is a performance tradeoff.

2. Looking into `truncate` (in sage.rings.polynomial.polynomial_element.Polynomial_generic_dense), one sees that the extra terms are tested for being zero by being evaluated in a Boolean context and then negated. This gives the same effect as `is_zero` or comparison with 0, namely something like `O(t^4) == 0` returns `True`. This may be the desired effect in certain contexts, but I think we can't use it in `__invert__` even if we fix the Karatsuba thing, since in some cases the *correct* behavior will involve having an `O(t^n)` term at the end. For example, let's uninvert the example from earlier:

```
sage: yy
1 + (t + O(t^2))*s + (t^2 + O(t^3))*s^2 + (t^3 + O(t^4))*s^3 + (t^4 + O(t^5))*s^4 + O(s^5)
sage: 1/yy                                                                    
1 + (-t + O(t^2))*s + O(s^5)
sage: (1/yy).list()                                                           
[1, -t + O(t^2)]
```

This is wrong because the 'zero' terms are actually inexact zeroes to certain precisions, which will lead to errors elsewhere if you try to use them.

This is a systemic problem with using the generic polynomial module with an inexact ring: it has a habit of truncating leading zeroes after virtually every arithmetic operation. This systemic problem needs a systemic solution: there needs to be a way to check whether an element of an inexact ring is an exact zero or not, so that `truncate` can preserve inexact leading zeroes, i.e., a method called `is_exact_zero` or something.


---

Comment by dmharvey created at 2009-01-22 16:10:30

> This is a systemic problem with using the generic polynomial module with an inexact ring: it has a habit of truncating leading zeroes after virtually every arithmetic operation. This systemic problem needs a systemic solution: there needs to be a way to check whether an element of an inexact ring is an exact zero or not, so that `truncate` can preserve inexact leading zeroes, i.e., a method called `is_exact_zero` or something.

I agree, this is the key. I believe it's been discussed several times in the past. Unfortunately the Sage development model seems to be very good at introducing systemic design bugs like this, but doesn't seem to be very good at fixing them (my perennial favourite is #3680). What we need is a hero with lots of time on their hands.

david


---

Comment by kedlaya created at 2009-01-23 19:06:23

In order to clarify things for newcomers to this discussion, I created a separate ticket #5075 to deal with the truncation of leading zeroes. Once that gets resolved, we can come back to the Karatsuba issue.


---

Comment by kedlaya created at 2009-05-22 03:34:59

All the examples on this ticket seem to be resolved in 4.0rc0. I'm not sure why, since #5075 is still open, but fixing #3056, #3184, and others may have helped. 

Especially in light of the existence of #6084 (which should fix #5075 among other things), I propose to call this issue fixed and put this ticket out of its misery.


---

Attachment

I decided this ticket should actually end up with a patch and a review, so I added a patch (mislabeled, sorry) to put another doctest from the above discussion into polynomial_element.pyx.


---

Comment by kedlaya created at 2009-12-03 03:26:34

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2009-12-07 08:25:55

Looks good.


---

Comment by mhansen created at 2009-12-07 08:25:55

Resolution: fixed
