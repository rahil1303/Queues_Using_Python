class Queue:
    ### Create a Queue
    def __init__(self):
        self.lists = []
    def __str__(self):
        values = [str(x) for x in self.lists]
        return " ".join(values)
    
    # TIME COMPLEXITY = O(1)
    # SPACE COMPLEXITY = O(1)
    
    ### isEmpty() Method
    def isEmpty(self):
        if self.lists == []:
            return True
        else:
            return False
    # TIME COMPLEXITY = O(1)
    # SPACE COMPLEXITY = O(1)
    
    ### Enqeuue() Method
    def enqueue(self,value):
        self.lists.append(value)
        return "The element is inserted at the end of the queue"
    # TIME COMPLEXITY = O(n)
    # SPACE COMPLEXITY = O(1)
    
    
    ### Dequeue() Method
    def dequeue(self):
        if self.isEmpty():
            return "This is not ny element in the queue"
        else:
            return self.lists.pop(0)
        
    # TIME COMPLEXITY = O(n)
    # SPACE COMPLEXITY = O(1)
    
