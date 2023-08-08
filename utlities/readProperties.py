import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('Common Info', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        Username = config.get('Common Info', 'username')
        return Username

    @staticmethod
    def getPassword():
        Password = config.get('Common Info', 'password')
        return Password

    @staticmethod
    def getinvalid_username():
        invalid_username = config.get('Common Info', 'invalid_username')
        return invalid_username

    @staticmethod
    def getinvalid_password():
        invalid_password = config.get('Common Info', 'invalid_password')
        return invalid_password

    @staticmethod
    def getUsername_space():
        username_space = config.get('Common Info', 'username_space')
        return username_space

    @staticmethod
    def getpasword_space():
        pasword_space = config.get('Common info', 'pasword_space')
        return pasword_space

    @staticmethod
    def getFirst_name():
        First_name = config.get('Common Info', 'First_name')
        return First_name

    @staticmethod
    def getlast_name():
        last_name = config.get('Common Info', 'last_name')
        return last_name

    @staticmethod
    def getname():
        name = config.get('Common Info', 'name')
        return name

    @staticmethod
    def getname_s():
        name_s = config.get('Common Info', 'name_s')
        return name_s

    @staticmethod
    def getrandom_num():
        random_num = config.get('Common Info', 'random_num')
        return random_num

    @staticmethod
    def getspecial_chars():
        special_cars = config.get('Common Info', 'special_cars')
        return special_cars

    @staticmethod
    def getrole_name():
        role = config.get('Common Info', 'role')
        return role

    @staticmethod
    def get_adduser_name():
        usname = config.get('Common Info', 'usname')
        return usname

    @staticmethod
    def role_text():
        roletext = config.get('Common Info', 'roletext')
        return roletext

    @staticmethod
    def amusername():
        amusername = config.get('Common Info', 'amusername')
        return amusername

    @staticmethod
    def ampassword():
        ampassword = config.get('Common Info', 'ampassword')
        return ampassword

    @staticmethod
    def hissearch():
        hissearch = config.get('Common Info', 'hissearch')