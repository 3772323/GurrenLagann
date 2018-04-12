from PIL import Image
import math
import numpy 

class Direction() :
    def __init__(self):
        self.x=0
        self.y=0
        self.z=0

    def trouverBalise(self,image):
        sigmar=0
        sigmav=0
        sigmaj=0
        sigmab=0
        img=image
        width = img.size[0]
        height = img.size[1]
        i=0
        j=0
        k=0
        l=0
        cptb=0
        cptj=0
        cptv=0
        cptr=0
        while j < 450:
            while i < 700:            
                img4=img.crop((j,i,j+20,i+20))
    
                for l in range(0,19):
                    for k in range(0,19):
                        (rouge,vert,bleu) = img4.getpixel(( l, k))
                        #affiner encore
                        if rouge > 190 and vert < 95 and bleu < 90 : #Rouge
                            cptr += 1

                        elif bleu > 130 and vert < 130 and rouge < 100 :#Blue	
                            cptb += 1
                            
                        elif vert > 110 and rouge < 115 and bleu < 83 : #Vert
                            cptv += 1

                        
                     #   elif rouge > 140 and vert > 140 and bleu < 80 : #jaune
                      #      cptj +=1
                print("cptr",cptr,"cptv",cptv,"cptb",cptb,"cptj",cptj)
                """sigmar=math.sqrt(((cptr-625)*(cptr-625))/2500)
                print("sigma rouge",sigmar)
                sigmab=math.sqrt(((cptb-625)*(cptb-625))/2500)
                print("sigma bleu",sigmab)
                sigmav=math.sqrt(((cptv-625)*(cptv-625))/2500)
                print("sigma vert ",sigmav)
                sigmaj=math.sqrt(((cptj-625)*(cptj-625))/2500)
                print("sigma jaune ",sigmaj)"""
                cptb=0
                cptj=0
                cptv=0
                cptr=0                
                print("i=",i,"j=",j)
                i=i+20
            i=0
            j=j+20
          #  print("j=",j)
        
                            
       # sigmab=math.sqrt((cptb-625)*(cptb-625)/2500)
       # print(sigmab)
        #if cptb and cptj and cptv and cptr:# il faudrait calculer l'ecart type regarder celui qui est le plus haut selon prof 
          #  return (i/height/2, j/width/2) #faudrait renvoyer un vecteur
               

            
img = Image.open("balise.jpeg")
d=Direction()
d.trouverBalise(img)
img.putpixel((300,150),(0,0,0))
rouge,vert,bleu=img.getpixel((300,150))
print(vert,bleu,rouge)
img.show()
