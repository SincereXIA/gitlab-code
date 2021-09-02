#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#
# https://leetcode-cn.com/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (52.06%)
# Likes:    471
# Dislikes: 0
# Total Accepted:    46.9K
# Total Submissions: 89.8K
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n' +
#  '[[],[1],[2],[],[3],[]]'
#
# 中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。
#
# 例如，
#
# [2,3,4] 的中位数是 3
#
# [2,3] 的中位数是 (2 + 3) / 2 = 2.5
#
# 设计一个支持以下两种操作的数据结构：
#
#
# void addNum(int num) - 从数据流中添加一个整数到数据结构中。
# double findMedian() - 返回目前所有元素的中位数。
#
#
# 示例：
#
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3)
# findMedian() -> 2
#
# 进阶:
#
#
# 如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
# 如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
#
#
#
import heapq
# @lc code=start
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queMax = list()  # 前半段
        self.queMin = list()  # 后半段

    def addNum(self, num: int) -> None:
      if not self.queMax or num < -self.queMax[0] :
        heapq.heappush(self.queMax, -num)
        if len(self.queMax) - len(self.queMin) > 1:
          n = heapq.heappop(self.queMax)
          heapq.heappush(self.queMin, -n)
      else:
        heapq.heappush(self.queMin, num)
        if len(self.queMin) - len(self.queMax) > 1:
          n = heapq.heappop(self.queMin)
          heapq.heappush(self.queMax, -n)
        
    def findMedian(self) -> float:
      if len(self.queMax) > len(self.queMin):
        return -self.queMax[0]
      elif len(self.queMax) < len(self.queMin):
        return self.queMin[0]
      else:
        return (self.queMin[0] - self.queMax[0]) / 2
        

        # Your MedianFinder object will be instantiated and called as such:
        # obj = MedianFinder()
        # obj.addNum(num)
        # param_2 = obj.findMedian()
        # @lc code=end

if __name__ == "__main__":
  mf  = MedianFinder()
  mf.addNum(6)
  mf.addNum(10)
  mf.addNum(2)
  mf.addNum(6)
  rs = mf.findMedian()
  print(rs)

  mf.addNum(3)

  rs = mf.findMedian()
  print(rs)