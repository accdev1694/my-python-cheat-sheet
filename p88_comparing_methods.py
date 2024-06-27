# if you try to compare methods without using magic methods, it will return false 
# because you are comparing objects memory location using the == operator

class Houses():
    def __init__(self, location, beds):
        self.location = location
        self.beds = beds
    
    def desciption(self):
        return f"{self.beds} bedroom house in {self.location}"
    
    # we need to use a mamagic method
    def __eq__(self, three_bed):
        return self.location == three_bed.location and self.beds == three_bed.beds
    

        
two_bed = Houses("Coventry", 3)
three_bed = Houses("Coventry", 3)

print(two_bed == three_bed)


