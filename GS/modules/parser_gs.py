import itertools

class Main_part():
    '''Класс раздела'''
    def __init__(self,obj,**kwargs):
        '''Инициализация атрибутов:
        name - название раздела
        desc - описание раздела¡
        tag - тег раздела
        '''
        self.obj = obj
        self.id = kwargs.get('ID')
        self.section = kwargs.get('SECTION')
        self.test_case = kwargs.get('TEST CASE')
        self.description = kwargs.get('DESCRIPTION')
        self.status = kwargs.get('STATUS')
        self.autotest = kwargs.get('AUTOTEST')
        self.tags = kwargs.get('TAGS')
        self.version = kwargs.get('VERSION')


        self.root_part = {'Root':{}}
        self.parts = {}
        self.sections = {}
        self.test_keys = {}

    def add_part(self,part,value):
        self.parts[part] = value

    def add_section(self,section,value):
        self.sections[section] = value

    def add_test_keys(self,test_keys,value):
        self.test_keys[test_keys] = value

    def table_assembly(self):
        for part, item in self.parts.items():
            tag_part = item.get('TAGS').split(sep=' ')
            tag_part = [tag.replace(',','') for tag in tag_part]
            item['SUBSECTION'] = {}
            self.root_part['Root'][part] = item
            for key, value in self.sections.items():
                tag_section = value.get('TAG').split(sep=' ')
                tag_section = [tag.replace(',', '') for tag in tag_section]
                if tag_part[0] == tag_section[0].replace(',',''):
                    value['TEST KEYS'] = {}
                    self.root_part['Root'][part]['SUBSECTION'][key] = value
                    for k, v in self.test_keys.items():
                        tag_test_keys = v.get('TAGS').split(sep=' ')
                        tag_test_keys = [tag.replace(',', '') for tag in tag_test_keys]
                        if tag_section[0] == tag_test_keys[0] and tag_section[1] == tag_test_keys[1]:
                            self.root_part['Root'][part]['SUBSECTION'][key]['TEST KEYS'][k] = v
                            print('-' * 100)
        return self.root_part

class Parser():
    '''Класс определяет как тип строки пришел с таблиц (Раздел, подраздел или тест-кейс)'''
    def __init__(self):
        '''
        Создаем дефолтный объект класса Main_part
        '''
        self.main_parts = Main_part(obj = [], name = 'Главный раздел')

    def pars_key_columns(self, data_gs):
        '''
        Функция, которая парсит верхнюю шапку в таблице
        :param data_gs: Список строк. Обычно нужно передавать только 1 строку с Header'ом
        :return: возвращает словарь с названиями столбцов
        '''
        result = [value for value in data_gs[0]]
        key_colunns_dict = dict()
        for id, item in enumerate(result):
            key_colunns_dict[str(item).upper()] = item
        return key_colunns_dict

    def parsing_in_parts(self, data_gs, key_colunns_dict):
        '''
        Функция, которая парсит всю дату таблицы, создавая
        :param data_gs: Строка из таблицы
        :param key_colunns_dict: Словарь Header'а таблицы
        :return:
        '''
        str_dict = dict(itertools.zip_longest(key_colunns_dict, data_gs, fillvalue=''))
        if str_dict['TAGS'] != '':
            tag_str = str(str_dict.get('TAGS', '')).split(sep=' ')
            if len(tag_str) == 1:
                print('This is Part')
                self.main_parts.obj.append(Main_part(obj = [], **str_dict))
                self.main_parts.add_part(str_dict.get('SECTION'),str_dict)
                print(self.main_parts.obj[0].tags)
            elif len(tag_str) > 1 and str_dict['TEST CASE'] == '':
                print('This in SECTION')
                len_part = len(self.main_parts.obj) - 1
                self.main_parts.obj[len_part].obj.append(Main_part(obj = [], **str_dict))
                print(self.main_parts.obj[0].obj[0].tags)
                self.main_parts.add_section(str_dict.get('SECTION'),str_dict)
            elif len(tag_str) > 1 and str_dict['TEST CASE'] != '':
                print('This is Test keys')
                len_part = len(self.main_parts.obj) - 1
                len_section = len(self.main_parts.obj[len_part].obj) - 1
                self.main_parts.obj[len_part].obj[len_section].obj.append(Main_part(obj = [], **str_dict))
                print(self.main_parts.obj[0].obj[2].obj)
                self.main_parts.add_test_keys(str_dict.get('TEST CASE'),str_dict)
        return

