对于网络隔离的堡垒主机的一种边信道攻击，利用主板蜂鸣器从主机上窃取文件。Just for fun。

### 原理

- #### 文件编码为音频

将堡垒主机上的文件内容进行二进制编码，调用主板蜂鸣器，长音为“1”，短音为“0”，最终转化为声音传输出去。

也可以利用音量大小，音调高低等进行编码;编码和解码方式也可以采取其他更复杂算法。

原始声频文件波形图：

![](./image/抓图1.png)


- #### 音频还原

将录制的音频解码，恢复为原始文件。

![](./image/figure_2.png)


### 使用

- 文件编码： python read_file_and_play_sound.py
- 音频解码： python sound2raw.py
