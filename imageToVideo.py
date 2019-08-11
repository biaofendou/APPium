import os
import cv2
from PIL import Image

path = 'C:/Users/11527/Desktop/pic/'
filelist = os.listdir(path)

fps = 24  # 视频每秒24帧
size = (48, 270)  # 需要转为视频的图片的尺寸
filelist.sort(key=lambda x: str(x[:-4]))
print(filelist)
# 可以使用cv2.resize()进行修改
video = cv2.VideoWriter("./video/Videop.avi", cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)
# 视频保存在当前目录下
i = 0
for item in filelist:
    if item.endswith('.png'):
        # 找到路径中所有后缀名为.png的文件，可以更换为.jpg或其它
        item = path + item
        if i == 0:
            im = Image.open(item)
            size = (im.size[0], im.size[1])
            video = cv2.VideoWriter("./video/Videop.avi", cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)
            img = cv2.imread(item)
            i += 1
        else:
            print(item)
            img = cv2.imread(item)
            # print(img)
            video.write(img)

video.release()
# cv2.destroyAllWindows()
# for i in range(0, 6000):
#     p = i
#     # print(str(p)+'.png'+'233333')
#     if os.path.exists('./result/output_' + str(p) + '.png'):  # 判断图片是否存在
#         img = cv2.imread(filename='./result/output_' + str(p) + '.png')
#         cv2.waitKey(100)
#         video.write(img)
#         print('output_'+str(p) + '.png' + ' done!')
# video.release()
