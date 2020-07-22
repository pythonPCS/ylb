import frida, sys
import time



test_sky = """
    Java.perform(function(){
        var cir = Java.use('com.iCitySuzhou.suzhou001.d.d'); 
        cir.a.overload('java.lang.String', 'java.lang.String').implementation = function(c, d){
            console.log("加密参数c: " + c);
            console.log("加密参数d: " + d);
            var s = this.a(c, d);
            console.log("返回结果: " + s);
            return s;
        }
    })

"""

api = """
    Java.perform(function () {
        Java.enumerateClassLoaders({
        "onMatch": function(loader) {
            console.log(loader);
        },
        "onComplete": function() {
            console.log("success");
        }
    });
});
"""



def read_file_all(file):
    fp = open(file, encoding='utf-8')
    text = fp.read()
    fp.close()
    return text

def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)

def yinlibo():
    process = frida.get_usb_device().attach('com.iCitySuzhou.suzhou001')
    # jss = read_file_all('hash.js')
    script = process.create_script(test_sky)
    # script = process.create_script(api)
    script.on('message', on_message)
    script.load()
    sys.stdin.read()



if __name__ == "__main__":
    yinlibo()