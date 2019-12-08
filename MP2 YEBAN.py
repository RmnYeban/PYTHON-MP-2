from math import sqrt
def DetRCenterVector(A1, B1, A2, B2, A3, B3) :
        PA1=(A1**2)
        PA2=(A2**2)
        PA3=(A3**2)
        PB1=(B1**2)
        PB2=(B2**2)
        PB3=(B3**2)
        A12 = A1 - A2;
        A13 = A1 - A3;
        B12 = B1 - B2;
        B13 = B1 - B3;
        B31 = B3 - B1;
        B21 = B2 - B1;
        A31 = A3 - A1;
        A21 = A2 - A1;
        mA13 = PA1-PA3 ;
        mB13 = PB1-PB3;
        mA21 = PA2 - PA1;
        mB21 = PB2 - PB1;
        multi1=(mA13) * (A12)
        multi2=(mB13) * (A12)
        multi3=(mA21) * (A13)
        multi4=(mB21) * (A13)
        multi5=(B31) * (A12)
        multi6=(B21) * (A13)
        multi7=(mA13) * (B12)
        multi8=(mB13) * (B12)
        multi9=(mA21) * (B13)
        multi10=(mB21) * (B13)
        multi11=(A31) * (B12)
        multi12=(A21) * (B13)
        f = ((multi1+multi2+multi3+multi4)// 
         (2 * (multi5 - multi6)));
        g = (( multi7+ multi8 + multi9 +multi10 ) // 
         (2 * ( multi11- multi12)));
        c = (-PA1 - PB1 - 2 * g * A1 - 2 * f * B1);
        
        h = -g;
        k = -f;
        sqr_of_r = h * h + k * k - c;
        r = round(sqrt(sqr_of_r), 5);
        c=(h,k)
        v=[f,g,c]
        print('\nThe center of the circle is ', c)
        print('\nThe radius of the circle is ', r)
        print('\nThe vector [D,E,F] is ', v)
              
