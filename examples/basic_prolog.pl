% TRAIN: Learn basic facts about family relationships
% Generate examples about parent, child, and sibling relationships

% Facts about family
parent(john, mary).
parent(john, bob).
parent(mary, alice).
parent(bob, tom).

% Rules for defining relationships
child(X, Y) :- parent(Y, X).
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.
grandparent(GP, GC) :- parent(GP, P), parent(P, GC).

% Examples to generate:
% "Who is the parent of mary?" -> "john is the parent of mary"
% "What are the children of john?" -> "mary and bob are children of john"
% "Are mary and bob siblings?" -> "Yes, mary and bob are siblings"
