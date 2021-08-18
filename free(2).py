def main():
    call_four()

def call_four(target_value = 3, output_message = '4で割り切れました。'):
    if target_value == 0:
        print('0で割ることはできません。')
    elif target_value % 4 == 0:
        print(output_message)
    else:
        print('4で割り切れませんでした。')

if __name__ == "__main__":
    main()




