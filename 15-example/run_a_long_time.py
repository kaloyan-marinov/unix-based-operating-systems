import datetime
import os
import time


def main():
    # flnm = __file__.replace('.py', '.log')
    flnm = os.path.join(
        os.path.dirname(__file__),
        'output.txt',
    )

    start = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    print(f'{start} - starting to write to {flnm}')

    with open(flnm, 'w') as f:
        for i in range(60):
            time.sleep(1)
            f.write(str(i) + '\n')

    final = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    print(f'{final} - finished writing to the file and closed the file')


if __name__ == '__main__':
    main()
