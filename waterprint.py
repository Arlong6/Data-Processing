import os,traceback
from PIL import Image

# 獲取資料夾圖片 get folder images
def get_folder(fpath,wm_file,save_path):
    try:
        img_suffix_list = ['png', 'jpg', 'bmp']
        for i in os.listdir(fpath):
            if i.split('.')[-1] in img_suffix_list:
                img_path = fpath + '/' + i
                img_water_mark(img_file=img_path,wm_file=wm_file,save_path=save_path)
    except Exception as e:
        print(traceback.print_exc())

# 圖片新增水印 add waterprint
def img_water_mark(img_file, wm_file,save_path):
    try:
        img = Image.open(img_file)  # 開啟圖片
        watermark = Image.open(wm_file)  # 開啟水印
        img_size = img.size
        wm_size = watermark.size
        # 如果圖片大小小於水印大小
        if img_size[0] < wm_size[0]:
            watermark.resize(tuple(map(lambda x: int(x * 0.5), watermark.size)))
        print('圖片大小：', img_size)
        wm_position = (img_size[0]-wm_size[0],img_size[1]-wm_size[1]-400) # 預設設定水印位置為右下角
        layer = Image.new('RGBA', img.size)  # 新建一個圖層
        layer.paste(watermark, wm_position)  # 將水印圖片新增到圖層上
        mark_img = Image.composite(layer, img, layer)
        new_file_name = '/new_'+img_file.split('/')[-1]
        mark_img.save(save_path + new_file_name)
    except Exception as e:
        print(traceback.print_exc())
#run the code
get_folder("waterprint\Real_data_original","waterprint\waterprint.png","waterprint\Real_data_water")