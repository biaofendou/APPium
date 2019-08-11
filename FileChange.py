import os

path = "/home/dgpu/Project/Ma/youku/data/round1_test_input/youku_00200_00249_l/"
path_output="/home/dgpu/Project/Ma/youku/data/round1_test_input/output/"
file = os.listdir(path)
def y4mToPic(file1):
    p = 200
    for item in file1:
        if item.endswith('.y4m'):
            itemdir = path + item
            os.system('mkdir /home/dgpu/Project/Ma/youku/data/round1_test_input/youku_00200_00249_l/'+str(p))
            os.system(
                'ffmpeg -i ' + itemdir + ' -vsync 0 /home/dgpu/Project/Ma/youku/data/round1_test_input/youku_00200_00249_l/' + str(
                    p) + '/' + item[:-4] + '%3d.bmp -y')
            p+=1
#   ffmpeg -i xxx.y4m -vf select=notmodn\,25)) -vsync 0  '(('-y xxx_sub25.y4m'))'
#  bmptoy4m: ffmpeg -i xx%3d.bmp  -pix_fmt yuv420p  -vsync 0 xx.y4m -y
def PicToy4m(file1):
    file1 = os.listdir(file1)
    file1.sort()
    #print(file1)
    pp = 0
    for item in file1:
        itemPic = os.path.join(path_output,item)
        itemPic_dir = os.listdir(itemPic)
        itemPic_dir.sort()
        os.system('ffmpeg -i '+ str(itemPic)+'%3d.bmp  -pix_fmt yuv420p  -vsync 0 /home/dgpu/Project/Ma/youku/data/round1_test_input/results/Youku_ 00'+str(item)+'_h_Res.y4m -y')
        pp+=1
        if pp >=20 :
            os.system('ffmpeg -i /home/dgpu/Project/Ma/youku/data/round1_test_input/results/Youku_ 00'+str(item)+'_h_Res.y4m -vf select=str(not(mod(n\,25))) -vsync 0  -y /home/dgpu/Project/Ma/youku/data/round1_test_input/Sub25/Youku_ 00'+str(item)+'_h_Sub25_Res.y4m')
        #print(itemPic)
        #for _ in itemPic_dir:
          #  if _.endswith('.png'):
           #     pic=os.path.join(itemPic,_)
            #    print(pic)

            #:print(_)
       
PicToy4m(path_output)
