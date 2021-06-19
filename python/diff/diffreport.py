# -*- coding: utf-8 -*-
import io
import json

class  Report():
    def __init__(self):
        self.counter = 0
        self.no_diff_count = 0
        self.no_auth_count=0
        self.diff_count = 0
        self.error_count = 0
        self.not_string_count = 0
        self.mailtext =""
        self.mailtop = ""
        self.sumtext = ""

    def begin(self,online_version,yf_version):
        self.mailtop = "===================Diff脚本执行报告===================" + "<br>"
        self.mailtop= self.mailtop+ 'online_version:' + str(online_version) + ';' + 'yf_version:' + str(yf_version)+ '<br>'
        self.mailtext = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>diff执行结果</title><style>h3{text-align:center;}</style><style type="text/css">body,html {margin: 0;padding: 0;height: 100%;}.left,.right {float: left;width: 50%;height: 20px;}.left { background-color: white; }.right { background-color: white; }</style></head><body>'
        self.counter+=1



    def diff(self,url,a,param1):
        self.diff_count += 1
        self.mailtext = self.mailtext + '[' + str(self.counter) + ']-----------<button   id="btn' + str(self.diff_count) + '" onclick="aaa(\'btn' + str(self.diff_count) + '\',' + str(self.diff_count) + ')">>>>展开</button><br>'
        self.mailtext = self.mailtext + url + '<br>'
        self.mailtext=self.mailtext+'online_param: '+str(param1)+'<br>'
        #self.mailtext=self.mailtext+'yf_param: '+str(param2)+'<br>'
        self.mailtext = self.mailtext + '<div name="window" id="div' + str(self.diff_count) + '">'
        self.mailtext = self.mailtext + '<div class="left" style="height: 400px; overflow:scroll"  id="div' + str(self.diff_count) + 'con1"  onscroll="move(' + str(self.diff_count) + ',2,1)"><ol> <pre id="div' + str(self.diff_count) + 'pre1">' + str(json.dumps(a[1], ensure_ascii=False)) + '</pre></ol></div>'
        self.mailtext = self.mailtext + '<div class="left" style="height: 400px; overflow:scroll"  id="div' + str(self.diff_count) + 'con2"  onscroll="move(' + str(self.diff_count) + ',1,2)"><ol> <pre id="div' + str(self.diff_count) + 'pre2">' + str(json.dumps(a[2], ensure_ascii=False)) + '</pre></ol></div>'
        self.mailtext = self.mailtext + '</div>'
        self.counter += 1

    def no_diff(self):
        self.no_diff_count += 1
        self.counter += 1

    def no_auth(self,url,param1):
        self.no_auth_count+=1
        self.mailtext = self.mailtext + '[' + str(self.counter) + ']～～～～～～～～～～～～无权限'+'<br>'
        self.mailtext=self.mailtext+url+'<br>'
        self.mailtext=self.mailtext+'param:'+str(param1)+'<br>'
        self.counter+=1

    def notjson(self,url,param):
        self.not_string_count += 1
        self.mailtext = self.mailtext + '[' + str(self.counter) + ']================= not a json string： ' + url + '==================' + "<br>"
        self.mailtext=self.mailtext+'[' + str(self.counter) + ']================= param is ： ' + str(param)+ '==================' + "<br>"
        self.counter += 1

    def error(self,url):
        self.no_diff_count += 1
        self.error_count += 1
        self.mailtext = self.mailtext + "error, url is: " + url + "<br>"
        self.counter += 1

    def end(self):
        self.mailtext = self.mailtext + '<script type="text/javascript"> var onOff=false; var ip =[]; var ids = document.getElementsByName("window"); for(var i=0;i<ids.length;i++) { ids[i].style.display="none"; }function move(a,b,c){ document.getElementById("div"+a+"con"+b).scrollTop = document.getElementById("div"+a+"con"+c).scrollTop; document.getElementById("div"+a+"con"+b).scrollLeft = document.getElementById("div"+a+"con"+c).scrollLeft; } function aaa(e,f) { var btn=document.getElementById(e); if(onOff==true) { document.getElementById("div"+f).style.display="none"; btn.innerHTML=">>>展开" } else { document.getElementById("div"+f).style.display="block"; btn.innerHTML ="<<<收缩"} onOff=!onOff; if (ip[f] != f) { var obj1 = document.getElementById("div"+f+"pre1").innerText; var obj2 = document.getElementById("div"+f+"pre2").innerText; var str1 = JSON.stringify(JSON.parse(obj1), null, 4); var str2 = JSON.stringify(JSON.parse(obj2), null, 4); output(ShowColor(str1),f); output2(ShowColor(str2),f); ip[f]=f; } return false; } function output(inp,f) { document.getElementById("div"+f+"pre1").innerHTML= inp; } function output2(inp,f) { document.getElementById("div"+f+"pre2").innerHTML= inp; } function ShowColor(json){ var a1 = "<span style=background:yellow;>"; var a2 = "<span style=background:pink;>"; var a3 = "</span>"; return json.replace(/ThisIdYellowBegin/g, a1).replace(/ThisIdYellowEnd/g, a3).replace(/ThisIdPinkBegin/g, a2).replace(/ThisIdPinkEnd/g, a3); } </script> </body> </html>'
        self.sumtext="脚本执行完成，总计对比"+str(self.counter)+"条url。<br>其中：无权限"+str(self.no_auth_count)+"条，无差异"+str(self.no_diff_count)+"条，有差异"+str(self.diff_count)+"条，返回值异常"+str(self.not_string_count)+"条，url错误"+str(self.error_count)+"条。<br>具体如下：<br><br>"
        self.mailtext = self.mailtop+self.sumtext+self.mailtext

        with io.open("//Users/zhaocuixia/ajaxdiff.html", "w", encoding='utf-8') as f:
            f.write(self.mailtext)
            f.close()

        return self.mailtext

if __name__=='__main__':
    report = Report()
    report.begin('4.1.1','4.1.0')
    a=(True, {'a': 'ThisIdYellowBegin123ThisIdYellowEnd', 'c': 'ThisIdYellowBegin[1, 2, 3, 4]ThisIdYellowEnd', 'd': {'test': 'ThisIdYellowBeginworkThisIdYellowEnd', 'yf': 'yl'}, 'ThisIdPinkBeginThisIdPinkBeginbThisIdPinkEndThisIdPinkEnd': 345}, {'a': 'ThisIdYellowBegin345ThisIdYellowEnd', 'c': 'ThisIdYellowBegin[2, 3, 4]ThisIdYellowEnd', 'd': {'test': 'ThisIdYellowBeginworksThisIdYellowEnd', 'yf': 'yl', 'ThisIdPinkBeginThisIdPinkBeginThisIdPinkBeginmoreThisIdPinkEndThisIdPinkEndThisIdPinkEnd': 'keys'}, 'ThisIdPinkBeginThisIdPinkBeginThisIdPinkBeginfThisIdPinkEndThisIdPinkEndThisIdPinkEnd': 'tst', 'ThisIdPinkBeginThisIdPinkBeginThisIdPinkBeginThisIdPinkBegineThisIdPinkEndThisIdPinkEndThisIdPinkEndThisIdPinkEnd': 123})
    report.diff('http://www.test.com',a,'test')
    report.end()
