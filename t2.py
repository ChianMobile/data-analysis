path = 'aaa.txt'
outputfile = path.split('.')[0]+'_w.csv'
print outputfile

print '2'>'1'


s = '2018-04-16 235158|V1.0.0|eeee|1|NBELFA4F7C11|2018-04-16 23:38:30|808|2018-04-16 23:51:58|0|46|192.168.1.1|172.21.19.179|DISCONNECTED|DISCONNECTED|DISCONNECTED|DISCONNECTED|CONNECTED|CONNECTED|ERROR_NONE|CONNECTED|5|5|1|1_TR069_R_VID_46|1.626|10793.135|2.833|10773.016|4|4_VOIP_R_VID_45|1.627|10793.113|2.833|10772.014|2|2_INTERNET_R_VID_41|1.623|10770.672|2.833|10772.379|3|3_OTTV_B_VID_48|1.623|10770.65|2.833|10772.014|5|5_OTTV_B_VID_50|1.623|10770.65|2.833|10773.836|1|1||android-1e8cb1a00195cac9|||e4:5a:a2:c2:23:26|0.918|3.712|1.232|7.133|2.4G|-60dBm|15724|1891|1||UNKNOWN|0||0|'
sa = s.split('|')
if sa[21] != '':
    index_a = 21 + int(sa[21]) * 6 + 2
    for i in range(int(sa[21])):
        pass
        # print sa[22+i*6], sa[23+i*6], sa[24+i*6], sa[25+i*6], sa[26+i*6], sa[27+i*6]
    if sa[index_a] == '1':
        if len(sa) >= index_a + 11:
            print len(sa)
            print index_a

            i = 0
            lan = sa[4] + ',' + sa[int(index_a) + 2 + i * 11] + ',' + sa[int(index_a) + 5 + i * 11] + ',' +\
                  sa[int(index_a) + 6 + i * 11] +\
                  ',' + sa[int(index_a) + 7 + i * 11] + ','
            print lan
    else:
        for i in range(int(sa[index_a])):
            if len(sa) >= index_a + 13*i:
                lan = sa[4] + ','+ sa[int(index_a) + 2 + i * 11] + ',' + sa[int(index_a) + 5 + i * 11] + ',' + sa[int(index_a) + 6 + i * 11] + ',' + sa[int(index_a) + 7 + i * 11] + ',' + sa[
                    int(index_a) + 10 + i * 11] + ',' + sa[int(index_a) + 11 + i * 11]
                print lan


#|2||android-82c826b8e84c0f87|||3c:f5:91:dd:75:21|34.583|1332.647|93.582|3801.395||||android-925cf8c720751fb1|||94:d0:29:90:97:89|34.641|1334.872|93.582|3801.391|||17679|97|1||UNKNOWN|0||0|