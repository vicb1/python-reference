class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def get_list_mid(nums):
    # if len(nums) % 2 == 1 or len(nums) == 2:
    #     mid = len(nums) // 2
    # else:
    #     mid = len(nums) // 2 - 1
    mid = len(nums) // 2
    return mid


def build(node, nums, prev_mid):
    if nums == []:
        return
    elif len(nums) == 1:
        if nums[0] < node.val:
            node.left = TreeNode(nums[0])
            return
        else:
            node.right = TreeNode(nums[0])
            return
    elif len(nums) == 2:
        # node.left = TreeNode(nums[0])
        # node.right = TreeNode(nums[1])
        node.left = TreeNode(nums[0])
        node.right = TreeNode(nums[1])
        return
    else:
        # mid = get_list_mid(nums)
        nums_left = nums[:prev_mid]
        mid_left = get_list_mid(nums_left)

        nums_right = nums[prev_mid:]
        mid_right = get_list_mid(nums_right)

        node.left = TreeNode(nums_left[mid_left])
        if nums_left != []: nums_left.pop(mid_left)

        build(node.left, nums_left, mid_left)
        node.right = TreeNode(nums_right[mid_right])
        if nums_right != []: nums_right.pop(mid_right)
        build(node.right, nums_right, mid_right)


def sortedArrayToBST(nums):
    nums.sort()
    if nums == []: return None
    mid = get_list_mid(nums)
    ret = TreeNode(nums[mid])
    node = ret
    nums.pop(mid)
    if nums == []:
        return ret
    else:
        node = build(node, nums, mid)
        return ret


sortedArrayToBST([-10,-3,0,5,9])


def sortedArrayToBST2(nums):
    # nums.sort()
    # if nums == []: return None
    # mid = get_list_mid(nums)
    # ret = TreeNode(nums[mid])
    # node = ret
    # nums.pop(mid)
    # if nums == []:
    #     return ret
    # else:
    #     node = build(node, nums, mid)
    #     return ret

    if not nums:
        return None

    mid = (len(nums) - 1) // 2

    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST2(nums[:mid])
    root.right = sortedArrayToBST2(nums[mid + 1:])

    return root

a = sortedArrayToBST2([-10,-3,0,5,9])

h


>>> sl *= 10_000_000
>>> sl.count('c')
10000000
>>> sl[-3:]
['e', 'e', 'e']

SortedDict({'a': 1, 'b': 2, 'c': 3})
>>>
('c', 3)
>>> 
>>> ss
SortedSet(['a', 'b', 'c', 'd', 'r'])
>>> ss.bisect_left('c')