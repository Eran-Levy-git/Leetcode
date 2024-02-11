"""
We are given two strings P and Q, each consisting of N lowercase English letters. For each position in the strings, we have to choose one letter from either P or Q, in order to construct a new string S, such that the number of distinct letters in S is minimal. Our task is to find the number of distinct letters in the resulting string S.
"""


def solution(P, Q):
    N = len(P)

    def minimal(index, distinct_letters):
        if index == N:
            return len(distinct_letters)
        if P[index] == Q[index]:
            return minimal(index + 1, distinct_letters | {P[index]})
        else:
            return min(
                minimal(index + 1, distinct_letters | {P[index]}),
                minimal(index + 1, distinct_letters | {Q[index]}),
            )

    return minimal(0, set())


print(solution(P="abc", Q="bcd"))  # 2
print(solution(P="axxz", Q="yzwy"))  # 2
print(solution(P="bacad", Q="abada"))  # 1
print(solution(P="amz", Q="amz"))  # 3

"""
Examples:

1. Given P = "abc", Q = "bcd", your function should return 2. All possible strings S that can be constructed are: "abc", "abd", "acc", "acd", "bbc", "bbd", "bcc", "bcd". The minimum number of distinct letters is 2, which be obtained by constructing the following strings: "acc", "bbc", "bbd", "bcc".

2. Given P = "axxz", Q = "yzwy", your function should return 2. String S must consist of at least two distinct letters in this case. We can construct S = "yxxy", where the number of distinct letters is equal to 2, and this is the only optimal solution.

3. Given P = "bacad", Q = "abada", your function should return 1. We can choose the letter 'a' in each position, so S can be equal to "aaaaa".

4. Given P = "amz", Q = "amz", your function should return 3. The input strings are identical, so the only possible S that can be constructed is "amz", and its number of distinct letters is 3.
"""
