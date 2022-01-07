# robosys2021_homework2
ロボットシステム学課題2のリポジトリです

## 概要
Google LCC様の[MediaPipe](https://github.com/google/mediapipe)を用いて骨格の座標を取得し、[ROS Wiki](http://wiki.ros.org/turtlesim)を参考にTutlesimを動かすパッケージです。

今回のプログラムは[こちら](https://github.com/MakiSakurai/robotdesign3_2021_1.git)のリポジトリを参考に制作しました。

## 使用方法

### セットアップ方法
```
cd ~/catkin_ws/src
```

```
git clone https://github.com/MakiSakurai/robosys2021_homework2.git
```

```
cd ~/catkin_ws
```

```
catkin build
```

```
source ~/.bashrc
```

MediaPipeのインストールは[こちら](https://google.github.io/mediapipe/getting_started/install.html#installing-on-debian-and-ubuntu)を参考にしてください

## 使用方法

### シミュレーター起動

```
roslaunch robosys2021_homework2 main_sim.launch
```

### 操作方法

右腕を右上に挙げると、亀が右回転します。右手首の座標を取得し適切な位置で判定をしています

![phonto (1)](https://user-images.githubusercontent.com/71488377/148590899-1473f4dc-7b83-416c-aa9f-75d903a7e3d2.png)

左腕を左上に挙げると、亀が左回転します。左手首の座標を取得し適切な位置で判定をしています

![IMG_4124](https://user-images.githubusercontent.com/71488377/148591236-990a045c-d881-414f-80f0-f33cb8bb1a44.jpg)

両腕を上に挙げると、亀が前進します。両肘の座標を取得し適切な位置で判定をしています

![無題120_20220108033250](https://user-images.githubusercontent.com/71488377/148591292-8d03c98b-22cf-4c62-a49d-88df76f020c6.png)


## 実際に動かしている様子
https://youtu.be/YPFb3Zt-CHQ

## ライセンス

このリポジトリはBSD 3-Clause Licenseを使用しています: [BSD 3-Clause License](https://github.com/MakiSakurai/robosys2021_homework2/blob/main/LICENSE)

MediaPipe: [Apache License 2.0](https://github.com/google/mediapipe/blob/master/LICENSE)

ROS Wiki: [Creative Commons Attribution 3.0](https://creativecommons.org/licenses/by/3.0/deed.ja)
