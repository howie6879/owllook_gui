#!/usr/bin/env python
"""
 Created by howie.hu at 2018/6/4.
"""
import logging
import os

from collections import namedtuple

logging_format = "[%(asctime)s] %(process)d-%(levelname)s "
logging_format += "%(module)s::%(funcName)s():l%(lineno)d: "
logging_format += "%(message)s"

logging.basicConfig(
    format=logging_format,
    level=logging.INFO
)


class Config:
    APP_TITLE = 'owllook 小说监控'
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    LOGGER = logging.getLogger()
    VERSION = 0.1

    # Engine config
    URL_PHONE = 'https://m.baidu.com/s'
    URL_PC = 'http://www.baidu.com/s'
    BAIDU_RN = 15
    SO_URL = "https://www.so.com/s"
    BY_URL = "https://www.bing.com/search"
    DUCKGO_URL = "https://duckduckgo.com/html"

    # Basic Config
    BLACK_DOMAIN = ['www.17k.com', 'mm.17k.com', 'www.xs8.cn', 'www.zongheng.com', 'yunqi.qq.com', 'chuangshi.qq.com',
                    'book.qidian.com', 'www.soduso.com', 'pages.book.qq.com', 'book.km.com', 'www.lread.net',
                    'www.0dsw.com', 'www.5200xsb.com', 'www.80txt.com', 'www.sodu.tw', 'www.shuquge.com',
                    'www.shenmanhua.com', 'xiaoshuo.sogou.com', 'www.999wx.com', 'zetianji8.com', 'www.bookso.net',
                    'm.23us.com', 'www.qbxsw.com', 'www.zhuzhudao.com', 'www.shengyan.org', 'www.360doc.com',
                    'www.ishuo.cn', 'read.qidian.com', 'www.yunlaige.com', 'www.qidian.com', 'www.sodu888.com',
                    'www.siluke.cc', 'read.10086.cn', 'www.pbtxt.com', 'c4txt.com', 'www.bokon.net', 'www.sikushu.net',
                    'www.is028.cn', 'www.tadu.com', 'www.kudu8.com', 'www.bmwen.com', 'www.5858xs.com', 'www.yiwan.com',
                    'www.x81zw.com', 'www.123du.cc', 'www.chashu.cc', '20xs.com', 'www.haxwx.net',
                    'www.dushiwenxue.com',
                    "www.yxdown.com", 'www.jingcaiyuedu.com', 'www.zhetian.org', 'www.xiaoshuo02.com',
                    'www.xiaoshuo77.com',
                    'www.868xh.com', 'dp.changyou.com', 'www.iyouman.com', 'www.qq717.com', 'www.yznn.com',
                    "www.69w.cc",
                    "www.doupocangqiong1.com", "www.manhuatai.com", "www.5wxs.com", "www.ggshuji.com", "www.msxf.net",
                    "www.mianhuatang.la", "www.boluoxs.com", "www.lbiquge.top", "www.69shu.com", "www.qingkan520.com",
                    "book.douban.com", "movie.douban.com", "www.txshuku.com", "lz.book.sohu.com", "www.3gsc.com.cn",
                    "www.txtshu365.com", "www.517yuedu.com", "www.baike.com", "read.jd.com", "www.zhihu.com",
                    "wshuyi.com",
                    "www.19lou.tw", "www.chenwangbook.com", "www.aqtxt.com", "book.114la.com", "www.niepo.net",
                    "me.qidian.com", "www.gengd.com", "www.77l.com", "www.geilwx.com", "www.97xiao.com", "www.anqu.com",
                    "www.wuxiaxs.com", "yuedu.163.com", "b.faloo.com", "bbs.qidian.com", "jingji.qidian.com",
                    "www.sodu.cc",
                    "forum.qdmm.com", "www.qdmm.com", "game.91.com", "www.11773.com", "mt.sohu.com",
                    "book.dajianet.com",
                    "haokan.17k.com", "www.qmdsj.com", "www.jjwxc.net", "ishare.iask.sina.com.cn", "www.cmread.com",
                    "www.52ranwen.net", "www.dingdianzw.com", "www.topber.com", "www.391k.com", "www.qqxzb.com",
                    "www.zojpw.com", "www.pp8.com", "www.bxwx.org", "www.hrsxb.com", "www.497.com", "www.d8qu.com",
                    "www.duwanjuan.com", "www.05935.com", "book.zongheng.com", "www.55x.cn", "www.freexs.cn",
                    "xiaoshuo.360.cn", "www.3kw.cc", "www.gzbpi.com", "book.sina.com.cn", "www.vodtw.com",
                    "wenda.so.com",
                    "product.dangdang.com", "www.chuiyao.com", "novel.slieny.com", "www.bilibili.com",
                    "donghua.dmzj.com",
                    "www.yaojingweiba.com", "www.qb5200.com", "www.520tingshu.com", "www.567zw.com", "www.zjrxz.com",
                    "v.qq.com", "blog.sina.com.cn", "www.hackhome.com", "news.fznews.com.cn", "www.jingyu.com",
                    "news.so.com", "www.sodu3.com", "vipreader.qidian.com", "www.mozhua9.com", "www.iqiyi.com"]

    LatestRules = namedtuple('LatestRules', 'plan meta_value selector')

    # 获取小说最新章节
    PLAN_01 = LatestRules(
        True,
        {'latest_chapter_name': 'og:novel:latest_chapter_name', 'latest_chapter_url': 'og:novel:latest_chapter_url'},
        None,
    )

    LATEST_RULES = {
        "www.biqugex.com": PLAN_01,
        "www.x23us.com": PLAN_01,
        "www.23us.la": PLAN_01,
        "www.sqsxs.com": PLAN_01,
        "www.nuomi9.com": PLAN_01,
        "www.biquge.info": PLAN_01,
        "www.biquge.tw": PLAN_01,
        "www.qu.la": PLAN_01,
        "www.ybdu.com": PLAN_01,
        "www.wenxuemi.com": PLAN_01,
        "www.biquge.com": PLAN_01,
        "www.23us.cc": PLAN_01,
        "www.xs222.com": PLAN_01,
        "www.lewen8.com": PLAN_01,
        "www.bqg5200.com": PLAN_01,
        "www.vodtw.com": PLAN_01,
        "www.6mao.com": PLAN_01,
        "www.biquge.sh": PLAN_01,
        "www.touxiang.la": PLAN_01,
        "www.bxquge.com": PLAN_01,
        "www.beidouxin.com": PLAN_01,
        "www.biquge.lu": PLAN_01,
        "www.263zw.com": PLAN_01,
        "www.3qzone.com": PLAN_01,
        "wwww.yooread.com": PLAN_01,
        "www.suimeng.la": PLAN_01,
        "www.bequge.com": PLAN_01,
        "www.biquku.co": PLAN_01,
        "www.xbqge.com": PLAN_01,
        "www.aiquxs.com": PLAN_01,
        "www.23us.com": PLAN_01,
        "www.biqiuge.com": PLAN_01,
        "www.ddbiquge.com": PLAN_01,
        "www.abocms.cn": PLAN_01,
        "www.a306.com": PLAN_01,
        "www.liewen.cc": PLAN_01,
        "www.8535.org": PLAN_01,
        "www.dingdianzw.com": PLAN_01,
        "www.biquge.cc": PLAN_01,
        "www.111bz.org": PLAN_01,
        "www.biqugebook.com": PLAN_01,
        "www.e8zw.com": PLAN_01,
        "www.xqqxs.com": PLAN_01,
        "tianyibook.la": PLAN_01,
        "www.lingdianksw.com": PLAN_01,
        "www.qb5.tw": PLAN_01,
        "www.quanben.com": PLAN_01,
        "www.58xs.com": PLAN_01,
        "www.biqukan.com": PLAN_01,
        "www.yssm.org": PLAN_01,
        "www.81zw.com": PLAN_01,
        "www.ymoxuan.com": PLAN_01,
        "www.mytxt.cc": PLAN_01,
        "www.woquge.com": PLAN_01,
        "www.biquguo.com": PLAN_01,
        "www.8jzw.cc": PLAN_01,
        "www.biquge.tv": PLAN_01,
        "www.biquge5200.com": PLAN_01,
        "www.8jzw.com": PLAN_01,
        "www.23xsw.cc": PLAN_01,
        "www.miaobige.com": PLAN_01,
        "www.xs.la": PLAN_01,
        "www.44pq.co": PLAN_01,
        "www.50zw.la": PLAN_01,
        "www.33xs.com": PLAN_01,
        "www.zwdu.com": PLAN_01,
        "www.ttzw.com": PLAN_01,
        "www.zanghaihuatxt.com": PLAN_01,
        "www.kuxiaoshuo.com": PLAN_01,
        "www.biqudu.com": PLAN_01,
        "www.biqugeg.com": PLAN_01,
        "www.23txt.com": PLAN_01,
        "www.baquge.tw": PLAN_01,
        "www.23qb.com": PLAN_01,
        "www.lread.cc": PLAN_01,
        "www.biqudao.com": PLAN_01,
        "www.laidudu.com": PLAN_01,
        "www.kxs7.com": PLAN_01,
        "www.biquguan.com": PLAN_01,
        "www.biquta.com": PLAN_01,
        "www.xs98.com": PLAN_01,
        "www.bqge.org": PLAN_01,
        "www.58xs.tw": PLAN_01,
        "www.187ks.com": PLAN_01,
        "www.yikanxiaoshuo.com": PLAN_01,
        "www.23zw.me": PLAN_01,
        "www.37zw.net": PLAN_01,
        "www.biquge.cm": PLAN_01,
        "www.kanshu58.com": PLAN_01,
        "www.biqumo.com": PLAN_01,
        "www.mpxiaoshuo.com": PLAN_01,
        "www.23wx.cm": PLAN_01,
        "www.biquge.jp": PLAN_01,
        "www.biqugexsw.com": PLAN_01,
        "www.biqu6.com": PLAN_01,
        "www.xiuxs.com": PLAN_01,
        "www.biqule.com": PLAN_01,
        "www.biquzi.com": PLAN_01,
        "www.biquku.la": PLAN_01,
        "www.00ksw.org": PLAN_01,
        "www.bqg.cc": PLAN_01,
        "www.biqugezw.com": PLAN_01,
        "www.bbiquge.com": PLAN_01,
        "www.aikantxt.la": PLAN_01
    }
