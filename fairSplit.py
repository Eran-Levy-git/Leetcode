from ast import List


class Solution:
    def fairSplit(self, A, B) -> int:
        """
        This function finds the index in arrays A and B where they can be split into two non-empty subarrays each, such that the sums of elements in corresponding subarrays of A and B are equal.

        Returns:
            int: The index at which the split can be made, or -1 if no such split exists.
        """

        N = len(A)

        # Precompute prefix sums using list comprehension for efficiency
        prefix_sum_A = [0] * (N + 1)
        prefix_sum_B = [0] * (N + 1)
        for i in range(1, N + 1):
            prefix_sum_A[i] = prefix_sum_A[i - 1] + A[i - 1]
            prefix_sum_B[i] = prefix_sum_B[i - 1] + B[i - 1]

        # Check for fair splits at each index for clarity and efficiency
        for k in range(1, N):
            if prefix_sum_A[k] == prefix_sum_B[k]:
                if (
                    prefix_sum_A[N] - prefix_sum_A[k]
                    == prefix_sum_B[N] - prefix_sum_B[k]
                ):
                    return k  # Fair split found

        return -1  # No fair split found


# Test Cases
A = [4, -1, 0, 3]
B = [-2, 5, 0, 3]

sol = Solution()

result = sol.fairSplit(A, B)
print(result)
