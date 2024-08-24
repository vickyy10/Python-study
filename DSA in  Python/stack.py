

# class Stack:
#     def __init__(self):
#         self.stack=[]

#     def push(self,item):
#         self.stack.append(item)
#         print(f"Pushed {item} into the stack.")

#     def pop(self):
#         removed_item=self.stack.pop()
#         print(f"Popped {removed_item} from the stack.")
#         return removed_item
    
#     def peek(self):
#         return self.stack[-1]
    
#     def is_empty(self):
#         return len(self.stack) == 0

#     def display(self):
#         print("stack : ",self.stack)


# stack=Stack()

# stack.push(10)
# stack.push(20)
# stack.push(200)
# stack.push(90)
# stack.display()
# stack.pop()
# stack.display()
# 0


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        for i,num in enumerate(nums):
            if num == target:
                return i
            
            else:
                continue