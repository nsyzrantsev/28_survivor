# https://skillsmart.ru/algo/lvl1/z75c.html

class Redactor:
    string = ''
    history = list()
    undo_ON = False
    undo_Reset = False
    count = -1
    count_reset = -1
    before_undo = ''
    before_redo = ''

    def __init__(self, command):
        self.command = command
    
    def getIndex(self):
        if len(self.command) > 0:
            return int(self.command[0])

    def getParameter(self):
        if len(self.command) >= 3:
            return self.command[2:]
        else:
            return False

    def addElements(self, parameter):
        Redactor.count = -1
        Redactor.before_undo = Redactor.string
        if Redactor.undo_ON and not Redactor.undo_Reset:
            Redactor.undo_Reset = True
            Redactor.count = Redactor.count_reset-1
        elif Redactor.undo_ON and Redactor.undo_Reset:
            Redactor.undo_ON = False
            Redactor.undo_Reset = False
        Redactor.string += parameter

    def deleteElements(self, num):
        Redactor.count = -1
        Redactor.before_undo = Redactor.string
        if Redactor.undo_ON and not Redactor.undo_Reset:
            Redactor.undo_Reset = True
            Redactor.undo_ON = False
        elif Redactor.undo_ON and Redactor.undo_Reset:
            Redactor.undo_ON = False
            Redactor.undo_Reset = False
        if num > len(Redactor.string):
            Redactor.string = ''
        else:
            Redactor.string = Redactor.string[0:len(Redactor.string)-num]
    
    def returnElements(self, i):
        if i > len(Redactor.string)-1 or i < 0:
            return ''
        return Redactor.string[i]

    def Undo(self):
        Redactor.before_redo = Redactor.string
        Redactor.count -= 1
        if not Redactor.undo_ON:
            Redactor.undo_ON = True
        if Redactor.undo_ON and Redactor.undo_Reset:
            Redactor.history = list()
            Redactor.history.append(Redactor.before_undo)
            return Redactor.before_undo
        if Redactor.count < -len(Redactor.history):
            Redactor.count = -len(Redactor.history)
            return Redactor.history[-len(Redactor.history)]
        return Redactor.history[Redactor.count]

    def Redo(self):
        if Redactor.undo_Reset and Redactor.undo_ON:
            return Redactor.before_redo
        elif Redactor.undo_Reset and not Redactor.undo_ON:
            return Redactor.string
        else:
            Redactor.count += 1
        if Redactor.count > -1:
            Redactor.count = -1
        return Redactor.history[Redactor.count]
    
    def redaction(self):
        index = self.getIndex()
        parameter = self.getParameter()
        if index == 1 and parameter:
            self.addElements(parameter)
            Redactor.history.append(Redactor.string)
        elif index == 2 and parameter:
            if parameter.isnumeric():
                self.deleteElements(int(parameter))
                Redactor.history.append(Redactor.string)
        elif index == 3 and parameter:
            if parameter.isnumeric():
                result = self.returnElements(int(parameter))
                return result
        elif index == 4 and not parameter:
            Redactor.string = self.Undo()
        elif index == 5 and not parameter and Redactor.undo_ON:
            Redactor.string = self.Redo()
        return Redactor.string

def BastShoe(command):
    action = Redactor(command)
    return action.redaction()

'''
while True:
    line = str(input())
    if line == 'exit':
        break
    print(BastShoe(line))
    print(Redactor.history)
    print(Redactor.count)
    print('-------------------')
'''
'''
data = ['1 Привет', '1 , Мир!', '1 ++', '2 2', '4', '4', '1 *', '4', '4', '4', '3 6', '2 100', '1 Привет', '1 , Мир!', '1 ++', '4', '4', '5', '4', '5', '5', '5', '5', '4', '4', '2 2', '4', '5', '5', '5']
'''

'''
for i in data:
    print(BastShoe(i))
    print(Redactor.history)
    print(f'count={Redactor.count}')
    print(f'before_undo={Redactor.before_undo}')
    print(f'before_redo={Redactor.before_redo}')
    print('-------------------')
'''
