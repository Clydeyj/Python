class AvailabilityQueue:
    def __init__(self, locationName):
        self.locationName = locationName
        self.queue = []

    def getLocationName(self):
        return self.locationName

    def front(self):
        if not self.isEmpty():
            return self.queue[0]
        else:
            raise IndexError("Queue is empty")

    def enqueue(self, driver):
        self.queue.append(driver)

    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            raise IndexError("Queue is empty")

    def isEmpty(self):
        return len(self.queue) == 0

# Example usage
queue = AvailabilityQueue("Location A")
queue.enqueue("Driver 1")
queue.enqueue("Driver 2")
queue.enqueue("Driver 3")

print(queue.getLocationName())  # Output: Location A
print(queue.front())  # Output: Driver 1

queue.dequeue()
print(queue.front())  # Output: Driver 2

print(queue.isEmpty())  # Output: False
