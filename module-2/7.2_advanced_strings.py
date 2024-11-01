# Keanu Foltz Module 7.2 9/22/24
# This program displays initials for first middle and last name

def initial_gen():
    full_name = input("Please write your full name: ")

    name_listed = full_name.split()

    try:
        first_name = name_listed[0]
        middle_name = name_listed[1]
        last_name = name_listed[-1]

        if middle_name == last_name:
            initials = first_name[0] + '.' + last_name[0] + '.'
        else:
            initials = first_name[0] + '.' + middle_name[0] + '.' + last_name[0] + '.'

        print(initials.upper())

    except IndexError:
        print('You must enter your full name')
        initial_gen()

def main():
    initial_gen()

if __name__ == "__main__":
    main()