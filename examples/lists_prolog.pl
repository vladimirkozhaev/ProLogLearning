% TRAIN: Learn Prolog list operations
% Generate examples about list manipulation, head/tail, member testing

% Basic list operations
head_of([H|_], H).
tail_of([_|T], T).
member(X, [X|_]).
member(X, [_|T]) :- member(X, T).

% List length calculation
length([], 0).
length([_|T], N) :- length(T, N1), N is N1 + 1.

% List concatenation
append([], L, L).
append([H|T], L, [H|R]) :- append(T, L, R).

% Examples to generate:
% "What is the head of [1,2,3]?" -> "1 is the head of [1,2,3]"
% "How to check if X is a member of list?" -> "Use member(X, List)"
% "How to concatenate two lists?" -> "Use append(List1, List2, Result)"
