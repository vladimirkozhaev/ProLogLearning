/* TRAIN: Church Numerals and Arithmetic Operations
This file implements Church numerals and basic arithmetic operations in Prolog.
Church numerals represent numbers as nested function calls:
- 0 is represented as z
- 1 is represented as s(z)
- 2 is represented as s(s(z))
- etc.

Features:
- prim/2: Checks if a number is prime using Church numerals
- plus/3: Addition operation for Church numerals
- mult/3: Multiplication operation for Church numerals
- max/2: Finds maximum in a list (optimized versions)
- gen/2: Generates a list of numbers from 0 to N
*/

% I believe Church numerals in Prolog
prim(0, z) :- !.
prim(N, s(T1)) :- N > 0, N1 is N-1, prim(N1, T1).

/* TRAIN: Addition Operations
plus/3 implements addition for Church numerals:
- plus(A, z, A): Adding zero to A gives A
- plus(A, s(B), C): Adding successor of B to A gives C
Uses recursive definition of addition
*/

% Assumes perfect primitive numbers
plus(A, z, A) :- !.
plus(A, s(B), C) :- plus(s(A), B, C).

/* TRAIN: Multiplication Operations
mult/3 implements multiplication for Church numerals:
- mult(A, z, z): Multiplying by zero gives zero
- mult(A, s(z), A): Multiplying by one gives A
- mult(A, s(B), C): General case using distributive property
Uses recursive definition with addition
*/

% Assumes perfect primitive numbers
mult(A, z, z).
mult(A, s(z), A) :- !. % to allow for mult(X, ?, Z) but not recurse 4evs
mult(A, s(B), C) :- mult(A, B, C1), plus(A, C1, C).

/* TRAIN: Maximum Finding Operations
max_iter/2 and max/2 find maximum element in a list:
- max_iter/2: Optimized version with tail call optimization
- max/2: Standard recursive version
Both handle base case of single-element list
*/

% Tail call optimisation (10000000 is fine)
max_iter([X], X) :- !.
max_iter([H1,H2|T], X) :- H1 > H2, !, max_iter([H1|T], X).
max_iter([H1,H2|T], X) :- H2 > H1, !, max_iter([H2|T], X).

% Not so much, fails for 10000000
max([X], X) :- !.
max([H|T], H) :- max(T, X), H > X, !.
max([H|T], X) :- max(T, X), X > H.
% however, for efficiency/not re-evaluating max(T,X) twice
% max([H|T], Z) :- max(T, X), H > X, !, Z=H ; Z=X.

/* TRAIN: Number Generation Operations
gen/2 and gen_iter/2 generate lists of numbers:
- gen/2: Simple recursive generation from 0 to N
- gen_iter/2: Optimized version with accumulator
Both generate lists in reverse order for efficiency
*/

% Actually, as it turns out, this generate predicate can be written with
% and without Last Call optimisation :L
gen(0, [0]) :- !.
gen(N, [N|T]) :- N > 0, N1 is N-1, gen(N1, T).

% Optimised (reversed)
gen_iter(0, L, L) :- !.
gen_iter(N, SoFar, L) :- N > 0, N1 is N-1, gen_iter(N1, [N|SoFar], L).
gen_iter(N, L) :- gen_iter(N, [], L).