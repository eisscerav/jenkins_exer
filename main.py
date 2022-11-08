import os


def demo():
    print("demo python")


if __name__ == '__main__':
    envs = os.environ
    for env in envs:
        print(f'{env}={envs[env]}')
    demo()

