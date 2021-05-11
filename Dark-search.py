import requests
import datetime



print(" ██▀███  ▓█████ ▄▄▄       ██▓     ██▀███   ▄▄▄      ▓█████▄  ██▓ ▒█████   ▄▄▄       ▄████▄  ▄▄▄█████▓ ██▓ ██▒   █▓▓█████ ")
print("▓██ ▒ ██▒▓█   ▀▒████▄    ▓██▒    ▓██ ▒ ██▒▒████▄    ▒██▀ ██▌▓██▒▒██▒  ██▒▒████▄    ▒██▀ ▀█  ▓  ██▒ ▓▒▓██▒▓██░   █▒▓█   ▀ ")
print("▓██ ░▄█ ▒▒███  ▒██  ▀█▄  ▒██░    ▓██ ░▄█ ▒▒██  ▀█▄  ░██   █▌▒██▒▒██░  ██▒▒██  ▀█▄  ▒▓█    ▄ ▒ ▓██░ ▒░▒██▒ ▓██  █▒░▒███   ")
print("▒██▀▀█▄  ▒▓█  ▄░██▄▄▄▄██ ▒██░    ▒██▀▀█▄  ░██▄▄▄▄██ ░▓█▄   ▌░██░▒██   ██░░██▄▄▄▄██ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ░██░  ▒██ █░░▒▓█  ▄ ")
print("░██▓ ▒██▒░▒████▒▓█   ▓██▒░██████▒░██▓ ▒██▒ ▓█   ▓██▒░▒████▓ ░██░░ ████▓▒░ ▓█   ▓██▒▒ ▓███▀ ░  ▒██▒ ░ ░██░   ▒▀█░  ░▒████▒")
print("░ ▒▓ ░▒▓░░░ ▒░ ░▒▒   ▓▒█░░ ▒░▓  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒▒▓  ▒ ░▓  ░ ▒░▒░▒░  ▒▒   ▓▒█░░ ░▒ ▒  ░  ▒ ░░   ░▓     ░ ▐░  ░░ ▒░ ░")
print("  ░▒ ░ ▒░ ░ ░  ░ ▒   ▒▒ ░░ ░ ▒  ░  ░▒ ░ ▒░  ▒   ▒▒ ░ ░ ▒  ▒  ▒ ░  ░ ▒ ▒░   ▒   ▒▒ ░  ░  ▒       ░     ▒ ░   ░ ░░   ░ ░  ░")
print("  ░░   ░    ░    ░   ▒     ░ ░     ░░   ░   ░   ▒    ░ ░  ░  ▒ ░░ ░ ░ ▒    ░   ▒   ░          ░       ▒ ░     ░░     ░   ")
print("   ░        ░  ░     ░  ░    ░  ░   ░           ░  ░   ░     ░      ░ ░        ░  ░░ ░                ░        ░     ░  ░")
print("                                                     ░                             ░                          ░          ")
print("--------------------------------------------------------------------------------------------------------------------------")
print("                                 This Program Is A Darkweb Search Engine ")
print("                                             By RealRadioActive           ")
print("                                     https://realradioactive.github.io/ ")
print("                                     https://github.com/Realradioactive ")
print("--------------------------------------------------------------------------------------------------------------------------")
print("▓█████▄  ▄▄▄       ██▀███   ██ ▄█▀     ██████ ▓█████ ▄▄▄       ██▀███   ▄████▄   ██░ ██ ")
print("▒██▀ ██▌▒████▄    ▓██ ▒ ██▒ ██▄█▒    ▒██    ▒ ▓█   ▀▒████▄    ▓██ ▒ ██▒▒██▀ ▀█  ▓██░ ██▒")
print("░██   █▌▒██  ▀█▄  ▓██ ░▄█ ▒▓███▄░    ░ ▓██▄   ▒███  ▒██  ▀█▄  ▓██ ░▄█ ▒▒▓█    ▄ ▒██▀▀██░")
print("░▓█▄   ▌░██▄▄▄▄██ ▒██▀▀█▄  ▓██ █▄      ▒   ██▒▒▓█  ▄░██▄▄▄▄██ ▒██▀▀█▄  ▒▓▓▄ ▄██▒░▓█ ░██ ")
print("░▒████▓  ▓█   ▓██▒░██▓ ▒██▒▒██▒ █▄   ▒██████▒▒░▒████▒▓█   ▓██▒░██▓ ▒██▒▒ ▓███▀ ░░▓█▒░██▓")
print(" ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▒ ▓▒   ▒ ▒▓▒ ▒ ░░░ ▒░ ░▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ░▒ ▒  ░ ▒ ░░▒░▒")
print(" ░ ▒  ▒   ▒   ▒▒ ░  ░▒ ░ ▒░░ ░▒ ▒░   ░ ░▒  ░ ░ ░ ░  ░ ▒   ▒▒ ░  ░▒ ░ ▒░  ░  ▒    ▒ ░▒░ ░")
print(" ░ ░  ░   ░   ▒     ░░   ░ ░ ░░ ░    ░  ░  ░     ░    ░   ▒     ░░   ░ ░         ░  ░░ ░")
print("   ░          ░  ░   ░     ░  ░            ░     ░  ░     ░  ░   ░     ░ ░       ░  ░  ░")
print(" ░                                                                     ░                ")
print("--------------------------------------------------------------------------------------------------------------------------")
#Bu program realradioactive tarafından yazılmıştır. Program güvenlik testleri sırasında araşturma için kullanılmak üzere yazılmıştır
#Yasadışı tüm kullanımı yasaktır, Tüm sorumluluk kullanıcıya aittir.
#Bu program ahmia.fi üzerinden basit şekilde arama yapar
print("Donate - BTC -: 1QByZjKJzTqiqKdWLRRsKDu1RFNAF7YD1S ")
print("Donate - ETH -: 0xb22323451e63cF6b7D4C2C3Fe4939Fe8D5b4483D ")
time=datetime.datetime.now()
print("Time:",time)
def temizle():

    open('darkseach.txt', 'w').close()



def ara():
    temizle()
    arama = input("Search:")


    sonuc = requests.get("https://ahmia.fi/search/?q="+str(arama),verify=True)
    #print(str(sonuc.content))
    dosya = open("darkseach.txt", "a")
    dosya.write(str(sonuc.content))
    dosya.close()
    dosya = open("darkseach.txt", "r")
    icerik = dosya.read()
    dosya.close()


    for line in open('darkseach.txt'):

        if "totalResults" in line:
            print('Search Found in DarkNet')
            total = line.rstrip("\n").split('totalResults')[1]
            totalfin = total.split('</span>')[0]
            totalfinb = totalfin.rsplit("n")[1]
            print("+++++++++++++++++++++++++++++++++++++++++++")
            print("Total Number Of Websites Found - Max Page -")
            print(totalfinb)
            print("+++++++++++++++++++++++++++++++++++++++++++")
            sayi = int(input("How Many Pages - Max 1000 Page -:"))
            save = str(input("Do you want to save the search? - yes or no -:"))



        else:
            print("Search Not Found Exiting Dark Search")
            print("Or Try Another Search Later")
            exit()

    #sayi = int(input("How Many Pages:"))
    sayi = sayi + 1

    for line in open('darkseach.txt'):
        for i in range(1, sayi, 1):

            second_field = line.rstrip('\n').split('redirect_url=')[i]
            second_fieldb = second_field.split('>')[0]
            print("---------------------------------------------------")
            print(i,'"'+second_fieldb)

            if save=="yes":
                dosya = open("darkseacharchive.txt", "a")
                veria=("---------------------------------------------------")
                veri = ("Search:",arama,"no:",i,"Time",str(time),second_fieldb,"\n")
                dosya.write(str(veri))
                dosya.close()


ara()

#aramamod = input("New search? yes or no:")
#if aramamod=="yes":
#    ara()
#else:
#    print("Exiting Dark Search")
#    print("Good by and Don't forget to donate ")
def tekrar():
    aramamod = input("New search? yes or no:")
    if aramamod == "yes":
        ara()
    else:
        print("Exiting Dark Search")
        print("Good by and Don't forget to donate ")
        exit()
while True:
    tekrar()