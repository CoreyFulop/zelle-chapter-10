# cball5.py

from projectile import Projectile

def getInputs():
    a = eval(input("Enter the launch angle (in degrees): "))
    v = eval(input("Enter the initial velocity (in metres/sec): "))
    h = eval(input("Enter the initial height (in metres): "))
    t = eval(input("Enter the time interval between position calculations: "))
    return a, v, h, t

def main():
    angle, vel, h0, time = getInputs()
    cball = Projectile(angle, vel, h0)
    maxH = cball.getY()
    while cball.getY() >= 0:
        cball.update(time)
        if cball.getY() > maxH:
            maxH = cball.getY()
    print(f"Distance travelled: {cball.getX():.1f} metres.")
    print(f"Maximum height: {maxH:.1f} metres.")

if __name__ == "__main__":
    main()
