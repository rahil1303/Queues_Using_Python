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
