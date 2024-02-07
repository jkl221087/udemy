def read_file(filename):
    lines = []
    with open (filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convers(lines):
    person = None
    allen_word_count = 0
    viki_word_count = 0
    allen_stick_count = 0
    viki_stick_count = 0
    allen_image_cont = 0
    viki_image_cont = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == "Allen":
            if s[2] == '貼圖':
                allen_stick_count += 1
            elif s[2] == '圖片':
                allen_image_cont += 1
            else:
                for m in s[2:]:
                    allen_word_count += len(m)
        elif name == "Viki":
            if s[2] == '貼圖':
                viki_stick_count += 1
            elif s[2] == '圖片':
                viki_image_cont += 1
            else:
                for m in s[2:]:
                    viki_word_count += len(m)
    print ("allen說了", allen_word_count, '傳了', allen_stick_count, '貼圖', allen_image_cont, '圖片')
    print ("viki說了", viki_word_count, '傳了', viki_stick_count, '貼圖', viki_image_cont, '圖片')

def write_file(filename, lines):
    with open (filename, 'w', encoding= 'utf-8') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('LINE-Viki.txt')
    lines = convers(lines)
    # write_file('output.txt', lines)
    
main()