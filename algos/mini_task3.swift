class Solution {
    func search(_ nums: [Int], _ target: Int) -> Int {
        var l: Int = 0
        var r: Int = nums.count - 1
        while l <= r {
            var pivot: Int = (l + r) / 2
            if nums[pivot] == target {
                return pivot
            }
            else if nums[pivot] > target{
                r = pivot - 1
            }
            else if nums[pivot] < target {
                l = pivot + 1
            }
        }
        return -1
    }
}