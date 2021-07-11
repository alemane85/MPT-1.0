import MyCsv

this=MyCsv.MyCsvFile()
myfields=[
            'NOME', 'Val1', 'Val2', 'Val3', 'Val4', 'Val5', 'Val6',
            'Val7', 'Val8', 'Val9', 'Val10', 'Val11', 'Val16',
            'Val17', 'Val18', 'Val19', 'Val20', 'Val21', 'Val22',
            'Val23', 'Val24', 'Val25'
        ]
this.load("samples\prova.txt",myfields)
print(this)
