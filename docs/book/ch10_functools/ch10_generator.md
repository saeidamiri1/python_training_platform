# Generator
It is a simple way of creating iteraion using function. 

def gen_1(n):
    print('first one')
    yield n+1
    print('second one')
    yield n+2
    print('third one')
    yield n+3

a = gen_1(0)
next(a)
next(a)
next(a)


# Generator 
def lazy_return_random_attacks():
    """Yield attacks each time"""
    import random
    attacks = {"kimura": "upper_body",
           "straight_ankle_lock":"lower_body", 
           "arm_triangle":"upper_body",
            "keylock": "upper_body",
            "knee_bar": "lower_body"}
    while True:
        random_attack = random.choices(list(attacks.keys()))
        yield random_attack

attack = lazy_return_random_attacks()


