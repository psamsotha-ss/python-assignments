
def main():
    def threes_a_crowd():
        names = ['Jordan', 'Kobe', 'Steph', 'Lebron', 'Durant']
        print(names)
        if len(names) > 3:
            print("Three's a crowd")
            names[2:] = []
            print(names)
            print("That's better")
        else:
            print('The room is not very crowded')
    threes_a_crowd()

    def six_is_a_mob():
        names = ['Jordan', 'Kobe', 'Steph', 'Lebron', 'Durant', 'Magic', 'Kareem']
        print(names)
        if len(names) > 5:
            print("There's a mob in the room")
        elif len(names) >= 3:
            print("The room is crowded")
        elif len(names) >= 1:
            print("The room's not crowded")
        else:
            print("The room is empty")
    six_is_a_mob()



if __name__ == '__main__':
    main()
