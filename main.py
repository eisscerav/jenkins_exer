import os


def demo():
    print("demo python")


if __name__ == '__main__':
    envs = os.environ
    for env in envs:
        print(f'key={env}, value={envs[env]}')
    demo()

