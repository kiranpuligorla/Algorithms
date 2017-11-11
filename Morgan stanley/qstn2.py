#!/bin/python3


def sort_numeric(st, bl):
    dt = {}
    for s in st:
        k,v = s.split()
        dt[k] = v
    d_view = [(int(v), k) for k, v in dt.items()]
    d_view.sort(reverse=bl)
    for v, k in d_view:
        print(k, dt[k])


def sort_lxg(st, bl):
    st.sort(reverse=bl)
    print('\n'.join(st))

if __name__ == "__main__":
    st = []
    for i in range(int(input())):
        st.append(input())
    ky, bl, st_type = input().split()

    if bl == 'false':
        bl=False
    elif bl =='true':
        bl=True

    if st_type == "numeric":
        sort_numeric(st, bl)
    else:
        sort_lxg(st, bl)