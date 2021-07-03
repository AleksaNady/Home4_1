#for i in range(20,240):
    #if i%20 ==0: #Если число кратно 20
        #print(i)

#range создал нам список
uniq_list = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
print(uniq_list)