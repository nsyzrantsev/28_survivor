# https://skillsmart.ru/algo/lvl1/z75c.html

class Redactor:
    string = ''
    history = list()
    reset = False
    count = -1
    last_index = 0
    undo_list = list()
    redo_unable = False

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
        old_string = Redactor.string
        Redactor.string += parameter
        if Redactor.last_index == 4:
            if not Redactor.reset:
                Redactor.reset = True
                Redactor.undo_list = list()
                Redactor.undo_list.append(old_string)
                Redactor.undo_list.append(Redactor.string)
        elif Redactor.reset:
            Redactor.undo_list.append(Redactor.string)
    
    def deleteElements(self, num):
        Redactor.count = -1
        Redactor.old_string = Redactor.string
        if num > len(Redactor.string):
            Redactor.string = ''
        else:
            Redactor.string = Redactor.string[0:len(Redactor.string)-num]
        if Redactor.last_index == 4:
            if not Redactor.reset:
                Redactor.reset = True
                Redactor.undo_list.append(Redactor.old_string)
                Redactor.undo_list.append(Redactor.string)
        elif Redactor.reset:
            Redactor.undo_list.append(Redactor.string)

    def returnElements(self, i):
        if i > len(Redactor.string)-1 or i < 0:
            return ''
        return Redactor.string[i]

    def Undo(self):
        Redactor.before_redo = Redactor.string
        Redactor.count -= 1
        if Redactor.reset:
            Redactor.history = Redactor.undo_list[:]
            Redactor.reset = False
        if Redactor.count < -len(Redactor.history):
            Redactor.count = -len(Redactor.history)
            return Redactor.history[-len(Redactor.history)]
        return Redactor.history[Redactor.count]

    def Redo(self):
        if Redactor.last_index == 4:
            Redactor.redo_unable = True
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
                Redactor.last_index = index
                return result
        elif index == 4 and not parameter:
            Redactor.string = self.Undo()
        elif index == 5 and not parameter:
            if Redactor.last_index == 4 or Redactor.redo_unable:
                Redactor.string = self.Redo()
        Redactor.last_index = index
        return Redactor.string

def BastShoe(command):
    action = Redactor(command)
    return action.redaction()
