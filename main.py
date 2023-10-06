def main():
    print("hello main")
    
def demo_zip():
    values1 = list(range(2, 20))
    values2 = list(range(10, 29, 3))
    print(values1)
    print(values2)
    
    for v1, v2 in zip(values1, values2):
        print("v1 =", v1, "v2 =", v2, "sum =", v1 + v2)

demo_zip()