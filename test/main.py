while True:
    soz = input("Topishmoq:")
    if soz == 'salom':
         print('Salom bir son oyladim 1 10gacham:')
         while True:
            javob =5
            son = int(input("Javob:"))
            if son == javob:
                print("barakalla")
                break
            elif son > javob:
                print('kattaroq son kiriting')
            elif son < javob:
                print('kichkina  son kiriting')
            else:
                print("topishmoqni ishga tushurish uchun {salom} yozin ")
    else:
        print('topishmoqni ishga tushurish uchun {salom} sozini kriting ')