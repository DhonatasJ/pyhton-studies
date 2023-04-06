archiveSize = float(input("Insira o tamanho do arquivo em MB: "));
internetSpeed = float(input("Insira a velocidade da internet em Mbps "));

archiveSize = archiveSize * 8;
timeDownload = archiveSize / internetSpeed;

timeDownload = timeDownload / 60;

print("Seu tempo de download será de " + str(round(timeDownload,2)) + " minutos.")