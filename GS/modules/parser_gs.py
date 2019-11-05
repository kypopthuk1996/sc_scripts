class Main_part():
    '''Класс раздела'''
    def __init__(self, name, desc, tag):
        '''Инициализация атрибутов:
        name - название раздела
        desc - описание раздела
        tag - тег раздела
        '''
        self.name = name
        self.desc = desc
        self.tag = ta

class Parser():
    '''Класс определяет как тип строки пришел с таблиц (Раздел, подраздел или тест-кейс)'''
    def pars_gs(self, *data_gs):
        result = [value for a in data_gs for value in a]
        m = 0
        j = 0
        res_dict = dict()
        #Парсим раздел
        status_pars = False
        for id, item in enumerate(result):
            res_dict[int(id)] = item
        for i in range(len(res_dict)):
            if i >= 2 and i <= 7:
                if res_dict[i] == '':
                    m += 1
                    if m == 6:
                        print('This is main part')
                        status_pars = True
        #Парсим подраздел
        if res_dict[0] == '':
            if res_dict[1] != '':
                if res_dict[2] == '':
                    if res_dict[3] != '':
                        if res_dict[4] != '':
                            print('This is part')
                            status_pars = True
        #Парсим тест-кейс
        for i in range(len(res_dict)):
            if i >= 1 and i <= 4:
                if res_dict[i] != '':
                    j += 1
                    if j == 4:
                        print('This is test keys')
                        status_pars = True
        #Если ничего не нашли
        if status_pars == False:
            print('Огнев заебал, пиши нормально тесты')
        return result
