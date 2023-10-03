
def greet(first_name):
    print(f'Hello {first_name.title()}, how are you doing?')

def leave(first_name):
    print(f'Goodbye {first_name.title()}, it was a pleasure seeing you.')


# Returns True if the current file is executed by name, will return False if being imported
if __name__ == '__main__':
    print('This is the test_module.py file and is currently being executed')