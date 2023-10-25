import random

class BoggleBoard:
  
    boardArr =''
    new_list = []

def main(self):
    game1 = BoggleBoard('Game1')
    game1.shake()
    game1.horizonal_word_list()
    valid_words = game1.horizonal_word_list()
    print(game1)

    score = 0
    option = ''
    while option != '0':
        option = input('Enter a 4 letter word: \nPress 0 to submit final score')
        if option == '0':
            print(f'Final score is {score}')
            break
        elif option in valid_words:
            score += 1


    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f" [{self.name}]\n{BoggleBoard.boardArr}"
    
    def shake(self):
        tempArr = ["\n"]
        temp_new_list = []

        for i in range(4):
            for j in range(4):
                tempArr.append(self.random_letter())
                tempArr.append("\n")
        for k in range(len(tempArr)):
            if tempArr[k] != "\n":
                temp_new_list.append(tempArr[k])
        BoggleBoard.new_list = temp_new_list[24:]
        BoggleBoard.boardArr = ' '.join(tempArr)


    @staticmethod
    def random_letter():
        random_number = random.randrange(0, 26)
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if alphabet[random_number] == "Q":
            return "Qu"
        else:
            return alphabet[random_number]
        
    def horizonal_word_list(self):
        another_new_list = []
        #print(BoggleBoard.new_list)
        another_new_list.append("".join(BoggleBoard.new_list[0:4]))
        another_new_list.append("".join(BoggleBoard.new_list[4:8]))
        another_new_list.append("".join(BoggleBoard.new_list[8:12]))
        another_new_list.append("".join(BoggleBoard.new_list[12:16]))
        print(another_new_list)

        another_new_list_reverse = []
        another_new_list_reverse.append("".join(reversed(BoggleBoard.new_list[0:4])))
        another_new_list_reverse.append("".join(reversed(BoggleBoard.new_list[4:8])))
        another_new_list_reverse.append("".join(reversed(BoggleBoard.new_list[8:12])))
        another_new_list_reverse.append("".join(reversed(BoggleBoard.new_list[12:16])))
        print(another_new_list_reverse)


game = BoggleBoard('Game1')
game.main()

#print(game1.horizonal_word_list())















