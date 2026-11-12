import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Простой калькулятор')
    parser.add_argument('x', type=float, help='Число x')
    parser.add_argument('y', type=float, help='Число y')
    parser.add_argument('--arithmetic', choices=['add', 'sub', 'mul', 'div'], help='Действие: add, sub, mul или div')
    parser.add_argument('--accuracy', type=int, default=1, help='Сколько знаков после запятой')

    args = parser.parse_args()

    if args.arithmetic is not None:
        result = None
        if args.arithmetic == 'add':
            result = args.x + args.y
        elif args.arithmetic == 'sub':
            result = args.x - args.y
        elif args.arithmetic == 'mul':
            result = args.x * args.y
        elif args.arithmetic == 'div':
            if args.y == 0:
                parser.error('Деление на ноль невозможно!')
            result = args.x / args.y
        accuracy = args.accuracy
        print('Результат: {:.{}f}'.format(result, accuracy))

    else:
        print(f'Число x={args.x}, число y={args.y}')
