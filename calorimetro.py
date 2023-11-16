#!/usr/bin/python3
m1 = 100;
c1 = 1;
tia = int(input("Qual a temperatura inicial da água? (Celsius)\r\n"));
tim = int(input("Qual a temperatura inicial da moeda? (Celsius)\r\n"));
tfa = int(input("Qual a temperatura final da água? (Celsius)\r\n "));
tfm = int(input("Qual a temperatura final da moeda? (Celsius)\r\n"));
m2 = 4.8;



c2 = -((m1*c1*(tfa - tia))/(m2*(tfm - tim)));
print("O calor específico da moeda é:", c2);