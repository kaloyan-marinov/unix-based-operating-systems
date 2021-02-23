import os
import time


def main():
    # flnm = __file__.replace('.py', '.log')
    flnm = os.path.join(
        os.path.dirname(__file__),
        'output.txt',
    )

    with open(flnm, 'w') as f:
        f.write('start' + '\n')

        for i in range(60):
            time.sleep(1)
            f.write(str(i) + '\n')

        f.write('end' + '\n')


if __name__ == '__main__':
    main()
