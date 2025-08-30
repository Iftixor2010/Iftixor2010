def get_full_name(ism, familiya, otasi=''):
    if otasi:
        return f"{ism} {otasi} {familiya}"   
    else:
        return f"{ism} {familiya}".title()