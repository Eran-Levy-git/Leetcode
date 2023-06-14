from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append('FizzBuzz')
            elif i % 3 == 0:
                answer.append('Fizz')
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer

# Test Cases
test_cases = [3, 8, 12]

sol = Solution()

for i, accounts in enumerate(test_cases):
    result = sol.fizzBuzz(accounts)
    print(f"Test Case {i + 1}: {result}")
