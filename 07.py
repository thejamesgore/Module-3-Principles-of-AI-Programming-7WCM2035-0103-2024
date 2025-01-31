import random

def random_number_generator(min_value, max_value):
    generated_int = random.randint(min_value, max_value)
    generated_float = random.uniform(min_value,max_value)
    
    print("Int number gen:", generated_int)
    print("Float number gen:", generated_float)
    
random_number_generator(-60,60)