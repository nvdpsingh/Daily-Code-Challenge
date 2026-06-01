class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        l, r = 0, len(people) - 1
        while l <= r:
            if l==r:
                count+=1
                break
            if people[l] + people[r] <= limit:
                count += 1
                l += 1
                r -= 1
                continue
            count += 1
            r -= 1
        return count