class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [] #maintains how much time each car takes to reach destination
        for i in range(len(position)):
            time = (target - position[i])/ speed[i] 
            cars.append((position[i], time))

        # Sort cars by position from closest to target to farthest
        cars.sort(reverse=True)
        stack = []
        for position,time in cars:
            if len(stack) == 0 or time > stack[-1]: #if stack is empty or current time greater than time in stack which means car cannot join the fleet
                stack.append(time) 
        
        return len(stack)