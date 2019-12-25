from utils.check_pid import is_valid

if __name__ == '__main__':
    my_pid = '1101401427542'
    if is_valid(my_pid):
        print("correct")
    else:
        print("incorrect")
