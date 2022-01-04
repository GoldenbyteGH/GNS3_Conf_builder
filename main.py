
from jinja2 import Environment,FileSystemLoader #Jinja work with template and python,is supermega useful 4 NetworkAutomation
import yaml
#declare template enviroment
ENV = Environment(loader=FileSystemLoader('.'))

template = ENV.get_template("template.j2")      # template IN
f_conf = open("config.txt", 'w')                #  config  OUT

if __name__ == "__main__":
    with open("devdata.yml") as f:
        devices = yaml.safe_load(f)

    for line in template.render(device_list=devices):
        f_conf.writelines(line)

    f_conf.close()

