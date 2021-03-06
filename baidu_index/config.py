#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 要启用的浏览器driver, 因为有些人PhantomJS配置可能有问题，默认使用Firefox(容易配置).
# 具体参考selenium的浏览器环境配置
browser_driver = 'Chrome'  # 可以替换为PhantomJS
# 百度用户名
user_name = ''
# 百度密码
password = ''
# 百度登陆链接
login_url = ('https://passport.baidu.com/v2/?login&tpl=mn&u='
             'http%3A%2F%2Fwww.baidu.com%2F')
# 一周
one_week_trend_url = ('http://index.baidu.com/?tpl=trend&type=0'
                      '&area={area}&time=12&word={word}')
#90天
ninety_days_trend_url = ('http://index.baidu.com/?tpl=trend&type=0'
                      '&area={area}&time=13&word={word}')

# 区间
time_range_trend_url = ('http://index.baidu.com/?tpl=trend&type=0&area={area}'
                        '&time={start_date}|{end_date}&word={word}')
# api
all_index_url = ('http://index.baidu.com/Interface/Search/getAllIndex/'
                 '?res={res}&res2={res2}&startdate={start_date}'
                 '&enddate={end_date}')
# 图片信息的api
index_show_url = ('http://index.baidu.com/Interface/IndexShow/show/?res='
                  '{res}&res2={res2}&classType=1&res3[]={enc_index}'
                  '&className=view-value&{t}'
                  )
# 判断登陆状态的地址
user_center_url = 'http://i.baidu.com/'
# 判断登陆的标记
login_sign = 'http://passport.baidu.com/?logout'
# 线程数
num_of_threads = 100

# 关键词index的区间开始
start_date = '2015-12-01'
# 关键词index的区间结束
end_date = '2016-07-31'

# 输出的格式，暂时只支持excel
# extension = 'excel'
# 输出的文件夹路径，可以自定义
out_file_path = './data/out'
# 关键词任务的文件路径，可以自定义
keywords_task_file_path = './baidu_index/keyword.txt'
cities_task_file_path = './baidu_index/city.txt'

# 要获取趋势的类别，默认是三种趋势都获取。all代表整体趋势，pc代表PC趋势, wise代表移动趋势
index_type_list = ['all', 'pc', 'wise']
#index_type_list = ['all']


def get_cities():

    bd_areamap = ["911,北京,514,北京","910,上海,57,上海","913,广东,95,广州,94,深圳,196,佛山,199,惠州,212,汕头,133,东莞,203,茂名,198,江门,200,珠海,197,湛江,209,肇庆,205,揭阳,207,中山,201,韶关,202,阳江,195,云浮,211,梅州,208,清远,204,潮州,213,汕尾,210,河源","923,天津,164,天津","927,河南,168,郑州,378,洛阳,262,南阳,263,新乡,373,信阳,370,安阳,266,平顶山,371,驻马店,265,焦作,381,三门峡,375,周口,268,许昌,264,开封,376,商丘,380,濮阳,379,漯河,374,鹤壁","914,四川,97,成都,98,绵阳,107,乐山,106,德阳,103,泸州,113,达州,291,眉山,111,自贡,104,南充,102,内江,96,宜宾,108,广安,114,雅安,109,资阳,99,广元,100,遂宁,112,攀枝花,101,巴中,417,甘孜,479,凉山,457,阿坝","904,重庆,11,重庆","916,江苏,126,苏州,125,南京,127,无锡,161,徐州,169,镇江,160,盐城,163,南通,162,常州,158,扬州,159,泰州,156,连云港,172,宿迁,157,淮安","906,湖北,28,武汉,35,宜昌,31,荆州,32,襄樊,36,十堰,34,荆门,33,黄冈,41,孝感,30,黄石,40,咸宁,38,恩施,37,随州,39,鄂州,42,仙桃,74,潜江,73,天门","917,浙江,138,杭州,149,温州,289,宁波,135,金华,287,台州,304,嘉兴,303,绍兴,305,湖州,134,丽水,288,衢州,306,舟山","909,福建,50,福州,55,泉州,54,厦门,56,漳州,87,宁德,52,三明,51,莆田,253,南平,53,龙岩","921,黑龙江,152,哈尔滨,153,大庆,324,绥化,319,齐齐哈尔,320,佳木斯,322,牡丹江,300,黑河,323,鸡西,295,伊春,301,鹤岗,359,双鸭山,302,七台河,297,大兴安岭","901,山东,1,济南,77,青岛,80,潍坊,78,烟台,79,临沂,81,淄博,353,泰安,352,济宁,83,聊城,82,东营,88,威海,86,德州,76,滨州,356,莱芜,85,枣庄,84,菏泽,366,日照","924,陕西,165,西安,275,渭南,277,咸阳,273,宝鸡,276,汉中,278,榆林,272,安康,401,延安,274,商洛,271,铜川","920,河北,141,石家庄,261,唐山,259,保定,148,沧州,292,邯郸,143,衡水,146,秦皇岛,147,廊坊,293,邢台,145,承德,144,张家口","907,辽宁,150,沈阳,29,大连,217,锦州,215,鞍山,224,辽阳,219,丹东,221,营口,220,本溪,218,铁岭,222,抚顺,216,朝阳,223,阜新,225,葫芦岛,151,盘锦","922,吉林,154,长春,270,吉林,525,延边,155,四平,410,白城,407,通化,194,松原,408,白山,191,辽源","915,云南,117,昆明,337,红河,123,玉溪,339,曲靖,334,大理,437,文山,438,保山,342,丽江,335,昭通,662,思茅,350,临沧,124,楚雄","926,新疆,467,乌鲁木齐,280,石河子,563,塔城,317,克拉玛依,315,阿克苏,312,哈密,499,巴音郭楞,383,阿勒泰,311,昌吉,660,伊犁哈萨克,310,吐鲁番,384,喀什,318,博尔塔拉,653,克孜勒苏柯尔克孜,386,和田,661,五家渠","912,广西,90,南宁,89,柳州,91,桂林,131,百色,119,河池,132,梧州,93,贵港,118,玉林,128,北海,129,钦州,506,来宾,92,贺州,130,防城港","929,山西,231,太原,233,运城,237,吕梁,230,晋中,232,临汾,227,大同,234,晋城,228,长治,229,忻州,236,阳泉,235,朔州","908,湖南,43,长沙,46,株洲,45,衡阳,49,郴州,68,常德,44,岳阳,269,永州,405,邵阳,67,怀化,48,益阳,47,湘潭,66,娄底,226,张家界,65,湘西","903,江西,5,南昌,10,赣州,6,九江,9,上饶,137,景德镇,115,吉安,7,鹰潭,256,宜春,8,抚州,136,萍乡,246,新余","928,安徽,189,合肥,182,滁州,179,宿州,186,安庆,181,六安,187,蚌埠,391,亳州,184,阜阳,188,芜湖,176,宣城,177,巢湖,173,铜陵,178,淮南,185,马鞍山,183,淮北,174,黄山,175,池州","905,内蒙古,20,呼和浩特,25,呼伦贝尔,21,赤峰,13,包头,15,巴彦淖尔,22,通辽,14,鄂尔多斯,16,乌海,331,乌兰察布,333,兴安盟,19,锡林郭勒盟,17,阿拉善盟","925,甘肃,166,兰州,283,武威,285,张掖,286,嘉峪关,308,天水,307,平凉,344,陇南,281,庆阳,282,定西,284,酒泉,309,白银,343,金昌,346,临夏","930,海南,239,海口,243,三亚,244,儋州,241,万宁,582,五指山,242,琼海,456,东方","902,贵州,2,贵阳,59,遵义,4,六盘水,3,黔南,426,毕节,424,安顺,422,铜仁,61,黔东南,588,黔西南","919,宁夏,140,银川,395,吴忠,472,石嘴山,396,固原,480,中卫","918,青海,139,西宁,608,海西,659,玉树,652,海东","931,台湾","932,西藏,466,拉萨,655,那曲,656,林芝,516,日喀则","933,香港,663,香港","934,澳门,664,澳门"]
    bd_areas = []

    def transformArea(s):
        items = s.split(',')
    
        for i in range(2,len(items),2):
            bd_areas.append((items[i],items[i+1]))
        return bd_areas
    
    list(map(transformArea,bd_areamap))

    return bd_areas