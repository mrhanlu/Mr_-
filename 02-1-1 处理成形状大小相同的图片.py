import cv2 as cv
import os
import numpy as np


# def cut_photo(norm_img,cut_img):           #把cut_img裁成和norm_img形状相同的图片
#     H,W,*_ = norm_img.shape
def cut_photo(H, W, cut_img):  # 设置输出固定形状的图片
    H, W = H, W
    h, w, *c = cut_img.shape
    size = 1 if [] == c else 3  # c是空c=1,其它c=3
    if H / h < W / w:
        img2 = cv.resize(cut_img, (int(w * (H / h)), H), interpolation=cv.INTER_LINEAR)
        _, w, *_ = img2.shape
        left = int((W - w) / 2)
        right = int(np.ceil((W - w) / 2))
        top, bottom = 0, 0
        img2_cut = cv.copyMakeBorder(img2, top, bottom, left, right, cv.BORDER_CONSTANT, value=np.zeros(size))
    else:
        img2 = cv.resize(cut_img, (W, int(h * (W / w))), interpolation=cv.INTER_LINEAR)
        h, _, *_ = img2.shape
        top = int((H - h) / 2)  # 距各边界宽度
        bottom = int(np.ceil((H - h) / 2))
        left, right = 0, 0
        img2_cut = cv.copyMakeBorder(img2, top, bottom, left, right, cv.BORDER_CONSTANT, value=np.zeros(size))
    return img2_cut


def read_photo(H, W, img_path, save_path):
    if not os.path.exists(save_path):  # 如果path存在，返回True；如果path不存在，返回False。
        os.mkdir(save_path)  # 创建目录
    for i, name in enumerate(os.listdir(img_path)):
        filename = os.path.join(img_path, name)
        img = cv.imdecode(np.fromfile(filename, np.uint8), -1)
        cut_img = cut_photo(H, W, img)
        cv.imwrite(os.path.join(save_path, "{}.jpg".format(str(i))), cut_img)


if __name__ == '__main__':
    img_path = r"F:\My_program\test_hello\Spiders\cat"
    save_path = r"./cut_img"
    read_photo(100, 100, img_path, save_path)
