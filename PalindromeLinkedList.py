class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        c = []
        while(head != None):
            c.append(head.val)
            head = head.next
            
        if c == c[::-1]:
            return True
        else:
            return False
            