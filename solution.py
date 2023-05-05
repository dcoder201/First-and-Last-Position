lass Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(nums, target, findFirst):
          n = len(nums)
          left, right = 0, n - 1
          result = -1
          while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid
                if findFirst:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
          return result

        first = search(nums, target, True)
        if first == -1:
          return [-1, -1]
        last = search(nums[first:], target, False)
        return [first, first + last]
