# Есть список из случайных чисел и строк.
# Создайте цикл, итерирующийся до тех пор, пока не встретится число "777".
# Если в течении 100 попыток число не будет найдено — остановить цикл и вызвать ошибку с соответсвующим сообщением.

attempt = 1
spisok = ['100','200','Super','Lviv','123','1','2','','75478','200','898','Lviv','123','1','2','','75478','200','Super','Lviv','123','1','2','','75478','200','Super','Lviv','123','1','2','','75478','200','Super','Lviv','123','1','2','','75478','200','Super','Lviv','123','1','2','','75478','200','Super','Lviv','123','1','2','','75478','200','Super','Lviv','123','1','2','','75478','200','Super','Lviv','123','1','2','','75478','200','Super','Lviv','123','1','2','','75478','200','Super','Lviv','123','1','2','','75478','200','Super','Lviv','123','1','2','','75478','200','Super','Lviv','123','1','2','','75478','200','Super','Lviv','123','1','2','','75478','200','Super','Lviv','123','1','2','','75478','200','Super','Lviv','123','1','2','','75478','200','Super','Lviv','123','1','2','','75478','200','Super','Lviv','123','1','2','','75478','200','Super','Lviv','123','1','2','','75478','200','Super','Lviv','123','1','2','','75478','1','2','','75478','200','Super','Lviv','123','1','2','','75478','200','Super','Lviv','123','1','2','','75478','200','Super','Lviv','123','1','2','','75478','200','Super','Lviv','123','1','2','','75478','200','Super','Lviv','123','1','2','','75478']
for x in spisok:
    attempt += 1
    if x == '777':
        print ('Найдено число 777 с попытки = ',attempt )
        break
    if attempt == 100:
        raise Exception("Количество попыток ограничено 100")       
