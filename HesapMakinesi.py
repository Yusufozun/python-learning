first_number= int(input())
print("please type the first number:",first_number)
second_number=int(input())
print("please type the second number:",second_number)
islem_sec=input()
print("chose between + , - , * , / ",islem_sec)
if islem_sec == "+":
    toplama_func()
elif islem_sec=="-":
    cikarma_func()
elif islem_sec=="*":
    carpma_func()
elif islem_sec=="/":
     bolme_func()   

else:
    print("Yanlış giris")
    
    def toplama_func():
        toplama_sonuc=first_number+second_number
        print(f"{toplama_sonuc}")

    def cikarma_func():
        cikarma_sonuc=first_number-second_number
        print(f"{cikarma_sonuc}")
    def carpma_func():
        carpma_sonuc=first_number*second_number
        print(f"{carpma_sonuc}")
    def bolme_func():
        bolme_sonuc=first_number/second_number
        print(f"{bolme_sonuc}")
