class IRingBell():
    def ringbell(self):
	    pass
        
class Ring_Big_Bell(IRingBell):
    def ringbell(self):
        print("Ring big bell, BOING!")
        
class Dance():
    def dance(self):
        print("Dance!")
        
def isRingBell(iface):
    if isinstance(iface,IRingBell):
        iface.ringbell()
    else:
        print("Not IRingBell interface")
        
def main():
    a = Ring_Big_Bell()
    b = Dance()
    
    isRingBell(a)
    isRingBell(b)


if __name__ == "__main__":
	main()