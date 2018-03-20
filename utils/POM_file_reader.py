import yaml
import os
from xlrd import open_workbook


class YamlReader(object):
    def __init__(self, yamlfile):
        if os.path.exists(yamlfile):
            self.yamlfile = yamlfile
        else:
            raise FileNotFoundError("Not find file: %s" % yamlfile)
        self._data = None

    # @property 用法介绍
    # https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386820062641f3bcc60a4b164f8d91df476445697b9e000
    @property   # 把方法设置成属性
    def data(self):
        if not self._data:
            with open(self.yamlfile, 'rb') as f:
                # load后是generator, 用list组织成列表
                self._data = list(yaml.safe_load_all(f))
                return self._data


class SheetTypeError(Exception):
        pass


class ExcelReader(object):
    def __init__(self, excelfile, sheet=0, title_line=True):
        if os.path.exists(excelfile):
            self.excelfile = excelfile
        else:
            raise FileNotFoundError("No find excel file: %s" % excelfile)
        self.sheet = sheet
        self.title_line = title_line
        self._data = list()

    @property
    def data(self):
        if not self._data:
            workbook = open_workbook(self.excelfile)
            if type(self.sheet) not in [int, str]:
                raise SheetTypeError("Please verify in <type int> or <type str>".format(type(self.sheet)))
            elif type(self.sheet) == int:
                s = workbook.sheet_by_index(self.sheet)
            else:
                s = workbook.sheet_by_name(self.sheet)

            if self.title_line:
                title = s.row_values(0)
                for col in range(1, s.nrows):
                    self._data.append(dict(zip(title, s.row_values(col))))
            else:
                for col in range(0, s.nrows):
                    self._data.append(s.row_values(col))
        return self._data


if __name__ == "__main__":
    yamlfile = os.path.dirname(os.path.abspath('.')) + '/config/' + 'config_yml.yml'
    print(yamlfile)
    reader = YamlReader(yamlfile)
    print(reader.data)

    excelfile = os.path.dirname(os.path.abspath('.')) + '/data/' + "data_excel.xlsx"
    print(excelfile)
    reader = ExcelReader(excelfile, title_line=False)
    print(reader.data)


