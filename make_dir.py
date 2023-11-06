import os

def main():
    p = os.getcwd() + '\\datasets\\person_head\\images'
    for i in os.listdir(p):
        with open('./datasets/person_head/'+ i +'_list.txt', 'w', encoding='utf-8') as f :
            for j in os.listdir(p + '\\' + i) :
                f.write(p +'\\'+i +'\\' + j + '\n')
            f.flush()

if __name__ == '__main__':
    main()