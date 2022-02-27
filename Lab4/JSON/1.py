import json

file = open("sample-data").read()  #прочтет файл в котором много строк с определенными обозначениями

object = json.loads(file) #преобразует строку в формате JSON в объект Python
print(
"Interface Status\n"
"================================================================================\n"
"DN                                                 Description           Speed    MTU \n"
"-------------------------------------------------- --------------------  ------  ------")
data = object["imdata"] #"imdata": [....] начало в файле название для дальнейшего использования
for i in data: #для каждого элемента возьмет обозначения специальные (посчитает)
    DN = i["l1PhysIf"]["attributes"]["dn"]  #topology/pod-1/node-201/sys/phys-[eth1/33] ...
    Desc = i["l1PhysIf"]["attributes"]["descr"]
    Speed = i["l1PhysIf"]["attributes"]["speed"] #inherit
    MTU = i["l1PhysIf"]["attributes"]["mtu"] #9150

    print("{0:50} {1:20} {2:7}   {3:6}".format(DN, Desc, Speed, MTU)) #выведет на определенных позициях значения размеров
