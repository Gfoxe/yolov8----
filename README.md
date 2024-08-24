## **yolov8车牌识别算法，支持12种中文车牌类型**
## **在原作基础上添加了MySQL数据库支持,识别车牌后写入MySQL表格，带有时间戳。**
## **需要MySQL环境，将sqldata文件夹下record.py中数据库账户密码变量改为自己的即可** ##
库名为plate，表名为licence plate







#### **图片测试demo:**

直接运行detect_plate.py 或者运行如下命令行：

```
python detect_rec_plate.py --detect_model weights/yolov8s.pt  --rec_model weights/plate_rec_color.pth --image_path imgs --output result
```

测试文件夹imgs，结果保存再 result 文件夹中

## **车牌检测训练**

车牌检测训练链接如下：

[车牌检测训练](https://github.com/we0091234/yolov8-plate/tree/master/readme)

## **车牌识别训练**

车牌识别训练链接如下：

[车牌识别训练](https://github.com/we0091234/crnn_plate_recognition)

#### **支持如下：**

- [X] 1.单行蓝牌
- [X] 2.单行黄牌
- [X] 3.新能源车牌
- [X] 4.白色警用车牌
- [X] 5.教练车牌
- [X] 6.武警车牌
- [X] 7.双层黄牌
- [X] 8.双层白牌
- [X] 9.使馆车牌
- [X] 10.港澳粤Z牌
- [X] 11.双层绿牌
- [X] 12.民航车牌

## References

* [https://github.com/derronqi/yolov8-face](https://github.com/derronqi/yolov8-face)
* [https://github.com/ultralytics/ultralytics](https://github.com/ultralytics/ultralytics)





## 联系
数据库支持 QQ2630111811

