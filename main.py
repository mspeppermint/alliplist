def main():
    range = [0,0,0,0]

    rounds = 374887
    while(range[0] != 256):
        
        range[3] += 1
        if(range[3] == 256 and range[2] != 256):
            range[2] += 1
            range[3] = 0

        if(range[2] == 256 and range[1] != 256):
            range[1] += 1
            range[2] = 0

        if(range[1] == 256 and range[0] != 256):
            range[0] += 1
            range[1] = 0
    
        
        print(f'\r Writing file {rounds}.txt with range {range[0]}', end='',flush=True)
        with open(f'{rounds}.txt','a') as f:
            f.write(f'{range[0]}.{range[1]}.{range[2]}.{range[3]}\n')
            f.close()
	
        with open(f'{rounds}.txt','r') as r:
            rl = len(r.readlines())
            if(rl == 10000):
                rounds += 1
	
	
        if(range[0] == 256):
            break
            print('end')
if(__name__ == "__main__"):
    main()
