import os
url = "veltechmultitech.org"
dir = "/home/pavisrini/Desktop/elliot/xsrfprobe-output/" + url + "/"
print(dir)
for dp, dn, fn in os.walk(dir):

      cmd = "mousepad " + dir + fn
      print(cmd)
      os.system(cmd)