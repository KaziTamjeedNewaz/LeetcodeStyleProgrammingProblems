#Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        result=[]
        nextLevel=[""]
        currentLevel=[]
        while(len(nextLevel)!=0):
            if root is None:
                break
            else:
                if len(currentLevel)==0:
                    currentLevel.append(root)
                    result.append([root.val])
                    nextLevel=[]
                    if root.left is not None:
                        nextLevel.append(root.left)
                    if root.right is not None:
                        nextLevel.append(root.right)
                elif len(nextLevel)>=1:
                    currentLevel=nextLevel
                    levelResult=[]
                    nextLevel=[]
                    for node in currentLevel:
                        levelResult.append(node.val)
                        if node.left is not None:
                            nextLevel.append(node.left)
                        if node.right is not None:
                            nextLevel.append(node.right)
                    result.append(levelResult)
                elif len(nextLevel)==0:
                    break


        return result
