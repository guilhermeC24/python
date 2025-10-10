#1: Converter seg em hrs, min e seg

segs = int(input("Insira os segundos para a conversão: "))

hrs = segs // 3600
segs_restantes = segs % 3600
min = segs_restantes // 60
segs2 = segs_restantes % 60

print("Horas:", hrs, "  Min:", min, "  Seg:", segs2)

