class MyQueue(object):
    def __init__(self):
        self.stack_main = []
        self.stack_aux = []
    
    def change_elements(self, stack_from, stack_to):
        while stack_from:
            stack_to.insert(0, stack_from.pop(0))

    def peek(self):
        if not self.stack_aux:
            self.change_elements(self.stack_main, self.stack_aux)
        return self.stack_aux[0]
        
    def pop(self):
        if not self.stack_aux:
            self.change_elements(self.stack_main, self.stack_aux)
        return self.stack_aux.pop(0)
        
    def put(self, value):
        self.stack_main.insert(0, value)

if __name__ == "__main__":
    queue = MyQueue()
    queue.put(10)
    queue.put(15)
    queue.put(20)
    print(queue.peek())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())