import random

class BoggleBoard:
  
    boardArr = ''
    new_list = []

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"\n  -[Boggle]-\n{BoggleBoard.boardArr}"
    
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
        BoggleBoard.new_list = []
        for x in temp_new_list:
            if x != ' ':
                BoggleBoard.new_list.append(x)
        BoggleBoard.boardArr = '  '.join(tempArr)

    @staticmethod
    def random_letter():
        random_number = random.randrange(0, 26)
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if alphabet[random_number] == "Q":
            return "Qu"
        else:
            return alphabet[random_number]
        
    def horizontal_word_list(self):
        another_new_list = [
        "".join(BoggleBoard.new_list[0:4]),
        "".join(BoggleBoard.new_list[4:8]),
        "".join(BoggleBoard.new_list[8:12]),
        "".join(BoggleBoard.new_list[12:16]),
        "".join(reversed(BoggleBoard.new_list[0:4])),
        "".join(reversed(BoggleBoard.new_list[4:8])),
        "".join(reversed(BoggleBoard.new_list[8:12])),
        "".join(reversed(BoggleBoard.new_list[12:16]))
        ]
        return another_new_list
    
    def vertical_word_list(self):
        vertical_words = []
        for col in range(4):
            word = "".join(BoggleBoard.new_list[col::4])
            vertical_words.append(word)
        return vertical_words

    def diagonal_word_list(self):
        diagonal_words = [
        "".join(BoggleBoard.new_list[::5]),
        "".join(BoggleBoard.new_list[15::-5]),
        "".join(BoggleBoard.new_list[3::3][:4]),
        "".join(BoggleBoard.new_list[12::-3][:4]),
        ]
        return [diagonal_words[0], diagonal_words[1], diagonal_words[2], diagonal_words[3]]


    def main(self):
        self.shake()
        valid_words = game.horizontal_word_list() + game.vertical_word_list() + game.diagonal_word_list()
        print(self)

        score = 0
        option = ''
        while option != '0':
            option = input('Press 0 to submit final score\nEnter a 4 letter word: ').upper()
            if option == '0':
                print(f'\nGame Over! Your final score is: {score}\n')
                break
            elif option in valid_words:
                score += 1

game = BoggleBoard('Game1')
game.main()
