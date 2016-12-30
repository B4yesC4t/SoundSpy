# coding: utf-8

import re
import scipy.io.wavfile
import matplotlib.pyplot as plt


wav_file = "./model1_abc.wav"


def read_raw_wav(wav_file, is_plot=False, SOUND=2000):
    """
    读取原始wav文件，利用阈值进行过滤
    :param wav_file: wav文件
    :param is_plot: 是否画图
    :param SOUND: 阈值
    :return:
    """
    wave_data = scipy.io.wavfile.read(wav_file)[1]
    max_sound = [i[0] for i in wave_data]
    str_tmp = ''
    for i in max_sound:
        if i > SOUND:
            str_tmp += '1'
        else:
            str_tmp += '0'
    if is_plot:
        plt.subplot(2, 1, 1), plt.plot(range(len(max_sound)), max_sound)
        plt.subplot(2, 1, 2), plt.plot(range(len(str_tmp)), [int(i) for i in str_tmp])
        plt.show()
    return str_tmp


def str2bin(str_tmp):
    """
    将音频字符串还原成二进制流
    :param str_tmp:
    :return:
    """
    sound_list = re.split(r'0{100,}', str_tmp)
    print len(sound_list)
    len_list = [len(i) for i in sound_list]
    max_len = max(len_list)
    min_len = min(len_list)
    middle_len = (max_len + min_len) / 2
    avg = sum(len_list) / len(len_list)
    min_list = [i for i in len_list if i < avg]
    min_avg = sum(min_list) / len(min_list)
    bin = ''
    for i in len_list:
        if i > middle_len:
            bin += '1'
        elif i > min_avg:
            bin += '0'
    return bin


def get_result(bin):
    """
    将二进制流还原成最终结果
    :param bin:
    :return:
    """
    result = ''
    num_char = len(bin) / 8
    for i in range(num_char):
        char_bin = bin[i*8:(i+1)*8]
        char_ascii = int(char_bin, 2)
        char = chr(char_ascii)
        print char_bin, char_ascii, char
        result += char
    print 'result is:', result
    

if __name__ == "__main__":
    str_tmp = read_raw_wav(wav_file, True)
    get_result(str2bin(str_tmp))
