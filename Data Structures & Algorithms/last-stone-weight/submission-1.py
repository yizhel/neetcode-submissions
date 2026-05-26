class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            h1 = stones.pop(stones.index(max(stones)))
            h2 = stones.pop(stones.index(max(stones)))
            print(h1,h2)
            if h1 > h2:
                stones.append(h1 - h2)
                print(stones)
        if stones:
            return stones[0]
        else:
            return 0