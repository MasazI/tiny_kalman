#encoding: utf-8
'''
カルマンフィルターの例題
'''
import numpy as np
import math

# 速度vは分散Qで変化する
# 正しい観測zはまったくノイズが無い値に対して、分散Rのノイズを与える

def get_u(base):
    d_v = np.random.normal(0, 1)
    return base + d_v


def get_z(base):
    d_z = np.random.normal(0, 5)
    return base + d_z


def main():
    t = 0.01
    v = 10.
    Q = 1.
    R = 5.
    P = 1000000000000.
    x_t0 = 0.
    x_t1 = 0.
    z_t0 = 0.
    z = 0.
    for i in xrange(1000):
        print "="*20
        print("No.%d" % i)
        x_t0 = x_t0 + t*get_u(10)
        print("sample x: %f" % x_t0)
        P = P + math.pow(t, 2)*Q
        print("p: %f" % (P))
        z_t0 = z_t0 + t*10
        print("z_t0: %f" % (z_t0))
        z = get_z(z_t0)
        print("obsavation z: %f" % z)
    
        # カルマンゲインの計算
        S = P + R
        print("S: %f" % S)
        K = P * (1/S)
        print("K: %f" % K)
        x_t1 = x_t0 + K*(z - x_t0)
        P = P - math.pow(K, 2)*S
        print("P: %f" % P)
        print("kalman sample: %f" % x_t1)
        x_t0 = x_t1

if __name__ == "__main__":
    main()
