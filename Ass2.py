def driver_make(firstName, lastName, carMakeAndModel):
    """Constructor for Driver ADT"""
    return [firstName, lastName, carMakeAndModel, 0]

def driver_getFirstName(driver):
    """Accessor for getting the first name of a driver"""
    return driver[0]

def driver_getLastName(driver):
    """Accessor for getting the last name of a driver"""
    return driver[1]

def driver_getCarMakeAndModel(driver):
    """Accessor for getting the car make and model of a driver"""
    return driver[2]

def driver_getNumberOfTripsCompleted(driver):
    """Accessor for getting the number of trips completed by a driver"""
    return driver[3]

def driver_increaseTripsCompleted(driver):
    """Mutator for increasing the number of trips completed by a driver"""
    driver[3] += 1

def driver_isNewDriver(driver):
    """Predicate for checking if a driver is new"""
    return driver[3] == 0

# Example usage
driver = driver_make('John', 'Doe', 'Toyota Camry')
print(driver_getFirstName(driver))  # Output: John
print(driver_getLastName(driver))   # Output: Doe
print(driver_getCarMakeAndModel(driver))  # Output: Toyota Camry
print(driver_getNumberOfTripsCompleted(driver))  # Output: 0
print(driver_isNewDriver(driver))  # Output: True

driver_increaseTripsCompleted(driver)
print(driver_getNumberOfTripsCompleted(driver))  # Output: 1
print(driver_isNewDriver(driver))  # Output: False
