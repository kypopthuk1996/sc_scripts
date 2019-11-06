import itertools

class Main_part():
    '''Класс раздела'''
    def __init__(self, root_part, name, desc, tag):
        '''Инициализация атрибутов:
        name - название раздела
        desc - описание раздела
        tag - тег раздела
        '''
        self.root_part = 'ROOT'
        self.desc = desc
        self.tag = tag

class Parser():
    '''Класс определяет как тип строки пришел с таблиц (Раздел, подраздел или тест-кейс)'''

    def pars_key_columns(self, data_gs):
        result = [value for value in data_gs[0]]
        key_colunns_dict = dict()
        for id, item in enumerate(result):
            key_colunns_dict[str(item).upper()] = item
        return key_colunns_dict

    def new_pars(self, data_gs, key_columns):
        #Парсим раздел
        result = [value for value in data_gs]
        str_dict = dict(itertools.zip_longest(key_columns, result, fillvalue=''))
        if str_dict['TAG'] != '':
            tag_str = str(str_dict.get('TAG', '')).split(sep=',')
            if len(tag_str) == 1:
                print('This is part')
        return str_dict


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
