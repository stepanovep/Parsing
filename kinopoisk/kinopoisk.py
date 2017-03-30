from urllib import request
from bs4 import BeautifulSoup


def get_html(url):
    response = request.urlopen(url)
    return response

html_raw = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:og="http://opengraphprotocol.org/schema/" dir="ltr" lang="ru-RU" prefix="og: http://ogp.me/ns# video: http://ogp.me/ns/video# ya: http://webmaster.yandex.ru/vocabularies/">
<head profile="http://gmpg.org/xfn/11">
<title>Профиль: enmishka - Списки</title>
<link rel="search" type="application/opensearchdescription+xml" title="Поиск на kinopoisk.ru" href="/kp_search.xml" />
<meta http-equiv="content-type" content="text/html; charset=windows-1251" />
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
<meta property="fb:app_id" content="121953784483000"/>

<meta name="title" content="Профиль: enmishka - Списки" />
<meta name="description" content="Профиль: enmishka - Списки" />
<meta name="og:title" content="Профиль: enmishka - Списки" />
<meta name="og:description" content="Профиль: enmishka - Списки" />


<script type="text/javascript" src="https://yandex.st/jquery/1.9.1/jquery.min.js" charset="utf-8"></script>

<script type="text/javascript">
    function getTrailersDomain() {
        return 'kp.cdn.yandex.net';
    }
    function getStaticsDomain() {
        return 'https://st.kp.yandex.net';
    }
    function getSerpSuggestUrl() {
        return 'https://suggest-kinopoisk.yandex.net/suggest-kinopoisk?srv=kinopoisk';
    }
    function isKUB() {
        return false;
    }
    function getUserLogin() {
        return '';
    }

    window.KP = window.KP || {};
    window.KP.helpers = window.KP.helpers || {};
    window.KP.config  = window.KP.config || {};

    KP.debug = false;
    window.KP.helpers.userIsAuth = function () {
        return false;
    };
    window.KP.helpers.isSocialUser = function () {
        return false;
    };
    window.KP.helpers.getOpenidType = function () {
        return window.KP.helpers.isSocialUser() && "";
    };
    window.KP.helpers.shouldShowBrandingFlash = function () {
        // Exclude Firefox 49.0.0.2
        return !(/^Mozilla\/5\.0\s\(Windows\sNT\s[0-9]\.[0-9]\;\sWOW64\;\srv\:49\.0\)\sGecko\/20100101\sFirefox\/49\.0$/i).test(navigator.userAgent);
    };
    window.KP.METRIKA_COUNTER_ID = '22663942';
    window.KP.FACEBOOK_APP_ID = 121953784483000;
    window.KP.config.adfoxEnabled = Boolean(1);
    window.KP.config.adfoxVideoAdUrls = {"flash":{"preroll":"https:\/\/ads.adfox.ru\/251518\/getCode?pp=g&ps=clfb&p2=foaq&fmt=1","postroll":"https:\/\/ads.adfox.ru\/251518\/getCode?pp=g&ps=clfb&p2=foar&fmt=1"},"html":{"preroll":"https:\/\/ads.adfox.ru\/251518\/getCode?pp=g&ps=clfa&p2=foaq&fmt=1","postroll":"https:\/\/ads.adfox.ru\/251518\/getCode?pp=g&ps=clfa&p2=foar&fmt=1"}};
    window.KP.config.cryEnabled = Boolean(true);
    window.KP.config.hasBranding = Boolean(false);
</script>

<link href="https://st.kp.yandex.net/images/favicon.ico" type="image/x-icon" rel="shortcut icon"/>
<!-- ADDITIONAL FAVICONS -->
<link href="https://st.kp.yandex.net/images/icons/favicon_16x16.png" type="image/png" rel="icon"/>
<link href="/news.rss" type="application/rss+xml" rel="alternate" title="RSS"/>
<link href="https://st.kp.yandex.net/js/style.css?v=f0d4c486049a65c53f4d8c0249eeceb9" type="text/css" rel="stylesheet" media="all"/>
<meta content="width=960" name="viewport" />

<link href="https://st.kp.yandex.net/js/profile.css?v=20131211" type="text/css" rel="stylesheet" media="all" />
<link href="https://st.kp.yandex.net/js/mykp.css?v=20131211" type="text/css" rel="stylesheet" media="all" />
<link href="https://st.kp.yandex.net/js/tab.css?v=20131211" type="text/css" rel="stylesheet" media="all" />

<link href="https://st.kp.yandex.net/js/superbanner_brand.css?v=20131211" type="text/css" rel="stylesheet" media="all" />

<script> var need_buy_button='1'; </script>
<script type="text/javascript" charset="utf-8" src="https://yastatic.net/browser-updater/v1/script.js"></script>
<script type="text/javascript">
$(function(){
    // setTimeout fixes initialization in IE8
    setTimeout(function(){
        new ya.browserUpdater.init({
            'lang':'ru',
            'browsers':{
                'yabrowser':'15.12',
                'chrome':'48',
                'ie':'9',
                'opera':'34',
                'safari':'8',
                'fx':'43',
                'iron':'35',
                'flock':'Infinity',
                'palemoon':'25',
                'camino':'Infinity',
                'maxthon':'4.5',
                'seamonkey':'2.3'
            },
            'theme':'yellow'
        });
    }, 1000);
});
</script>
<script>
    window.Ya = window.Ya || {};
    window.Ya.Kinopoisk = window.Ya.Kinopoisk || {};

    window.Ya.Kinopoisk.basehost = 'plus.kinopoisk.ru';
    window.KPP_FRONT_HOST = 'plus.kinopoisk.ru';
</script>
<script type="text/javascript" src="https://st.kp.yandex.net/js/jquery.other.js?v=20130319-1" charset="utf-8"></script>
<script type="text/javascript" src="https://st.kp.yandex.net/js/jquery-migrate-1.1.1.js?v=20130328"></script>
<script type="text/javascript" src="https://yandex.st/jquery-ui/1.10.2/jquery-ui.min.js" charset="utf-8"></script>
<script src="//yandex.st/swfobject/2.2/swfobject.min.js"></script>
<script type="text/javascript">var xsrftoken = '802250a34dbbf3e82e79a051a66433d9';
    $.ajaxSetup({data: {'token': xsrftoken}});</script>
<script type="text/javascript" src="https://st.kp.yandex.net/js/jquery.cookie.js" charset="utf-8"></script>
<script type="text/javascript" src="https://st.kp.yandex.net/js/jquery.selectBox.min.js"></script>
<script type="text/javascript" src="https://st.kp.yandex.net/js/main.js?v=13240df7598589867afb6658492a8040" charset="utf-8"></script>
<script type="text/javascript" src="https://plus.kinopoisk.ru/cinemaplayer/authapi.js"></script>
<script type="text/javascript" charset="utf-8" src="https://st.kp.yandex.net/js/jquery.autocomplete.js?v=20160118"></script>
<script type="text/javascript" charset="utf-8" src="https://st.kp.yandex.net/js/jquery.autocomplete_express.js?v=20140616"></script>
<script type="text/javascript" charset="utf-8" src="https://st.kp.yandex.net/js/mobile_detector.js?v=20140616"></script>


<script src="https://st.kp.yandex.net/js/votes.js?v=8ef90b561129febf4c5f5cb390369b2f" type="text/javascript"></script><link href="https://st.kp.yandex.net/js/votes.css?20140519" type="text/css" rel="stylesheet" media="all" />
<style>#vnflashplayer {position: relative}</style>
<script type="text/javascript"> var _plg=''; var _version='0'; </script>
<script src="https://yandex.st/awaps-ad-sdk-js/1_0/adsdk.js" charset="utf-8" type="text/javascript"></script>
<script src="https://st.kp.yandex.net/js/kinopoiskPlayer.js?20151011_2" type="text/javascript"></script>
<script src="https://st.kp.yandex.net/js/jquery.popupTrailer.js?v=20150625" type="text/javascript" charset="utf-8"></script>

<script type="text/javascript" src="https://st.kp.yandex.net/js/flap_img.js?v=20130726-01"></script>
<script type="text/javascript" src="https://st.kp.yandex.net/js/reviews.js?v=20131220"></script><script type="text/javascript" src="https://st.kp.yandex.net/js/text2blog_v1.1.js?2"></script>
    <script type="text/javascript" src="https://st.kp.yandex.net/js/amcharts_v2.8.2.js"></script>
    <script type="text/javascript" src="https://st.kp.yandex.net/js/raphael.js"></script>
    <script type="text/javascript" src="https://st.kp.yandex.net/js/KPChart.js?20121202-01"></script>

<link href="https://st.kp.yandex.net/js/devices/chrome.css?v=20130128-01" type="text/css" rel="stylesheet" media="all" />
<script src="https://st.kp.yandex.net/js/mymovies_ajax_guest.js?v=20140217" charset="utf-8"></script>
<link href="https://st.kp.yandex.net/js/mymovies_ajax.css?v=20131211" type="text/css" rel="stylesheet" />
<script type="text/javascript" src="https://st.kp.yandex.net/js/get_count_word.js?v=20101011"></script><script src='https://st.kp.yandex.net/js/up_button.js?20130927-1218' type='text/javascript'></script>
<script src='https://st.kp.yandex.net/js/push.js?20120416-2' type='text/javascript'></script>
<script>pushAvailable = true;</script>

<script>var dbUnavailable = false;</script>
<script type="text/javascript">
    $(document).ready(function () {
        DOCUMENT_LOADED = true;
            });
    var ar_bn1 = Math.floor(Math.random() * 5 + 1);
</script>


<script src="https://yastatic.net/share2/share.js" charset="utf-8" defer></script>

<script type="text/javascript">var abExperiments = [{"experimentName":"selector_control","experimentDescription":"\u041a\u043e\u043d\u0442\u0440\u043e\u043b\u044c\u043d\u044b\u0439 \u044d\u043a\u0441\u043f\u0435\u0440\u0438\u043c\u0435\u043d\u0442: \u0437\u0430\u043c\u0435\u0440\u044f\u0435\u043c \u043f\u043e\u0433\u0440\u0435\u0448\u043d\u043e\u0441\u0442\u044c \u0441\u0435\u043b\u0435\u043a\u0442\u043e\u0440\u0430","metricValue":"default_0","backendValue":"default"},{"experimentName":"superbanners_internal","experimentDescription":"\u0421\u0443\u043f\u0435\u0440\u0431\u0430\u043d\u043d\u0435\u0440\u044b \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430\u0445 \u0444\u0438\u043b\u044c\u043c\u043e\u0432 \u0438 \u043f\u0435\u0440\u0441\u043e\u043d","metricValue":"experiment","backendValue":"experiment"},{"experimentName":"superbanners_trp_internal","experimentDescription":"\u0421\u0443\u043f\u0435\u0440\u0431\u0430\u043d\u043d\u0435\u0440\u044b TRP \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430\u0445 \u0444\u0438\u043b\u044c\u043c\u043e\u0432 \u0438 \u043f\u0435\u0440\u0441\u043e\u043d","metricValue":"default","backendValue":"default"},{"experimentName":"awaps_branding","experimentDescription":"awapsss","metricValue":"experiment_0","backendValue":"experiment_0"},{"experimentName":"editorial_restyle","experimentDescription":"edrestyle","metricValue":"experiment_2","backendValue":"experiment_2"},{"experimentName":"antiadblock_cookie","experimentDescription":"Antiadblock cookie","metricValue":"experiment_0","backendValue":"experiment_0"},{"experimentName":"touch","experimentDescription":"\u0422\u0430\u0447-\u0432\u0435\u0440\u0441\u0438\u044f ","metricValue":"default_0","backendValue":"default"},{"experimentName":"autoplay_smarttv","experimentDescription":"\u0410\u0432\u0442\u043e\u043f\u043b\u0435\u0439 \u0441\u043c\u0430\u0440\u0442 \u0442\u0432","metricValue":"experiment","backendValue":"experiment"},{"experimentName":"iframe_for_main_trailer","experimentDescription":"\u0422\u0440\u0435\u0439\u043b\u0435\u0440 \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435 \u0444\u0438\u043b\u044c\u043c\u0430 \u0432 \u044f.\u0432\u0438\u0434\u0435\u043e iframe","metricValue":"default","backendValue":"default"}];</script>
</head>
<body  onload="" onblur="" onfocus="" onclick="" onmouseover="" onmouseout="">

<!-- android_smartbanner -->
    <!-- fullscreen -->
    <script type="text/javascript">
        if ( typeof( globalseed ) == "undefined") {
            var globalseed = Math.round(Math.random()*65535);
        }
        function CAWBrowser(){
            var haveFlash = [];
            var i;
            for (i=6; i<15; i++ ) haveFlash[i] = false;
            var ua = navigator.userAgent;
            this.msie = (ua && ( parseFloat( navigator.appVersion ) >=4 ) && ( ua.indexOf("Opera") < 0 ) && ( ua.indexOf("MSIE 4") < 0 ) && ( ua.indexOf( "MSIE" ) >=0) );
            this.win = (ua && ((ua.indexOf( "Windows 95" ) >=0) || (ua.indexOf("Windows NT") >=0 ) || (ua.indexOf("Windows 98") >=0) ) );
            this.mac = (navigator.platform && (navigator.platform.indexOf('Mac')!=-1));
            this.opera7 = ((ua.indexOf('Opera') != -1) && window.opera && document.readyState) ? 1 : 0;
            this.gecko = (ua.toLowerCase().indexOf('gecko') != -1) && (ua.indexOf('safari') == -1);
            var flash_nonie = (navigator.mimeTypes && navigator.mimeTypes["application/x-shockwave-flash"]) ? navigator.mimeTypes["application/x-shockwave-flash"].enabledPlugin : 0;
            if( flash_nonie){
                for (i=6; i<15; i++ ){
                    haveFlash[i] = flash_nonie;
                    haveFlash[i] = (parseInt(haveFlash[i].description.substring(haveFlash[i].description.indexOf(".")-2))>=i);
                }
            }else if ( this.msie && this.win && !this.mac){
                for (i=6; i<15; i++ )
                    try {
                        haveFlash[i] = new ActiveXObject("ShockwaveFlash.ShockwaveFlash." + i);
                    } catch (e) {
                    }
            }
            this.other = !( (this.gecko || this.msie) && this.win && !this.mac);
            this.flash = 0;
            for (i=6; i<15; i++ ) if (haveFlash[i]) this.flash = i;
        }
        var aw_br = new CAWBrowser();
        var jssrc = "//awsync.yandex.ru/8/10956/000000.?" + globalseed +
            "-0-" + globalseed + "&swfcode=6&awcode=41&subsection=0&flash=" + aw_br.flash;
        var jssrc_code = '<sc'+'ript src="' + jssrc +'"></sc'+'ript>';
        var no = 'awfs';
        var hasFulscreen = true;
        for (var i = 0, parts = document.cookie.split(';'); i < parts.length; i++) {
            var c = parts[i];
            c = c.split('=')[0];
            c = c.replace(/^(\s|\u00A0)+/g, '');
            if (c.indexOf(no) === 0) {
                hasFulscreen = false;
                break;
            }
        }
        if (aw_br.flash >= 10 && hasFulscreen) {
            var period = 7 * 24 * 60 * 60;
            document.cookie = no + '=1' + ';domain=.kinopoisk.ru;path=/;max-age=' + period;
            document.write(jssrc_code);
        }
    </script>
    <!-- /fullscreen -->





<style type="text/css">
    #promo_player_container { display:none; background: #000; width: 100%; height: 100%; overflow: scroll; position: fixed; top: 0; left: 0; z-index: 2000; }
    #promo_player_container a { background: url(/img/fe/trailers/close_trailer_wh.png); width: 21px; height: 21px; cursor: pointer; position: absolute; top: 10px; right: 10px }
    #promo_player_content { width: 900px; height:600px; margin: 0 auto; z-index: 1400; }
</style>

<div id="promo_player_container">
    <table style="width: 100%; height: 100%; border-collapse: collapse">
        <tr>
            <td style="width: 100%; height: 100%; text-align: center; vertical-align: middle; padding: 0">
                <a class="png" href="#" onclick='ClosePromoPlayer("promo_player"); return false;'></a>
                <div id="promo_player_content"></div>
            </td>
        </tr>
    </table>
</div>

<!-- maybe-deprecated-feature -->
<!-- end of maybe-deprecated-feature -->



<div id="top">
    <div class="hidden">
        <img src="https://awaps.yandex.net/99/c1/txsqeebA2PjMc+djW72uXwRGXvc9FsPea8UDGH7SYwLYwllJeMe-vFD9WAfwD_t-HX62f0MUg3zVz0AZq6nEZaPVow2zMpYHRMylSgUqqBDDaxtAUMX582Dhe3W_tftMXZNh7z2XYSd1gbGQBXlhO2-keR+yVABKKtEOHmC5Onr6sUhwyTFGzzgKq_tohCnAGRFL4YyJ8c81VgQ2885lqhD50hYKI4aBZcF8Nl8SOCJIxVKGUf3QjON_tR9ORWeI2PEJtSxqIps5v20GIVy8wiW5fBiZ2a4dcn40tY8A+TQ00Vcxuwgzr_nLr4FGcI8fcU3X1wHybCEK23qt+paQ9mDWo6cijWOV77MYXKRWc9u_A_.gif" width="1" height="1" alt="">

        <noindex>
	<!-- tns-counter.ru -->
	<script language="JavaScript">

	var TopContentPoint=120;
		var img = new Image();
		img.src = 'https://www.tns-counter.ru/V13a***R>' + document.referrer.replace(/\*/g,'%2a') + '*kinopoisk_ru/ru/CP1251/tmsec=kinopoisk_total/';
	</script>
	<noscript>
		<img src="https://www.tns-counter.ru/V13a****kinopoisk_ru/ru/CP1251/tmsec=kinopoisk_total/" width="1" height="1" alt="" />
	</noscript>
	<!--/ tns-counter.ru -->
   </noindex>
</div>

<script>
    advBlock({type: "branding", name: "branding", enabled: false});
</script>

   <script type="text/javascript">mainMenu('top');</script>
<noscript>
<ul class="menu_noscript">
  <li>
     <span>афиша &amp; тв</span>
     <p><s></s><a href="/afisha/new/">сегодня в кино</a></p>
     <p><s></s><a href="/bilet/">билеты в кино</a></p>
     <p><s></s><a href="/premiere/">график премьер</a></p>
     <p><s></s><a href="/tv/">фильмы на ТВ</a></p>
     <p><s></s><a href="/events/">кинособытия</a></p>
     <p><s></s><a href="/cinemas/">все кинотеатры</a></p>
     <p><s></s><a href="/map/">карта города</a></p>
  </li>
  <li>
     <span>тексты</span>
     <p><s></s><a href="/news/">новости кино</a></p>
     <p><s></s><a href="/blogs/">редакционные блоги</a></p>
     <p><s></s><a href="/reviews/">рецензии пользователей</a></p>
     <p><s></s><a href="/photostory/">репортажи</a></p>
     <p><s></s><a href="/interview/">интервью</a> &amp; <a href="/article/">статьи</a></p>
     <p><s></s><a href="/review/3500/">3500 кинорецензий</a></p>
  </li>
  <li>
     <span>медиа</span>
     <p><s></s><a href="/photos/">фотографии</a></p>
     <p><s></s><a href="/wall/">обои для рабочего стола</a></p>
     <p><s></s><a href="/posters/">постеры</a> &amp; <a href="/flyers/">флаеры</a></p>
     <p><s></s><a href="/video/">трейлеры</a></p>
     <p><s></s><a href="/shows/">программы о кино</a></p>
     <p><s></s><a href="/podcast/">подкасты</a></p>
     <p><s></s><a href="/tracks/">саундтреки</a></p>
  </li>
  <li>
     <span>общение</span>
     <p><s></s><a href="/reviews/">рецензии пользователей</a></p>
     <p><s></s><a href="/social/">звёзды в соцсетях</a></p>
     <p><s></s><a href="https://forum.kinopoisk.ru/">форум на КиноПоиске</a></p>
     <p><s></s><a href="/polls/">опросы</a></p>
     <p><s></s><a href="/feedback/">обратная связь</a></p>
  </li>
  <li>
     <span>рейтинги</span>
     <p><s></s><a href="/votes/">оценки пользователей</a></p>
     <p><s></s><a href="/top/">Top250</a>, <a href="/comingsoon/">самые ожидаемые</a></p>
     <p><s></s><a href="/popular/">популярные фильмы</a> и <a href="/popular/names/">имена</a></p>
     <p><s></s><a href="/top/navigator/">поиск лучших</a> и <a href="/top/lists/">списки</a></p>
     <p><s></s><a href="/recommend/">персональные рекомендации</a></p>
     <p><s></s><a href="/awards/">кинонаграды</a> и <a href="/fame/">аллея славы</a></p>
     <p><s></s><a href="/box/">сборы в России</a>, <a href="/box/usa/">в США</a>, <a href="/box/world/">в мире</a></p>
     <p><s></s><a href="/box/best_usa/">кассовые рекорды</a></p>
  </li>
  <li>
     <span>DVD &amp; Blu-Ray</span>
     <p><s></s><a href="/dvd/">DVD-диски</a>, <a href="/bluray/">Blu-Ray</a></p>
     <p><s></s><a href="/comingsoon/dvd/">скоро на DVD</a>, <a href="/comingsoon/bluray/">на Blu-Ray</a></p>
     <p><s></s><a href="/top/dvd/">рейтинги DVD</a></p>
     <p><s></s><a href="/box/usa/dvd/">продажи DVD в США</a></p>
     <p><s></s><a href="/books/">книги</a>, <a href="/gameshop/">игры</a>, <a href="/tracks/buy/">саундтреки</a></p>
  </li>
  <li class="last">
     <span>играть!</span>
     <p><s></s><a href="/quiz/">розыгрыши призов</a></p>
     <p><s></s><a href="/chance/">случайный фильм</a></p>
     <p><s></s><a href="/oscargame/">угадай победителей Оскара!</a></p>
     <p class="unact"><s></s><a href="/goldenglobegame/">... и Золотого глобуса!</a></p>
     <p><s></s><a href="/oscartote/">Оскар-тотализатор</a></p>
  </li>
</ul>
</noscript>

    <style type="text/css">
    .dark_t {display: none}
    .dark {display:none; background: #000; width: 100%; height: 100%; position: fixed; top: 0; left: 0; z-index: 1000; filter: alpha(opacity=90); opacity: 0.9; -moz-opacity: 0.9; -khtml-opacity: 0.9 }
    .dark_trailer {width: 850px; position: absolute; top: 0; left: 0; z-index: 1400; display:none;}
    .dark_trailer .container {border: 13px #000 solid; position: fixed; top: 70px; left: 50%}
    .dark_trailer .container a {background: url(https://st.kp.yandex.net/images/spec/closeTrailerWhite.png); width: 21px; height: 21px; cursor: pointer; position: absolute; top: -50px; right: -15px}

    .dark_t_branding {display: none}
    .dark_branding {display:none; background: #000; width: 100%; height: 100%; position: fixed; top: 0; left: 0; z-index: 1000; filter: alpha(opacity=90); opacity: 0.9; -moz-opacity: 0.9; -khtml-opacity: 0.9 }
    .dark_trailer_branding {width: 850px; position: absolute; top: 0; left: 0; z-index: 1400; display:none;}
    .dark_trailer_branding .container_branding {border: 13px #000 solid; position: fixed; top: 70px; left: 50%}
    .dark_trailer_branding .container_branding a {background: url(https://st.kp.yandex.net/images/spec/closeTrailerWhite.png); width: 21px; height: 21px; cursor: pointer; position: absolute; top: -50px; right: -15px}






    </style>
    <div class="dark" id='dark_overlay'></div>
    <script>
        if(top.location.hash == '#trailer' || top.location.hash == '#trailer_x2') {
            document.getElementById('dark_overlay').style.display = 'block';
        }
    </script>
    <div class="dark_trailer" id='dark_trailer'>
       <div class="container" id='container'>
       </div>
    </div>






<div class="png_block"></div>


<div class="wrap_form">
    <form data-metrika="no_login" id="top_form" name="searchForm" action="/index.php" method="get">
       <input name="first" type="hidden" value="no">
       <input name="what" id='SearchMode' type="hidden" value="">


          <div class="about">всё о любом фильме:</div>





       <a href='/'><img data-metrika="logo" class="logo" src="https://st.kp.yandex.net/images/logoWhite.png" alt="КиноПоиск &ndash; Все фильмы планеты" title="КиноПоиск &ndash; Все фильмы планеты" /></a>

       <!-- profile_top start -->

          <div class="login"><a data-metrika="login" class="js-external-login-action" href="#/login/">Войти на сайт</a> <span>&bull;</span> <a data-metrika="register" class="js-external-register-action" href="#/login/#new">Регистрация</a></div>
          <div class="why_logout"><a data-metrika="join" href="/docs/join/">зачем?</a></div>

       <!-- profile_top end -->
       <div class="advancedSearch"><a data-metrika="advanced_search" href="/level/7/">расширенный поиск</a> <span>&bull;</span> <a data-metrika="direct_search" href="/level/81/">что ищут?</a></div>
       <div class="formText"><input id="search_input" class="text" type="text" name="kp_query" autocomplete="off" maxlength="256" value="" tabindex="1" /></div>
       <input data-metrika="search" class="searchButton1" type="button" value="" tabindex="2" onclick="if(!!document.getElementById('search_input').value) {document.searchForm.first.value = 'no'; document.searchForm.submit(); sendSearchButtonStat('search');}" />
       <input data-metrika="direct_search" class="searchButton2" type="button" value="" tabindex="3" onclick="if(!!document.getElementById('search_input').value) {document.searchForm.first.value = 'yes'; document.searchForm.submit(); sendSearchButtonStat('direct_search');}" title="перейти к первому результату поиска (Ctrl+Enter)" />
       <div class="mez_rez">
          <!-- top_notices -->


          <!-- /top_notices -->
       </div>
       <div class="casual_link_nav"><a data-metrika="chance" href="/chance/" title="Случайный фильм!"></a></div>
    </form>
</div>
    </div>


<div class="shadow shadow-restyle content">



    <div id="content_block"  style="background-color: #fff; min-height: 600px"  class="contentBlock79">

    <table  style="background-color: #fff; width: 850px; margin: 0 auto" cellpadding="0" cellspacing="0">
    <tr>

<td colspan="3">
<style type="text/css">
.navigator {margin: 19px 0 5px 0 !important}
.navigator_bottom .navigator {margin-top: 12px !important}
.eyeLoader {margin-left:190px !important; background: url("https://st.kp.yandex.net/images/icons/transparent_loader.png") repeat scroll 0 0 transparent !important;}
</style>

<style type="text/css">
#top {margin-bottom: 55px}
.profileInserts span {color: #f60}

</style>

<div class="profileInsertsMenu">
<ul class="list ">
   <li class="menuButton1"><a href="/user/4594998/">Профиль</a></li>

   <li class="off menuButton2"><span>Рецензии</span></li>

   <li class="menuButton3"><a href="/user/4594998/votes/">Оценки</a></li>


   <li class="off menuButton4"><span>Комментарии</span></li>

   <li class="menuButton5"><a href="/user/4594998/friends/">Друзья</a></li>


   <li class="menuButton6"><a href="/user/4594998/movies/">Фильмы</a></li>


   <li class="off menuButton7"><span>Звёзды</span></li>

   <li class="menuButton8 act_white"><span>Списки</span></li>



</ul>
</div>

<!-- мини-профайл человека + статсы -->
<table cellspacing="0" cellpadding="0" width="100%" border="0">
    <tr>
        <td style="padding-top: 10px; padding-left: 20px">
            <!-- мини-профайл человека -->
            <table cellspacing="0" cellpadding="0" width="100%" border="0">
                <tr>
                    <td style="padding-top: 10px" width="46" valign=top><img src="https://st.kp.yandex.net/images/users/sm_4594998-20-236565.jpg" width="46" style="border: 5px solid #ccc"></td>
                    <td width="10"><br /></td>
                    <td valign=top>
                        <p class="profile_name" style="white-space: nowrap">
                            <s></s>
                            <a href="/user/4594998/">enmishka</a> &gt;
                            <a href="/user/4594998/list/vs/">Списки</a>
                            &gt; <span><a href="/user/4594998/list/vs/kinopoisk/">КиноПоиск</a></span>

                            <span style="display: block; padding-top: 13px; white-space: normal">Топ-500</span>

                        </p>
                    </td>
                </tr>
                <tr><td colspan="3" height="10">&nbsp;</td></tr>
            </table>
            <!-- мини-профайл человека /-->
        </td>
    </tr>
    <tr>
        <td colspan="2" valign="top" style="padding: 15px 20px 50px 20px">

<style type="text/css">
#block_right {margin-top:-105px;}
.progressBar {background: #e5e5f0; width: 555px; height: 30px; color: #393946; font-weight: bold; overflow: hidden; position: relative; margin: 20px 0 1px 0}
   .progressBar * {display: block}
   .progressBar b {background: #bfbfea; height: 30px}
   .progressBar i, .progressBar u {position: absolute; top: 8px}
   .progressBar i {font-style: normal; left: 10px}
   .progressBar u {text-decoration: none; right: 10px}
   .progressBar.my {background: #ffe3d1; margin-top: 1px}
   .progressBar.my b {background: #f60}
.rangImp {color: #f60}
.ten_items .gray_text {color: #888; font-family: arial; font-size: 11px; display: block; margin-bottom: 9px}
.ten_items .gray_text i {font-style: normal}
.ten_items .lined {color: #888; text-decoration: none}
.ten_items .lined:hover {text-decoration: underline}
   .ten_items .num {position: absolute; margin-left: -30px; color: #777; width: 30px; text-align: center}
   .ten_items .rangImp {color: #f60}

.rating_bottom {white-space: nowrap; font-size: 10px}
    .rating_bottom * {color: #999 !important}
    .rating_bottom a {text-decoration: underline}
    .rating_bottom span {position: relative}
    .rating_bottom .remove {padding-right: 5px}
    .rating_bottom .loader {background: url(https://st.kp.yandex.net/images/ajax_star.gif); width: 10px; height: 10px; overflow: hidden; display: block; position: absolute; top: 2px; left: 123px}

.eye {cursor: pointer; position: absolute; margin: 16px 0 0 186px}
.eye.alien {cursor: default; background: url(https://st.kp.yandex.net/images/movies/to_friend_lite.png) -20px -76px}
.eye.alien:hover {background-position: -20px -76px; opacity: 1}
.eye.my {margin-top: 46px}
.eye:hover {background-position: -20px -57px; filter: alpha(opacity=50); opacity: 0.5; -moz-opacity: 0.5; -khtml-opacity: 0.5}
.eye_act {background-position: -20px -57px}
.eye_act:hover {background-position: -20px -57px; filter: alpha(opacity=100) !important; opacity: 1 !important; -moz-opacity: 1 !important; -khtml-opacity: 1 !important}
.userVote {background: #bfbfea; width: 23px; height: 19px; color: #fff; text-align: center; position: absolute; margin: 17px 0 0 176px; padding-top: 4px}
.MyKP_Folder_Select {margin-top:53px;}
.userVote {background: #bfbfea; width: 23px; height: 19px; color: #fff; text-align: center; position: absolute; margin: 17px 0 0 186px; padding-top: 4px}
    .userVote p {margin: -1px 0 0 0; color: #fff}
.myVote {background: #f60; width: 23px; height: 19px; color: #fff; text-align: center; position: absolute; margin: 42px 0 0 186px; padding-top: 4px}
    .myVote p {margin: 1px 0 0 0; color: #fff}

.navigator {padding-left: 0; width: 555px}

.ten_items td {border-bottom: 1px #bbb dotted}
.bottom_marg {margin-bottom:7px; display:block;}
.ratingBlockP {background: #5f5f5f; width: 92px; height: 19px; color: #fff; text-align: center; position: absolute; margin: 17px 0 0 2px; padding-top: 4px}
.ratingBlockP a {color:#ffffff !important;}
.ratingBlockP span {font-size:10px !important;}
</style>
<!--[if lte IE 6]>
<style type="text/css">
.films_list div {height: 88px}
</style>
<![endif]-->

<script type="text/javascript">
function isGuest() { return true; }
function noAccess() { return false; }
function showErrors() { return false; }
function getLevel() {return '79list';}

$(function(){
    $('#sb_filtr, #sb_sort').change(function(){
        var $this = $(this);

        if ($this.attr('id') == 'sb_filtr' && ($this.val() == 'v' || $this.val() == 'n')) {
            $this.val('all');
            $.app.notice($.app.notices.authRequired);
            return false;
        }

        $('#f_hidden_filtr')
            .find('input[name="_filtr"]').val($('#sb_filtr').val()).end()
            .find('input[name="_sort"]').val($('#sb_sort').val()).end()
            .submit();
    });
});
</script>

<p style="width: 555px; font-size: 12px; margin: 10px 0 25px 0">Список представляет собой расширенную версию <a style="color: #f60; text-decoration: underline" href="/level/20/" target="_blank">рейтинга лучших фильмов</a> по версии пользователей КиноПоиска.</p>

    <div class="progressBar" title="Прогресс enmishka"><b style="width: 18.6%"></b><i>18.6%</i><u>93 / 500</u></div>



<form name="f_hidden_filtr" id="f_hidden_filtr" action="/index.php" method="get">
<input name="level" type="hidden" value="79" />
<input name="user" type="hidden" value="4594998" />
<input name="list" type="hidden" value="list" />
<input name="lid" type="hidden" value="1" />
<input name="_filtr" type="hidden" value="all" />
<input name="_sort" type="hidden" value="order" />


</form>
<div style="height: 26px; width: 555px; padding-top: 20px">
    <select id="sb_filtr" style="width: 163px; font-family: tahoma, verdana, 'trebuchet ms'; font-size: 12px; float: left; padding: 4px 2px">
        <option value="all" selected="selected">все</option>
        <option value="v">просмотренные</option>
        <option value="n">непросмотренные</option>
        <option value="vu">смотрел (enmishka)</option>
        <option value="nu">не смотрел (enmishka)</option>
    </select>
    <select id="sb_sort" style="width: 171px; font-family: tahoma, verdana, 'trebuchet ms'; font-size: 12px; float: right; padding: 4px 2px">
        <option value="order" selected="selected">порядку</option>
        <option value="year">году</option>
        <option value="name">названию</option>
        <option value="oname">оригинальному названию</option>
        <option value="rating">рейтингу КиноПоиска</option>
        <option value="rating_imdb">рейтингу IMDb</option>
        <option value="votes">количеству оценок</option>
        <option value="my_vote">моей оценке</option>
        <option value="vote">оценке пользователя</option>
    </select>
    <span style="color: #777; font-size: 12px; float: right; display: block; padding: 6px 10px 0 0">сортировать по:</span>
</div>
<!--[if lte IE 7]>
<style type="text/css">
.sortAwaits span {padding-top: 3px !important}
</style>
<![endif]-->

<script type="text/javascript">
self_url = '/user/4594998/list/1/filtr/all/sort/order/';
ancher = '';
</script>
<div class="navigator">


            <div class="show">
                <u>показывать:</u>
                <select class="navigator_per_page">
                    <option value="10">10</option>
                    <option value="25">25</option>
                    <option value="50">50</option>
                    <option value="75">75</option>
                    <option value="100" selected="selected">100</option>
                    <option value="200">200</option>
                </select>
            </div>



        <ul class="list">


                    <li><span>1</span></li>



                    <li ><a href="/user/4594998/list/1/filtr/all/sort/order/page/2/">2</a></li>



                    <li ><a href="/user/4594998/list/1/filtr/all/sort/order/page/3/">3</a></li>



                    <li ><a href="/user/4594998/list/1/filtr/all/sort/order/page/4/">4</a></li>



                    <li class="arr"><a href="/user/4594998/list/1/filtr/all/sort/order/page/2/">&raquo;</a></li>



                    <li class="arr"><a href="/user/4594998/list/1/filtr/all/sort/order/page/5/">&raquo;&raquo;</a></li>


        </ul>

    <div class="pagesFromTo">1&mdash;100 из 500</div>
</div>


<table class="ten_items" style="margin-left: -20px" cellspacing=0 cellpadding=0 width="575" border=0>


<tr id="tr_326" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px; border-top: 1px #bbb dotted">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px; border-top: 1px #bbb dotted">
        <div class="num rangImp">1</div>
        <a class="bottom_marg" href="/film/326/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/326.jpg"  style="border:3px solid #ccc" alt="Побег из Шоушенка (The Shawshank Redemption1994)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px; border-top: 1px #bbb dotted">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/326/" class="all">Побег из Шоушенка</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">The Shawshank Redemption (1994) <nobr>142 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/24262/">Фрэнк Дарабонт</a></i><br />
            (драма, криминал)
        </span>
        <span class="gray_text"><a class="lined" href="/name/7987/">Тим Роббинс</a>, <a class="lined" href="/name/6750/">Морган Фриман</a>, <a class="lined" href="/film/326/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0; border-top: 1px #bbb dotted">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_326" value="9.115"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_326",
                rating:9.115,

                guest:true,

                user_code:'64c07cbaec53a8d2eab203a2eb4673a2',
                filmId:326,
                filmName:'Побег из Шоушенка'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/326/votes/" class="all">9.115 <span>(415&nbsp;602)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">9.197</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 9.30<small style="display: block; margin-top: -1px">1&nbsp;780&nbsp;970</small></div>

        <div title="Оценка enmishka" class="userVote"><p class="all">10</p></div>


        <div id="user_vote_326" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_326"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_326" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_435" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">2</div>
        <a class="bottom_marg" href="/film/435/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/435.jpg"  style="border:3px solid #ccc" alt="Зеленая миля (The Green Mile1999)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/435/" class="all">Зеленая миля</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">The Green Mile (1999) <nobr>189 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/24262/">Фрэнк Дарабонт</a></i><br />
            (фэнтези, драма, криминал...)
        </span>
        <span class="gray_text"><a class="lined" href="/name/9144/">Том Хэнкс</a>, <a class="lined" href="/name/12759/">Дэвид Морс</a>, <a class="lined" href="/film/435/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_435" value="9.066"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_435",
                rating:9.066,

                guest:true,

                user_code:'02dfc1325e83ef7b3035bde8272bc67b',
                filmId:435,
                filmName:'Зеленая миля'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/435/votes/" class="all">9.066 <span>(396&nbsp;096)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">9.149</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.50<small style="display: block; margin-top: -1px">835&nbsp;935</small></div>

        <div title="Оценка enmishka" class="userVote"><p class="all">10</p></div>


        <div id="user_vote_435" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_435"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_435" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_448" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">3</div>
        <a class="bottom_marg" href="/film/448/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/448.jpg"  style="border:3px solid #ccc" alt="Форрест Гамп (Forrest Gump1994)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/448/" class="all">Форрест Гамп</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Forrest Gump (1994) <nobr>142 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/2435/">Роберт Земекис</a></i><br />
            (драма, комедия)
        </span>
        <span class="gray_text"><a class="lined" href="/name/9144/">Том Хэнкс</a>, <a class="lined" href="/name/8887/">Робин Райт</a>, <a class="lined" href="/film/448/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_448" value="8.924"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_448",
                rating:8.924,

                guest:true,

                user_code:'c8cb3f52b127e29a4c9e5477579cc5c8',
                filmId:448,
                filmName:'Форрест Гамп'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/448/votes/" class="all">8.924 <span>(389&nbsp;342)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">9.002</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.80<small style="display: block; margin-top: -1px">1&nbsp;339&nbsp;234</small></div>

        <div title="Оценка enmishka" class="userVote"><p class="all">7</p></div>


        <div id="user_vote_448" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_448"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_448" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_329" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">4</div>
        <a class="bottom_marg" href="/film/329/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/329.jpg"  style="border:3px solid #ccc" alt="Список Шиндлера (Schindler's List1993)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/329/" class="all">Список Шиндлера</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Schindler's List (1993) <nobr>195 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/22260/">Стивен Спилберг</a></i><br />
            (драма, биография, история)
        </span>
        <span class="gray_text"><a class="lined" href="/name/6534/">Лиам Нисон</a>, <a class="lined" href="/name/6846/">Бен Кингсли</a>, <a class="lined" href="/film/329/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_329" value="8.816"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_329",
                rating:8.816,

                guest:true,

                user_code:'c85de4ccc99c39fb7a763e4f1b444511',
                filmId:329,
                filmName:'Список Шиндлера'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/329/votes/" class="all">8.816 <span>(208&nbsp;301)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.895</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.90<small style="display: block; margin-top: -1px">911&nbsp;699</small></div>



        <div id="user_vote_329" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_329"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_329" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_535341" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">5</div>
        <a class="bottom_marg" href="/film/535341/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/535341.jpg"  style="border:3px solid #ccc" alt="1+1 (Intouchables2011)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag8"><a href="/lists/m_act%5Bcountry%5D/8/" title="Франция"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/535341/" class="all">1+1</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Intouchables (2011) <nobr>112 мин.</nobr></span></div>
        <span class="gray_text">
            Франция,
            <i>реж. <a class="lined" href="/name/382906/">Оливье Накаш</a>...</i><br />
            (драма, комедия, биография)
        </span>
        <span class="gray_text"><a class="lined" href="/name/71427/">Франсуа Клюзе</a>, <a class="lined" href="/name/41644/">Омар Си</a>, <a class="lined" href="/film/535341/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_535341" value="8.816"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_535341",
                rating:8.816,

                guest:true,

                user_code:'b0ee7840ea4fb4b2c7962c9bb9a292bb',
                filmId:535341,
                filmName:'1+1'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/535341/votes/" class="all">8.816 <span>(402&nbsp;787)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.868</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.60<small style="display: block; margin-top: -1px">546&nbsp;876</small></div>

        <div title="Оценка enmishka" class="userVote"><p class="all">10</p></div>


        <div id="user_vote_535341" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_535341"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_535341" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_447301" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">6</div>
        <a class="bottom_marg" href="/film/447301/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/447301.jpg"  style="border:3px solid #ccc" alt="Начало (Inception2010)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div><div style="float: left; margin: 0 2px 5px 0" class="flag flag11"><a href="/lists/m_act%5Bcountry%5D/11/" title="Великобритания"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/447301/" class="all">Начало</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Inception (2010) <nobr>148 мин.</nobr></span></div>
        <span class="gray_text">
            США...
            <i>реж. <a class="lined" href="/name/41477/">Кристофер Нолан</a></i><br />
            (фантастика, боевик, триллер...)
        </span>
        <span class="gray_text"><a class="lined" href="/name/37859/">Леонардо ДиКаприо</a>, <a class="lined" href="/name/9867/">Джозеф Гордон-Левитт</a>, <a class="lined" href="/film/447301/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_447301" value="8.665"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_447301",
                rating:8.665,

                guest:true,

                user_code:'aa6eaafb7ccd5ccf89ad4337a6e7a6ad',
                filmId:447301,
                filmName:'Начало'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/447301/votes/" class="all">8.665 <span>(441&nbsp;773)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.768</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.80<small style="display: block; margin-top: -1px">1&nbsp;563&nbsp;513</small></div>



        <div id="user_vote_447301" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_447301"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_447301" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_2360" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">7</div>
        <a class="bottom_marg" href="/film/2360/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/2360.jpg"  style="border:3px solid #ccc" alt="Король Лев (The Lion King1994)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/2360/" class="all">Король Лев</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">The Lion King (1994) <nobr>88 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/7313/">Роджер Аллерс</a>...</i><br />
            (мультфильм, мюзикл, драма...)
        </span>
        <span class="gray_text"><a class="lined" href="/name/10968/">Мэттью Бродерик</a>, <a class="lined" href="/name/33061/">Джереми Айронс</a>, <a class="lined" href="/film/2360/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_2360" value="8.781"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_2360",
                rating:8.781,

                guest:true,

                user_code:'d5235bfb809e0647aaf6e8088ae9460c',
                filmId:2360,
                filmName:'Король Лев'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/2360/votes/" class="all">8.781 <span>(271&nbsp;892)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.768</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.50<small style="display: block; margin-top: -1px">685&nbsp;548</small></div>

        <div title="Оценка enmishka" class="userVote"><p class="all">8</p></div>


        <div id="user_vote_2360" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_2360"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_2360" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_389" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">8</div>
        <a class="bottom_marg" href="/film/389/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/389.jpg"  style="border:3px solid #ccc" alt="Леон (L&#233;on1994)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag8"><a href="/lists/m_act%5Bcountry%5D/8/" title="Франция"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/389/" class="all">Леон</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">L&#233;on (1994) <nobr>133 мин.</nobr></span></div>
        <span class="gray_text">
            Франция,
            <i>реж. <a class="lined" href="/name/24505/">Люк Бессон</a></i><br />
            (триллер, драма, криминал)
        </span>
        <span class="gray_text"><a class="lined" href="/name/11505/">Жан Рено</a>, <a class="lined" href="/name/6650/">Гари Олдман</a>, <a class="lined" href="/film/389/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_389" value="8.686"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_389",
                rating:8.686,

                guest:true,

                user_code:'49b727336ec5af0d8f9213eff5cbfa81',
                filmId:389,
                filmName:'Леон'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/389/votes/" class="all">8.686 <span>(323&nbsp;622)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.764</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.60<small style="display: block; margin-top: -1px">760&nbsp;781</small></div>



        <div id="user_vote_389" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_389"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_389" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_361" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">9</div>
        <a class="bottom_marg" href="/film/361/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/361.jpg"  style="border:3px solid #ccc" alt="Бойцовский клуб (Fight Club1999)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div><div style="float: left; margin: 0 2px 5px 0" class="flag flag3"><a href="/lists/m_act%5Bcountry%5D/3/" title="Германия"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/361/" class="all">Бойцовский клуб</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Fight Club (1999) <nobr>131 мин.</nobr></span></div>
        <span class="gray_text">
            США...
            <i>реж. <a class="lined" href="/name/2944/">Дэвид Финчер</a></i><br />
            (триллер, драма, криминал)
        </span>
        <span class="gray_text"><a class="lined" href="/name/25774/">Эдвард Нортон</a>, <a class="lined" href="/name/25584/">Брэд Питт</a>, <a class="lined" href="/film/361/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_361" value="8.659"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_361",
                rating:8.659,

                guest:true,

                user_code:'3cc17b24d9143c3aaf923d9b3b5f595d',
                filmId:361,
                filmName:'Бойцовский клуб'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/361/votes/" class="all">8.659 <span>(377&nbsp;361)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.701</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.80<small style="display: block; margin-top: -1px">1&nbsp;432&nbsp;951</small></div>



        <div id="user_vote_361" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_361"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_361" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_381" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">10</div>
        <a class="bottom_marg" href="/film/381/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/381.jpg"  style="border:3px solid #ccc" alt="Жизнь прекрасна (La vita &#232; bella1997)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag14"><a href="/lists/m_act%5Bcountry%5D/14/" title="Италия"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/381/" class="all">Жизнь прекрасна</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">La vita &#232; bella (1997) <nobr>116 мин.</nobr></span></div>
        <span class="gray_text">
            Италия,
            <i>реж. <a class="lined" href="/name/38057/">Роберто Бениньи</a></i><br />
            (драма, мелодрама, комедия...)
        </span>
        <span class="gray_text"><a class="lined" href="/name/38057/">Роберто Бениньи</a>, <a class="lined" href="/name/38060/">Николетта Браски</a>, <a class="lined" href="/film/381/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_381" value="8.625"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_381",
                rating:8.625,

                guest:true,

                user_code:'5655e1b2b5c823162952e0916229c81d',
                filmId:381,
                filmName:'Жизнь прекрасна'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/381/votes/" class="all">8.625 <span>(131&nbsp;911)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.693</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.60<small style="display: block; margin-top: -1px">444&nbsp;718</small></div>

        <div class="eye eye_act alien" title="Просмотр enmishka"></div>


        <div id="user_vote_381" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_381"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_381" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_42664" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">11</div>
        <a class="bottom_marg" href="/film/42664/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/42664.jpg"  style="border:3px solid #ccc" alt="Иван Васильевич меняет профессию (1973)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag13"><a href="/lists/m_act%5Bcountry%5D/13/" title="СССР"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/42664/" class="all">Иван Васильевич меняет профессию</a><span style="color: #888; font-family: arial; font-size: 11px; display: block"> (1973) <nobr>88 мин.</nobr></span></div>
        <span class="gray_text">
            СССР,
            <i>реж. <a class="lined" href="/name/191587/">Леонид Гайдай</a></i><br />
            (фантастика, комедия, приключения)
        </span>
        <span class="gray_text"><a class="lined" href="/name/284624/">Александр Демьяненко</a>, <a class="lined" href="/name/25269/">Юрий Яковлев</a>, <a class="lined" href="/film/42664/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_42664" value="8.789"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_42664",
                rating:8.789,

                guest:true,

                user_code:'b5c80c1e71e2efa844927610aa433b11',
                filmId:42664,
                filmName:'Иван Васильевич меняет профессию'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/42664/votes/" class="all">8.789 <span>(295&nbsp;022)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.691</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.50<small style="display: block; margin-top: -1px">10&nbsp;873</small></div>

        <div title="Оценка enmishka" class="userVote"><p class="all">8</p></div>


        <div id="user_vote_42664" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_42664"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_42664" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_32898" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">12</div>
        <a class="bottom_marg" href="/film/32898/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/32898.jpg"  style="border:3px solid #ccc" alt="Достучаться до небес (Knockin' on Heaven's Door1997)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag3"><a href="/lists/m_act%5Bcountry%5D/3/" title="Германия"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/32898/" class="all">Достучаться до небес</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Knockin' on Heaven's Door (1997) <nobr>87 мин.</nobr></span></div>
        <span class="gray_text">
            Германия,
            <i>реж. <a class="lined" href="/name/83086/">Томас Ян</a></i><br />
            (драма, комедия, криминал)
        </span>
        <span class="gray_text"><a class="lined" href="/name/26503/">Тиль Швайгер</a>, <a class="lined" href="/name/83087/">Ян Йозеф Лиферс</a>, <a class="lined" href="/film/32898/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_32898" value="8.636"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_32898",
                rating:8.636,

                guest:true,

                user_code:'29ff8a34a3e485e2a1812247a72f5b58',
                filmId:32898,
                filmName:'Достучаться до небес'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/32898/votes/" class="all">8.636 <span>(310&nbsp;130)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.645</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.00<small style="display: block; margin-top: -1px">21&nbsp;467</small></div>



        <div id="user_vote_32898" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_32898"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_32898" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_325" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">13</div>
        <a class="bottom_marg" href="/film/325/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/325.jpg"  style="border:3px solid #ccc" alt="Крестный отец (The Godfather1972)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/325/" class="all">Крестный отец</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">The Godfather (1972) <nobr>175 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/12665/">Фрэнсис Форд Коппола</a></i><br />
            (драма, криминал)
        </span>
        <span class="gray_text"><a class="lined" href="/name/33037/">Марлон Брандо</a>, <a class="lined" href="/name/26240/">Аль Пачино</a>, <a class="lined" href="/film/325/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_325" value="8.737"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_325",
                rating:8.737,

                guest:true,

                user_code:'122033946c70a95f63dee1d120db4ec8',
                filmId:325,
                filmName:'Крестный отец'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/325/votes/" class="all">8.737 <span>(180&nbsp;694)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.641</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 9.20<small style="display: block; margin-top: -1px">1&nbsp;214&nbsp;093</small></div>



        <div id="user_vote_325" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_325"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_325" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_195334" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">14</div>
        <a class="bottom_marg" href="/film/195334/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/195334.jpg"  style="border:3px solid #ccc" alt="Престиж (The Prestige2006)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div><div style="float: left; margin: 0 2px 5px 0" class="flag flag11"><a href="/lists/m_act%5Bcountry%5D/11/" title="Великобритания"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/195334/" class="all">Престиж</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">The Prestige (2006) <nobr>125 мин.</nobr></span></div>
        <span class="gray_text">
            США...
            <i>реж. <a class="lined" href="/name/41477/">Кристофер Нолан</a></i><br />
            (фантастика, триллер, драма...)
        </span>
        <span class="gray_text"><a class="lined" href="/name/8213/">Хью Джекман</a>, <a class="lined" href="/name/21495/">Кристиан Бэйл</a>, <a class="lined" href="/film/195334/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_195334" value="8.529"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_195334",
                rating:8.529,

                guest:true,

                user_code:'c06d7d4576cd125280e2649cfcc1e1d7',
                filmId:195334,
                filmName:'Престиж'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/195334/votes/" class="all">8.529 <span>(343&nbsp;230)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.622</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.50<small style="display: block; margin-top: -1px">863&nbsp;264</small></div>

        <div title="Оценка enmishka" class="userVote"><p class="all">9</p></div>


        <div id="user_vote_195334" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_195334"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_195334" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_530" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">15</div>
        <a class="bottom_marg" href="/film/530/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/530.jpg"  style="border:3px solid #ccc" alt="Игры разума (A Beautiful Mind2001)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/530/" class="all">Игры разума</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">A Beautiful Mind (2001) <nobr>135 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/8919/">Рон Ховард</a></i><br />
            (драма, биография)
        </span>
        <span class="gray_text"><a class="lined" href="/name/10019/">Рассел Кроу</a>, <a class="lined" href="/name/7888/">Эд Харрис</a>, <a class="lined" href="/film/530/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_530" value="8.562"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_530",
                rating:8.562,

                guest:true,

                user_code:'907a14e41a70b8630328a023f09b4d6f',
                filmId:530,
                filmName:'Игры разума'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/530/votes/" class="all">8.562 <span>(285&nbsp;163)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.622</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.20<small style="display: block; margin-top: -1px">648&nbsp;293</small></div>

        <div title="Оценка enmishka" class="userVote"><p class="all">10</p></div>


        <div id="user_vote_530" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_530"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_530" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_258687" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">16</div>
        <a class="bottom_marg" href="/film/258687/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/258687.jpg"  style="border:3px solid #ccc" alt="Интерстеллар (Interstellar2014)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div><div style="float: left; margin: 0 2px 5px 0" class="flag flag11"><a href="/lists/m_act%5Bcountry%5D/11/" title="Великобритания"></a></div><div style="float: left; margin: 0 2px 5px 0" class="flag flag6"><a href="/lists/m_act%5Bcountry%5D/6/" title="Канада"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/258687/" class="all">Интерстеллар</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Interstellar (2014) <nobr>169 мин.</nobr></span></div>
        <span class="gray_text">
            США...
            <i>реж. <a class="lined" href="/name/41477/">Кристофер Нолан</a></i><br />
            (фантастика, драма, приключения)
        </span>
        <span class="gray_text"><a class="lined" href="/name/797/">Мэттью МакКонахи</a>, <a class="lined" href="/name/38703/">Энн Хэтэуэй</a>, <a class="lined" href="/film/258687/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_258687" value="8.583"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_258687",
                rating:8.583,

                guest:true,

                user_code:'bd9ff5ff65e88b364c620042e49bc613',
                filmId:258687,
                filmName:'Интерстеллар'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/258687/votes/" class="all">8.583 <span>(329&nbsp;657)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.615</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.60<small style="display: block; margin-top: -1px">1&nbsp;015&nbsp;833</small></div>

        <div title="Оценка enmishka" class="userVote"><p class="all">8</p></div>


        <div id="user_vote_258687" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_258687"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_258687" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_342" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">17</div>
        <a class="bottom_marg" href="/film/342/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/342.jpg"  style="border:3px solid #ccc" alt="Криминальное чтиво (Pulp Fiction1994)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/342/" class="all">Криминальное чтиво</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Pulp Fiction (1994) <nobr>154 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/7640/">Квентин Тарантино</a></i><br />
            (триллер, комедия, криминал)
        </span>
        <span class="gray_text"><a class="lined" href="/name/6479/">Джон Траволта</a>, <a class="lined" href="/name/7164/">Сэмюэл Л. Джексон</a>, <a class="lined" href="/film/342/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_342" value="8.624"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_342",
                rating:8.624,

                guest:true,

                user_code:'a5c129f728a5211e7550cbb402c04754',
                filmId:342,
                filmName:'Криминальное чтиво'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/342/votes/" class="all">8.624 <span>(273&nbsp;212)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.615</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.90<small style="display: block; margin-top: -1px">1&nbsp;398&nbsp;472</small></div>



        <div id="user_vote_342" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_342"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_342" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_42782" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">18</div>
        <a class="bottom_marg" href="/film/42782/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/42782.jpg"  style="border:3px solid #ccc" alt="Операция «Ы» и другие приключения Шурика (1965)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag13"><a href="/lists/m_act%5Bcountry%5D/13/" title="СССР"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/42782/" class="all">Операция «Ы» и другие приключения Шурика</a><span style="color: #888; font-family: arial; font-size: 11px; display: block"> (1965) <nobr>95 мин.</nobr></span></div>
        <span class="gray_text">
            СССР,
            <i>реж. <a class="lined" href="/name/191587/">Леонид Гайдай</a></i><br />
            (мелодрама, комедия, криминал)
        </span>
        <span class="gray_text"><a class="lined" href="/name/284624/">Александр Демьяненко</a>, <a class="lined" href="/name/307598/">Наталья Селезнёва</a>, <a class="lined" href="/film/42782/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_42782" value="8.719"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_42782",
                rating:8.719,

                guest:true,

                user_code:'eb8854b6692f6e1970f71340d894fd7f',
                filmId:42782,
                filmName:'Операция «Ы» и другие приключения Шурика'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/42782/votes/" class="all">8.719 <span>(260&nbsp;169)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.610</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.70<small style="display: block; margin-top: -1px">8&nbsp;277</small></div>

        <div title="Оценка enmishka" class="userVote"><p class="all">9</p></div>


        <div id="user_vote_42782" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_42782"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_42782" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_3498" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">19</div>
        <a class="bottom_marg" href="/film/3498/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/3498.jpg"  style="border:3px solid #ccc" alt="Властелин колец: Возвращение Короля (The Lord of the Rings: The Return of the King2003)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div><div style="float: left; margin: 0 2px 5px 0" class="flag flag35"><a href="/lists/m_act%5Bcountry%5D/35/" title="Новая Зеландия"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/3498/" class="all">Властелин колец: Возвращение Короля</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">The Lord of the Rings: The Return of the King (2003) <nobr>201 мин.</nobr></span></div>
        <span class="gray_text">
            США...
            <i>реж. <a class="lined" href="/name/32383/">Питер Джексон</a></i><br />
            (фэнтези, драма, приключения)
        </span>
        <span class="gray_text"><a class="lined" href="/name/20287/">Элайджа Вуд</a>, <a class="lined" href="/name/10779/">Вигго Мортенсен</a>, <a class="lined" href="/film/3498/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_3498" value="8.611"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_3498",
                rating:8.611,

                guest:true,

                user_code:'c9d674e0ceb99eee530603274bb57628',
                filmId:3498,
                filmName:'Властелин колец: Возвращение Короля'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/3498/votes/" class="all">8.611 <span>(281&nbsp;183)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.594</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.90<small style="display: block; margin-top: -1px">1&nbsp;283&nbsp;786</small></div>

        <div title="Оценка enmishka" class="userVote"><p class="all">10</p></div>


        <div id="user_vote_3498" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_3498"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_3498" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_474" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">20</div>
        <a class="bottom_marg" href="/film/474/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/474.jpg"  style="border:3px solid #ccc" alt="Гладиатор (Gladiator2000)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div><div style="float: left; margin: 0 2px 5px 0" class="flag flag11"><a href="/lists/m_act%5Bcountry%5D/11/" title="Великобритания"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/474/" class="all">Гладиатор</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Gladiator (2000) <nobr>155 мин.</nobr></span></div>
        <span class="gray_text">
            США...
            <i>реж. <a class="lined" href="/name/10015/">Ридли Скотт</a></i><br />
            (боевик, драма, приключения)
        </span>
        <span class="gray_text"><a class="lined" href="/name/10019/">Рассел Кроу</a>, <a class="lined" href="/name/10020/">Хоакин Феникс</a>, <a class="lined" href="/film/474/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_474" value="8.593"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_474",
                rating:8.593,

                guest:true,

                user_code:'c68d43b2e8f4853cbd18df29683c0517',
                filmId:474,
                filmName:'Гладиатор'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/474/votes/" class="all">8.593 <span>(262&nbsp;813)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.585</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.50<small style="display: block; margin-top: -1px">997&nbsp;940</small></div>

        <div title="Оценка enmishka" class="userVote"><p class="all">10</p></div>


        <div id="user_vote_474" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_474"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_474" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_476" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">21</div>
        <a class="bottom_marg" href="/film/476/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/476.jpg"  style="border:3px solid #ccc" alt="Назад в будущее (Back to the Future1985)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/476/" class="all">Назад в будущее</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Back to the Future (1985) <nobr>116 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/2435/">Роберт Земекис</a></i><br />
            (фантастика, комедия, приключения)
        </span>
        <span class="gray_text"><a class="lined" href="/name/181/">Майкл Дж. Фокс</a>, <a class="lined" href="/name/3514/">Кристофер Ллойд</a>, <a class="lined" href="/film/476/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_476" value="8.626"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_476",
                rating:8.626,

                guest:true,

                user_code:'687faf7482bffcd2761b5111c1f6ef1a',
                filmId:476,
                filmName:'Назад в будущее'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/476/votes/" class="all">8.626 <span>(276&nbsp;985)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.556</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.50<small style="display: block; margin-top: -1px">779&nbsp;936</small></div>



        <div id="user_vote_476" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_476"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_476" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_522" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">22</div>
        <a class="bottom_marg" href="/film/522/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/522.jpg"  style="border:3px solid #ccc" alt="Карты, деньги, два ствола (Lock, Stock and Two Smoking Barrels1998)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag11"><a href="/lists/m_act%5Bcountry%5D/11/" title="Великобритания"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/522/" class="all">Карты, деньги, два ствола</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Lock, Stock and Two Smoking Barrels (1998) <nobr>107 мин.</nobr></span></div>
        <span class="gray_text">
            Великобритания,
            <i>реж. <a class="lined" href="/name/45159/">Гай Ричи</a></i><br />
            (комедия, криминал)
        </span>
        <span class="gray_text"><a class="lined" href="/name/1514/">Джейсон Стэйтем</a>, <a class="lined" href="/name/4542/">Ник Моран</a>, <a class="lined" href="/film/522/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_522" value="8.543"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_522",
                rating:8.543,

                guest:true,

                user_code:'c1f1c5e7be5042c52187aa021282e11b',
                filmId:522,
                filmName:'Карты, деньги, два ствола'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/522/votes/" class="all">8.543 <span>(239&nbsp;716)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.544</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.20<small style="display: block; margin-top: -1px">435&nbsp;065</small></div>



        <div id="user_vote_522" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_522"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_522" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_355" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">23</div>
        <a class="bottom_marg" href="/film/355/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/355.jpg"  style="border:3px solid #ccc" alt="Пианист (The Pianist2002)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag32"><a href="/lists/m_act%5Bcountry%5D/32/" title="Польша"></a></div><div style="float: left; margin: 0 2px 5px 0" class="flag flag8"><a href="/lists/m_act%5Bcountry%5D/8/" title="Франция"></a></div><div style="float: left; margin: 0 2px 5px 0" class="flag flag11"><a href="/lists/m_act%5Bcountry%5D/11/" title="Великобритания"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/355/" class="all">Пианист</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">The Pianist (2002) <nobr>149 мин.</nobr></span></div>
        <span class="gray_text">
            Польша...
            <i>реж. <a class="lined" href="/name/16563/">Роман Полански</a></i><br />
            (драма, военный, биография)
        </span>
        <span class="gray_text"><a class="lined" href="/name/2523/">Эдриан Броуди</a>, <a class="lined" href="/name/38080/">Эмилия Фокс</a>, <a class="lined" href="/film/355/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_355" value="8.481"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_355",
                rating:8.481,

                guest:true,

                user_code:'b9dec53eee166584e0c0187387aab4d2',
                filmId:355,
                filmName:'Пианист'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/355/votes/" class="all">8.481 <span>(164&nbsp;685)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.534</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.50<small style="display: block; margin-top: -1px">508&nbsp;559</small></div>



        <div id="user_vote_355" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_355"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_355" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_324" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">24</div>
        <a class="bottom_marg" href="/film/324/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/324.jpg"  style="border:3px solid #ccc" alt="Поймай меня, если сможешь (Catch Me If You Can2002)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div><div style="float: left; margin: 0 2px 5px 0" class="flag flag6"><a href="/lists/m_act%5Bcountry%5D/6/" title="Канада"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/324/" class="all">Поймай меня, если сможешь</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Catch Me If You Can (2002) <nobr>141 мин.</nobr></span></div>
        <span class="gray_text">
            США...
            <i>реж. <a class="lined" href="/name/22260/">Стивен Спилберг</a></i><br />
            (драма, криминал, биография)
        </span>
        <span class="gray_text"><a class="lined" href="/name/37859/">Леонардо ДиКаприо</a>, <a class="lined" href="/name/9144/">Том Хэнкс</a>, <a class="lined" href="/film/324/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_324" value="8.522"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_324",
                rating:8.522,

                guest:true,

                user_code:'0aa42a779c3978a360086a26d76720bf',
                filmId:324,
                filmName:'Поймай меня, если сможешь'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/324/votes/" class="all">8.522 <span>(274&nbsp;288)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.530</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.00<small style="display: block; margin-top: -1px">575&nbsp;453</small></div>



        <div id="user_vote_324" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_324"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_324" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_25108" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">25</div>
        <a class="bottom_marg" href="/film/25108/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/25108.jpg"  style="border:3px solid #ccc" alt="В бой идут одни «старики» (1973)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag13"><a href="/lists/m_act%5Bcountry%5D/13/" title="СССР"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/25108/" class="all">В бой идут одни «старики»</a><span style="color: #888; font-family: arial; font-size: 11px; display: block"> (1973) <nobr>87 мин.</nobr></span></div>
        <span class="gray_text">
            СССР,
            <i>реж. <a class="lined" href="/name/327321/">Леонид Быков</a></i><br />
            (драма, комедия, военный)
        </span>
        <span class="gray_text"><a class="lined" href="/name/327321/">Леонид Быков</a>, <a class="lined" href="/name/287651/">Сергей Подгорный</a>, <a class="lined" href="/film/25108/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_25108" value="8.712"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_25108",
                rating:8.712,

                guest:true,

                user_code:'d41300e27df8f57ecb449a0182cd7660',
                filmId:25108,
                filmName:'В бой идут одни «старики»'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/25108/votes/" class="all">8.712 <span>(126&nbsp;815)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.515</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.60<small style="display: block; margin-top: -1px">2&nbsp;989</small></div>



        <div id="user_vote_25108" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_25108"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_25108" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_328" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">26</div>
        <a class="bottom_marg" href="/film/328/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/328.jpg"  style="border:3px solid #ccc" alt="Властелин колец: Братство кольца (The Lord of the Rings: The Fellowship of the Ring2001)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div><div style="float: left; margin: 0 2px 5px 0" class="flag flag35"><a href="/lists/m_act%5Bcountry%5D/35/" title="Новая Зеландия"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/328/" class="all">Властелин колец: Братство кольца</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">The Lord of the Rings: The Fellowship of the Ring (2001) <nobr>178 мин.</nobr></span></div>
        <span class="gray_text">
            США...
            <i>реж. <a class="lined" href="/name/32383/">Питер Джексон</a></i><br />
            (фэнтези, драма, приключения)
        </span>
        <span class="gray_text"><a class="lined" href="/name/20287/">Элайджа Вуд</a>, <a class="lined" href="/name/8215/">Иэн МакКеллен</a>, <a class="lined" href="/film/328/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_328" value="8.558"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_328",
                rating:8.558,

                guest:true,

                user_code:'4f6e15c6e372b06d9e4e67f8a7820a19',
                filmId:328,
                filmName:'Властелин колец: Братство кольца'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/328/votes/" class="all">8.558 <span>(276&nbsp;633)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.511</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.80<small style="display: block; margin-top: -1px">1&nbsp;305&nbsp;404</small></div>

        <div title="Оценка enmishka" class="userVote"><p class="all">10</p></div>


        <div id="user_vote_328" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_328"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_328" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_81314" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">27</div>
        <a class="bottom_marg" href="/film/81314/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/81314.jpg"  style="border:3px solid #ccc" alt="Отступники (The Departed2006)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div><div style="float: left; margin: 0 2px 5px 0" class="flag flag28"><a href="/lists/m_act%5Bcountry%5D/28/" title="Гонконг"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/81314/" class="all">Отступники</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">The Departed (2006) <nobr>151 мин.</nobr></span></div>
        <span class="gray_text">
            США...
            <i>реж. <a class="lined" href="/name/10988/">Мартин Скорсезе</a></i><br />
            (триллер, драма, криминал)
        </span>
        <span class="gray_text"><a class="lined" href="/name/37859/">Леонардо ДиКаприо</a>, <a class="lined" href="/name/6458/">Мэтт Дэймон</a>, <a class="lined" href="/film/81314/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_81314" value="8.461"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_81314",
                rating:8.461,

                guest:true,

                user_code:'a6448c6612667a14b1ba7f92ac2a7ac2',
                filmId:81314,
                filmName:'Отступники'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/81314/votes/" class="all">8.461 <span>(256&nbsp;957)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.510</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.50<small style="display: block; margin-top: -1px">915&nbsp;753</small></div>



        <div id="user_vote_81314" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_81314"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_81314" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_46225" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">28</div>
        <a class="bottom_marg" href="/film/46225/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/46225.jpg"  style="border:3px solid #ccc" alt="Бриллиантовая рука (1968)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag13"><a href="/lists/m_act%5Bcountry%5D/13/" title="СССР"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/46225/" class="all">Бриллиантовая рука</a><span style="color: #888; font-family: arial; font-size: 11px; display: block"> (1968) <nobr>94 мин.</nobr></span></div>
        <span class="gray_text">
            СССР,
            <i>реж. <a class="lined" href="/name/191587/">Леонид Гайдай</a></i><br />
            (комедия, криминал, приключения...)
        </span>
        <span class="gray_text"><a class="lined" href="/name/188847/">Юрий Никулин</a>, <a class="lined" href="/name/181144/">Андрей Миронов</a>, <a class="lined" href="/film/46225/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_46225" value="8.528"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_46225",
                rating:8.528,

                guest:true,

                user_code:'6d5a7ed6c754ead1edcbb634d5496563',
                filmId:46225,
                filmName:'Бриллиантовая рука'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/46225/votes/" class="all">8.528 <span>(237&nbsp;385)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.510</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.60<small style="display: block; margin-top: -1px">9&nbsp;237</small></div>



        <div id="user_vote_46225" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_46225"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_46225" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_301" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">29</div>
        <a class="bottom_marg" href="/film/301/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/301.jpg"  style="border:3px solid #ccc" alt="Матрица (The Matrix1999)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/301/" class="all">Матрица</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">The Matrix (1999) <nobr>136 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/23330/">Лана Вачовски</a>...</i><br />
            (фантастика, боевик)
        </span>
        <span class="gray_text"><a class="lined" href="/name/7836/">Киану Ривз</a>, <a class="lined" href="/name/9838/">Лоренс Фишбёрн</a>, <a class="lined" href="/film/301/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_301" value="8.491"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_301",
                rating:8.491,

                guest:true,

                user_code:'c24c03551c515dd210e1bb7882da1b14',
                filmId:301,
                filmName:'Матрица'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/301/votes/" class="all">8.491 <span>(299&nbsp;200)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.504</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.70<small style="display: block; margin-top: -1px">1&nbsp;271&nbsp;203</small></div>



        <div id="user_vote_301" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_301"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_301" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_312" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">30</div>
        <a class="bottom_marg" href="/film/312/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/312.jpg"  style="border:3px solid #ccc" alt="Властелин колец: Две крепости (The Lord of the Rings: The Two Towers2002)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div><div style="float: left; margin: 0 2px 5px 0" class="flag flag35"><a href="/lists/m_act%5Bcountry%5D/35/" title="Новая Зеландия"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/312/" class="all">Властелин колец: Две крепости</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">The Lord of the Rings: The Two Towers (2002) <nobr>179 мин.</nobr></span></div>
        <span class="gray_text">
            США...
            <i>реж. <a class="lined" href="/name/32383/">Питер Джексон</a></i><br />
            (фэнтези, драма, приключения)
        </span>
        <span class="gray_text"><a class="lined" href="/name/20287/">Элайджа Вуд</a>, <a class="lined" href="/name/28426/">Шон Эстин</a>, <a class="lined" href="/film/312/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_312" value="8.555"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_312",
                rating:8.555,

                guest:true,

                user_code:'753e669f390305c28de5663b3d6b37ea',
                filmId:312,
                filmName:'Властелин колец: Две крепости'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/312/votes/" class="all">8.555 <span>(262&nbsp;586)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.501</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.70<small style="display: block; margin-top: -1px">1&nbsp;163&nbsp;300</small></div>

        <div title="Оценка enmishka" class="userVote"><p class="all">10</p></div>


        <div id="user_vote_312" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_312"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_312" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_382" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">31</div>
        <a class="bottom_marg" href="/film/382/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/382.jpg"  style="border:3px solid #ccc" alt="Американская история&nbsp;Х (American History X1998)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/382/" class="all">Американская история&nbsp;Х</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">American History X (1998) <nobr>119 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/66424/">Тони Кэй</a></i><br />
            (драма, криминал)
        </span>
        <span class="gray_text"><a class="lined" href="/name/25774/">Эдвард Нортон</a>, <a class="lined" href="/name/9275/">Эдвард Ферлонг</a>, <a class="lined" href="/film/382/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_382" value="8.301"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_382",
                rating:8.301,

                guest:true,

                user_code:'fe10026c2cae685b115520ef28151042',
                filmId:382,
                filmName:'Американская история&nbsp;Х'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/382/votes/" class="all">8.301 <span>(205&nbsp;719)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.489</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.60<small style="display: block; margin-top: -1px">826&nbsp;212</small></div>



        <div id="user_vote_382" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_382"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_382" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_526" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">32</div>
        <a class="bottom_marg" href="/film/526/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/526.jpg"  style="border:3px solid #ccc" alt="Большой куш (Snatch.2000)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag11"><a href="/lists/m_act%5Bcountry%5D/11/" title="Великобритания"></a></div><div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/526/" class="all">Большой куш</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Snatch. (2000) <nobr>102 мин.</nobr></span></div>
        <span class="gray_text">
            Великобритания...
            <i>реж. <a class="lined" href="/name/45159/">Гай Ричи</a></i><br />
            (криминал, комедия)
        </span>
        <span class="gray_text"><a class="lined" href="/name/1514/">Джейсон Стэйтем</a>, <a class="lined" href="/name/25584/">Брэд Питт</a>, <a class="lined" href="/film/526/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_526" value="8.530"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_526",
                rating:8.530,

                guest:true,

                user_code:'ed83dc272a3dae462d52dd900d32e54a',
                filmId:526,
                filmName:'Большой куш'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/526/votes/" class="all">8.530 <span>(233&nbsp;409)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.487</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.30<small style="display: block; margin-top: -1px">631&nbsp;562</small></div>



        <div id="user_vote_526" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_526"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_526" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_279102" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">33</div>
        <a class="bottom_marg" href="/film/279102/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/279102.jpg"  style="border:3px solid #ccc" alt="ВАЛЛ·И (WALL&#183;E2008)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/279102/" class="all">ВАЛЛ·И</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">WALL&#183;E (2008) <nobr>98 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/23951/">Эндрю Стэнтон</a></i><br />
            (мультфильм, фантастика, приключения...)
        </span>
        <span class="gray_text"><a class="lined" href="/name/24330/">Бен Бертт</a>, <a class="lined" href="/name/1114274/">Элисса Найт</a>, <a class="lined" href="/film/279102/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_279102" value="8.302"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_279102",
                rating:8.302,

                guest:true,

                user_code:'824b8e8e4376bb2ced2f12894f47a9a2',
                filmId:279102,
                filmName:'ВАЛЛ·И'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/279102/votes/" class="all">8.302 <span>(263&nbsp;451)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.485</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.40<small style="display: block; margin-top: -1px">755&nbsp;527</small></div>

        <div title="Оценка enmishka" class="userVote"><p class="all">5</p></div>


        <div id="user_vote_279102" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_279102"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_279102" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_397667" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">34</div>
        <a class="bottom_marg" href="/film/397667/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/397667.jpg"  style="border:3px solid #ccc" alt="Остров проклятых (Shutter Island2009)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/397667/" class="all">Остров проклятых</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Shutter Island (2009) <nobr>138 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/10988/">Мартин Скорсезе</a></i><br />
            (триллер, детектив)
        </span>
        <span class="gray_text"><a class="lined" href="/name/37859/">Леонардо ДиКаприо</a>, <a class="lined" href="/name/10467/">Марк Руффало</a>, <a class="lined" href="/film/397667/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_397667" value="8.494"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_397667",
                rating:8.494,

                guest:true,

                user_code:'5821085809a1ea77478352649d628e21',
                filmId:397667,
                filmName:'Остров проклятых'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/397667/votes/" class="all">8.494 <span>(331&nbsp;497)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.483</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.10<small style="display: block; margin-top: -1px">843&nbsp;871</small></div>

        <div title="Оценка enmishka" class="userVote"><p class="all">8</p></div>


        <div id="user_vote_397667" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_397667"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_397667" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_336" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">35</div>
        <a class="bottom_marg" href="/film/336/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/336.jpg"  style="border:3px solid #ccc" alt="Пролетая над гнездом кукушки (One Flew Over the Cuckoo's Nest1975)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/336/" class="all">Пролетая над гнездом кукушки</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">One Flew Over the Cuckoo's Nest (1975) <nobr>133 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/20418/">Милош Форман</a></i><br />
            (драма)
        </span>
        <span class="gray_text"><a class="lined" href="/name/30056/">Джек Николсон</a>, <a class="lined" href="/name/15021/">Луиза Флетчер</a>, <a class="lined" href="/film/336/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_336" value="8.569"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_336",
                rating:8.569,

                guest:true,

                user_code:'488d2d16c68e4da707646a1c0af67c72',
                filmId:336,
                filmName:'Пролетая над гнездом кукушки'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/336/votes/" class="all">8.569 <span>(189&nbsp;919)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.472</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.70<small style="display: block; margin-top: -1px">715&nbsp;558</small></div>



        <div id="user_vote_336" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_336"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_336" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_4374" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">36</div>
        <a class="bottom_marg" href="/film/4374/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/4374.jpg"  style="border:3px solid #ccc" alt="Пираты Карибского моря: Проклятие Черной жемчужины (Pirates of the Caribbean: The Curse of the Black Pearl2003)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/4374/" class="all">Пираты Карибского моря: Проклятие Черной жемчужины</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Pirates of the Caribbean: The Curse of the Black Pearl (2003) <nobr>143 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/30870/">Гор Вербински</a></i><br />
            (фэнтези, боевик, приключения)
        </span>
        <span class="gray_text"><a class="lined" href="/name/6245/">Джонни Депп</a>, <a class="lined" href="/name/24683/">Джеффри Раш</a>, <a class="lined" href="/film/4374/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_4374" value="8.343"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_4374",
                rating:8.343,

                guest:true,

                user_code:'7b6e28733d11921068fd1c70ff752c77',
                filmId:4374,
                filmName:'Пираты Карибского моря: Проклятие Черной жемчужины'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/4374/votes/" class="all">8.343 <span>(305&nbsp;411)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.471</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.10<small style="display: block; margin-top: -1px">808&nbsp;076</small></div>

        <div title="Оценка enmishka" class="userVote"><p class="all">9</p></div>


        <div id="user_vote_4374" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_4374"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_4374" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_44386" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">37</div>
        <a class="bottom_marg" href="/film/44386/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/44386.jpg"  style="border:3px solid #ccc" alt="Джентльмены удачи (1971)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag13"><a href="/lists/m_act%5Bcountry%5D/13/" title="СССР"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/44386/" class="all">Джентльмены удачи</a><span style="color: #888; font-family: arial; font-size: 11px; display: block"> (1971) <nobr>84 мин.</nobr></span></div>
        <span class="gray_text">
            СССР,
            <i>реж. <a class="lined" href="/name/315892/">Александр Серый</a></i><br />
            (драма, комедия, криминал...)
        </span>
        <span class="gray_text"><a class="lined" href="/name/343964/">Евгений Леонов</a>, <a class="lined" href="/name/179092/">Георгий Вицин</a>, <a class="lined" href="/film/44386/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_44386" value="8.523"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_44386",
                rating:8.523,

                guest:true,

                user_code:'cddf5a54afa74b9ad12c53329339bfc7',
                filmId:44386,
                filmName:'Джентльмены удачи'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/44386/votes/" class="all">8.523 <span>(208&nbsp;314)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.470</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.60<small style="display: block; margin-top: -1px">7&nbsp;383</small></div>



        <div id="user_vote_44386" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_44386"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_44386" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_2950" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">38</div>
        <a class="bottom_marg" href="/film/2950/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/2950.jpg"  style="border:3px solid #ccc" alt="Пробуждение (Awakenings1990)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/2950/" class="all">Пробуждение</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Awakenings (1990) <nobr>121 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/48316/">Пенни Маршалл</a></i><br />
            (драма, биография)
        </span>
        <span class="gray_text"><a class="lined" href="/name/718/">Роберт Де Ниро</a>, <a class="lined" href="/name/20087/">Робин Уильямс</a>, <a class="lined" href="/film/2950/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_2950" value="8.451"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_2950",
                rating:8.451,

                guest:true,

                user_code:'df9d7815ed53c6acdf4a46ee1a65b643',
                filmId:2950,
                filmName:'Пробуждение'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/2950/votes/" class="all">8.451 <span>(93&nbsp;055)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.470</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 7.80<small style="display: block; margin-top: -1px">97&nbsp;066</small></div>



        <div id="user_vote_2950" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_2950"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_2950" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_111543" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">39</div>
        <a class="bottom_marg" href="/film/111543/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/111543.jpg"  style="border:3px solid #ccc" alt="Темный рыцарь (The Dark Knight2008)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div><div style="float: left; margin: 0 2px 5px 0" class="flag flag11"><a href="/lists/m_act%5Bcountry%5D/11/" title="Великобритания"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/111543/" class="all">Темный рыцарь</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">The Dark Knight (2008) <nobr>152 мин.</nobr></span></div>
        <span class="gray_text">
            США...
            <i>реж. <a class="lined" href="/name/41477/">Кристофер Нолан</a></i><br />
            (фантастика, боевик, триллер...)
        </span>
        <span class="gray_text"><a class="lined" href="/name/21495/">Кристиан Бэйл</a>, <a class="lined" href="/name/1183/">Хит Леджер</a>, <a class="lined" href="/film/111543/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_111543" value="8.502"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_111543",
                rating:8.502,

                guest:true,

                user_code:'e53aefe24fc594d165d9527a06c7564e',
                filmId:111543,
                filmName:'Темный рыцарь'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/111543/votes/" class="all">8.502 <span>(304&nbsp;862)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.469</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 9.00<small style="display: block; margin-top: -1px">1&nbsp;743&nbsp;854</small></div>

        <div title="Оценка enmishka" class="userVote"><p class="all">9</p></div>


        <div id="user_vote_111543" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_111543"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_111543" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_51481" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">40</div>
        <a class="bottom_marg" href="/film/51481/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/51481.jpg"  style="border:3px solid #ccc" alt="Хористы (Les Choristes2004)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag8"><a href="/lists/m_act%5Bcountry%5D/8/" title="Франция"></a></div><div style="float: left; margin: 0 2px 5px 0" class="flag flag21"><a href="/lists/m_act%5Bcountry%5D/21/" title="Швейцария"></a></div><div style="float: left; margin: 0 2px 5px 0" class="flag flag3"><a href="/lists/m_act%5Bcountry%5D/3/" title="Германия"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/51481/" class="all">Хористы</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Les Choristes (2004) <nobr>95 мин.</nobr></span></div>
        <span class="gray_text">
            Франция...
            <i>реж. <a class="lined" href="/name/48612/">Кристоф Барратье</a></i><br />
            (драма, музыка)
        </span>
        <span class="gray_text"><a class="lined" href="/name/105780/">Жерар Жюньо</a>, <a class="lined" href="/name/16766/">Франсуа Берлеан</a>, <a class="lined" href="/film/51481/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_51481" value="8.278"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_51481",
                rating:8.278,

                guest:true,

                user_code:'a0593174cb81dd7cc9c32675a3dce991',
                filmId:51481,
                filmName:'Хористы'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/51481/votes/" class="all">8.278 <span>(84&nbsp;069)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.463</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 7.90<small style="display: block; margin-top: -1px">46&nbsp;091</small></div>

        <div title="Оценка enmishka" class="userVote"><p class="all">9</p></div>


        <div id="user_vote_51481" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_51481"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_51481" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_346" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">41</div>
        <a class="bottom_marg" href="/film/346/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/346.jpg"  style="border:3px solid #ccc" alt="12 разгневанных мужчин (12 Angry Men1957)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/346/" class="all">12 разгневанных мужчин</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">12 Angry Men (1957) <nobr>96 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/25080/">Сидни Люмет</a></i><br />
            (драма, криминал)
        </span>
        <span class="gray_text"><a class="lined" href="/name/166531/">Генри Фонда</a>, <a class="lined" href="/name/81064/">Мартин Болсам</a>, <a class="lined" href="/film/346/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_346" value="8.507"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_346",
                rating:8.507,

                guest:true,

                user_code:'e1f3a8b73290ca8121abc12dcd9bc821',
                filmId:346,
                filmName:'12 разгневанных мужчин'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/346/votes/" class="all">8.507 <span>(61&nbsp;591)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.460</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.90<small style="display: block; margin-top: -1px">472&nbsp;843</small></div>



        <div id="user_vote_346" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_346"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_346" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_2213" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">42</div>
        <a class="bottom_marg" href="/film/2213/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/2213.jpg"  style="border:3px solid #ccc" alt="Титаник (Titanic1997)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/2213/" class="all">Титаник</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Titanic (1997) <nobr>194 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/27977/">Джеймс Кэмерон</a></i><br />
            (драма, мелодрама)
        </span>
        <span class="gray_text"><a class="lined" href="/name/37859/">Леонардо ДиКаприо</a>, <a class="lined" href="/name/21709/">Кейт Уинслет</a>, <a class="lined" href="/film/2213/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_2213" value="8.371"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_2213",
                rating:8.371,

                guest:true,

                user_code:'1eb434302ddf7079f26d5a32e6bb085f',
                filmId:2213,
                filmName:'Титаник'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/2213/votes/" class="all">8.371 <span>(337&nbsp;871)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.457</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 7.70<small style="display: block; margin-top: -1px">835&nbsp;316</small></div>

        <div title="Оценка enmishka" class="userVote"><p class="all">6</p></div>


        <div id="user_vote_2213" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_2213"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_2213" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_387556" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">43</div>
        <a class="bottom_marg" href="/film/387556/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/387556.jpg"  style="border:3px solid #ccc" alt="Хатико: Самый верный друг (Hachi: A Dog's Tale2008)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div><div style="float: left; margin: 0 2px 5px 0" class="flag flag11"><a href="/lists/m_act%5Bcountry%5D/11/" title="Великобритания"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/387556/" class="all">Хатико: Самый верный друг</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Hachi: A Dog's Tale (2008) <nobr>89 мин.</nobr></span></div>
        <span class="gray_text">
            США...
            <i>реж. <a class="lined" href="/name/6221/">Лассе Халльстрём</a></i><br />
            (драма, семейный)
        </span>
        <span class="gray_text"><a class="lined" href="/name/21822/">Ричард Гир</a>, <a class="lined" href="/name/6651/">Джоан Аллен</a>, <a class="lined" href="/film/387556/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_387556" value="8.349"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_387556",
                rating:8.349,

                guest:true,

                user_code:'429cf0e0b4e6e7eb8ec49ddd063500bf',
                filmId:387556,
                filmName:'Хатико: Самый верный друг'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/387556/votes/" class="all">8.349 <span>(246&nbsp;777)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.457</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.10<small style="display: block; margin-top: -1px">173&nbsp;861</small></div>

        <div title="Оценка enmishka" class="userVote"><p class="all">10</p></div>


        <div id="user_vote_387556" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_387556"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_387556" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_4871" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">44</div>
        <a class="bottom_marg" href="/film/4871/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/4871.jpg"  style="border:3px solid #ccc" alt="Запах женщины (Scent of a Woman1992)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/4871/" class="all">Запах женщины</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Scent of a Woman (1992) <nobr>156 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/32268/">Мартин Брест</a></i><br />
            (драма)
        </span>
        <span class="gray_text"><a class="lined" href="/name/26240/">Аль Пачино</a>, <a class="lined" href="/name/10305/">Крис О’Доннелл</a>, <a class="lined" href="/film/4871/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_4871" value="8.472"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_4871",
                rating:8.472,

                guest:true,

                user_code:'dbbb4d4e5200f39eba9af67a9deb208e',
                filmId:4871,
                filmName:'Запах женщины'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/4871/votes/" class="all">8.472 <span>(152&nbsp;870)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.457</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.00<small style="display: block; margin-top: -1px">203&nbsp;115</small></div>



        <div id="user_vote_4871" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_4871"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_4871" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_356" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">45</div>
        <a class="bottom_marg" href="/film/356/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/356.jpg"  style="border:3px solid #ccc" alt="В джазе только девушки (Some Like It Hot1959)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/356/" class="all">В джазе только девушки</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Some Like It Hot (1959) <nobr>119 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/93354/">Билли Уайлдер</a></i><br />
            (мелодрама, комедия, криминал...)
        </span>
        <span class="gray_text"><a class="lined" href="/name/74571/">Мэрилин Монро</a>, <a class="lined" href="/name/25873/">Тони Кертис</a>, <a class="lined" href="/film/356/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_356" value="8.471"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_356",
                rating:8.471,

                guest:true,

                user_code:'577f531b04b59edb8e9d4b6a30fa9213',
                filmId:356,
                filmName:'В джазе только девушки'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/356/votes/" class="all">8.471 <span>(166&nbsp;857)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.454</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.30<small style="display: block; margin-top: -1px">185&nbsp;124</small></div>



        <div id="user_vote_356" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_356"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_356" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_370" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">46</div>
        <a class="bottom_marg" href="/film/370/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/370.jpg"  style="border:3px solid #ccc" alt="Унесённые призраками (Sen to Chihiro no kamikakushi2001)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag9"><a href="/lists/m_act%5Bcountry%5D/9/" title="Япония"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/370/" class="all">Унесённые призраками</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Sen to Chihiro no kamikakushi (2001) <nobr>125 мин.</nobr></span></div>
        <span class="gray_text">
            Япония,
            <i>реж. <a class="lined" href="/name/47753/">Хаяо Миядзаки</a></i><br />
            (аниме, мультфильм, фэнтези...)
        </span>
        <span class="gray_text"><a class="lined" href="/name/47756/">Руми Хираги</a>, <a class="lined" href="/name/47758/">Ирино Мию</a>, <a class="lined" href="/film/370/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_370" value="8.418"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_370",
                rating:8.418,

                guest:true,

                user_code:'b4008d9d58629f0d3644a5a60b061b02',
                filmId:370,
                filmName:'Унесённые призраками'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/370/votes/" class="all">8.418 <span>(172&nbsp;988)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.453</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.60<small style="display: block; margin-top: -1px">447&nbsp;308</small></div>

        <div title="Оценка enmishka" class="userVote"><p class="all">8</p></div>


        <div id="user_vote_370" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_370"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_370" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_414" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">47</div>
        <a class="bottom_marg" href="/film/414/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/414.jpg"  style="border:3px solid #ccc" alt="Огни большого города (City Lights1931)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/414/" class="all">Огни большого города</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">City Lights (1931) <nobr>87 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/78810/">Чарльз Чаплин</a></i><br />
            (драма, мелодрама, комедия)
        </span>
        <span class="gray_text"><a class="lined" href="/name/78810/">Чарльз Чаплин</a>, <a class="lined" href="/name/115712/">Вирджиния Черрилл</a>, <a class="lined" href="/film/414/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_414" value="8.514"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_414",
                rating:8.514,

                guest:true,

                user_code:'a87d70cb7ee6f057cf6ae2019d32d95c',
                filmId:414,
                filmName:'Огни большого города'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/414/votes/" class="all">8.514 <span>(37&nbsp;321)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.453</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.60<small style="display: block; margin-top: -1px">115&nbsp;919</small></div>



        <div id="user_vote_414" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_414"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_414" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_348" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">48</div>
        <a class="bottom_marg" href="/film/348/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/348.jpg"  style="border:3px solid #ccc" alt="Эта замечательная жизнь (It's a Wonderful Life1946)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/348/" class="all">Эта замечательная жизнь</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">It's a Wonderful Life (1946) <nobr>130 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/154897/">Фрэнк Капра</a></i><br />
            (фэнтези, драма, семейный)
        </span>
        <span class="gray_text"><a class="lined" href="/name/22329/">Джеймс Стюарт</a>, <a class="lined" href="/name/205093/">Донна Рид</a>, <a class="lined" href="/film/348/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_348" value="8.474"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_348",
                rating:8.474,

                guest:true,

                user_code:'7c2fd508bbb562bcf237f84b88f50788',
                filmId:348,
                filmName:'Эта замечательная жизнь'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/348/votes/" class="all">8.474 <span>(33&nbsp;749)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.452</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.60<small style="display: block; margin-top: -1px">290&nbsp;398</small></div>



        <div id="user_vote_348" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_348"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_348" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_43395" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">49</div>
        <a class="bottom_marg" href="/film/43395/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/43395.jpg"  style="border:3px solid #ccc" alt="...А зори здесь тихие (1972)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag13"><a href="/lists/m_act%5Bcountry%5D/13/" title="СССР"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/43395/" class="all">...А зори здесь тихие</a><span style="color: #888; font-family: arial; font-size: 11px; display: block"> (1972) <nobr>160 мин.</nobr></span></div>
        <span class="gray_text">
            СССР,
            <i>реж. <a class="lined" href="/name/290395/">Станислав Ростоцкий</a></i><br />
            (драма, военный, история)
        </span>
        <span class="gray_text"><a class="lined" href="/name/102363/">Елена Драпеко</a>, <a class="lined" href="/name/331485/">Екатерина Маркова</a>, <a class="lined" href="/film/43395/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_43395" value="8.495"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_43395",
                rating:8.495,

                guest:true,

                user_code:'dcbf7cf3f8f39c97687818a56aaa6f89',
                filmId:43395,
                filmName:'...А зори здесь тихие'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/43395/votes/" class="all">8.495 <span>(84&nbsp;742)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.446</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.40<small style="display: block; margin-top: -1px">2&nbsp;385</small></div>



        <div id="user_vote_43395" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_43395"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_43395" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_77263" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">50</div>
        <a class="bottom_marg" href="/film/77263/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/77263.jpg"  style="border:3px solid #ccc" alt="Приключения Шерлока Холмса и доктора Ватсона: Собака Баскервилей  (ТВ) (1981)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag13"><a href="/lists/m_act%5Bcountry%5D/13/" title="СССР"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/77263/" class="all">Приключения Шерлока Холмса и доктора Ватсона: Собака Баскервилей  (ТВ)</a><span style="color: #888; font-family: arial; font-size: 11px; display: block"> (1981) <nobr>154 мин.</nobr></span></div>
        <span class="gray_text">
            СССР,
            <i>реж. <a class="lined" href="/name/284219/">Игорь Масленников</a></i><br />
            (криминал, детектив)
        </span>
        <span class="gray_text"><a class="lined" href="/name/266224/">Василий Ливанов</a>, <a class="lined" href="/name/174122/">Виталий Соломин</a>, <a class="lined" href="/film/77263/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_77263" value="8.601"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_77263",
                rating:8.601,

                guest:true,

                user_code:'10710ab32a51a122f406afb91466043c',
                filmId:77263,
                filmName:'Приключения Шерлока Холмса и доктора Ватсона: Собака Баскервилей'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/77263/votes/" class="all">8.601 <span>(98&nbsp;828)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.438</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.90<small style="display: block; margin-top: -1px">3&nbsp;934</small></div>



        <div id="user_vote_77263" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_77263"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_77263" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_349" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">51</div>
        <a class="bottom_marg" href="/film/349/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/349.jpg"  style="border:3px solid #ccc" alt="Хороший, плохой, злой (Il buono, il brutto, il cattivo1966)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag14"><a href="/lists/m_act%5Bcountry%5D/14/" title="Италия"></a></div><div style="float: left; margin: 0 2px 5px 0" class="flag flag15"><a href="/lists/m_act%5Bcountry%5D/15/" title="Испания"></a></div><div style="float: left; margin: 0 2px 5px 0" class="flag flag18"><a href="/lists/m_act%5Bcountry%5D/18/" title="Германия (ФРГ)"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/349/" class="all">Хороший, плохой, злой</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Il buono, il brutto, il cattivo (1966) <nobr>178 мин.</nobr></span></div>
        <span class="gray_text">
            Италия...
            <i>реж. <a class="lined" href="/name/156585/">Серджио Леоне</a></i><br />
            (вестерн)
        </span>
        <span class="gray_text"><a class="lined" href="/name/22948/">Клинт Иствуд</a>, <a class="lined" href="/name/158442/">Ли Ван Клиф</a>, <a class="lined" href="/film/349/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_349" value="8.543"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_349",
                rating:8.543,

                guest:true,

                user_code:'22f6c49682a7a6f79b0a2089cd5e70ac',
                filmId:349,
                filmName:'Хороший, плохой, злой'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/349/votes/" class="all">8.543 <span>(80&nbsp;002)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.433</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.90<small style="display: block; margin-top: -1px">526&nbsp;751</small></div>



        <div id="user_vote_349" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_349"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_349" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_327" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">52</div>
        <a class="bottom_marg" href="/film/327/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/327.jpg"  style="border:3px solid #ccc" alt="Крестный отец&nbsp;2 (The Godfather: Part II1974)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/327/" class="all">Крестный отец&nbsp;2</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">The Godfather: Part II (1974) <nobr>202 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/12665/">Фрэнсис Форд Коппола</a></i><br />
            (драма, криминал)
        </span>
        <span class="gray_text"><a class="lined" href="/name/26240/">Аль Пачино</a>, <a class="lined" href="/name/718/">Роберт Де Ниро</a>, <a class="lined" href="/film/327/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_327" value="8.547"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_327",
                rating:8.547,

                guest:true,

                user_code:'1198e63a60ea5ef1783a6273d3736371',
                filmId:327,
                filmName:'Крестный отец&nbsp;2'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/327/votes/" class="all">8.547 <span>(108&nbsp;276)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.417</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 9.00<small style="display: block; margin-top: -1px">830&nbsp;053</small></div>



        <div id="user_vote_327" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_327"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_327" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_345" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">53</div>
        <a class="bottom_marg" href="/film/345/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/345.jpg"  style="border:3px solid #ccc" alt="Молчание ягнят (The Silence of the Lambs1990)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/345/" class="all">Молчание ягнят</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">The Silence of the Lambs (1990) <nobr>114 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/12659/">Джонатан Демме</a></i><br />
            (триллер, криминал, детектив...)
        </span>
        <span class="gray_text"><a class="lined" href="/name/26070/">Джоди Фостер</a>, <a class="lined" href="/name/8968/">Энтони Хопкинс</a>, <a class="lined" href="/film/345/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_345" value="8.339"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_345",
                rating:8.339,

                guest:true,

                user_code:'bc61ba9c00f15c1d3dac4c4a3b5a9928',
                filmId:345,
                filmName:'Молчание ягнят'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/345/votes/" class="all">8.339 <span>(214&nbsp;848)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.416</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.60<small style="display: block; margin-top: -1px">946&nbsp;778</small></div>



        <div id="user_vote_345" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_345"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_345" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_44745" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">54</div>
        <a class="bottom_marg" href="/film/44745/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/44745.jpg"  style="border:3px solid #ccc" alt="Кавказская пленница, или Новые приключения Шурика (1966)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag13"><a href="/lists/m_act%5Bcountry%5D/13/" title="СССР"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/44745/" class="all">Кавказская пленница, или Новые приключения Шурика</a><span style="color: #888; font-family: arial; font-size: 11px; display: block"> (1966) <nobr>82 мин.</nobr></span></div>
        <span class="gray_text">
            СССР,
            <i>реж. <a class="lined" href="/name/191587/">Леонид Гайдай</a></i><br />
            (мелодрама, комедия, приключения...)
        </span>
        <span class="gray_text"><a class="lined" href="/name/284624/">Александр Демьяненко</a>, <a class="lined" href="/name/192726/">Наталья Варлей</a>, <a class="lined" href="/film/44745/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_44745" value="8.464"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_44745",
                rating:8.464,

                guest:true,

                user_code:'b37b88c8c0d14c644446a47a6a95dad6',
                filmId:44745,
                filmName:'Кавказская пленница, или Новые приключения Шурика'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/44745/votes/" class="all">8.464 <span>(211&nbsp;907)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.415</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.40<small style="display: block; margin-top: -1px">7&nbsp;418</small></div>

        <div title="Оценка enmishka" class="userVote"><p class="all">8</p></div>


        <div id="user_vote_44745" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_44745"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_44745" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_280172" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">55</div>
        <a class="bottom_marg" href="/film/280172/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/280172.jpg"  style="border:3px solid #ccc" alt="Как приручить дракона (How to Train Your Dragon2010)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/280172/" class="all">Как приручить дракона</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">How to Train Your Dragon (2010) <nobr>98 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/39365/">Дин ДеБлуа</a>...</i><br />
            (мультфильм, фэнтези, комедия...)
        </span>
        <span class="gray_text"><a class="lined" href="/name/7247/">Джей Барушель</a>, <a class="lined" href="/name/12086/">Джерард Батлер</a>, <a class="lined" href="/film/280172/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_280172" value="8.221"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_280172",
                rating:8.221,

                guest:true,

                user_code:'8d7a41fb43ccc141767c44d2f0ef998d',
                filmId:280172,
                filmName:'Как приручить дракона'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/280172/votes/" class="all">8.221 <span>(216&nbsp;038)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.413</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.20<small style="display: block; margin-top: -1px">517&nbsp;496</small></div>



        <div id="user_vote_280172" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_280172"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_280172" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_377" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">56</div>
        <a class="bottom_marg" href="/film/377/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/377.jpg"  style="border:3px solid #ccc" alt="Семь (Se7en1995)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/377/" class="all">Семь</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Se7en (1995) <nobr>127 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/2944/">Дэвид Финчер</a></i><br />
            (триллер, драма, криминал...)
        </span>
        <span class="gray_text"><a class="lined" href="/name/25584/">Брэд Питт</a>, <a class="lined" href="/name/6750/">Морган Фриман</a>, <a class="lined" href="/film/377/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_377" value="8.299"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_377",
                rating:8.299,

                guest:true,

                user_code:'07ae4bb30b39db275ab994450a609009',
                filmId:377,
                filmName:'Семь'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/377/votes/" class="all">8.299 <span>(237&nbsp;523)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.410</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.60<small style="display: block; margin-top: -1px">1&nbsp;089&nbsp;263</small></div>



        <div id="user_vote_377" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_377"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_377" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_586397" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">57</div>
        <a class="bottom_marg" href="/film/586397/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/586397.jpg"  style="border:3px solid #ccc" alt="Джанго освобожденный (Django Unchained2012)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/586397/" class="all">Джанго освобожденный</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Django Unchained (2012) <nobr>165 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/7640/">Квентин Тарантино</a></i><br />
            (драма, вестерн, приключения...)
        </span>
        <span class="gray_text"><a class="lined" href="/name/514/">Джейми Фокс</a>, <a class="lined" href="/name/245737/">Кристоф Вальц</a>, <a class="lined" href="/film/586397/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_586397" value="8.162"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_586397",
                rating:8.162,

                guest:true,

                user_code:'6ca079d7406e75b6a1a21916fda91807',
                filmId:586397,
                filmName:'Джанго освобожденный'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/586397/votes/" class="all">8.162 <span>(273&nbsp;020)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.399</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.40<small style="display: block; margin-top: -1px">1&nbsp;021&nbsp;124</small></div>

        <div title="Оценка enmishka" class="userVote"><p class="all">9</p></div>


        <div id="user_vote_586397" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_586397"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_586397" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_4541" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">58</div>
        <a class="bottom_marg" href="/film/4541/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/4541.jpg"  style="border:3px solid #ccc" alt="Шоу Трумана (The Truman Show1998)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/4541/" class="all">Шоу Трумана</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">The Truman Show (1998) <nobr>103 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/63414/">Питер Уир</a></i><br />
            (фантастика, драма, комедия)
        </span>
        <span class="gray_text"><a class="lined" href="/name/6141/">Джим Керри</a>, <a class="lined" href="/name/10965/">Лора Линни</a>, <a class="lined" href="/film/4541/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_4541" value="8.254"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_4541",
                rating:8.254,

                guest:true,

                user_code:'19c1351a1dee1ae2a525dd95ffefaa87',
                filmId:4541,
                filmName:'Шоу Трумана'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/4541/votes/" class="all">8.254 <span>(233&nbsp;626)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.399</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.10<small style="display: block; margin-top: -1px">708&nbsp;807</small></div>

        <div title="Оценка enmishka" class="userVote"><p class="all">10</p></div>


        <div id="user_vote_4541" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_4541"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_4541" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_12244" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">59</div>
        <a class="bottom_marg" href="/film/12244/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/12244.jpg"  style="border:3px solid #ccc" alt="Нокдаун (Cinderella Man2005)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/12244/" class="all">Нокдаун</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Cinderella Man (2005) <nobr>144 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/8919/">Рон Ховард</a></i><br />
            (драма, биография, спорт)
        </span>
        <span class="gray_text"><a class="lined" href="/name/10019/">Рассел Кроу</a>, <a class="lined" href="/name/6142/">Рене Зеллвегер</a>, <a class="lined" href="/film/12244/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_12244" value="8.212"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_12244",
                rating:8.212,

                guest:true,

                user_code:'5b948d79c1ae4ea95bff1524e0a737c9',
                filmId:12244,
                filmName:'Нокдаун'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/12244/votes/" class="all">8.212 <span>(95&nbsp;738)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.394</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.00<small style="display: block; margin-top: -1px">144&nbsp;756</small></div>



        <div id="user_vote_12244" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_12244"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_12244" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_77269" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">60</div>
        <a class="bottom_marg" href="/film/77269/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/77269.jpg"  style="border:3px solid #ccc" alt="Шерлок Холмс и доктор Ватсон: Знакомство  (ТВ) (1979)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag13"><a href="/lists/m_act%5Bcountry%5D/13/" title="СССР"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/77269/" class="all">Шерлок Холмс и доктор Ватсон: Знакомство  (ТВ)</a><span style="color: #888; font-family: arial; font-size: 11px; display: block"> (1979) <nobr>68 мин.</nobr></span></div>
        <span class="gray_text">
            СССР,
            <i>реж. <a class="lined" href="/name/284219/">Игорь Масленников</a></i><br />
            (криминал, детектив)
        </span>
        <span class="gray_text"><a class="lined" href="/name/266224/">Василий Ливанов</a>, <a class="lined" href="/name/174122/">Виталий Соломин</a>, <a class="lined" href="/film/77269/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_77269" value="8.554"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_77269",
                rating:8.554,

                guest:true,

                user_code:'8262e0e26152bb97f151d0adf4a5f0cd',
                filmId:77269,
                filmName:'Шерлок Холмс и доктор Ватсон: Знакомство'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/77269/votes/" class="all">8.554 <span>(82&nbsp;846)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.387</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.70<small style="display: block; margin-top: -1px">2&nbsp;273</small></div>



        <div id="user_vote_77269" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_77269"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_77269" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_12198" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">61</div>
        <a class="bottom_marg" href="/film/12198/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/12198.jpg"  style="border:3px solid #ccc" alt="Игра (The Game1997)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/12198/" class="all">Игра</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">The Game (1997) <nobr>129 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/2944/">Дэвид Финчер</a></i><br />
            (триллер, драма, детектив...)
        </span>
        <span class="gray_text"><a class="lined" href="/name/10094/">Майкл Дуглас</a>, <a class="lined" href="/name/1293/">Шон Пенн</a>, <a class="lined" href="/film/12198/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_12198" value="8.261"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_12198",
                rating:8.261,

                guest:true,

                user_code:'ac610c64e057990a099e1665666490dc',
                filmId:12198,
                filmName:'Игра'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/12198/votes/" class="all">8.261 <span>(187&nbsp;342)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.385</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 7.80<small style="display: block; margin-top: -1px">275&nbsp;279</small></div>



        <div id="user_vote_12198" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_12198"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_12198" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_775276" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">62</div>
        <a class="bottom_marg" href="/film/775276/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/775276.jpg"  style="border:3px solid #ccc" alt="Зверополис (Zootopia2016)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/775276/" class="all">Зверополис</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Zootopia (2016) <nobr>108 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/1562107/">Байрон Ховард</a>...</i><br />
            (мультфильм, комедия, криминал...)
        </span>
        <span class="gray_text"><a class="lined" href="/name/30098/">Джиннифер Гудвин</a>, <a class="lined" href="/name/1858/">Джейсон Бейтман</a>, <a class="lined" href="/film/775276/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_775276" value="8.331"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_775276",
                rating:8.331,

                guest:true,

                user_code:'367920ee81a0b45f6f20c84a13e6540a',
                filmId:775276,
                filmName:'Зверополис'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/775276/votes/" class="all">8.331 <span>(168&nbsp;072)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.385</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.10<small style="display: block; margin-top: -1px">282&nbsp;199</small></div>

        <div title="Оценка enmishka" class="userVote"><p class="all">7</p></div>


        <div id="user_vote_775276" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_775276"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_775276" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_77335" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">63</div>
        <a class="bottom_marg" href="/film/77335/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/77335.jpg"  style="border:3px solid #ccc" alt="Собачье сердце  (ТВ) (1988)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag13"><a href="/lists/m_act%5Bcountry%5D/13/" title="СССР"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/77335/" class="all">Собачье сердце  (ТВ)</a><span style="color: #888; font-family: arial; font-size: 11px; display: block"> (1988) <nobr>136 мин.</nobr></span></div>
        <span class="gray_text">
            СССР,
            <i>реж. <a class="lined" href="/name/256810/">Владимир Бортко</a></i><br />
            (фантастика, драма, комедия)
        </span>
        <span class="gray_text"><a class="lined" href="/name/277309/">Владимир Толоконников</a>, <a class="lined" href="/name/190105/">Евгений Евстигнеев</a>, <a class="lined" href="/film/77335/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_77335" value="8.345"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_77335",
                rating:8.345,

                guest:true,

                user_code:'7878363deab799a553e24c4b3d746720',
                filmId:77335,
                filmName:'Собачье сердце'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/77335/votes/" class="all">8.345 <span>(133&nbsp;179)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.381</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.90<small style="display: block; margin-top: -1px">4&nbsp;526</small></div>



        <div id="user_vote_77335" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_77335"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_77335" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_841081" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">64</div>
        <a class="bottom_marg" href="/film/841081/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/841081.jpg"  style="border:3px solid #ccc" alt="Ла-Ла Ленд (La La Land2016)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div><div style="float: left; margin: 0 2px 5px 0" class="flag flag28"><a href="/lists/m_act%5Bcountry%5D/28/" title="Гонконг"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/841081/" class="all">Ла-Ла Ленд</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">La La Land (2016) <nobr>128 мин.</nobr></span></div>
        <span class="gray_text">
            США...
            <i>реж. <a class="lined" href="/name/2074963/">Дэмьен Шазелл</a></i><br />
            (мюзикл, драма, мелодрама...)
        </span>
        <span class="gray_text"><a class="lined" href="/name/10143/">Райан Гослинг</a>, <a class="lined" href="/name/1130955/">Эмма Стоун</a>, <a class="lined" href="/film/841081/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_841081" value="8.328"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_841081",
                rating:8.328,

                guest:true,

                user_code:'d68ccb754f4d0160d758abc3595b10fb',
                filmId:841081,
                filmName:'Ла-Ла Ленд'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/841081/votes/" class="all">8.328 <span>(72&nbsp;325)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.378</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.40<small style="display: block; margin-top: -1px">214&nbsp;992</small></div>

        <div title="Оценка enmishka" class="userVote"><p class="all">7</p></div>


        <div id="user_vote_841081" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_841081"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_841081" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_399" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">65</div>
        <a class="bottom_marg" href="/film/399/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/399.jpg"  style="border:3px solid #ccc" alt="Храброе сердце (Braveheart1995)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/399/" class="all">Храброе сердце</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Braveheart (1995) <nobr>178 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/7405/">Мэл Гибсон</a></i><br />
            (драма, военный, биография...)
        </span>
        <span class="gray_text"><a class="lined" href="/name/7405/">Мэл Гибсон</a>, <a class="lined" href="/name/2363/">Софи Марсо</a>, <a class="lined" href="/film/399/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_399" value="8.286"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_399",
                rating:8.286,

                guest:true,

                user_code:'4350b1947d9ce45463c17ac0452f3399',
                filmId:399,
                filmName:'Храброе сердце'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/399/votes/" class="all">8.286 <span>(145&nbsp;705)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.374</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.40<small style="display: block; margin-top: -1px">773&nbsp;527</small></div>



        <div id="user_vote_399" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_399"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_399" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_725190" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">66</div>
        <a class="bottom_marg" href="/film/725190/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/725190.jpg"  style="border:3px solid #ccc" alt="Одержимость (Whiplash2013)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/725190/" class="all">Одержимость</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Whiplash (2013) <nobr>106 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/2074963/">Дэмьен Шазелл</a></i><br />
            (драма, музыка)
        </span>
        <span class="gray_text"><a class="lined" href="/name/1669945/">Майлз Теллер</a>, <a class="lined" href="/name/8552/">Дж.К. Симмонс</a>, <a class="lined" href="/film/725190/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_725190" value="8.319"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_725190",
                rating:8.319,

                guest:true,

                user_code:'f8f5d952ac12549ebf4488e2fbf09e26',
                filmId:725190,
                filmName:'Одержимость'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/725190/votes/" class="all">8.319 <span>(127&nbsp;143)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.372</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.50<small style="display: block; margin-top: -1px">465&nbsp;678</small></div>



        <div id="user_vote_725190" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_725190"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_725190" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_42736" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">67</div>
        <a class="bottom_marg" href="/film/42736/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/42736.jpg"  style="border:3px solid #ccc" alt="Офицеры (1971)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag13"><a href="/lists/m_act%5Bcountry%5D/13/" title="СССР"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/42736/" class="all">Офицеры</a><span style="color: #888; font-family: arial; font-size: 11px; display: block"> (1971) <nobr>91 мин.</nobr></span></div>
        <span class="gray_text">
            СССР,
            <i>реж. <a class="lined" href="/name/304659/">Владимир Роговой</a></i><br />
            (драма, мелодрама)
        </span>
        <span class="gray_text"><a class="lined" href="/name/174335/">Георгий Юматов</a>, <a class="lined" href="/name/256968/">Василий Лановой</a>, <a class="lined" href="/film/42736/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_42736" value="8.456"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_42736",
                rating:8.456,

                guest:true,

                user_code:'19e7c9d432997f9f61f52800e4c9b015',
                filmId:42736,
                filmName:'Офицеры'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/42736/votes/" class="all">8.456 <span>(47&nbsp;832)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.367</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 7.90<small style="display: block; margin-top: -1px">944</small></div>



        <div id="user_vote_42736" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_42736"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_42736" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_444" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">68</div>
        <a class="bottom_marg" href="/film/444/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/444.jpg"  style="border:3px solid #ccc" alt="Терминатор 2: Судный день (Terminator 2: Judgment Day1991)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div><div style="float: left; margin: 0 2px 5px 0" class="flag flag8"><a href="/lists/m_act%5Bcountry%5D/8/" title="Франция"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/444/" class="all">Терминатор 2: Судный день</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Terminator 2: Judgment Day (1991) <nobr>137 мин.</nobr></span></div>
        <span class="gray_text">
            США...
            <i>реж. <a class="lined" href="/name/27977/">Джеймс Кэмерон</a></i><br />
            (фантастика, боевик, триллер)
        </span>
        <span class="gray_text"><a class="lined" href="/name/6264/">Арнольд Шварценеггер</a>, <a class="lined" href="/name/28012/">Линда Хэмилтон</a>, <a class="lined" href="/film/444/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_444" value="8.304"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_444",
                rating:8.304,

                guest:true,

                user_code:'d19e80233ed3db42445b56342b913242',
                filmId:444,
                filmName:'Терминатор 2: Судный день'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/444/votes/" class="all">8.304 <span>(226&nbsp;725)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.366</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.50<small style="display: block; margin-top: -1px">774&nbsp;905</small></div>



        <div id="user_vote_444" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_444"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_444" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_470553" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">69</div>
        <a class="bottom_marg" href="/film/470553/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/470553.jpg"  style="border:3px solid #ccc" alt="Прислуга (The Help2011)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div><div style="float: left; margin: 0 2px 5px 0" class="flag flag29"><a href="/lists/m_act%5Bcountry%5D/29/" title="Индия"></a></div><div style="float: left; margin: 0 2px 5px 0" class="flag flag119"><a href="/lists/m_act%5Bcountry%5D/119/" title="ОАЭ"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/470553/" class="all">Прислуга</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">The Help (2011) <nobr>146 мин.</nobr></span></div>
        <span class="gray_text">
            США...
            <i>реж. <a class="lined" href="/name/42672/">Тейт Тейлор</a></i><br />
            (драма)
        </span>
        <span class="gray_text"><a class="lined" href="/name/1130955/">Эмма Стоун</a>, <a class="lined" href="/name/37058/">Виола Дэвис</a>, <a class="lined" href="/film/470553/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_470553" value="8.160"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_470553",
                rating:8.160,

                guest:true,

                user_code:'912314efae99b68767f5aa613b914ee7',
                filmId:470553,
                filmName:'Прислуга'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/470553/votes/" class="all">8.160 <span>(130&nbsp;012)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.361</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.10<small style="display: block; margin-top: -1px">305&nbsp;420</small></div>



        <div id="user_vote_470553" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_470553"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_470553" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_46708" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">70</div>
        <a class="bottom_marg" href="/film/46708/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/46708.jpg"  style="border:3px solid #ccc" alt="Москва слезам не верит (1979)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag13"><a href="/lists/m_act%5Bcountry%5D/13/" title="СССР"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/46708/" class="all">Москва слезам не верит</a><span style="color: #888; font-family: arial; font-size: 11px; display: block"> (1979) <nobr>150 мин.</nobr></span></div>
        <span class="gray_text">
            СССР,
            <i>реж. <a class="lined" href="/name/174283/">Владимир Меньшов</a></i><br />
            (драма, мелодрама, комедия)
        </span>
        <span class="gray_text"><a class="lined" href="/name/174285/">Вера Алентова</a>, <a class="lined" href="/name/174286/">Ирина Муравьёва</a>, <a class="lined" href="/film/46708/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_46708" value="8.364"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_46708",
                rating:8.364,

                guest:true,

                user_code:'daf8960cb798dfb4eb7a56ef995f5d9c',
                filmId:46708,
                filmName:'Москва слезам не верит'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/46708/votes/" class="all">8.364 <span>(130&nbsp;117)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.357</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.20<small style="display: block; margin-top: -1px">8&nbsp;321</small></div>

        <div class="eye eye_act alien" title="Просмотр enmishka"></div>


        <div id="user_vote_46708" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_46708"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_46708" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_2127" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">71</div>
        <a class="bottom_marg" href="/film/2127/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/2127.jpg"  style="border:3px solid #ccc" alt="Малыш (The Kid1921)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/2127/" class="all">Малыш</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">The Kid (1921) <nobr>68 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/78810/">Чарльз Чаплин</a></i><br />
            (драма, комедия, семейный)
        </span>
        <span class="gray_text"><a class="lined" href="/name/78810/">Чарльз Чаплин</a>, <a class="lined" href="/name/115713/">Джеки Кугэн</a>, <a class="lined" href="/film/2127/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_2127" value="8.242"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_2127",
                rating:8.242,

                guest:true,

                user_code:'e4681a686d21d8c845fe2497e5edf048',
                filmId:2127,
                filmName:'Малыш'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/2127/votes/" class="all">8.242 <span>(25&nbsp;410)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.343</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.30<small style="display: block; margin-top: -1px">72&nbsp;697</small></div>



        <div id="user_vote_2127" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_2127"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_2127" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_104938" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">72</div>
        <a class="bottom_marg" href="/film/104938/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/104938.jpg"  style="border:3px solid #ccc" alt="В погоне за счастьем (The Pursuit of Happyness2006)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/104938/" class="all">В погоне за счастьем</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">The Pursuit of Happyness (2006) <nobr>117 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/224998/">Габриэле Муччино</a></i><br />
            (драма, биография)
        </span>
        <span class="gray_text"><a class="lined" href="/name/513/">Уилл Смит</a>, <a class="lined" href="/name/906113/">Джейден Смит</a>, <a class="lined" href="/film/104938/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_104938" value="8.259"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_104938",
                rating:8.259,

                guest:true,

                user_code:'09a6ebd0beb4d6862e97e78efb97a312',
                filmId:104938,
                filmName:'В погоне за счастьем'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/104938/votes/" class="all">8.259 <span>(173&nbsp;715)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.336</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.00<small style="display: block; margin-top: -1px">330&nbsp;205</small></div>



        <div id="user_vote_104938" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_104938"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_104938" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_7724" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">73</div>
        <a class="bottom_marg" href="/film/7724/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/7724.jpg"  style="border:3px solid #ccc" alt="Летят журавли (1957)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag13"><a href="/lists/m_act%5Bcountry%5D/13/" title="СССР"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/7724/" class="all">Летят журавли</a><span style="color: #888; font-family: arial; font-size: 11px; display: block"> (1957) <nobr>97 мин.</nobr></span></div>
        <span class="gray_text">
            СССР,
            <i>реж. <a class="lined" href="/name/185684/">Михаил Калатозов</a></i><br />
            (драма, мелодрама, военный)
        </span>
        <span class="gray_text"><a class="lined" href="/name/201758/">Татьяна Самойлова</a>, <a class="lined" href="/name/174287/">Алексей Баталов</a>, <a class="lined" href="/film/7724/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_7724" value="8.286"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_7724",
                rating:8.286,

                guest:true,

                user_code:'e99ccbb7346b637a7116b276a52d0abc',
                filmId:7724,
                filmName:'Летят журавли'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/7724/votes/" class="all">8.286 <span>(37&nbsp;098)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.335</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.30<small style="display: block; margin-top: -1px">10&nbsp;843</small></div>



        <div id="user_vote_7724" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_7724"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_7724" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_408410" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">74</div>
        <a class="bottom_marg" href="/film/408410/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/408410.jpg"  style="border:3px solid #ccc" alt="Гран Торино (Gran Torino2008)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div><div style="float: left; margin: 0 2px 5px 0" class="flag flag3"><a href="/lists/m_act%5Bcountry%5D/3/" title="Германия"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/408410/" class="all">Гран Торино</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Gran Torino (2008) <nobr>116 мин.</nobr></span></div>
        <span class="gray_text">
            США...
            <i>реж. <a class="lined" href="/name/22948/">Клинт Иствуд</a></i><br />
            (драма)
        </span>
        <span class="gray_text"><a class="lined" href="/name/22948/">Клинт Иствуд</a>, <a class="lined" href="/name/1649450/">Би Ванг</a>, <a class="lined" href="/film/408410/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_408410" value="8.130"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_408410",
                rating:8.130,

                guest:true,

                user_code:'591c394cb2c7d840fc8dc69f7a6ac9ac',
                filmId:408410,
                filmName:'Гран Торино'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/408410/votes/" class="all">8.130 <span>(147&nbsp;845)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.333</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.20<small style="display: block; margin-top: -1px">590&nbsp;213</small></div>



        <div id="user_vote_408410" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_408410"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_408410" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_627" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">75</div>
        <a class="bottom_marg" href="/film/627/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/627.jpg"  style="border:3px solid #ccc" alt="Изгой (Cast Away2000)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/627/" class="all">Изгой</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Cast Away (2000) <nobr>143 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/2435/">Роберт Земекис</a></i><br />
            (драма, мелодрама, приключения)
        </span>
        <span class="gray_text"><a class="lined" href="/name/9144/">Том Хэнкс</a>, <a class="lined" href="/name/9146/">Хелен Хант</a>, <a class="lined" href="/film/627/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_627" value="8.256"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_627",
                rating:8.256,

                guest:true,

                user_code:'6d59996ed83af064dd4ea4569fe7575f',
                filmId:627,
                filmName:'Изгой'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/627/votes/" class="all">8.256 <span>(196&nbsp;933)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.328</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 7.70<small style="display: block; margin-top: -1px">414&nbsp;826</small></div>



        <div id="user_vote_627" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_627"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_627" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_519" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">76</div>
        <a class="bottom_marg" href="/film/519/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/519.jpg"  style="border:3px solid #ccc" alt="Человек дождя (Rain Man1988)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/519/" class="all">Человек дождя</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Rain Man (1988) <nobr>133 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/108/">Барри Левинсон</a></i><br />
            (драма)
        </span>
        <span class="gray_text"><a class="lined" href="/name/22234/">Дастин Хоффман</a>, <a class="lined" href="/name/20302/">Том Круз</a>, <a class="lined" href="/film/519/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_519" value="8.258"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_519",
                rating:8.258,

                guest:true,

                user_code:'356d1c133e7034972c9a55c89dc99df2',
                filmId:519,
                filmName:'Человек дождя'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/519/votes/" class="all">8.258 <span>(167&nbsp;015)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.328</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.00<small style="display: block; margin-top: -1px">398&nbsp;211</small></div>



        <div id="user_vote_519" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_519"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_519" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_7097" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">77</div>
        <a class="bottom_marg" href="/film/7097/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/7097.jpg"  style="border:3px solid #ccc" alt="Балто (Balto1995)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/7097/" class="all">Балто</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Balto (1995) <nobr>71 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/39137/">Саймон Уэллс</a></i><br />
            (мультфильм, драма, приключения...)
        </span>
        <span class="gray_text"><a class="lined" href="/name/7939/">Кевин Бейкон</a>, <a class="lined" href="/name/3714/">Боб Хоскинс</a>, <a class="lined" href="/film/7097/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_7097" value="8.339"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_7097",
                rating:8.339,

                guest:true,

                user_code:'3405c47368361b09cb7a2ad017d38a29',
                filmId:7097,
                filmName:'Балто'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/7097/votes/" class="all">8.339 <span>(103&nbsp;460)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.324</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 7.10<small style="display: block; margin-top: -1px">31&nbsp;586</small></div>

        <div title="Оценка enmishka" class="userVote"><p class="all">7</p></div>


        <div id="user_vote_7097" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_7097"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_7097" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_44027" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">78</div>
        <a class="bottom_marg" href="/film/44027/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/44027.jpg"  style="border:3px solid #ccc" alt="Судьба человека (1959)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag13"><a href="/lists/m_act%5Bcountry%5D/13/" title="СССР"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/44027/" class="all">Судьба человека</a><span style="color: #888; font-family: arial; font-size: 11px; display: block"> (1959) <nobr>97 мин.</nobr></span></div>
        <span class="gray_text">
            СССР,
            <i>реж. <a class="lined" href="/name/174228/">Сергей Бондарчук</a></i><br />
            (драма, военный)
        </span>
        <span class="gray_text"><a class="lined" href="/name/174228/">Сергей Бондарчук</a>, <a class="lined" href="/name/200860/">Павел Полунин</a>, <a class="lined" href="/film/44027/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_44027" value="8.363"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_44027",
                rating:8.363,

                guest:true,

                user_code:'329e25be00f93e2db964e42c31067664',
                filmId:44027,
                filmName:'Судьба человека'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/44027/votes/" class="all">8.363 <span>(36&nbsp;439)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.319</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.10<small style="display: block; margin-top: -1px">1&nbsp;842</small></div>



        <div id="user_vote_44027" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_44027"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_44027" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_46068" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">79</div>
        <a class="bottom_marg" href="/film/46068/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/46068.jpg"  style="border:3px solid #ccc" alt="Белый Бим Черное ухо (1976)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag13"><a href="/lists/m_act%5Bcountry%5D/13/" title="СССР"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/46068/" class="all">Белый Бим Черное ухо</a><span style="color: #888; font-family: arial; font-size: 11px; display: block"> (1976) <nobr>183 мин.</nobr></span></div>
        <span class="gray_text">
            СССР,
            <i>реж. <a class="lined" href="/name/290395/">Станислав Ростоцкий</a></i><br />
            (драма)
        </span>
        <span class="gray_text"><a class="lined" href="/name/101751/">Вячеслав Тихонов</a>, <a class="lined" href="/name/294248/">Никита Астахов</a>, <a class="lined" href="/film/46068/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_46068" value="8.370"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_46068",
                rating:8.370,

                guest:true,

                user_code:'b9786990ce350cb8115a162a84e2f0a4',
                filmId:46068,
                filmName:'Белый Бим Черное ухо'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/46068/votes/" class="all">8.370 <span>(58&nbsp;343)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.315</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.40<small style="display: block; margin-top: -1px">1&nbsp;212</small></div>



        <div id="user_vote_46068" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_46068"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_46068" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_395" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">80</div>
        <a class="bottom_marg" href="/film/395/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/395.jpg"  style="border:3px solid #ccc" alt="Шестое чувство (The Sixth Sense1999)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/395/" class="all">Шестое чувство</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">The Sixth Sense (1999) <nobr>107 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/20366/">М. Найт Шьямалан</a></i><br />
            (триллер, драма, детектив)
        </span>
        <span class="gray_text"><a class="lined" href="/name/110/">Брюс Уиллис</a>, <a class="lined" href="/name/11381/">Хэйли Джоэл Осмент</a>, <a class="lined" href="/film/395/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_395" value="8.179"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_395",
                rating:8.179,

                guest:true,

                user_code:'521e072ed5f86bdb2b84265ac0377376',
                filmId:395,
                filmName:'Шестое чувство'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/395/votes/" class="all">8.179 <span>(174&nbsp;521)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.313</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.10<small style="display: block; margin-top: -1px">714&nbsp;255</small></div>



        <div id="user_vote_395" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_395"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_395" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_63912" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">81</div>
        <a class="bottom_marg" href="/film/63912/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/63912.jpg"  style="border:3px solid #ccc" alt="Укрощение строптивого (Il bisbetico domato1980)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag14"><a href="/lists/m_act%5Bcountry%5D/14/" title="Италия"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/63912/" class="all">Укрощение строптивого</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Il bisbetico domato (1980) <nobr>104 мин.</nobr></span></div>
        <span class="gray_text">
            Италия,
            <i>реж. <a class="lined" href="/name/288363/">Франко Кастеллано</a>...</i><br />
            (комедия)
        </span>
        <span class="gray_text"><a class="lined" href="/name/178831/">Адриано Челентано</a>, <a class="lined" href="/name/4720/">Орнелла Мути</a>, <a class="lined" href="/film/63912/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_63912" value="8.393"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_63912",
                rating:8.393,

                guest:true,

                user_code:'84197c64cec9a970cd23723679f8b2a5',
                filmId:63912,
                filmName:'Укрощение строптивого'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/63912/votes/" class="all">8.393 <span>(156&nbsp;608)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.310</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 7.70<small style="display: block; margin-top: -1px">4&nbsp;401</small></div>

        <div title="Оценка enmishka" class="userVote"><p class="all">10</p></div>


        <div id="user_vote_63912" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_63912"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_63912" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_456" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">82</div>
        <a class="bottom_marg" href="/film/456/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/456.jpg"  style="border:3px solid #ccc" alt="Унесенные ветром (Gone with the Wind1939)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/456/" class="all">Унесенные ветром</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Gone with the Wind (1939) <nobr>222 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/210445/">Виктор Флеминг</a>...</i><br />
            (драма, мелодрама, военный...)
        </span>
        <span class="gray_text"><a class="lined" href="/name/24974/">Вивьен Ли</a>, <a class="lined" href="/name/178193/">Кларк Гейбл</a>, <a class="lined" href="/film/456/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_456" value="8.397"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_456",
                rating:8.397,

                guest:true,

                user_code:'fd4bdba21bc241783f104da70492dafd',
                filmId:456,
                filmName:'Унесенные ветром'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/456/votes/" class="all">8.397 <span>(98&nbsp;064)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.304</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.20<small style="display: block; margin-top: -1px">226&nbsp;576</small></div>



        <div id="user_vote_456" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_456"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_456" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_540" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">83</div>
        <a class="bottom_marg" href="/film/540/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/540.jpg"  style="border:3px solid #ccc" alt="Красавица и чудовище (Beauty and the Beast1991)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/540/" class="all">Красавица и чудовище</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Beauty and the Beast (1991) <nobr>84 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/173/">Гари Труздейл</a>...</i><br />
            (мультфильм, мюзикл, фэнтези...)
        </span>
        <span class="gray_text"><a class="lined" href="/name/114170/">Робби Бенсон</a>, <a class="lined" href="/name/7364/">Джесси Корти</a>, <a class="lined" href="/film/540/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_540" value="8.282"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_540",
                rating:8.282,

                guest:true,

                user_code:'196f0b097d3536fc4e12801f1441f07c',
                filmId:540,
                filmName:'Красавица и чудовище'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/540/votes/" class="all">8.282 <span>(139&nbsp;454)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.301</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.00<small style="display: block; margin-top: -1px">319&nbsp;810</small></div>

        <div title="Оценка enmishka" class="userVote"><p class="all">9</p></div>


        <div id="user_vote_540" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_540"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_540" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_469" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">84</div>
        <a class="bottom_marg" href="/film/469/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/469.jpg"  style="border:3px solid #ccc" alt="Однажды в Америке (Once Upon a Time in America1983)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag14"><a href="/lists/m_act%5Bcountry%5D/14/" title="Италия"></a></div><div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/469/" class="all">Однажды в Америке</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Once Upon a Time in America (1983) <nobr>229 мин.</nobr></span></div>
        <span class="gray_text">
            Италия...
            <i>реж. <a class="lined" href="/name/156585/">Серджио Леоне</a></i><br />
            (драма, криминал)
        </span>
        <span class="gray_text"><a class="lined" href="/name/718/">Роберт Де Ниро</a>, <a class="lined" href="/name/22953/">Джеймс Вудс</a>, <a class="lined" href="/film/469/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_469" value="8.281"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_469",
                rating:8.281,

                guest:true,

                user_code:'17c75415a78941da11265413ab7e7ab7',
                filmId:469,
                filmName:'Однажды в Америке'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/469/votes/" class="all">8.281 <span>(79&nbsp;903)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.298</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.40<small style="display: block; margin-top: -1px">230&nbsp;388</small></div>



        <div id="user_vote_469" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_469"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_469" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_497" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">85</div>
        <a class="bottom_marg" href="/film/497/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/497.jpg"  style="border:3px solid #ccc" alt="Римские каникулы (Roman Holiday1953)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/497/" class="all">Римские каникулы</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Roman Holiday (1953) <nobr>118 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/151340/">Уильям Уайлер</a></i><br />
            (мелодрама, комедия)
        </span>
        <span class="gray_text"><a class="lined" href="/name/91625/">Грегори Пек</a>, <a class="lined" href="/name/135681/">Одри Хепберн</a>, <a class="lined" href="/film/497/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_497" value="8.297"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_497",
                rating:8.297,

                guest:true,

                user_code:'d6e321a1448f98c8153286d9fe563726',
                filmId:497,
                filmName:'Римские каникулы'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/497/votes/" class="all">8.297 <span>(72&nbsp;377)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.297</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.10<small style="display: block; margin-top: -1px">105&nbsp;861</small></div>



        <div id="user_vote_497" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_497"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_497" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_371" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">86</div>
        <a class="bottom_marg" href="/film/371/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/371.jpg"  style="border:3px solid #ccc" alt="Спасти рядового Райана (Saving Private Ryan1998)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/371/" class="all">Спасти рядового Райана</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Saving Private Ryan (1998) <nobr>169 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/22260/">Стивен Спилберг</a></i><br />
            (драма, военный)
        </span>
        <span class="gray_text"><a class="lined" href="/name/9144/">Том Хэнкс</a>, <a class="lined" href="/name/8517/">Том Сайзмор</a>, <a class="lined" href="/film/371/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_371" value="8.180"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_371",
                rating:8.180,

                guest:true,

                user_code:'0a22b9757fc9b125f917492a7d09e714',
                filmId:371,
                filmName:'Спасти рядового Райана'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/371/votes/" class="all">8.180 <span>(155&nbsp;904)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.296</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.60<small style="display: block; margin-top: -1px">933&nbsp;364</small></div>



        <div id="user_vote_371" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_371"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_371" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_3561" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">87</div>
        <a class="bottom_marg" href="/film/3561/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/3561.jpg"  style="border:3px solid #ccc" alt="Дневник памяти (The Notebook2004)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/3561/" class="all">Дневник памяти</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">The Notebook (2004) <nobr>124 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/11371/">Ник Кассаветис</a></i><br />
            (драма, мелодрама)
        </span>
        <span class="gray_text"><a class="lined" href="/name/10143/">Райан Гослинг</a>, <a class="lined" href="/name/36310/">Рэйчел МакАдамс</a>, <a class="lined" href="/film/3561/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_3561" value="8.266"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_3561",
                rating:8.266,

                guest:true,

                user_code:'0284be982ff26f716db7232165418c9e',
                filmId:3561,
                filmName:'Дневник памяти'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/3561/votes/" class="all">8.266 <span>(206&nbsp;990)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.295</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 7.90<small style="display: block; margin-top: -1px">417&nbsp;216</small></div>

        <div title="Оценка enmishka" class="userVote"><p class="all">9</p></div>


        <div id="user_vote_3561" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_3561"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_3561" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_5167" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">88</div>
        <a class="bottom_marg" href="/film/5167/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/5167.jpg"  style="border:3px solid #ccc" alt="Эффект бабочки (The Butterfly Effect2003)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div><div style="float: left; margin: 0 2px 5px 0" class="flag flag6"><a href="/lists/m_act%5Bcountry%5D/6/" title="Канада"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/5167/" class="all">Эффект бабочки</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">The Butterfly Effect (2003) <nobr>113 мин.</nobr></span></div>
        <span class="gray_text">
            США...
            <i>реж. <a class="lined" href="/name/30650/">Эрик Бресс</a>...</i><br />
            (фантастика, триллер)
        </span>
        <span class="gray_text"><a class="lined" href="/name/10633/">Эштон Кутчер</a>, <a class="lined" href="/name/9696/">Эми Смарт</a>, <a class="lined" href="/film/5167/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_5167" value="8.173"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_5167",
                rating:8.173,

                guest:true,

                user_code:'d61235ac97677662cbe56af6187d7d7b',
                filmId:5167,
                filmName:'Эффект бабочки'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/5167/votes/" class="all">8.173 <span>(275&nbsp;813)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.285</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 7.70<small style="display: block; margin-top: -1px">370&nbsp;845</small></div>

        <div title="Оценка enmishka" class="userVote"><p class="all">8</p></div>


        <div id="user_vote_5167" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_5167"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_5167" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_596125" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">89</div>
        <a class="bottom_marg" href="/film/596125/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/596125.jpg"  style="border:3px solid #ccc" alt="Гонка (Rush2013)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag11"><a href="/lists/m_act%5Bcountry%5D/11/" title="Великобритания"></a></div><div style="float: left; margin: 0 2px 5px 0" class="flag flag3"><a href="/lists/m_act%5Bcountry%5D/3/" title="Германия"></a></div><div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/596125/" class="all">Гонка</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Rush (2013) <nobr>123 мин.</nobr></span></div>
        <span class="gray_text">
            Великобритания...
            <i>реж. <a class="lined" href="/name/8919/">Рон Ховард</a></i><br />
            (спорт, драма, биография)
        </span>
        <span class="gray_text"><a class="lined" href="/name/1300401/">Крис Хемсворт</a>, <a class="lined" href="/name/242467/">Даниэль Брюль</a>, <a class="lined" href="/film/596125/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_596125" value="8.091"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_596125",
                rating:8.091,

                guest:true,

                user_code:'4076574c5e5626621a60be8cd5b5bb87',
                filmId:596125,
                filmName:'Гонка'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/596125/votes/" class="all">8.091 <span>(114&nbsp;399)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.285</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.10<small style="display: block; margin-top: -1px">309&nbsp;210</small></div>

        <div title="Оценка enmishka" class="userVote"><p class="all">6</p></div>


        <div id="user_vote_596125" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_596125"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_596125" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_126196" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">90</div>
        <a class="bottom_marg" href="/film/126196/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/126196.jpg"  style="border:3px solid #ccc" alt="Жизнь других (Das Leben der Anderen2006)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag3"><a href="/lists/m_act%5Bcountry%5D/3/" title="Германия"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/126196/" class="all">Жизнь других</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Das Leben der Anderen (2006) <nobr>137 мин.</nobr></span></div>
        <span class="gray_text">
            Германия,
            <i>реж. <a class="lined" href="/name/777631/">Флориан Хенкель фон Доннерсмарк</a></i><br />
            (триллер, драма)
        </span>
        <span class="gray_text"><a class="lined" href="/name/44389/">Ульрих  Мюэ</a>, <a class="lined" href="/name/44393/">Себастьян Кох</a>, <a class="lined" href="/film/126196/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_126196" value="8.057"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_126196",
                rating:8.057,

                guest:true,

                user_code:'eb86216a39027228a3f95046afb81319',
                filmId:126196,
                filmName:'Жизнь других'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/126196/votes/" class="all">8.057 <span>(59&nbsp;119)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.284</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.50<small style="display: block; margin-top: -1px">273&nbsp;193</small></div>



        <div id="user_vote_126196" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_126196"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_126196" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_5502" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">91</div>
        <a class="bottom_marg" href="/film/5502/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/5502.jpg"  style="border:3px solid #ccc" alt="Назад в будущее&nbsp;2 (Back to the Future Part II1989)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/5502/" class="all">Назад в будущее&nbsp;2</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Back to the Future Part II (1989) <nobr>108 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/2435/">Роберт Земекис</a></i><br />
            (фантастика, боевик, комедия...)
        </span>
        <span class="gray_text"><a class="lined" href="/name/181/">Майкл Дж. Фокс</a>, <a class="lined" href="/name/3514/">Кристофер Ллойд</a>, <a class="lined" href="/film/5502/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_5502" value="8.288"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_5502",
                rating:8.288,

                guest:true,

                user_code:'ea0137aaa8e6fb57f0103beca9c8418e',
                filmId:5502,
                filmName:'Назад в будущее&nbsp;2'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/5502/votes/" class="all">8.288 <span>(202&nbsp;452)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.280</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 7.80<small style="display: block; margin-top: -1px">362&nbsp;167</small></div>



        <div id="user_vote_5502" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_5502"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_5502" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_49684" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">92</div>
        <a class="bottom_marg" href="/film/49684/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/49684.jpg"  style="border:3px solid #ccc" alt="Ходячий замок (Hauru no ugoku shiro2004)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag9"><a href="/lists/m_act%5Bcountry%5D/9/" title="Япония"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/49684/" class="all">Ходячий замок</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Hauru no ugoku shiro (2004) <nobr>119 мин.</nobr></span></div>
        <span class="gray_text">
            Япония,
            <i>реж. <a class="lined" href="/name/47753/">Хаяо Миядзаки</a></i><br />
            (аниме, мультфильм, фантастика...)
        </span>
        <span class="gray_text"><a class="lined" href="/name/321406/">Тиэко Байсё</a>, <a class="lined" href="/name/226483/">Такуя Кимура</a>, <a class="lined" href="/film/49684/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_49684" value="8.281"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_49684",
                rating:8.281,

                guest:true,

                user_code:'9fef19917ef63e996b477edc81ba05f3',
                filmId:49684,
                filmName:'Ходячий замок'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/49684/votes/" class="all">8.281 <span>(135&nbsp;479)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.279</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.20<small style="display: block; margin-top: -1px">230&nbsp;683</small></div>



        <div id="user_vote_49684" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_49684"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_49684" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_437410" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">93</div>
        <a class="bottom_marg" href="/film/437410/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/437410.jpg"  style="border:3px solid #ccc" alt="Темный рыцарь: Возрождение легенды (The Dark Knight Rises2012)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div><div style="float: left; margin: 0 2px 5px 0" class="flag flag11"><a href="/lists/m_act%5Bcountry%5D/11/" title="Великобритания"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/437410/" class="all">Темный рыцарь: Возрождение легенды</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">The Dark Knight Rises (2012) <nobr>165 мин.</nobr></span></div>
        <span class="gray_text">
            США...
            <i>реж. <a class="lined" href="/name/41477/">Кристофер Нолан</a></i><br />
            (фантастика, боевик, триллер...)
        </span>
        <span class="gray_text"><a class="lined" href="/name/21495/">Кристиан Бэйл</a>, <a class="lined" href="/name/39984/">Том Харди</a>, <a class="lined" href="/film/437410/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_437410" value="8.144"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_437410",
                rating:8.144,

                guest:true,

                user_code:'3160f766cb752203a933a635dcde48b6',
                filmId:437410,
                filmName:'Темный рыцарь: Возрождение легенды'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/437410/votes/" class="all">8.144 <span>(238&nbsp;009)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.276</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.50<small style="display: block; margin-top: -1px">1&nbsp;208&nbsp;085</small></div>

        <div title="Оценка enmishka" class="userVote"><p class="all">9</p></div>


        <div id="user_vote_437410" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_437410"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_437410" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_354799" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">94</div>
        <a class="bottom_marg" href="/film/354799/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/354799.jpg"  style="border:3px solid #ccc" alt="Шерлок Холмс и доктор Ватсон: Смертельная схватка  (ТВ) (1980)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag13"><a href="/lists/m_act%5Bcountry%5D/13/" title="СССР"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/354799/" class="all">Шерлок Холмс и доктор Ватсон: Смертельная схватка  (ТВ)</a><span style="color: #888; font-family: arial; font-size: 11px; display: block"> (1980) <nobr>64 мин.</nobr></span></div>
        <span class="gray_text">
            СССР,
            <i>реж. <a class="lined" href="/name/284219/">Игорь Масленников</a></i><br />
            (криминал, детектив)
        </span>
        <span class="gray_text"><a class="lined" href="/name/266224/">Василий Ливанов</a>, <a class="lined" href="/name/174122/">Виталий Соломин</a>, <a class="lined" href="/film/354799/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_354799" value="8.446"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_354799",
                rating:8.446,

                guest:true,

                user_code:'9a6e7719f13ece8b6f9edcf3efb973c9',
                filmId:354799,
                filmName:'Шерлок Холмс и доктор Ватсон: Смертельная схватка'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/354799/votes/" class="all">8.446 <span>(66&nbsp;253)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.271</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.70<small style="display: block; margin-top: -1px">1&nbsp;757</small></div>



        <div id="user_vote_354799" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_354799"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_354799" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_397" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">95</div>
        <a class="bottom_marg" href="/film/397/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/397.jpg"  style="border:3px solid #ccc" alt="Амадей (Amadeus1984)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div><div style="float: left; margin: 0 2px 5px 0" class="flag flag8"><a href="/lists/m_act%5Bcountry%5D/8/" title="Франция"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/397/" class="all">Амадей</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Amadeus (1984) <nobr>153 мин.</nobr></span></div>
        <span class="gray_text">
            США...
            <i>реж. <a class="lined" href="/name/20418/">Милош Форман</a></i><br />
            (драма, биография, история...)
        </span>
        <span class="gray_text"><a class="lined" href="/name/85902/">Том Халс</a>, <a class="lined" href="/name/7782/">Ф. Мюррэй Абрахам</a>, <a class="lined" href="/film/397/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_397" value="8.154"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_397",
                rating:8.154,

                guest:true,

                user_code:'4e1531207cebf10d82e04d5b6faa06e6',
                filmId:397,
                filmName:'Амадей'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/397/votes/" class="all">8.154 <span>(39&nbsp;635)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.269</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.30<small style="display: block; margin-top: -1px">287&nbsp;171</small></div>



        <div id="user_vote_397" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_397"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_397" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_43869" class="_NO_HIGHLIGHT_ active_f">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">96</div>
        <a class="bottom_marg" href="/film/43869/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/43869.jpg"  style="border:3px solid #ccc" alt="Служебный роман (1977)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag13"><a href="/lists/m_act%5Bcountry%5D/13/" title="СССР"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/43869/" class="all">Служебный роман</a><span style="color: #888; font-family: arial; font-size: 11px; display: block"> (1977) <nobr>159 мин.</nobr></span></div>
        <span class="gray_text">
            СССР,
            <i>реж. <a class="lined" href="/name/224619/">Эльдар Рязанов</a></i><br />
            (мелодрама, комедия)
        </span>
        <span class="gray_text"><a class="lined" href="/name/231205/">Андрей Мягков</a>, <a class="lined" href="/name/174262/">Алиса Фрейндлих</a>, <a class="lined" href="/film/43869/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_43869" value="8.288"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_43869",
                rating:8.288,

                guest:true,

                user_code:'9f1ef613faf476e99ba68d430207cf06',
                filmId:43869,
                filmName:'Служебный роман'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/43869/votes/" class="all">8.288 <span>(158&nbsp;069)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.267</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.50<small style="display: block; margin-top: -1px">5&nbsp;372</small></div>

        <div title="Оценка enmishka" class="userVote"><p class="all">9</p></div>


        <div id="user_vote_43869" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_43869"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_43869" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_86326" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">97</div>
        <a class="bottom_marg" href="/film/86326/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/86326.jpg"  style="border:3px solid #ccc" alt="Счастливое число Слевина (Lucky Number Slevin2005)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag3"><a href="/lists/m_act%5Bcountry%5D/3/" title="Германия"></a></div><div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/86326/" class="all">Счастливое число Слевина</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Lucky Number Slevin (2005) <nobr>110 мин.</nobr></span></div>
        <span class="gray_text">
            Германия...
            <i>реж. <a class="lined" href="/name/14359/">Пол МакГиган</a></i><br />
            (триллер, драма, криминал...)
        </span>
        <span class="gray_text"><a class="lined" href="/name/206/">Джош Хартнетт</a>, <a class="lined" href="/name/110/">Брюс Уиллис</a>, <a class="lined" href="/film/86326/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_86326" value="8.119"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_86326",
                rating:8.119,

                guest:true,

                user_code:'4f4f85da84145f9d525fc0aa672daeaf',
                filmId:86326,
                filmName:'Счастливое число Слевина'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/86326/votes/" class="all">8.119 <span>(187&nbsp;502)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.265</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 7.80<small style="display: block; margin-top: -1px">264&nbsp;335</small></div>



        <div id="user_vote_86326" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_86326"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_86326" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_281251" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">98</div>
        <a class="bottom_marg" href="/film/281251/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/281251.jpg"  style="border:3px solid #ccc" alt="Мальчик в полосатой пижаме (The Boy in the Striped Pyjamas2008)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag11"><a href="/lists/m_act%5Bcountry%5D/11/" title="Великобритания"></a></div><div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/281251/" class="all">Мальчик в полосатой пижаме</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">The Boy in the Striped Pyjamas (2008) <nobr>90 мин.</nobr></span></div>
        <span class="gray_text">
            Великобритания...
            <i>реж. <a class="lined" href="/name/32397/">Марк Херман</a></i><br />
            (драма, военный)
        </span>
        <span class="gray_text"><a class="lined" href="/name/1268067/">Эйса Баттерфилд</a>, <a class="lined" href="/name/1306292/">Джек Скэнлон</a>, <a class="lined" href="/film/281251/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_281251" value="8.177"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_281251",
                rating:8.177,

                guest:true,

                user_code:'aaeabb9b1a663cfe9f1b4c3541329e96',
                filmId:281251,
                filmName:'Мальчик в полосатой пижаме'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/281251/votes/" class="all">8.177 <span>(122&nbsp;527)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.262</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 7.80<small style="display: block; margin-top: -1px">131&nbsp;086</small></div>



        <div id="user_vote_281251" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_281251"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_281251" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_42770" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">99</div>
        <a class="bottom_marg" href="/film/42770/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/42770.jpg"  style="border:3px solid #ccc" alt="Они сражались за Родину (1975)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag13"><a href="/lists/m_act%5Bcountry%5D/13/" title="СССР"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/42770/" class="all">Они сражались за Родину</a><span style="color: #888; font-family: arial; font-size: 11px; display: block"> (1975) <nobr>160 мин.</nobr></span></div>
        <span class="gray_text">
            СССР,
            <i>реж. <a class="lined" href="/name/174228/">Сергей Бондарчук</a></i><br />
            (драма, военный)
        </span>
        <span class="gray_text"><a class="lined" href="/name/192745/">Василий Шукшин</a>, <a class="lined" href="/name/101751/">Вячеслав Тихонов</a>, <a class="lined" href="/film/42770/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_42770" value="8.375"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_42770",
                rating:8.375,

                guest:true,

                user_code:'ea5a83e636b38d0de13876afacdc7ea5',
                filmId:42770,
                filmName:'Они сражались за Родину'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/42770/votes/" class="all">8.375 <span>(37&nbsp;719)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.255</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.10<small style="display: block; margin-top: -1px">1&nbsp;428</small></div>



        <div id="user_vote_42770" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_42770"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_42770" type="film" style=""></div>
    </td>
</tr>

<tr id="tr_489" class="_NO_HIGHLIGHT_">
    <td style="width: 20px">&nbsp;</td>
    <td valign="top" style="width: 65px; padding: 28px 0 28px 10px">
        <div class="num rangImp">100</div>
        <a class="bottom_marg" href="/film/489/"><img class="flap_img" src="https://st.kp.yandex.net/images/spacer.gif" title="/images/sm_film/489.jpg"  style="border:3px solid #ccc" alt="Свидетель обвинения (Witness for the Prosecution1957)" width=52></a>
        <div style="float: left; margin: 0 2px 5px 0" class="flag flag1"><a href="/lists/m_act%5Bcountry%5D/1/" title="США"></a></div>
    </td>
    <td valign=top class=news style="padding: 28px 0 28px 10px">
        <div style="margin-bottom: 9px"><a style="font-size: 13px; font-weight: bold" href="/film/489/" class="all">Свидетель обвинения</a><span style="color: #888; font-family: arial; font-size: 11px; display: block">Witness for the Prosecution (1957) <nobr>116 мин.</nobr></span></div>
        <span class="gray_text">
            США,
            <i>реж. <a class="lined" href="/name/93354/">Билли Уайлдер</a></i><br />
            (триллер, драма, криминал...)
        </span>
        <span class="gray_text"><a class="lined" href="/name/74882/">Тайрон Пауэр</a>, <a class="lined" href="/name/2907/">Марлен Дитрих</a>, <a class="lined" href="/film/489/cast/#actor">...</a></span>
        <span class="gray_text"></span>
    </td>
    <td style="width: 219px; vertical-align: top; padding: 28px 6px 0 0">
        <div class="WidgetStars" style="height: 30px; width: 219px; position: relative" id="film_votes_489" value="8.117"></div>
        <script type="text/javascript">
        $(function(){
            KP.Stars.widget({
                divcontainer:"#film_votes_489",
                rating:8.117,

                guest:true,

                user_code:'426d1aed029d3037904ea1d57433cb12',
                filmId:489,
                filmName:'Свидетель обвинения'
            });
        });
        </script>


            <div class="ratingBlockP  ratingGreenBG">
               <a href="/film/489/votes/" class="all">8.117 <span>(10&nbsp;509)</span></a>
            </div>
















        <div style="color: #f60; font-family: arial; position: absolute; margin: 51px 0 0 118px">8.251</div>



        <div style="color: #777; position: absolute; margin: 14px 0 0 118px;  padding-top: 2px;">IMDb: 8.40<small style="display: block; margin-top: -1px">67&nbsp;078</small></div>



        <div id="user_vote_489" title="Моя оценка" class="myVote" style="display: none"><p class="all"></p></div>
        <div class="eye my" title="фильм просмотрен" id="film_eye_489"></div>
        <div class="MyKP_Folder_Select shortselect" id="MyKP_Folder_489" type="film" style=""></div>
    </td>
</tr>


</table>

<script type="text/javascript">
self_url = '/user/4594998/list/1/filtr/all/sort/order/';
ancher = '';
</script>
<div class="navigator">


            <div class="show">
                <u>показывать:</u>
                <select class="navigator_per_page">
                    <option value="10">10</option>
                    <option value="25">25</option>
                    <option value="50">50</option>
                    <option value="75">75</option>
                    <option value="100" selected="selected">100</option>
                    <option value="200">200</option>
                </select>
            </div>



        <ul class="list">


                    <li><span>1</span></li>



                    <li ><a href="/user/4594998/list/1/filtr/all/sort/order/page/2/">2</a></li>



                    <li ><a href="/user/4594998/list/1/filtr/all/sort/order/page/3/">3</a></li>



                    <li ><a href="/user/4594998/list/1/filtr/all/sort/order/page/4/">4</a></li>



                    <li class="arr"><a href="/user/4594998/list/1/filtr/all/sort/order/page/2/">&raquo;</a></li>



                    <li class="arr"><a href="/user/4594998/list/1/filtr/all/sort/order/page/5/">&raquo;&raquo;</a></li>


        </ul>

    <div class="pagesFromTo">1&mdash;100 из 500</div>
</div>


<table><tr><td>


        </table>
        </td>
        <!-- Правая сторона -->

<td height="100%" bgcolor="#ffffff" valign="top" class="_noreachbanner_" id="block_right_wrapper">
<div id="block_right" class="right-sidebar no_padds">

<!-- right_banner start -->
<div class="rightTeaser">
    <a href=https://www.kinopoisk.ru/quiz/1594/?kpmain_teaserspecial_vremya28032017 target='_blank'>
        <img src='https://st.kp.yandex.net/images/bnnr/9de57c9a.jpg' style='max-width:240px'>

    </a>
</div>
                            <div id="loadb" class="right-sidebar__banner">
                                <script type="text/javascript">
                                    advBlock({
                                        id: 251518,
                                        type: "adfox",
                                        name: "sidebar_top",
                                        adfoxParams: {
                                            pt: "b",
                                            pp: "g",
                                            ps: "cjby",
                                            p2: "fkyg",
                                            pct: "a",
                                            pfc: "a",
                                            pfb: "a"
                                        },
                                        mobileAdfoxParams: {
                                            pp: "g",
                                            ps: "cjzx",
                                            p2: "fkyg",
                                            plp: "a",
                                            pli: "a",
                                            pop: "a"
                                        },
                                        priority: 90,
                                        useCustomStyles: true
                                    });
                                </script>
                            </div>

<!-- right_banner end -->
<style type="text/css">
.genres, .genres * {font-family: tahoma, verdana; font-size: 11px; list-style: none; margin: 0; padding: 0}
.genres {padding-left: 23px}
   .genres dt {color: #333; font-weight: bold; padding: 17px 0}
   .genres dd {color: #555; position: relative; padding: 0 0 8px 23px}
   .genres .flag {position: absolute; top: 2px; left: -17px}
   .genres input {position: absolute; top: 1px; left: 4px}
   .genres .act {color: #f60; font-weight: bold}
   .genres .button {padding-top: 10px; padding-left: 0}
   .genres .button input {width: 125px; color: #777; cursor: pointer; position: static; padding: 1px 0 2px 0}

.genres {width: 120px; float: left; padding: 0}
.genres .act, .countries .act {color: #ff6600; font-weight: 700}
.genres dt {padding-top: 5px}
.genres dd {padding-left: 19px; white-space: nowrap}
.genres dd input {left: 0}
.countries dt {padding-left: 21px}
.countries dd {padding-left: 40px}
.countries dd .flag {left: 0}
.countries dd input {left: 21px}
.button_genres_countries {clear: left; padding: 10px 0 0 50px}
.button_genres_countries input {width: 125px; color: #777; font-family: tahoma, verdana; font-size: 11px; padding: 1px 0 2px 0; margin-bottom: 20px}
</style>

<form name="genre_country" action="/user/4594998/list/1/" method="post" style="width: 240px">
    <input name="_filtr" type="hidden" value="all" />
    <input name="_sort" type="hidden" value="order" />
    <input name="_ord" type="hidden" value="" />

        <dl class="genres">
            <dt>Жанры:</dt>

                <dd>
                    <input type="checkbox" name="_genre[1750]" value="1750" />
                    <a href="/user/4594998/list/1/filtr/all/sort/order/genre%5B1750%5D/1750/" class="all" style="color:#555;">аниме</a>&nbsp;(15)
                </dd>

                <dd>
                    <input type="checkbox" name="_genre[22]" value="22" />
                    <a href="/user/4594998/list/1/filtr/all/sort/order/genre%5B22%5D/22/" class="all" style="color:#555;">биография</a>&nbsp;(45)
                </dd>

                <dd>
                    <input type="checkbox" name="_genre[3]" value="3" />
                    <a href="/user/4594998/list/1/filtr/all/sort/order/genre%5B3%5D/3/" class="all" style="color:#555;">боевик</a>&nbsp;(57)
                </dd>

                <dd>
                    <input type="checkbox" name="_genre[13]" value="13" />
                    <a href="/user/4594998/list/1/filtr/all/sort/order/genre%5B13%5D/13/" class="all" style="color:#555;">вестерн</a>&nbsp;(13)
                </dd>

                <dd>
                    <input type="checkbox" name="_genre[19]" value="19" />
                    <a href="/user/4594998/list/1/filtr/all/sort/order/genre%5B19%5D/19/" class="all" style="color:#555;">военный</a>&nbsp;(63)
                </dd>

                <dd>
                    <input type="checkbox" name="_genre[17]" value="17" />
                    <a href="/user/4594998/list/1/filtr/all/sort/order/genre%5B17%5D/17/" class="all" style="color:#555;">детектив</a>&nbsp;(58)
                </dd>

                <dd>
                    <input type="checkbox" name="_genre[8]" value="8" />
                    <a href="/user/4594998/list/1/filtr/all/sort/order/genre%5B8%5D/8/" class="all" style="color:#555;">драма</a>&nbsp;(355)
                </dd>

                <dd>
                    <input type="checkbox" name="_genre[23]" value="23" />
                    <a href="/user/4594998/list/1/filtr/all/sort/order/genre%5B23%5D/23/" class="all" style="color:#555;">история</a>&nbsp;(23)
                </dd>

                <dd>
                    <input type="checkbox" name="_genre[6]" value="6" />
                    <a href="/user/4594998/list/1/filtr/all/sort/order/genre%5B6%5D/6/" class="all" style="color:#555;">комедия</a>&nbsp;(137)
                </dd>

                <dd>
                    <input type="checkbox" name="_genre[16]" value="16" />
                    <a href="/user/4594998/list/1/filtr/all/sort/order/genre%5B16%5D/16/" class="all" style="color:#555;">криминал</a>&nbsp;(90)
                </dd>

                <dd>
                    <input type="checkbox" name="_genre[7]" value="7" />
                    <a href="/user/4594998/list/1/filtr/all/sort/order/genre%5B7%5D/7/" class="all" style="color:#555;">мелодрама</a>&nbsp;(114)
                </dd>

                <dd>
                    <input type="checkbox" name="_genre[21]" value="21" />
                    <a href="/user/4594998/list/1/filtr/all/sort/order/genre%5B21%5D/21/" class="all" style="color:#555;">музыка</a>&nbsp;(23)
                </dd>

                <dd>
                    <input type="checkbox" name="_genre[14]" value="14" />
                    <a href="/user/4594998/list/1/filtr/all/sort/order/genre%5B14%5D/14/" class="all" style="color:#555;">мультфильм</a>&nbsp;(55)
                </dd>

                <dd>
                    <input type="checkbox" name="_genre[9]" value="9" />
                    <a href="/user/4594998/list/1/filtr/all/sort/order/genre%5B9%5D/9/" class="all" style="color:#555;">мюзикл</a>&nbsp;(22)
                </dd>

                <dd>
                    <input type="checkbox" name="_genre[10]" value="10" />
                    <a href="/user/4594998/list/1/filtr/all/sort/order/genre%5B10%5D/10/" class="all" style="color:#555;">приключения</a>&nbsp;(97)
                </dd>

                <dd>
                    <input type="checkbox" name="_genre[11]" value="11" />
                    <a href="/user/4594998/list/1/filtr/all/sort/order/genre%5B11%5D/11/" class="all" style="color:#555;">семейный</a>&nbsp;(66)
                </dd>

                <dd>
                    <input type="checkbox" name="_genre[24]" value="24" />
                    <a href="/user/4594998/list/1/filtr/all/sort/order/genre%5B24%5D/24/" class="all" style="color:#555;">спорт</a>&nbsp;(15)
                </dd>

                <dd>
                    <input type="checkbox" name="_genre[4]" value="4" />
                    <a href="/user/4594998/list/1/filtr/all/sort/order/genre%5B4%5D/4/" class="all" style="color:#555;">триллер</a>&nbsp;(74)
                </dd>

                <dd>
                    <input type="checkbox" name="_genre[1]" value="1" />
                    <a href="/user/4594998/list/1/filtr/all/sort/order/genre%5B1%5D/1/" class="all" style="color:#555;">ужасы</a>&nbsp;(7)
                </dd>

                <dd>
                    <input type="checkbox" name="_genre[2]" value="2" />
                    <a href="/user/4594998/list/1/filtr/all/sort/order/genre%5B2%5D/2/" class="all" style="color:#555;">фантастика</a>&nbsp;(46)
                </dd>

                <dd>
                    <input type="checkbox" name="_genre[18]" value="18" />
                    <a href="/user/4594998/list/1/filtr/all/sort/order/genre%5B18%5D/18/" class="all" style="color:#555;">фильм-нуар</a>&nbsp;(3)
                </dd>

                <dd>
                    <input type="checkbox" name="_genre[5]" value="5" />
                    <a href="/user/4594998/list/1/filtr/all/sort/order/genre%5B5%5D/5/" class="all" style="color:#555;">фэнтези</a>&nbsp;(66)
                </dd>

        </dl>


        <dl class="genres countries">
        <dt>Страны:</dt>

            <dd>
                <div class="flag flag25"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B25%5D/25/"></a></div>
                <input type="checkbox" name="_country[25]" value="25" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B25%5D/25/" class="all" style="color:#555;">Австралия</a>&nbsp;(5)
            </dd>

            <dd>
                <div class="flag flag57"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B57%5D/57/"></a></div>
                <input type="checkbox" name="_country[57]" value="57" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B57%5D/57/" class="all" style="color:#555;">Австрия</a>&nbsp;(3)
            </dd>

            <dd>
                <div class="flag flag24"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B24%5D/24/"></a></div>
                <input type="checkbox" name="_country[24]" value="24" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B24%5D/24/" class="all" style="color:#555;">Аргентина</a>&nbsp;(1)
            </dd>

            <dd>
                <div class="flag flag69"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B69%5D/69/"></a></div>
                <input type="checkbox" name="_country[69]" value="69" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B69%5D/69/" class="all" style="color:#555;">Беларусь</a>&nbsp;(2)
            </dd>

            <dd>
                <div class="flag flag41"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B41%5D/41/"></a></div>
                <input type="checkbox" name="_country[41]" value="41" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B41%5D/41/" class="all" style="color:#555;">Бельгия</a>&nbsp;(3)
            </dd>

            <dd>
                <div class="flag flag63"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B63%5D/63/"></a></div>
                <input type="checkbox" name="_country[63]" value="63" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B63%5D/63/" class="all" style="color:#555;">Болгария</a>&nbsp;(1)
            </dd>

            <dd>
                <div class="flag flag10"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B10%5D/10/"></a></div>
                <input type="checkbox" name="_country[10]" value="10" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B10%5D/10/" class="all" style="color:#555;">Бразилия</a>&nbsp;(1)
            </dd>

            <dd>
                <div class="flag flag11"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B11%5D/11/"></a></div>
                <input type="checkbox" name="_country[11]" value="11" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B11%5D/11/" class="all" style="color:#555;">Великобри...</a>&nbsp;(55)
            </dd>

            <dd>
                <div class="flag flag49"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B49%5D/49/"></a></div>
                <input type="checkbox" name="_country[49]" value="49" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B49%5D/49/" class="all" style="color:#555;">Венгрия</a>&nbsp;(1)
            </dd>

            <dd>
                <div class="flag flag3"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B3%5D/3/"></a></div>
                <input type="checkbox" name="_country[3]" value="3" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B3%5D/3/" class="all" style="color:#555;">Германия</a>&nbsp;(35)
            </dd>

            <dd>
                <div class="flag flag60"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B60%5D/60/"></a></div>
                <input type="checkbox" name="_country[60]" value="60" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B60%5D/60/" class="all" style="color:#555;">Германия ...</a>&nbsp;(3)
            </dd>

            <dd>
                <div class="flag flag18"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B18%5D/18/"></a></div>
                <input type="checkbox" name="_country[18]" value="18" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B18%5D/18/" class="all" style="color:#555;">Германия ...</a>&nbsp;(7)
            </dd>

            <dd>
                <div class="flag flag28"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B28%5D/28/"></a></div>
                <input type="checkbox" name="_country[28]" value="28" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B28%5D/28/" class="all" style="color:#555;">Гонконг</a>&nbsp;(4)
            </dd>

            <dd>
                <div class="flag flag55"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B55%5D/55/"></a></div>
                <input type="checkbox" name="_country[55]" value="55" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B55%5D/55/" class="all" style="color:#555;">Греция</a>&nbsp;(1)
            </dd>

            <dd>
                <div class="flag flag61"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B61%5D/61/"></a></div>
                <input type="checkbox" name="_country[61]" value="61" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B61%5D/61/" class="all" style="color:#555;">Грузия</a>&nbsp;(1)
            </dd>

            <dd>
                <div class="flag flag4"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B4%5D/4/"></a></div>
                <input type="checkbox" name="_country[4]" value="4" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B4%5D/4/" class="all" style="color:#555;">Дания</a>&nbsp;(4)
            </dd>

            <dd>
                <div class="flag flag29"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B29%5D/29/"></a></div>
                <input type="checkbox" name="_country[29]" value="29" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B29%5D/29/" class="all" style="color:#555;">Индия</a>&nbsp;(6)
            </dd>

            <dd>
                <div class="flag flag38"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B38%5D/38/"></a></div>
                <input type="checkbox" name="_country[38]" value="38" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B38%5D/38/" class="all" style="color:#555;">Ирландия</a>&nbsp;(3)
            </dd>

            <dd>
                <div class="flag flag37"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B37%5D/37/"></a></div>
                <input type="checkbox" name="_country[37]" value="37" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B37%5D/37/" class="all" style="color:#555;">Исландия</a>&nbsp;(2)
            </dd>

            <dd>
                <div class="flag flag15"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B15%5D/15/"></a></div>
                <input type="checkbox" name="_country[15]" value="15" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B15%5D/15/" class="all" style="color:#555;">Испания</a>&nbsp;(6)
            </dd>

            <dd>
                <div class="flag flag14"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B14%5D/14/"></a></div>
                <input type="checkbox" name="_country[14]" value="14" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B14%5D/14/" class="all" style="color:#555;">Италия</a>&nbsp;(31)
            </dd>

            <dd>
                <div class="flag flag6"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B6%5D/6/"></a></div>
                <input type="checkbox" name="_country[6]" value="6" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B6%5D/6/" class="all" style="color:#555;">Канада</a>&nbsp;(11)
            </dd>

            <dd>
                <div class="flag flag31"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B31%5D/31/"></a></div>
                <input type="checkbox" name="_country[31]" value="31" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B31%5D/31/" class="all" style="color:#555;">Китай</a>&nbsp;(4)
            </dd>

            <dd>
                <div class="flag flag26"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B26%5D/26/"></a></div>
                <input type="checkbox" name="_country[26]" value="26" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B26%5D/26/" class="all" style="color:#555;">Корея Южная</a>&nbsp;(4)
            </dd>

            <dd>
                <div class="flag flag59"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B59%5D/59/"></a></div>
                <input type="checkbox" name="_country[59]" value="59" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B59%5D/59/" class="all" style="color:#555;">Люксембург</a>&nbsp;(2)
            </dd>

            <dd>
                <div class="flag flag111"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B111%5D/111/"></a></div>
                <input type="checkbox" name="_country[111]" value="111" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B111%5D/111/" class="all" style="color:#555;">Мальта</a>&nbsp;(1)
            </dd>

            <dd>
                <div class="flag flag17"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B17%5D/17/"></a></div>
                <input type="checkbox" name="_country[17]" value="17" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B17%5D/17/" class="all" style="color:#555;">Мексика</a>&nbsp;(2)
            </dd>

            <dd>
                <div class="flag flag12"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B12%5D/12/"></a></div>
                <input type="checkbox" name="_country[12]" value="12" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B12%5D/12/" class="all" style="color:#555;">Нидерланды</a>&nbsp;(2)
            </dd>

            <dd>
                <div class="flag flag35"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B35%5D/35/"></a></div>
                <input type="checkbox" name="_country[35]" value="35" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B35%5D/35/" class="all" style="color:#555;">Новая Зел...</a>&nbsp;(7)
            </dd>

            <dd>
                <div class="flag flag33"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B33%5D/33/"></a></div>
                <input type="checkbox" name="_country[33]" value="33" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B33%5D/33/" class="all" style="color:#555;">Норвегия</a>&nbsp;(2)
            </dd>

            <dd>
                <div class="flag flag119"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B119%5D/119/"></a></div>
                <input type="checkbox" name="_country[119]" value="119" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B119%5D/119/" class="all" style="color:#555;">ОАЭ</a>&nbsp;(1)
            </dd>

            <dd>
                <div class="flag flag32"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B32%5D/32/"></a></div>
                <input type="checkbox" name="_country[32]" value="32" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B32%5D/32/" class="all" style="color:#555;">Польша</a>&nbsp;(7)
            </dd>

            <dd>
                <div class="flag flag2"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B2%5D/2/"></a></div>
                <input type="checkbox" name="_country[2]" value="2" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B2%5D/2/" class="all" style="color:#555;">Россия</a>&nbsp;(9)
            </dd>

            <dd>
                <div class="flag flag46"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B46%5D/46/"></a></div>
                <input type="checkbox" name="_country[46]" value="46" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B46%5D/46/" class="all" style="color:#555;">Румыния</a>&nbsp;(1)
            </dd>

            <dd>
                <div class="flag flag177"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B177%5D/177/"></a></div>
                <input type="checkbox" name="_country[177]" value="177" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B177%5D/177/" class="all" style="color:#555;">Сербия</a>&nbsp;(1)
            </dd>

            <dd>
                <div class="flag flag13"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B13%5D/13/"></a></div>
                <input type="checkbox" name="_country[13]" value="13" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B13%5D/13/" class="all" style="color:#555;">СССР</a>&nbsp;(108)
            </dd>

            <dd>
                <div class="flag flag1"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B1%5D/1/"></a></div>
                <input type="checkbox" name="_country[1]" value="1" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B1%5D/1/" class="all" style="color:#555;">США</a>&nbsp;(280)
            </dd>

            <dd>
                <div class="flag flag27"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B27%5D/27/"></a></div>
                <input type="checkbox" name="_country[27]" value="27" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B27%5D/27/" class="all" style="color:#555;">Тайвань</a>&nbsp;(1)
            </dd>

            <dd>
                <div class="flag flag7"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B7%5D/7/"></a></div>
                <input type="checkbox" name="_country[7]" value="7" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B7%5D/7/" class="all" style="color:#555;">Финляндия</a>&nbsp;(2)
            </dd>

            <dd>
                <div class="flag flag8"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B8%5D/8/"></a></div>
                <input type="checkbox" name="_country[8]" value="8" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B8%5D/8/" class="all" style="color:#555;">Франция</a>&nbsp;(50)
            </dd>

            <dd>
                <div class="flag flag34"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B34%5D/34/"></a></div>
                <input type="checkbox" name="_country[34]" value="34" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B34%5D/34/" class="all" style="color:#555;">Чехия</a>&nbsp;(3)
            </dd>

            <dd>
                <div class="flag flag21"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B21%5D/21/"></a></div>
                <input type="checkbox" name="_country[21]" value="21" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B21%5D/21/" class="all" style="color:#555;">Швейцария</a>&nbsp;(4)
            </dd>

            <dd>
                <div class="flag flag5"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B5%5D/5/"></a></div>
                <input type="checkbox" name="_country[5]" value="5" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B5%5D/5/" class="all" style="color:#555;">Швеция</a>&nbsp;(7)
            </dd>

            <dd>
                <div class="flag flag53"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B53%5D/53/"></a></div>
                <input type="checkbox" name="_country[53]" value="53" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B53%5D/53/" class="all" style="color:#555;">Эстония</a>&nbsp;(1)
            </dd>

            <dd>
                <div class="flag flag30"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B30%5D/30/"></a></div>
                <input type="checkbox" name="_country[30]" value="30" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B30%5D/30/" class="all" style="color:#555;">ЮАР</a>&nbsp;(1)
            </dd>

            <dd>
                <div class="flag flag19"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B19%5D/19/"></a></div>
                <input type="checkbox" name="_country[19]" value="19" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B19%5D/19/" class="all" style="color:#555;">Югославия</a>&nbsp;(1)
            </dd>

            <dd>
                <div class="flag flag66"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B66%5D/66/"></a></div>
                <input type="checkbox" name="_country[66]" value="66" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B66%5D/66/" class="all" style="color:#555;">Югославия...</a>&nbsp;(2)
            </dd>

            <dd>
                <div class="flag flag9"><a href="/user/4594998/list/1/filtr/all/sort/order/country%5B9%5D/9/"></a></div>
                <input type="checkbox" name="_country[9]" value="9" />
                <a href="/user/4594998/list/1/filtr/all/sort/order/country%5B9%5D/9/" class="all" style="color:#555;">Япония</a>&nbsp;(29)
            </dd>

        </dl>

    <div class="button_genres_countries"><input type="button" value="обновить список" onclick="document.genre_country.submit()" /></div>
</form><dl class="block block_tv">
   <dt><a class="headerLink" href="/tv/"></a>Фильмы на телевидении</dt>
   <dd>
   <form name="right_tv_form" action="/index.php" method="get">
      <input type="hidden" name="level" value="88" />
      <select name="day_view"><option value='2017-03-30' selected='selected'>сегодня</option><option value='2017-03-31' >пт, 31 марта</option><option value='2017-04-01' >сб, 01 апреля</option><option value='2017-04-02' >вс, 02 апреля</option><option value='2017-04-03' >пн, 03 апреля</option></select>
      <span><a href="#" onclick="javascript: document.right_tv_form.submit(); return false">фильмы на ТВ</a> &raquo;</span>
   </form>
   </dd>
   <dd class="more"><a href="/tv/">ТВ-программа</a></dd>
</dl>
<dl class="block block_cash" id="rigth_box_weekend_usa">
   <dt><a class="headerLink" href="/box/type/usa/"></a>Кинокасса США <b>&bull;</b> $ <a href="#" onclick="document.getElementById('rigth_box_weekend_rus').style.visibility='visible'; document.getElementById('rigth_box_weekend_usa').style.visibility='hidden'; return false">Россия</a></dt>
      <dd class="dl"><a href="/film/744987/"><b>1.</b><i><s>Красавица и чудовище</s>Beauty and the Beast</i><u>90&nbsp;426&nbsp;717</u></a></dd>
   <dd class="dl"><a href="/film/841627/"><b>2.</b><i><s>Могучие рейнджеры</s>Power Rangers</i><u>40&nbsp;300&nbsp;288</u></a></dd>
   <dd class="dl"><a href="/film/843147/"><b>3.</b><i><s>Конг: Остров черепа</s>Kong: Skull Island</i><u>14&nbsp;670&nbsp;653</u></a></dd>
   <dd class="dl"><a href="/film/161053/"><b>4.</b><i><s></s>Kong: Skull Island</i><u>12&nbsp;501&nbsp;936</u></a></dd>
   <dd class="dl"><a href="/film/807682/"><b>5.</b><i><s>Логан</s>Logan</i><u>10&nbsp;334&nbsp;390</u></a></dd>

   <dd class="more"><i>24.03&nbsp;&mdash;&nbsp;26.03</i><a href="/box/type/usa/">подробнее</a></dd>
</dl>

<dl class="block block_cash" id="rigth_box_weekend_rus">
   <dt><a class="headerLink" href="/box/"></a>Кинокасса России <b>&bull;</b> руб. <a href="#" onclick="document.getElementById('rigth_box_weekend_usa').style.visibility='visible'; document.getElementById('rigth_box_weekend_rus').style.visibility='hidden'; return false">США</a></dt>
      <dd class="dl"><a href="/film/842567/"><b>1.</b><i><s>Босс-молокосос</s>The Boss Baby</i><u>654&nbsp;195&nbsp;980</u></a></dd>
   <dd class="dl"><a href="/film/966995/"><b>2.</b><i><s>Живое</s>Life</i><u>177&nbsp;952&nbsp;082</u></a></dd>
   <dd class="dl"><a href="/film/744987/"><b>3.</b><i><s>Красавица и чудовище</s>Beauty and the Beast</i><u>174&nbsp;195&nbsp;578</u></a></dd>
   <dd class="dl"><a href="/film/930534/"><b>4.</b><i><s>Сплит</s>Split</i><u>114&nbsp;794&nbsp;707</u></a></dd>
   <dd class="dl"><a href="/film/841627/"><b>5.</b><i><s>Могучие рейнджеры</s>Power Rangers</i><u>47&nbsp;506&nbsp;125</u></a></dd>

   <dd class="more"><i>24.03&nbsp;&mdash;&nbsp;26.03</i><a href="/box/">подробнее</a></dd>
</dl>

<dl class="block block_cashup">
   <dt><a class="headerLink" href="/box/"></a>Результаты уик-энда</dt>

       <dd class="pls">
          <b>Зрители</b><i>5&nbsp;310&nbsp;078</i><u>1&nbsp;575&nbsp;429</u>
          <s class="arr"></s>
          <span><s class="el_4"></s><s class="el_2"></s></span>
       </dd>


       <dd class="pls">
          <b>Деньги</b><i>1&nbsp;321&nbsp;362&nbsp;711 руб.</i><u>331&nbsp;864&nbsp;079</u>
          <s class="arr"></s>
          <span><s class="el_3"></s><s class="el_4"></s></span>
       </dd>


       <dd style="margin: 0 !important" class="ticket mns">
          <b>Цена билета</b><i>248,84 руб.</i><u>16,11</u>

              <s class="arr"></s>
              <span><s class="el_6"></s></span>

       </dd>

   <dd class="more" style="font-family: tahoma, verdana">
      <i style="font-weight: normal; left: 12px">24.03&nbsp;&mdash;&nbsp;26.03</i><a href="/box/">подробнее</a>
   </dd>
</dl>
<dl class="block block_top250">
   <dt><a class="headerLink" href="/top/"></a>Лучшие фильмы &mdash; Top 250</dt>
      <dd class="dl"><a href="/film/8147/"><b>235.</b><i><s>Русалочка</s>The Little Mermaid</i><u>8.059</u></a></dd>

   <dd class="dl"><a href="/film/38145/"><b>236.</b><i><s>История Хатико</s>Hachik&#244; monogatari</i><u>8.059</u></a></dd>

   <dd class="dl"><a href="/film/8227/"><b>237.</b><i><s>Леди и бродяга</s>Lady and the Tramp</i><u>8.058</u></a></dd>

   <dd class="dl"><a href="/film/7660/"><b>238.</b><i><s>Холодное лето пятьдесят третьего...</s></i><u>8.058</u></a></dd>

   <dd class="dl"><a href="/film/89514/"><b>239.</b><i><s>Рататуй</s>Ratatouille</i><u>8.057</u></a></dd>


   <dd class="more"><a href="/top/">лучшие фильмы</a></dd>
</dl>
<dl class="block block_top250">
   <dt><a class="headerLink" href="/comingsoon/"></a>Ожидаемые фильмы</dt>
      <dd class="dl"><a href="/film/970873/"><b>6.</b><i><s>Роковое искушение</s>The Beguiled</i><u>95.99%</u></a></dd>

   <dd class="dl"><a href="/film/931677/"><b>7.</b><i><s>Дюнкерк</s>Dunkirk</i><u>95.82%</u></a></dd>

   <dd class="dl"><a href="/film/589290/"><b>8.</b><i><s>Бегущий по лезвию 2049</s>Blade Runner 2049</i><u>95.61%</u></a></dd>

   <dd class="dl"><a href="/film/824437/"><b>9.</b><i><s>Меч короля Артура</s>King Arthur: Legend of the Sword</i><u>95.46%</u></a></dd>

   <dd class="dl"><a href="/film/695548/"><b>10.</b><i><s>Чужой: Завет</s>Alien: Covenant</i><u>95.02%</u></a></dd>


   <dd class="more"><a href="/comingsoon/">ожидаемые фильмы</a></dd>
</dl>
<dl class="block block_popular">
    <dt><a class="headerLink" href="/popular/"></a>Популярные фильмы</dt>

        <dd class="dl"><a href="/film/843789/">
            <b>1.</b>
            <i><s>Призрак в доспехах</s>Ghost in the Shell</i>
            <u class="up">

                    +
                    2

            </u>
        </a></dd>

        <dd class="dl"><a href="/film/966995/">
            <b>2.</b>
            <i><s>Живое</s>Life</i>
            <u class="down">

                    -
                    1

            </u>
        </a></dd>

        <dd class="dl"><a href="/film/930534/">
            <b>3.</b>
            <i><s>Сплит</s>Split</i>
            <u class="down">

                    -
                    1

            </u>
        </a></dd>

        <dd class="dl"><a href="/film/744987/">
            <b>4.</b>
            <i><s>Красавица и чудовище</s>Beauty and the Beast</i>
            <u>

            </u>
        </a></dd>

        <dd class="dl"><a href="/film/453397/">
            <b>5.</b>
            <i><s>Оно</s>It</i>
            <u class="up">

                    +
                    67

            </u>
        </a></dd>

    <dd class="more"><a href="/popular/">еще фильмы</a></dd>
</dl>
<dl class="block block_review">
   <dt><a class="headerLink" href="/reviews/"></a>Новые рецензии<i>всего</i></dt>
      <dd class="dl"><a href="/film/843789/"><b></b><i><s>Призрак в доспехах</s>Ghost in the Shell</i><u>8</u></a></dd>
   <dd class="dl"><a href="/film/470689/"><b></b><i><s>Пассажиры</s>Passengers</i><u>241</u></a></dd>
   <dd class="dl"><a href="/film/7103/"><b></b><i><s>Назад в будущее&nbsp;3</s>Back to the Future Part III</i><u>62</u></a></dd>
   <dd class="dl"><a href="/film/784389/"><b></b><i><s>Прежде чем мы расстанемся</s>Before We Go</i><u>39</u></a></dd>

   <dd class="more"><a href="/reviews/">все рецензии</a></dd>
</dl>
<dl class="block block_show">
   <dt><a class="headerLink" href="/afisha/new/"></a>Сегодня в кино<i>рейтинг</i></dt>
      <dd class="dl"><a href="/film/843789/"><b></b><i><s>Призрак в доспехах</s>Ghost in the Shell</i><u>6.712</u></a></dd>
   <dd class="dl"><a href="/film/842567/"><b></b><i><s>Босс-молокосос</s>The Boss Baby</i><u>6.578</u></a></dd>
   <dd class="dl"><a href="/film/966995/"><b></b><i><s>Живое</s>Life</i><u>6.741</u></a></dd>
   <dd class="dl"><a href="/film/915111/"><b></b><i><s>Лекарство от здоровья</s>A Cure for Wellness</i><u>6.012</u></a></dd>
   <dd class="dl"><a href="/film/681406/"><b></b><i><s>Смурфики: Затерянная деревня</s>Smurfs: The Lost Village</i><u></u></a></dd>

   <dd class="more"><a href="/afisha/new/">афиша</a></dd>
</dl>
<div class="block_podcast">
   <div class="title"><a href="/podcast/658/">Подкаст &laquo;Полкино&raquo;</a><i>№192</i></div>
   <div class="podcast">
      <div class="gray"></div>
      <object type="application/x-shockwave-flash" data="https://st.kp.yandex.net/js/aplayer.swf" width="200" height="20">
         <param name="movie" value="https://st.kp.yandex.net/js/aplayer.swf" />
         <param name="wmode" value="transparent" />
         <param name="FlashVars" value="mp3=https://st.kp.yandex.net/podcast/658.mp3&amp;bgcolor=cccccc&amp;loadingcolor=ff6600&amp;buttoncolor=ff6600&amp;slidercolor=999999" />
      </object>
      <span class="listening">о премьерах недели с юмором</span>
   </div>
   <span class="more"><a href="/podcast/">все подкасты</a></span>
</div>
<dl class="block block_soon">
   <dt><a class="headerLink" href="/premiere/ru/"></a>Скоро в кино<i>премьера</i></dt>
   <dd class="dl"><a href="/film/885316/"><b></b><i><s>Время первых</s></i><u>06.04</u></a></dd>
   <dd class="dl"><a href="/film/894027/"><b></b><i><s>Форсаж&nbsp;8</s>The Fate of the Furious</i><u>13.04</u></a></dd>
   <dd class="dl"><a href="/film/840261/"><b></b><i><s>Кухня. Последняя битва</s></i><u>20.04</u></a></dd>
   <dd class="dl"><a href="/film/432794/"><b></b><i><s>Затерянный город&nbsp;Z</s>The Lost City of Z</i><u>27.04</u></a></dd>
   <dd class="dl"><a href="/film/909550/"><b></b><i><s>Сфера</s>The Circle</i><u>27.04</u></a></dd>
   <dd class="more"><a href="/premiere/ru/">премьеры</a></dd>
</dl>
<p class="dt">Новости</p>
<table cellspacing=0 cellpadding=0 width=240 border=0>
	<tr>
		<td style="background-color: #f2f2f2; text-align: left; vertical-align: top">
			<div style="background-color: #e3e8f0; padding: 7px">
			<a href="/news/2924878/" class="all"><img src="https://st.kp.yandex.net/images/news/sm_2924878_1490862969.jpg" border=0 width=67 height=50 align=left hspace=5 vspace=2 style="border:1px solid #999"></a>
			<a href="/news/2924878/" class="all">Минкультуры не стало переносить релиз «Форсажа 8»</a> <small style="color: #777">30.03.2017</small></div><br /><div style="padding: 0 10px">Ведомство готово выдать новой части франшизы прокатное удостоверение на 13 апреля, однако «Времени первых» будет отдано максимальное количество сеансов. &nbsp;<a href="/news/2924878/" class="all">(...)</a></div>&nbsp;
		</td>
	</tr>
</table>
<b class="dt_more"><a href="/news/">все новости</a></b>
<script type="text/javascript">
$(function(){
    function showSoctabs(select) {
        $('.tabs_soc').css({'height': '0px', 'overflow': 'hidden'});
        select.css('height', '267px');
    }
    var randomizelt = Math.floor(Math.random()*2);
    if (randomizelt == 0) {
        showSoctabs($('.vk_tabs'));
    } else {
        showSoctabs($('.facebook_tabs'));
    }
    $(".soc_tabs li").eq(randomizelt).addClass('act_soc_tab');
    $(".soc_tabs a").bind("click", function(event){
        event.preventDefault();
        $(".soc_tabs li").removeClass('act_soc_tab');
        $(this).parent().addClass('act_soc_tab');
        if (event.target.id == 'soc_tabs_vk') {
            showSoctabs($('.vk_tabs'));
        } else if(event.target.id == 'soc_tabs_fb') {
            showSoctabs($('.facebook_tabs'));
        } else if(event.target.id == 'soc_tabs_odn') {
            showSoctabs($('.odnoklassniki_tabs'));
        }
    });
});
</script>
<script type="text/javascript" src="//vk.com/js/api/openapi.js?75"></script>
<ul class="soc_tabs clearfix">
    <li class="tabs_vk"><i></i><a id="soc_tabs_vk" href="#">ВКонтакте</a></li>
    <li class="tabs_fb"><i></i><a id="soc_tabs_fb" href="#">Facebook</a></li>
    <li class="tabs_odn"><i></i><a id="soc_tabs_odn" href="#">OK</a></li>
</ul>
<div class="socRight">
    <div class="vk_tabs tabs_soc">
        <div id="vk_groups"></div>
    </div>
    <script type="text/javascript">
        var vkInitRight_status = false;
        function vkInitRight() {
            if (!vkInitRight_status) {
                vkInitRight_status = true;
                VK.Widgets.Group("vk_groups", {mode: 0, width: "217", height: "250"}, 108468);
            }
        }
        if (typeof(VK) !== 'undefined') vkInitRight();
        !function (d, id, did, st) {
            var js = d.createElement("script");
            js.src = "https://connect.ok.ru/connect.js";
            js.onload = js.onreadystatechange = function () {
            if (!this.readyState || this.readyState == "loaded" || this.readyState == "complete") {
              if (!this.executed) {
                this.executed = true;
                setTimeout(function () {
                  OK.CONNECT.insertGroupWidget(id,did,st);
                }, 0);
              }
            }}
            d.documentElement.appendChild(js);
         }(document,"ok_group_widget","52728120934492","{width:240,height:250}");
    </script>
    <div class="facebook_tabs tabs_soc">
        <iframe src="//www.facebook.com/plugins/likebox.php?href=http%3A%2F%2Fwww.facebook.com%2Fkinopoisk&amp;width=244&amp;height=350&amp;colorscheme=light&amp;show_faces=true&amp;border_color=white&amp;stream=false&amp;force_wall=true&amp;header=false"
            scrolling="no" frameborder="0" style="border:none; overflow:hidden; width:244px; height:260px;" allowTransparency="true">
           <style type="text/css">.pluginBoxContainer {border:none !important;}</style>
        </iframe>
    </div>
    <div class="odnoklassniki_tabs tabs_soc" id="ok_group_widget">
    </div>
    <div class="twitter">
        <iframe allowtransparency="true" frameborder="0" scrolling="no"
            src="//platform.twitter.com/widgets/follow_button.html?screen_name=kinopoiskru&lang=en" style="width:232px; height:20px">
        </iframe>
    </div>
</div><div class="randomMovie">
   <div class="title"></div>
   <div class="pic"><a href="/level/1/film/416824/"><img src="https://st.kp.yandex.net/images/chance/953167.jpg" alt="Рок-волна" /><span class="name"><u>Рок-волна</u> The Boat That Rocked, 2009</span></a></div>
   <div class="all"><a href="/chance/"><s></s>другой случайный фильм</a></div>
</div>

    <!-- Яндекс.Директ -->
    <div class="right-sidebar__sticky-ad-banner" id="js-right-sidebar__sticky-ad">
        <script type="text/javascript">
            (function() {
                var isDebug = location.hostname.indexOf('dev.kinopoisk.ru') !== -1;
                var stickyAdBannerId = 'js-right-sidebar__sticky-ad';
                var $stickyAdBanner = $('#' + stickyAdBannerId);
                var MIN_AVAILABLE_HEIGHT = 800;

                function hasAvailableHeight() {
                    var blockRightWrapperHeight = $('#block_right_wrapper').innerHeight();
                    var blockRightHeight = $('#block_right').innerHeight();
                    var availableHeight = Math.round(blockRightWrapperHeight - blockRightHeight);
                    if (availableHeight < MIN_AVAILABLE_HEIGHT && isDebug) {
                        console.log(
                            'Place for #js-right-sidebar__sticky-ad has not enough height for showing (' +
                            availableHeight + 'px < ' + MIN_AVAILABLE_HEIGHT + 'px). ' +
                            'Banner was hidden.'
                        );
                    }
                    return availableHeight >= MIN_AVAILABLE_HEIGHT;
                }

                advBlock({
                    id: isKUB() ? 'R-A-53100-32' : 'R-A-53100-20',
                    mobileId: isKUB() ? 'R-A-53100-36' : undefined,
                    type: 'direct',
                    name: 'sidebar_bottom_sticky',
                    onRender: function () {
                        if (!bd_mobile_detector.isMobile()) {
                            initStickyAdBehaviour();
                        }

                        $('#js-right-sidebar__sticky-ad').show();
                    },
                    shouldRender: function () {
                        return hasAvailableHeight();
                    },
                    useCustomStyles: true,
                    priority: 80
                });

                function initStickyAdBehaviour() {
                    var $stickyAd = $('#js-right-sidebar__sticky-ad');
                    var $blockRightWrapper = $('#block_right_wrapper');
                    var $rightBlock = $('#block_right');
                    var TOP_MENU_HEIGHT = 30;
                    var BOX_MARGIN = 10;
                    $(window).on('scroll', function (evt) {
                        if (!$stickyAdBanner.is(':visible')) {
                            return;
                        }
                        var bottomPos = $blockRightWrapper.offset().top + $blockRightWrapper.height() - BOX_MARGIN;
                        var stickBoxPosition = $rightBlock.offset().top + $rightBlock.height();
                        var scrollTop = $(window).scrollTop() + TOP_MENU_HEIGHT;
                        var stickBoxHeight = $stickyAd.height();
                        var stickedBoxBottomPos = scrollTop + stickBoxHeight + BOX_MARGIN;
                        // decrease height if right block if box fixed
                        if (!$('.right-sidebar__sticky-ad_fixed').length && !$('.right-sidebar__sticky-ad_fixed_bottom').length) {
                            stickBoxPosition = stickBoxPosition - stickBoxHeight - BOX_MARGIN;
                        }
                        // fixed position
                        if (scrollTop >= stickBoxPosition && stickedBoxBottomPos < bottomPos) {
                            $stickyAd.removeClass('right-sidebar__sticky-ad_fixed_bottom');
                            $stickyAd.addClass('right-sidebar__sticky-ad_fixed');
                        // bottom position
                        } else if (scrollTop >= stickBoxPosition && stickedBoxBottomPos >= bottomPos) {
                            $stickyAd.removeClass('right-sidebar__sticky-ad_fixed');
                            $stickyAd.addClass('right-sidebar__sticky-ad_fixed_bottom');
                        // stable position
                        } else if (scrollTop < stickBoxPosition) {
                            $stickyAd.removeClass('right-sidebar__sticky-ad_fixed_bottom');
                            $stickyAd.removeClass('right-sidebar__sticky-ad_fixed');
                        }
                    });
                }
            })();
        </script>
    </div>
</div>
<br /><br /><br /><br /><br /><br />
</td>


<!-- / Правая сторона -->

    </tr>
    </table>

    </div> <!-- content block -->


<div id="footer_wrapper">
    <div id="yandex_direct_D-A-53100-19_D-A-53100-27" class="direct-kp-customize"></div>
    <script type="text/javascript">
        advBlock({
            id: 'D-A-53100-19',
            mobileId: 'D-A-53100-27',
            type: 'direct',
            name: 'before_footer',
            dependsOn: 'sidebar_bottom_sticky',
            renderTo: 'yandex_direct_D-A-53100-19_D-A-53100-27',
            priority: 50
        });
    </script>


    <div id="hot_news_line" data-metrika="other">


                <a href="/news/2920844/" data-metrika="strip">Появился новый трейлер фильма «Лига справедливости»</a>

                <a href="/news/2920122/" data-metrika="strip">Райан Гослинг объяснил причину своего смеха на «Оскарах»</a>

                <a href="/article/2920778/" data-metrika="strip">Семейные узы: 40 важнейших братьев и сестер современного кино</a>

                <a href="/article/2920054/" data-metrika="strip">Невеселая карусель: Почему нашей анимации далеко до Disney и Pixar?</a>

                <a href="/article/2920066/" data-metrika="strip">Мир будущего: Станут ли фильмы о вторжении инопланетян реальностью?</a>

                <a href="/news/2920002/" data-metrika="strip">Появился новый постер фильма «Чужой: Завет»</a>

                <a href="/news/2922844/" data-metrika="strip">Появились официальные кадры из «Лары Крофт»</a>

                <a href="/news/2923856/" data-metrika="strip">Появился новый трейлер фильма «Человек-паук: Возвращение домой»</a>

                <a href="/news/2920938/" data-metrika="strip">Бокс-офис США: «Красавица и чудовище» и самый кассовый март в истории</a>

                <a href="/news/2919325/" data-metrika="strip">«Зверополис» подозревают в плагиате</a>

            <script>
                function context(obj,func){
                    return function(){func(obj);}
                };
                var bestNews = {
                    i: 0,
                    init: function(id) {
                        this.items = $(id);
                        this.item = this.items[this.i];
                        return this;
                    },
                    run: function() {
                        var next = context({obj: this}, function(data){
                            // определить новый
                            data.obj.i++;
                            if (data.obj.i >= data.obj.items.length) {
                                data.obj.i = 0;
                            }
                            data.obj.item = data.obj.items[data.obj.i];

                            var next_run = context({obj: data.obj}, function(data){
                                // запустить занова
                                data.obj.run();
                            });
                            // показать новый
                            //$(data.obj.item).fadeIn('fast', next_run);
                            $(data.obj.item).show('drop', {direction: 'left'}, 1000, next_run);
                        });
                        // скрыть текущий
                        $(this.item).delay(6000).effect('drop', {direction: 'right'}, 1000, next);
                    }
                }
                bestNews.init('#hot_news_line a').run();

            </script>

    </div>

    <div id="footer" class="clearfix">
        <div class="col_footer col_footer_first">
            <h5>Мобильные приложения</h5>
            <ul class="footer_list">
                <li><a href="/iphone/">iPhone & iPad</a></li>
                <li><a href="/android/">Android</a></li>
                <li><a href="/winphone/">Windows Phone</a></li>
                <li><a target="_blank" href="http://apps.microsoft.com/webpdp/ru-ru/app/bd2f563f-0e1e-4bdd-bd34-ed0b18ee9a11">Windows 8</a></li>
                <li><a href="/games/guessmovie/">Игра: Угадай кино!</a></li>

            </ul>
        </div>
        <div class="col_footer">
            <h5><a href="/docs/services/">КиноПоиск в соцсетях</a></h5>
            <ul class="footer_list">
                <li><a href="/docs/facebook/">Facebook</a></li>
                <li><a href="/docs/twitter/">Twitter</a></li>
                <li><a href="/docs/vkontakte/">ВКонтакте</a></li>
                <li><a href="https://instagram.com/kinopoisk" target="_blank">Instagram</a></li>
                <li><a href="https://telegram.me/kinopoisk" target="_blank">Telegram</a></li>
                <li><a href="https://ok.ru/group/52728120934492" target="_blank">Одноклассники</a></li>
            </ul>
        </div>
        <div class="col_footer">
            <h5><a href="/docs/services/">Сервисы</a></h5>
            <ul class="footer_list">
                <li><a href="/docs/services/">Вокруг КиноПоиска</a></li>
                <li><a href="/docs/rss/">RSS</a></li>
                <li><a href="/docs/searchbutton/">Поисковые кнопки</a></li>
                <li><a href="http://mykp.ru">КиноПоиск.Mini</a></li>
                <li><a href="/docs/widgets/">Виджеты</a></li>
            </ul>
        </div>
        <div class="col_footer clearfix">
            <h5>О сайте</h5>
            <ul class="footer_list clearfix">
                <li><a href="/">Главная страница</a></li>
                <li><a target="_blank" href="https://advertising.yandex.ru/media/banner/kinopoisk.xml">Реклама на сайте</a></li>
                <li><a href="http://plus.kinopoisk.ru">КиноПоиск+</a></li>
            </ul>
        </div>
        <div class="footer_img"></div>
        <p class="copyright">&copy; 2003&ndash;2017&nbsp;&nbsp;<a href="/">КиноПоиск</a> • <a href="/feedback/">Книга жалоб и предложений</a> • <a href="/docs/usage/">Условия использования сайта</a> • 18+</p>
    </div>
</div> <!-- END of footer -->
<div id="nav_express">
    <div class="border_left"></div>
        <div class="express">
            <a class="logo_ex" href="/"></a>
			<form  name="searchFormex" action="/index.php" method="get">
			   <input name="first" type="hidden" value="no">
			   <input name="what" id='SearchModeex' type="hidden" value="">
			   <div class="formText"><input id="search_inputex" class="text" type="text" name="kp_query" autocomplete="off" maxlength="256" value="" tabindex="1" /></div>
			   <input class="searchButton1" type="button" value="" tabindex="2" onclick="if(document.getElementById('search_inputex').value != 'поиск фильмов и актёров') {document.searchFormex.first.value = 'no'; document.searchFormex.submit();}" />
		    </form>
        </div>
    <div class="border_right"></div>
</div>




</div> <!-- shadow block -->






</div>


    <div id="vk_api_transport"></div>
    <script type="text/javascript">
        window.vkAsyncInit = function() {
            VK.init({apiId: 1864793, nameTransportPath: "/api/vkontakte/xd_receiver.php"});
            setTimeout(function() {
                if (typeof(vkInit) == "function") {
                    vkInit();
                }
            }, 0);
        };

        setTimeout(function(){
            var el = document.createElement("script");
            el.type = "text/javascript";
            el.src = "https://vkontakte.ru/js/api/openapi.js";
            el.async = true;
            document.getElementById("vk_api_transport").appendChild(el);
        }, 0);
    </script>

<link href="https://st.kp.yandex.net/js/feature.css?v=20130618" type="text/css" rel="stylesheet" />
<script type="text/javascript">(function(){window.featureData = [{"id":"14","name":"await_friends_movies\t","level":"79","title":"\u0423\u0440\u0430!","description":"\u0424\u0438\u043b\u044c\u043c\u044b, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u0436\u0434\u0443\u0442 \u0432\u0430\u0448\u0438 \u0434\u0440\u0443\u0437\u044c\u044f.","start_date":"2013-06-19","end_date":"2013-08-31","top":"0.2","left":"0","side":"right","offset":"0.2","for_all":"1","clear_url":"","picture_url":null,"region":"","cookie_expire":"-1228"},{"id":"13","name":"favfilms_nofilms","level":"79","title":"\u041a\u0441\u0442\u0430\u0442\u0438!","description":"\u0427\u0442\u043e\u0431\u044b \u0432\u044b\u0432\u0435\u0441\u0442\u0438 \u0441\u044e\u0434\u0430 \u043a\u0430\u0434\u0440\u044b \u0438\u0437 \u0444\u0438\u043b\u044c\u043c\u043e\u0432, \u0441\u043e\u0437\u0434\u0430\u0439\u0442\u0435 \u0443 \u0441\u0435\u0431\u044f \u0432 \u043f\u0440\u043e\u0444\u0438\u043b\u0435 <a href='\/mykp\/movies\/list\/type\/6\/'>\u043f\u0430\u043f\u043a\u0443 \u00ab\u041b\u044e\u0431\u0438\u043c\u044b\u0435 \u0444\u0438\u043b\u044c\u043c\u044b\u00bb<\/a> \u0438 \u043e\u0441\u0442\u0430\u0432\u044c\u0442\u0435 \u0435\u0435 \u043e\u0442\u043a\u0440\u044b\u0442\u043e\u0439 \u0434\u043b\u044f \u0432\u0441\u0435\u0445.","start_date":"2013-06-01","end_date":"2013-09-01","top":"1","left":"0.5","side":"top","offset":"0.2","for_all":"1","clear_url":"","picture_url":null,"region":"","cookie_expire":"-1228"},{"id":"8","name":"favourite_friends_movies","level":"79","title":"\u0423\u0440\u0430!","description":"\u0424\u0438\u043b\u044c\u043c\u044b, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u0434\u0440\u0443\u0437\u044c\u044f \u043e\u0446\u0435\u043d\u0438\u043b\u0438 \u043f\u043e \u0434\u043e\u0441\u0442\u043e\u0438\u043d\u0441\u0442\u0432\u0443","start_date":"2013-02-12","end_date":"2013-06-05","top":"0","left":"0","side":"bottom","offset":"0.3","for_all":"1","clear_url":"","picture_url":null,"region":"","cookie_expire":"-1228"}];}())</script><script type="text/javascript" src="https://st.kp.yandex.net/js/feature.js?v=20170214"></script>

<script type="text/javascript" id="ticketsScript" src="https://kassa.rambler.ru/s/widget/js/TicketManager.js"></script>
<div style="position: absolute; top: -20px">




</div>


<!-- Yandex.Metrika counter -->
<script type="text/javascript">
    'use strict';

    (function (d, w, c) {
        (w[c] = w[c] || []).push(function() {
            try {
                w.yaCounter22663942 = new Ya.Metrika({
                    id:22663942,
                    webvisor:true,
                    clickmap:true,
                    trackLinks:true,
                    accurateTrackBounce:true
                });
                window.Metrika.onLoad();
            } catch(e) { }
        });

        var n = d.getElementsByTagName("script")[0],
            s = d.createElement("script"),
            f = function () { n.parentNode.insertBefore(s, n); };
        s.type = "text/javascript";
        s.async = true;
        s.src = (d.location.protocol == "https:" ? "https:" : "http:") + "//mc.yandex.ru/metrika/watch.js";

        if (w.opera == "[object Opera]") {
            d.addEventListener("DOMContentLoaded", f, false);
        } else { f(); }
    })(document, window, "yandex_metrika_callbacks");
</script>

<noscript><div><img src="//mc.yandex.ru/watch/22663942" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
<!-- /Yandex.Metrika counter -->
<!-- Cчетчик скорости канала для видеорекламы TRP -->
<iframe src="//awsync.yandex.ru/0/9947/001001.htm" width="1" height="1" marginwidth="0" marginheight="0" hspace="0" vspace="0" frameborder="0" scrolling="no" bordercolor="#000000" style="left: -9999px; position: absolute;"></iframe>
<!-- /Cчетчик скорости канала для видеорекламы TRP -->
<iframe frameBorder="0" src="//kiks.kinopoisk.ru/su/" style="width:40px;height:40px;overflow:hidden;position:absolute;left:-40px;top:0;opacity:0"></iframe>
<iframe frameBorder="0" src="//static.kp.yandex.net/google-conversion.html" style="width:1px;height:1px;overflow:hidden;position:absolute;left:-40px;top:0;opacity:0"></iframe>
</body>
</html>
'''


def main():
    soup = BeautifulSoup(html_raw, 'html.parser')
    table = soup.find('table', attrs={'class': 'ten_items'})

    movies = table.find_all('tr', recursive=False)
    user_votes = []
    for movie in movies:
        ratingBlock = movie.find('div', {'class': 'ratingBlockP'})
        kinopoisk_rating = ratingBlock.find('a').text.split(' ')[0]

        user_vote_block = movie.find('div', {'class': 'userVote'})
        user_vote = 0
        if user_vote_block != None:
            user_vote = user_vote_block.find('p').text

        user_votes += [user_vote]
        # print('Общий рейтинг: {}'.format(kinopoisk_rating))
        # print('Рейнтинг пользователя: {}'.format(user_vote))

    print(*user_votes)


if __name__ == '__main__':
    main()
