class Solution(object):
    def combinationSum(self, candidates, target):

        result = []

        def backtrack(start, target, path):

            # Target complete
            if target == 0:
                result.append(path[:])
                return

            # Target cross ho gaya
            if target < 0:
                return

            for i in range(start, len(candidates)):

                # Choose
                path.append(candidates[i])

                # Explore
                backtrack(i, target - candidates[i], path)

                # Undo choice
                path.pop()

        backtrack(0, target, [])

        return result