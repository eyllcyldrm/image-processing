import cv2

resim = cv2.imread("fotii.jpg")
red = cv2.imread("fotii.jpg")
blue = cv2.imread("fotii.jpg")
green = cv2.imread("fotii.jpg")

#Görüntünün kendisi
cv2.imshow("Arabalar",resim)
cv2.waitKey(0)
#Katmanların gösterilişi
red[:,:,0] = 0
red[:,:,1] = 0
cv2.imshow("kirmizi",red)
cv2.waitKey(0)

green[:,:,0] = 0
green[:,:,2] = 0
cv2.imshow("yesil",green)
cv2.waitKey(0)

blue[:,:,1] = 0
blue[:,:,2] = 0
cv2.imshow("Mavi",blue)
cv2.waitKey(0)

#Kırpılmış görüntü
#print(resim.shape)
rows = resim.shape[0]
start_row = int(rows/2)

resminyarisi = resim[start_row:,:]
cv2.imshow("yaridan asagisi", resminyarisi)
cv2.waitKey(0)

#Gri resim
resimGri = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
cv2.imshow("gri",resimGri)
cv2.waitKey(0)

#90 derece saat yönünde dönmüş resim
rows, cols = resim.shape[:2]
yon_matrisi = cv2.getRotationMatrix2D((cols/2,rows/2),-90,0.5)
donmus_resim = cv2.warpAffine(resim,yon_matrisi,(cols,rows))
cv2.imshow("saat yonunda 90 derece donmus resim",donmus_resim)

cv2.waitKey(0)
cv2.destroyAllWindows()