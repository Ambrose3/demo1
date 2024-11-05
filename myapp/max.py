import fire

def hello(name="Word"):
    return "Hello %s!" % name

if __name__ == '__main__':
    fire.Fire(hello)