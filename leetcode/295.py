from sortedcontainers import SortedList
class MedianFinder:
    """
    easiest thing, sort everything by means of some pqueue in python or something.

    median of medians don't work.
    simple counting doesn't work either (median reference and left/right)
    we can keep track of a min heap or a max heap quickly
    but don't think that'll work here. why? property doesn't hold. max of max is max. median of median is not necessarily.

    so, what
    the additive part is one thing, we always do add, never remove.
    i see, so min heap and max heap. but bst is the same as in log n as well.
    """

    def __init__(self):
        self.sl = SortedList()

    def addNum(self, num: int) -> None:
        self.sl.add(num)

    def findMedian(self) -> float:
        mid = len(self.sl) // 2
        if len(self.sl) % 2 == 0:
            return self.sl[mid - 1] + self.sl[mid]
        else:
            return self.sl[mid]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

