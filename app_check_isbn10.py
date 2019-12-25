from utils.check_isbn10 import is_valid

if __name__ == '__main__':
    isbn10 = '1218651032'

    if len(isbn10) == 10 & isbn10.isnumeric():
        if is_valid(isbn10):
            print('correct')
        else:
            print('incorrect')
    else:
        print('This is not ISBN10')