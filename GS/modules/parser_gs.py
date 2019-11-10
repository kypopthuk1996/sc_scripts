import itertools

class Main_part():
    '''Класс раздела'''
    def __init__(self,name,desc,tag):
        '''Инициализация атрибутов:
        name - название раздела
        desc - описание раздела¡
        tag - тег раздела
        '''
        self.name = name
        self.desc = desc
        self.tag = tag

        self.root_part = {'Root':{}}
        self.parts = {}
        self.section = {}
        self.test_keys = {}

    def add_part(self,part,value):
        self.parts[part] = value

    def add_section(self,section,value):
        self.section[section] = value

    def add_test_keys(self,test_keys,value):
        self.test_keys[test_keys] = value

    def table_assembly(self):
        for part, item in self.parts.items():
            tag_part = item.get('TAG').split(sep=' ')
            tag_part = [tag.replace(',','') for tag in tag_part]
            item['SUBSECTION'] = {}
            self.root_part['Root'][part] = item
            for key, value in self.section.items():
                tag_section = value.get('TAG').split(sep=' ')
                tag_section = [tag.replace(',', '') for tag in tag_section]
                if tag_part[0] == tag_section[0].replace(',',''):
                    value['TEST KEYS'] = {}
                    self.root_part['Root'][part]['SUBSECTION'][key] = value
                    for k, v in self.test_keys.items():
                        tag_test_keys = v.get('TAG').split(sep=' ')
                        tag_test_keys = [tag.replace(',', '') for tag in tag_test_keys]
                        if tag_section[0] == tag_test_keys[0] and tag_section[1] == tag_test_keys[1]:
                            self.root_part['Root'][part]['SUBSECTION'][key]['TEST KEYS'][k] = v
                            print('-' * 100)
        return self.root_part

class Parser():
    '''Класс определяет как тип строки пришел с таблиц (Раздел, подраздел или тест-кейс)'''
    def __init__(self):
        self.main_parts = Main_part('Root', 'Главный раздел', 'root')

    def pars_key_columns(self, data_gs):
        result = [value for value in data_gs[0]]
        key_colunns_dict = dict()
        for id, item in enumerate(result):
            key_colunns_dict[str(item).upper()] = item
        return key_colunns_dict

    def parsing_in_parts(self, data_gs, key_colunns_dict):
        #Парсим раздел
        result = [value for value in data_gs]
        str_dict = dict(itertools.zip_longest(key_colunns_dict, result, fillvalue=''))
        if str_dict['TAG'] != '':
            tag_str = str(str_dict.get('TAG', '')).split(sep=' ')
            if len(tag_str) == 1:
                print('This is Part')
                self.main_parts.add_part(str_dict.get('SECTION'),str_dict)
            elif len(tag_str) > 1 and str_dict['TEST CASE'] == '':
                print('This in SECTION')
                self.main_parts.add_section(str_dict.get('SECTION'),str_dict)
            elif len(tag_str) > 1 and str_dict['TEST CASE'] != '':
                print('This is Test keys')
                self.main_parts.add_test_keys(str_dict.get('TEST CASE'),str_dict)
        return

