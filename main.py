def wish(self):
    print('Человек захотел отправить (напишите кого) ')
    who = input()
    return who


def place(self, who):
    print('Отправим на отдых ', who, ' в (напишите любую страну) ')
    where = input()
    return where

def request(self, who, where):
    print('Куплю билет для ', who, ' в ', where)


def result(self):
    print('Ура отдых!')
