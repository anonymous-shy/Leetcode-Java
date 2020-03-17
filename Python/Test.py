from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i, num in enumerate(nums):
        if hashmap.get(target - num) is not None:
            return [i, hashmap.get(target - num)]
        # 这句不能放在if语句之前，解决list中有重复值或target-num=num的情况
        hashmap[num] = i


if __name__ == "__main__":
    res = twoSum([3, 2, 4], 6)
    print(res)
