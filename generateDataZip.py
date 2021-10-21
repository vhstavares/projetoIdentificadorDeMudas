import cv2
import os


##Ler os dados
if __name__ == "__main__":
    listDir = r"C:\Users\Victor\Documents\Facens 2021\TCC - 2\Base"
    lista = os.listdir(listDir)

    for i in range(len(lista)):
        muda = lista[i]
        path = os.path.join(listDir, muda)
        listMuda = os.listdir(path)

        lenTrain = int(len(listMuda) * 0.8)
        lenTest = int(len(listMuda) * 0.2)

        print("Treino")
        for j in range(lenTrain):
            img = os.path.join(path, listMuda[j])
            readImg = cv2.resize(cv2.imread(img, cv2.IMREAD_COLOR), (180, 120), interpolation=cv2.INTER_CUBIC)
            pathTest = os.path.join(r"C:\Users\Victor\Documents\Facens 2021\TCC - 2\Mudas\test", muda)
            if not os.path.exists(pathTest):
                os.makedirs(pathTest)
            cv2.imwrite(f'{pathTest}/{muda}{j}.jpg', readImg)

        print("Test")
        for j in range(lenTrain, len(listMuda)):
            img = os.path.join(path, listMuda[j])
            readImg = cv2.resize(cv2.imread(img, cv2.IMREAD_COLOR), (180, 120), interpolation=cv2.INTER_CUBIC)
            pathTrain = os.path.join(r"C:\Users\Victor\Documents\Facens 2021\TCC - 2\Mudas\train", muda)
            if not os.path.exists(pathTrain):
                os.makedirs(pathTrain)
            cv2.imwrite(f'{pathTrain}/{muda}{j}.jpg', readImg)