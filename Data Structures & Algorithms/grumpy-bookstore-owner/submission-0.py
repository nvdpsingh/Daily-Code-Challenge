class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        base = 0
        extra = 0

        for c, g in zip(customers, grumpy):
            if g == 0:
                base += c

        window = 0
        best = 0

        for r in range(len(customers)):
            if grumpy[r] == 1:
                window += customers[r]

            if r >= minutes and grumpy[r - minutes] == 1:
                window -= customers[r - minutes]

            best = max(best, window)

        return base + best