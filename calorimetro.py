#!/usr/bin/python3
m1 = 100;
c1 = 1;
tia = float(input("Qual a temperatura inicial da água? (Celsius)\r\n"));
tim = float(input("Qual a temperatura inicial da moeda? (Celsius)\r\n"));
tfa = float(input("Qual a temperatura final da água? (Celsius)\r\n "));
tfm = float(input("Qual a temperatura final da moeda? (Celsius)\r\n"));
m2 = 4.78;

c2 = (-((m1*c1*(tfa - tia))/(m2*(tfm - tim))));
print("O calor específico da moeda é:", c2, "cal/g.");