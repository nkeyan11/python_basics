import math
print('Choose from the choices below:')
print('1. Area of the trapezoid   2.Volume of sphere')
print('3. Volume of cone          4.Volume of cuboid')
x=int(input('Enter the choice of operation: '))
if x==1:
    a=float(input('Enter the first parallel side: '))
    b=float(input('Enter the second parallel side: '))
    h=float(input('Enter the perpendicular distance between parallel sides: '))
    area=round(.5*(a+b)*h,2)
    print('Area of the trapezoid is: ',area)

if x==2:
    sr=float(input('Enter the radius of the sphere: '))
    vs=round((4/3)*(math.pi)*(sr**3),2)
    print('Volume of the sphere is: ',vs)

if x==3:
    cr=float(input('Enter the radius of the cone: '))
    ch=float(input('Enter the height of the cone: '))
    vc=round((1/3)*(math.pi)*(cr**2)*ch,2)
    print('Volume of the cone is: ',vc)

if x==4:
    cua=float(input('Enter the first side of the cuboid: '))
    cub=float(input('Enter the second side of the cuboid: '))
    cuc=float(input('Enter the third side of the cuboid: '))
    vcu=round((cua*cub*cuc),2)
    print('Volume of the cuboid is: ',vcu)
l=[1,2,3,4]
if x not in l:
    print('invalid input')
    
    
    
