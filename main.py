welcome_message = "WELCOME TO MOUSEPY GAMES !" 
mousepy_position=2
print ("********************************")
print (f"**** {welcome_message}*****")
print ("********************************")
nama_user = input("Masukan nama kamu : ")
print (f'''
Hallo {nama_user}! Coba perhatikan Goa dibawah ini 
|_| |_| |_| |_|
''')
pilihan_user = input("Menurut kamu digoa nomor berapa MOUSEPY berada? [1 / 2 / 3 / 4]")
print(f"Pilihan kamu adalah {pilihan_user}")
if pilihan_user == mousepy_position:
     print ("Selamat kamu menang")
else:
     print ("Kamu kalah! MOUSEPY bukan berada di situ")
     
