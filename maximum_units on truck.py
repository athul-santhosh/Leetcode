class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(key = lambda x:x[1],reverse = True)
        
        load = 0
        box_count = 0
        for box,num_box in boxTypes:

            if box_count + box > truckSize:
                box = truckSize - box_count
            box_count += box
            load += box * num_box
            
            if box_count == truckSize:
                return load
        return load