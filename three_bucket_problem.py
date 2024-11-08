#We have 3 bucket: 3 liter, 5 liter and 9 liter.
#The desired result is that the 3rd bucket is 7 liters.

import random as r
first_bucket = []
second_bucket = []
third_bucket = []
step_counter = 0

def fill_first_bucket():
    global first_bucket
    while 3 - first_bucket.count(1) > 0:
        first_bucket.append(1)
            
def fill_second_bucket():
    global second_bucket
    while 5 - second_bucket.count(1) > 0:
        second_bucket.append(1)

def fill_third_bucket():
    global third_bucket
    while 9 - third_bucket.count(1) > 0:
        third_bucket.append(1)



def pour_first_bucket():
    first_bucket.clear()

def pour_second_bucket():
    second_bucket.clear()

def pour_third_bucket():
    third_bucket.clear()
        
    
    
def pour_first_to_second():
    if first_bucket.count(1) > 0 and second_bucket.count(1) != 5:
        while first_bucket.count(1) > 0 and third_bucket.count(1) < 5:
            first_bucket.pop()
            second_bucket.append(1)
        
def pour_first_to_third():
    if first_bucket.count(1) > 0 and third_bucket.count(1) != 9:
        while first_bucket.count(1) > 0 and third_bucket.count(1) < 9:
            first_bucket.pop()
            third_bucket.append(1)


def pour_second_to_first():
    if first_bucket.count(1) < 3 and second_bucket.count(1) > 0:
        while first_bucket.count(1) < 3 and second_bucket.count(1) > 0:
            second_bucket.pop()
            first_bucket.append(1)
    
def pour_second_to_third():
    if second_bucket.count(1) > 0 and third_bucket.count(1) < 9:
        while second_bucket.count(1) > 0 and third_bucket.count(1) < 9:
            second_bucket.pop()
            third_bucket.append(1)


def pour_third_to_first():
    if first_bucket.count(1) < 3 and third_bucket.count(1) > 0:
        while first_bucket.count(1) < 3 and third_bucket.count(1) > 0:
            third_bucket.pop()
            first_bucket.append(1)
            
def pour_third_to_second(): 
    if second_bucket.count(1) < 5 and third_bucket.count(1) > 0:
        while second_bucket.count(1) < 5 and third_bucket.count(1) > 0:
            third_bucket.pop()
            second_bucket.append(1)

def random_func_generator():
    while third_bucket.count(1) != 7:
        random_method = r.randint(0, 12)
        if random_method == 0:
            fill_first_bucket()
        elif random_method == 1:
            fill_second_bucket()
        elif random_method == 2:
            fill_third_bucket()
        elif random_method == 3:
            pour_first_bucket()
        elif random_method == 4:
            pour_second_bucket()
        elif random_method == 5:
            pour_third_bucket()
        elif random_method == 6: 
            pour_first_to_second()
        elif random_method == 7:
            pour_first_to_third()
        elif random_method == 8:
            pour_second_to_first()
        elif random_method == 9:
            pour_second_to_third()
        elif random_method == 10:
            pour_third_to_first()
        elif random_method == 11:
            pour_third_to_second()
        global step_counter
        step_counter += 1
        if third_bucket.count(1) == 7:
            break
            
random_func_generator()

print(f"The process took place in {step_counter} stages")
print(f"First bucket: {first_bucket.count(1)}")
print(f"Second bucket: {second_bucket.count(1)}")
print(f"Third bucket: {third_bucket.count(1)}")